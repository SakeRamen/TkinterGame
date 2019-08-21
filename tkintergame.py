import tkinter as tk
import random

class Player:

    def __init__(this, color):
        this.x = this.randomPoz(N_X)
        this.y = this.randomPoz(N_Y)
        this.color = color

    def draw(this):
        this.player = canvas.create_oval((this.x,this.y),(this.x+step,this.y+step),fill=this.color)
        
    def randomPoz(this, top):
        return random.randint(1,top-1)*step

    def repaint(this, x, y):
        canvas.move(this.player, x, y)

    def checkPos(this, other):
        return ((this.x == other.x) and (this.y == other.y))

def keyPress(event):
    if event.keycode == 87:
        player.y -= step
        player.repaint(0, -step)
    elif event.keycode == 83:
        player.y += step
        player.repaint(0, step)
    elif event.keycode == 65:
        player.x -= step
        player.repaint(-step, 0)
    elif event.keycode == 68:
        player.x += step
        player.repaint(step, 0)
    endGame()

def endGame():
    if player.checkPos(exit_g):
        print('Game over')
        print('You won!')

    
master = tk.Tk()
step = 60
N_X = 10
N_Y = 10
canvas = tk.Canvas(master,bg='#6BE0E7',height = step*N_X,width=step*N_Y)

player = Player('#29D6DA')
player.draw();
exit_g = Player('#F7F8A2')
exit_g.draw();

canvas.pack()
master.bind('<KeyPress>', keyPress)
master.mainloop()
