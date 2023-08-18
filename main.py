import numpy as np
import cv2
import os
import random
import piece
import vlc


def update_mat(_piece):
    # location(y,x) ,width, height
    for y in range(_piece.location[0], _piece.location[0]+_piece.height):
        for x in range(_piece.location[1], _piece.location[1]+_piece.width):
            is_painted_mat[y, x] = 1


def check_collision_right(_piece):
    if _piece.location[1] + 10 < canvasImage.shape[1] - _piece.width:
        for y in range(_piece.location[0], _piece.location[0]+_piece.height):
            for x in range(_piece.location[1]+_piece.width, _piece.location[1]+_piece.width+10):
                if is_painted_mat[y, x] == 1:
                    return False
        return True
    return False


def check_collision_left(_piece):
    if _piece.location[1] - 10 > 0:
        for y in range(_piece.location[0], _piece.location[0]+_piece.height):
            for x in range(_piece.location[1]-10, _piece.location[1]):
                if is_painted_mat[y, x] == 1:
                    return False
        return True
    return False


def check_collision_down(_piece):
    if _piece.location[0] + _piece.height > canvasImage_orig.shape[0] - 10:
        return True
    for y in range(_piece.location[0]+_piece.height, _piece.location[0]+_piece.height+10):
        for x in range(_piece.location[1], _piece.location[1]+_piece.width):
            if is_painted_mat[y, x] == 1:
                return True
    return False


def check_collision_up(_piece):
    return _piece.location[0] < 10


background = vlc.MediaPlayer(r'C:\Users\The user\Desktop\BootCamp\project-python-tetris\project\images\background1.mp3')
canvasPath = r'C:\Users\The user\Desktop\BootCamp\project-python-tetris\project\images\Canvas.png'
piecesRootFolder = r'C:\Users\The user\Desktop\BootCamp\project-python-tetris\project\images\pieces'
fileNames = os.listdir(piecesRootFolder)
filePaths_example = [os.path.join(piecesRootFolder, f_name) for f_name in fileNames]

canvasImage_orig = cv2.imread(canvasPath)
# canvasImage_orig = cv2.resize(canvasImage_orig, (1600, 780))

cv2.namedWindow('canvas', cv2.WINDOW_NORMAL)
                                # 1080,1920,3
canvasImage = canvasImage_orig.copy()

is_painted_mat = np.zeros((canvasImage_orig.shape[0] + 2, canvasImage_orig.shape[1] + 2))

background.play()
while True:
    isReachedEndOfCanvas = False
    p = piece.Piece(random.choice(filePaths_example), canvasImage_orig.shape[1])
    while not isReachedEndOfCanvas:
        canvasImage = canvasImage_orig.copy()
        p.draw(canvasImage)
        cv2.imshow('canvas', canvasImage)
        key = cv2.waitKey(1)
        if key == ord('a') and check_collision_left(p):
            p.location[1] -= 10
        elif key == ord('d') and check_collision_right(p):
            p.location[1] += 10
        isReachedEndOfCanvas = check_collision_down(p)
        if isReachedEndOfCanvas:
            finish = vlc.MediaPlayer(
                r'C:\Users\The user\Desktop\BootCamp\project-python-tetris\project\images\finish1.mp3')
            finish.play()
            canvasImage_orig = canvasImage
            update_mat(p)
    if check_collision_up(p):
        break

background.pause()
org = (150, 600)
fontScale = 10
color = (50, 50, 255)
thickness = 15
canvasImage = cv2.putText(canvasImage, 'Game Over', org, cv2.FONT_HERSHEY_SIMPLEX,
                          fontScale, color, thickness, cv2.LINE_AA)
cv2.imshow('canvas', canvasImage)
key1 = cv2.waitKey(10)
while key1 != 27:
    key1 = cv2.waitKey(10)
