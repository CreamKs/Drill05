import random

from pico2d import *

TUK_WIDTH, TUK_HEIGHT = 1280, 1024
open_canvas(TUK_WIDTH, TUK_HEIGHT)

TUK_ground = load_image('TUK_GROUND.png')
character = load_image('animation_sheet.png')
hand = load_image('hand_arrow.png')
def handle_events():
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False

def move_character(hx, hy):
    global x, y
    x = x +  math.cos(math.atan2(hy - y, hx - x))
    y = y +  math.sin(math.atan2(hy - y, hx - x))


running = True
hx, hy = random.randint(0, TUK_WIDTH), random.randint(0, TUK_HEIGHT)
x, y = 400, 300

frame = 0
hide_cursor()

while running:
    clear_canvas()
    TUK_ground.draw(TUK_WIDTH // 2, TUK_HEIGHT // 2)
    hand.draw(hx, hy)
    move_character(hx,hy)
    if x < hx:
        character.clip_draw(frame * 100, 100 * 1, 100, 100, x, y)
    elif x >= hx:
        character.clip_composite_draw((8 - frame) * 100, 100 * 1, 100, 100, 0, 'h', x, y, 100, 100)
    if hx - 1 <= x and x <= hx + 1 and hy - 1 <= y and y <= hy + 1:
        hx, hy = random.randint(0, TUK_WIDTH), random.randint(0, TUK_HEIGHT)
    update_canvas()
    frame = (frame + 1) % 8

    handle_events()

close_canvas()




