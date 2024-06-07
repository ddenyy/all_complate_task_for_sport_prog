

import pygame
import random
from pygame import gfxdraw
import functools

pygame.init() 

WIDTH = 400
HEIGHT = 400
window = pygame.display.set_mode((WIDTH, HEIGHT), pygame.RESIZABLE)

WHITE = (255, 255, 255)
COL = (102, 255, 255)
BLACK = (0,0,0)

RUN = True


@functools.lru_cache()
def TS(A,B,C, n):
    if n == 0:
        return
    pygame.draw.line( window, WHITE , A, B, 1 )
    pygame.draw.line( window, WHITE , B, C, 1 )
    pygame.draw.line( window, WHITE , C, A, 1 )
    A_1 = ((A[0] + B[0]) / 2, (A[1] + B[1]) / 2)
    B_1 = ((C[0] + B[0]) / 2, (C[1] + B[1]) / 2)
    C_1 = ((A[0] + C[0]) / 2, (A[1] + C[1]) / 2)
    TS(A, A_1, C_1, n - 1)
    TS(A_1, B, B_1, n - 1)
    TS(C_1, B_1, C, n - 1)
    

scale = 1
x_linear_transf = 0
y_linear_transf = 0
count_iteration = 8

def get_user_base_coord():
    point_A = input("input point A")
    point_A = tuple(int(x) for x in point_A.split(" "))
    point_B = input("input point B")
    point_B = tuple(int(x) for x in point_B.split(" "))
    point_C = input("input point C")
    point_C = tuple(int(x) for x in point_C.split(" "))
    return point_A, point_B, point_C

def get_user_scale():
    user_scale = int(input("input your scale 1,2,3,4"))
    if user_scale > 4:
        print("error, scale <= 4 and scale >= 1")
        user_scale = 1
    return user_scale

#point_A, point_B, point_C = get_user_base_coord()
point_A, point_B, point_C = (0,0), (WIDTH, 0), (WIDTH/2, HEIGHT)
#scale = get_user_scale()
clock = pygame.time.Clock()

TS(point_A,point_B,point_C, count_iteration)
pygame.display.update()
while RUN:

    clock.tick(60)
    for event in pygame.event.get():
        if (event.type == pygame.QUIT):
            RUN  = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                window.fill((0,0,0))
                x_linear_transf -= 40
                print("right")
            elif event.key == pygame.K_LEFT:
                window.fill((0,0,0))
                x_linear_transf += 40
                print("left")
            elif event.key == pygame.K_DOWN:
                window.fill((0,0,0))
                y_linear_transf += 40
            elif event.key == pygame.K_UP:
                window.fill((0,0,0))
                y_linear_transf -= 40
            elif event.key == pygame.K_0:
                window.fill((0,0,0))
                scale *= 1.1
            elif event.key == pygame.K_9:
                window.fill((0,0,0))
                scale *= 0.9
            elif event.key == pygame.K_333:
                print("k")
                pygame.image.save(window, f"image{random.randint(100,10000)}.jpeg")
    print(scale)
    if scale >= 4:
        A = ((point_A[0] * scale) / scale + x_linear_transf , (point_A[1] * scale) / scale + y_linear_transf)
        B = ((point_B[0] * scale) / scale + x_linear_transf, (point_B[1] * scale ) / scale + y_linear_transf)
        C = ((point_C[0] * scale) / scale + x_linear_transf, (point_C[1] * scale ) / scale + y_linear_transf)
        scale = 1
    else:
        A = ((point_A[0] * scale + x_linear_transf) , (point_A[1] * scale + y_linear_transf))
        B = ((point_B[0] * scale + x_linear_transf), (point_B[1] * scale + y_linear_transf))
        C = ((point_C[0] * scale + x_linear_transf), (point_C[1] * scale + y_linear_transf))
    TS(A,B,C, count_iteration)
    pygame.display.update()
pygame.quit()
