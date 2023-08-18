import random
import cv2
import numpy as np


class Piece:
    def __init__(self, path, canvas_width):
        # self.image = cv2.imread(path, cv2.IMREAD_UNCHANGED)
        self.image = cv2.imread(path)
        self.height, self.width, self.channels = self.image.shape
        self.location = np.array([0, random.randint(0, canvas_width-self.width)])
        self.location = self.location - self.location % 10
        print(self.location)
        self.velocity = np.array([1, 0])

    def draw(self, canvas):
        canvas[self.location[0]:self.location[0] + self.height,
               self.location[1]:self.location[1] + self.width, :] = self.image
        self.location = self.location + self.velocity

    # def draw(self, canvas):
    #     height, width = self.image.shape[:2]
    #     for y in range(self.location[0], self.location[0] + height):
    #         for x in range(self.location[1], self.location[1] + width):
    #             overlay_color = self.image[y - self.location[0], x - self.location[1],
    #                                        :3]  # first three elements are color (RGB)
    #             overlay_alpha = self.image[
    #                                 y - self.location[0], x - self.location[
    #                                     1], 3] / 255  # 4th element is the alpha channel, convert from 0-255 to 0.0-1.0
    #             # get the color from the background image
    #             background_color = canvas[y, x]
    #             # combine the background color and the self.image color weighted by alpha
    #             composite_color = background_color * (1 - overlay_alpha) + overlay_color * overlay_alpha
    #             # update the background image in place
    #             canvas[y, x] = composite_color
    #     self.location = self.location + self.velocity
