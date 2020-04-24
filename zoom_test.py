"""
zoom_test.py

A vispy program to examine artifacts seen when zooming way in. At around 5000x
zoom you can start to see rough edges on the border between 2 single pixels.
At 100,000x there are huge sawtooths. This is using "nearest neighbor"
interpolation.

We draw a 2x2 image with 2 black pixels and 2 white ones. Use left mouse 
button to map and mouse scrollwheel to zoom.

Derived from vispy/examples/basics/scene/image.py
"""
import sys
from vispy import scene
from vispy import app
from vispy.io import load_data_file, read_png
import numpy as np

# 2x2 pixel checkerboard
WIDTH = 2

class TestPanZoomCamera(scene.PanZoomCamera):
    """
    Just add printing zoom statistics to the real PanZoomCamera.
    """
    def zoom(self, factor, center=None):
        super().zoom(factor, center)
        zoom = WIDTH / view.camera.rect.width
        print(f"zoom = {zoom:.1f}")

def checkerboard():
    """
    Return 2x2 pixel black and white checkboard image.
    """
    black = [0, 0, 0]
    white = [255, 255, 255]
    return np.array([(black, white), (white, black)], dtype=np.uint8)

canvas = scene.SceneCanvas(keys='interactive')
canvas.size = 600, 600
canvas.title = 'Zoom Test'
canvas.show()

# Set up a viewbox to display the image with interactive pan/zoom
view = canvas.central_widget.add_view()

image = scene.visuals.Image(checkerboard(), interpolation='nearest',
                            parent=view.scene, method='subdivide')


view.camera = TestPanZoomCamera(aspect=1)
# flip y-axis to have correct alignment
view.camera.flip = (0, 1, 0)
view.camera.set_range()
view.camera.zoom(0.1, (1, 1))

if __name__ == '__main__' and sys.flags.interactive == 0:
    app.run()
