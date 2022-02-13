'''
A simple ping pong game made with Pygame, taken from NeuralNine: https://www.youtube.com/watch?v=HNCAi0sjAz8&ab_channel=NeuralNine
Idk pygame, don't judge me :D
'''

from glob import glob
import pygame


# Variables
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

WIDTH = 800
HEIGHT = 800

pygame.init()
font = pygame.font.Font('./font.ttf', 40)

latency = 30

player_speed = 20

paddle_width = 10
paddle_height = 100

p1_x_pos = WIDTH - paddle_width - 10
p1_y_pos = HEIGHT / 2 - paddle_height / 2

p2_x_pos = WIDTH - paddle_width - 10
p2_y_pos = WIDTH / 2 - paddle_height / 2

p1_score = 0
p2_score = 0

p1_up = False
p1_down = False
p2_up = False
p2_down = False

ball_x_pos = WIDTH / 2
ball_y_pos = HEIGHT / 2
ball_width = 8
ball_x_vel = -10

screen = pygame.display.set_mode((WIDTH, HEIGHT))

#drawing objects
def draw_objects():
    pygame.draw.rect(screen, WHITE, (int(p1_x_pos), int(p1_y_pos), paddle_width, paddle_height))
    pygame.draw.rect(screen, WHITE, (int(p2_x_pos), int(p2_y_pos), paddle_width, paddle_height))
    pygame.draw.circle(screen, WHITE,(ball_x_pos, ball_y_pos),ball_width)

    score = font.render(f"{str(p1_score)} - {str(p2_score)}", False, WHITE)
    screen.blit(score, (WIDTH / 2,30))

def apply_player_movement():
    global p1_y_pos, p2_y_pos

    if p1_up:
        p1_y_pos = max(p1_y_pos - player_speed, 0)
    if p1_down:
        p1_y_pos = min(p1_y_pos + player_speed, HEIGHT)
    if p2_up:
        p2_y_pos = max(p2_y_pos - player_speed, 0)
    if p2_down:
        p2_y_pos = min(p2_y_pos + player_speed, HEIGHT)


