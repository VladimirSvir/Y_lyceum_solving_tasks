import os
import sys

import pygame
import requests

print('введите координаты')
first_input = float(input())
second_input = float(input())
zoom = float(input())

map_request = f"http://static-maps.yandex.ru/1.x/?ll={first_input},{second_input}8&spn={zoom},{zoom}&l=map"
response = requests.get(map_request)

if not response:
    print("Ошибка выполнения запроса:")
    print(map_request)
    print("Http статус:", response.status_code, "(", response.reason, ")")
    sys.exit(1)

map_file = "map.png"
with open(map_file, "wb") as file:
    file.write(response.content)

pygame.init()
screen = pygame.display.set_mode((600, 450))
screen.blit(pygame.image.load(map_file), (0, 0))
pygame.display.flip()
while pygame.event.wait().type != pygame.QUIT:
    pass
pygame.quit()

os.remove(map_file)