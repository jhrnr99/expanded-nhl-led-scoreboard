from PIL import Image
from images.image_helper import ImageHelper
from utils import get_file

PATH = "assets/loading/loading.gif"

class Loading:
    def __init__(self, matrix):
        self.matrix = matrix
        
    def render(self):
        self.play_gif(PATH)

    def play_gif(self, file):
        im = Image.open(get_file(file))

        # Set the frame index to 0
        frame_nub = 0
        # Set number of loop to 1 (if you want to play you animation more then once, change this variable)
        numloop = 20
        self.matrix.clear()

        # Go through the frames
        x = 0
        while x is not numloop:
            try:
                im.seek(frame_nub)
            except EOFError:
                x += 1
                if x == numloop:
                    return
                frame_nub = 0
                im.seek(frame_nub)

            self.matrix.draw_image(("50%", 0), im, "center")
            self.matrix.render()

            frame_nub += 1