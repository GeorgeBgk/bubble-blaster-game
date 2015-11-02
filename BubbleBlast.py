from tkinter import *
HEIGHT = 500
WIDTH = 800
window = Tk()
instructions = Tk()
instructions.title('How to play')
w = Label(instructions, text="Control boat using arrows. ")
w.pack()
window.title("The Bubble Blaster Game (Охотник за пузырями)")
c = Canvas(window, width=WIDTH, height=HEIGHT,bg='darkblue')
c.pack()
ship1 = c.create_polygon(5, 5, 5, 25, 30, 15, fill='red')
ship2 = c.create_oval(0, 0, 30, 30, outline='red')
SHIP_R = 15
MID_X = 400
MID_Y = 250
c.move(ship1, MID_X, MID_Y)
c.move(ship2, MID_X, MID_Y)

SHIP_SPD = 3
def move_ship(event):
    if event.keysym == 'Up':
        c.move(ship1, 0, -SHIP_SPD)
        c.move(ship2, 0, -SHIP_SPD)
    elif event.keysym == 'Down':
        c.move(ship1, 0, SHIP_SPD)
        c.move(ship2, 0, SHIP_SPD)
    elif event.keysym == 'Left':
        c.move(ship1, -SHIP_SPD, 0)
        c.move(ship2, -SHIP_SPD, 0)
    elif event.keysym == 'Right':
        c.move(ship1, SHIP_SPD, 0)
        c.move(ship2, SHIP_SPD, 0)
c.bind_all('<Key>', move_ship)

from random import randint
bub_id = list()
bub_r = list()
bub_speed = list()
MIN_BUB_R = 10
MAX_BUB_R = 30
MAX_BUB_SPD = 10
GAP = 100
def create_bubble() :
    x = WIDTH + GAP
    y = randint(0, HEIGHT)
    r = randint(MIN_BUB_R, MAX_BUB_R)
    id1 = c.create_oval(x - r, y - r, x + r, y + r, outline='white')
    bub_id.append(id1)
    bub_r.append(r)
    bub_speed.append(randint(1, MAX_BUB_SPD))
def move_bubbles() :
    for i in range(len(bub_id)) :
        c.move(bub_id[i], -bub_speed[i], 0)
def get_coords(id_num) :
    pos = c.coords(id_num)
    x = (pos[0] + pos[2])/2
    y = (pos[1] + pos[3])/2
    return x, y
def del_bubble(i) :
    del bub_r[i]
    del bub_speed[i]
    c.delete(bub_id[i])
    del bub_id[i]
def clean_up_bubs() :
    for i in range(len(bub_id)-1, -1, -1) :
        x, y = get_coords(bub_id[i])
        if x < -GAP:
            del_bubble(i)
from math import sqrt
def distance(id1, id2):
    x1, y1 = get_coords(id1)
    x2, y2 = get_coords(id2)
    return sqrt((x2 - x1)**2 + (y2 - y1)**2)
def collision():
    points = 0
    for bub in range(len(bub_id)-1, -1, -1):
        if distance(ship2, bub_id[bub]) < (SHIP_R + bub_r[bub]):
            points += (bub_r[bub] + bub_speed[bub])
            del_bubble(bub)
    return points
from time import sleep, time

BUB_CHANCE = 30
scorewindow = Tk()
scorewindow.title('Scoreboard')
print('Init completed, starting main loop')
score = 0
scorelabel = Label(scorewindow, fg="black", font = "Helvetica 32 bold")
scorelabel.pack()
while True:
    if randint(1, BUB_CHANCE) == 1:
        create_bubble()
    move_bubbles()
    clean_up_bubs()
    score += collision()
    scorestring = "Score: " + str(score)
    #print(score)
    window.update()
    sleep(0.01)
    scorelabel.config(text=scorestring)
window.destroy()

