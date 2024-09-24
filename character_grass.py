from pico2d import *
import math



open_canvas()

grass = load_image('grass.png')
character = load_image('character.png')

grass.draw_now(400, 30)
character.draw_now(400, 90)

x = 400
y = 90
z = 270
move = 5
while True:
    clear_canvas_now()
    grass.draw_now(400, 30)
    character.draw_now(x, y)
    if move == 0:
        if x > 780:
            move = 1
        else:
            x = x + 2
    elif move == 1:
        if y > 560:
            move = 2
        else:
            y = y + 2
    elif move == 2:
        if x < 20:
            move = 3
        else:
            x = x - 2
    elif move == 3:
        if y <= 90:
            move = 4
        else:
            y = y - 2
    elif move == 4:
        if x >= 400:
            move = 5
        else:
            x = x + 2
    elif move == 5:
        if x > 800:
            move = 6
            z = 180
        else:
            x = x + 2
            y = y + (math.sin(z / 360 * 2 * math.pi) + 1)
            z = z + 1
    elif move == 6:
        if x < 400:
            move = 7
            z = 90
        else:
            x = x - 2
            y = y + (math.sin(z / 360 * 2 * math.pi) + 1)
            z = z -1
    elif move == 7:
        if x <= 0:
            move = 8
            z = 180
        else:
            x = x - 2
            y = y - (math.sin(z / 360 * 2 * math.pi) + 1)
            z = z - 1
    elif move == 8:
        if x >= 400:
            move = 0
            x = 400
            y = 90
            z = 270
        else:
            x = x + 2
            y = y + (math.sin(z / 360 * 2 * math.pi) + 1)
            z = z + 1
    delay(0.01)

    

close_canvas()
