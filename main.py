import turtle
import time
import random

width, height = 1000, 1000
colors = ['red','green','orange','black','blue','yellow','purple','pink','magenta','cyan']
def init_racers():

    screen = turtle.Screen()
    screen.setup(width, height)
    screen.title('Race')
    screen.bgcolor('grey')



def get_racer_num():

    while True:
        racers=input('Enter the number of racers (2 - 10): ')

        if racers.isdigit() and 2 <= int(racers) <= 10:
            racers = int(racers)

            return racers
        else:
            print('Please enter an int value within range 2-10')
            continue

def create_racer(colors):
    racers=[]
    spacing_y=height // (len(colors)+1)

    for i,color in enumerate(colors):
        racer = turtle.Turtle()
        racer.color(color)
        racer.shape('arrow')
        racer.penup()
        racer.setpos(-width//2+20,-height//2+(spacing_y)*(i+1))
        racer.pendown()
        racers.append(racer)

    return racers

def race(colors):
    racers= create_racer(colors)
    finish= turtle.Turtle()
    finish.penup()
    finish.color('black')
    finish.shape('circle')
    finish.setpos((width//2-20),height//2)
    finish.speed(4)
    finish.right(90)
    finish.pendown()
    finish.forward(width)
    while True:
        for racer in racers:
            distance= random.randrange(1,20)
            racer.stamp()
            racer.forward(distance)
            x,y=racer.pos()
            if x>=width//2-20:
                return  colors[racers.index(racer)].upper()



racers = get_racer_num()
init_racers()
random.shuffle(colors)
colors = colors[:racers]

winner=race(colors)
print(winner+" Wins!")
time.sleep(5)
