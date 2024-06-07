import random
from typing import Any, Optional
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.backend_bases import KeyEvent
from numpy import ndarray, float64


def genMidpointDisplacement(
        point_left: list[float, float],
        point_right: list[float, float]
) -> list[float]:
    diff_x = abs(point_left[0] - point_right[0])
    if diff_x <= 1:
        return []
    R = 0.4
    new_point = [(point_left[0] + point_right[0]) / 2,
                 (point_left[1] + point_right[1]) / 2 + R *
                 random.uniform(-1, 1) * diff_x]
    points = []
    points += genMidpointDisplacement(point_left, new_point)
    points += genMidpointDisplacement(new_point, point_right)
    points += new_point
    return points


def genLandSpace(
        points: list[[float, float]]
) -> ndarray[[float64, float64]]:
    result = points[0]
    for i in range(1, len(points)):
        result += genMidpointDisplacement(points[i - 1], points[i]) + points[i]
    result = np.array(result)
    result = result.reshape((len(result) // 2, 2))
    result = np.array(sorted(result, key=lambda point: point[0]))
    return result


def key_event(e: KeyEvent):
    global POINTS, START_IDX
    if str(e.key) == 'r':
        POINTS = genLandSpace([[0, 128], [256, 128], [512, 384]])
        START_IDX = 0
        drawLandSpace(POINTS)
    elif str(e.key) == 'right':
        START_IDX += 64
        last_point = POINTS[-1]
        new_points = genLandSpace(
            [list(last_point), [last_point[0] + 64,
                                last_point[1] + 80 * random.uniform(-1.1, 1)]]
        )
        POINTS = np.append(POINTS, new_points[1:])
        POINTS = POINTS.reshape((len(POINTS) // 2, 2))
        drawLandSpace(POINTS)
    elif str(e.key) == 'left':
        START_IDX -= 64
        if START_IDX < 0:
            START_IDX = 0
            first_point = POINTS[0]
            new_points = genLandSpace(
                [[first_point[0] - 64,
                  first_point[1] + 80 * random.uniform(-1.1, 1)],
                 list(first_point)]
            )
            POINTS = np.append(new_points[:-1], POINTS)
            POINTS = POINTS.reshape((len(POINTS) // 2, 2))
        drawLandSpace(POINTS)


def drawLandSpace(points: ndarray[[float64, float64]]):
    WIDTH = 512
    HEIGHT = 512
    shift = points[START_IDX][0]
    x, y = points[START_IDX:].T
    x = np.array([item - shift for item in x])
    FIG.clear()
    plt.plot(x, y)
    plt.fill_between(x, y, -100)
    plt.xlim([0, WIDTH])
    plt.ylim([-100, HEIGHT])
    plt.draw()


def main():
    global POINTS, FIG
    plt.ion()
    plt.style.use("ggplot")
    FIG = plt.figure()
    FIG.canvas.mpl_connect('key_press_event', key_event)
    #A = list(map(int, input("input point in 2 coords").split()))
    #B = list(map(int, input("input point in 2 coords").split()))
    #C = list(map(int, input("input point in 2 coords").split()))
    A, B, C = [0, 128], [256, 128], [512, 384]
    POINTS = genLandSpace([A, B, C])
    drawLandSpace(POINTS)
    plt.ioff()
    plt.show()


if __name__ == '__main__':
    POINTS: ndarray[[float64, float64]] = np.array([])
    FIG: Optional[Any] = None
    START_IDX: int = 0
    main()
