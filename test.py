import tkinter as tk
#from tkinter.ttk import Progressbar
#from tkinter import ttk
#import math
import random

class Player:
    objects ={(-1,-1)}
    
    def __init__(this,color):
        this.x,this.y = -1,-1
        while (this.x,this.y) in Player.objects:
            this.x = this.randomPoz(N_X)
            this.y = this.randomPoz(N_Y)
        Player.objects.add((this.x,this.y))
        this.color = color
        this.draw()
        
    def draw(this):
        this.player = canvas.create_oval((this.x,this.y),(this.x+step,this.y+step),fill=this.color)
        
    def randomPoz(this, top):
        return random.randint(1,top-1)*step

    def repaint(this, x, y):
        old_x, old_y = this.x, this.y
        this.x = (this.x +x)%(step*N_X)
        this.y = (this.y +y)%(step*N_Y)
        canvas.move(this.player,(this.x - old_x),(this.y-old_y))

class Semen(Player):
    def checkPos(this, other):
        return ((this.x == other.x) and (this.y == other.y))

    def __init__(this):
        this.x,this.y = -1,-1
        while (this.x,this.y) in Player.objects:
            this.x = this.randomPoz(N_X)
            this.y = this.randomPoz(N_Y)
        Player.objects.add((this.x,this.y))
        this.player = canvas.create_image((this.x, this.y),image=img, anchor='nw')
       

class Exit(Player):
     def __init__(this):
        this.x,this.y = -1,-1
        while (this.x,this.y) in Exit.objects:
            this.x = this.randomPoz(N_X)
            this.y = this.randomPoz(N_Y)
        Player.objects.add((this.x,this.y))
        this.player = canvas.create_image((this.x, this.y),image=save, anchor='nw') 

class Enemy(Player):
    def __init__(this):
        this.x,this.y = -1,-1
        while (this.x,this.y) in Enemy.objects:
            this.x = this.randomPoz(N_X)
            this.y = this.randomPoz(N_Y)
        Player.objects.add((this.x,this.y))
        this.player = canvas.create_image((this.x, this.y),image=png, anchor='nw')

class EnemyD(Enemy):
    def __init__(this):
        this.x,this.y = -1,-1
        while (this.x,this.y) in EnemyD.objects:
            this.x = this.randomPoz(N_X)
            this.y = this.randomPoz(N_Y)
        Player.objects.add((this.x,this.y))
        this.player = canvas.create_image((this.x, this.y),image=img1, anchor='nw')

    def randomStep(this):
        r = random.randint(1,4)
        if r == 1:
            super().repaint( step, 0)
        elif r == 2:
            super().repaint(-step, 0)
        elif r == 3:
            super().repaint( 0, step)
        else:
            super().repaint(0, -step)
            
class EnemyC(EnemyD):
    def __init__(this):
        this.x,this.y = -1,-1
        while (this.x,this.y) in EnemyC.objects:
            this.x = this.randomPoz(N_X)
            this.y = this.randomPoz(N_Y)
        Player.objects.add((this.x,this.y))
        this.player = canvas.create_image((this.x, this.y),image=img1, anchor='nw')

    def Phunter(this):
        if key == 87 or key == 38:
            super().repaint(0, -step)
        elif key == 83 or key == 40:
            super().repaint(0, -step)
        elif key == 65 or key == 37:
            super().repaint(-step, 0)
        elif key == 68 or key == 39:
            super().repaint(step, 0)

def keyPress(event):
    keys = {37,38,39,40,65,68,83,87}
    if event.keycode in keys:
        keyListener(event.keycode)
        enemiesStep()
        endGame()

def keyListener(key):
        if key == 87 or key == 38:
            player.repaint(0, -step)
        elif key == 83 or key == 40:
            player.repaint(0, step)
        elif key == 65 or key == 37:
            player.repaint(-step, 0)
        elif key == 68 or key == 39:
            player.repaint(step, 0)

def enemiesStep():
    for Enemy in enemies_d:    
        Enemy.randomStep()

def endGame():
    if player.checkPos(exit_g):
        print('YOU WON!')
        root.destroy()
        print('Game over')
    enemies = enemies_d + enemies_s + enemies_c
    for enemy in enemies:
        if player.checkPos(enemy):
            print('YOU DIED!')
            root.destroy()
            print('Game over')
            break

def addEnemies():
    for i in range(5):
        enemy = Enemy()
        enemies_s.append(enemy)
    for i in range(3):
        enemy = EnemyD()
        enemies_d.append(enemy)
    for i in range(2):
        enemy = EnemyC()
        enemies_c.append(enemy)
    
root = tk.Tk()
step = 60
N_X = 10
N_Y = 10
enemies_c = []
enemies_s = []
enemies_d = []
canvas = tk.Canvas(root,bg='#00FFFF',height = step*N_X,width=step*N_Y)

img = tk.PhotoImage(file='images\catcher.png')
img1 = tk.PhotoImage(file='images\dog.png')
save = tk.PhotoImage(file='images\exit.png')
png = tk.PhotoImage(file='images\cow.png')

addEnemies()
player = Semen()
exit_g = Exit()

#style = ttk.Style()
#style.theme_use('default')
#style.configure("red.Horizontal.TProgressbar", background='red')
#bar = Progressbar(root, length=350, style='red.Horizontal.TProgressbar')
#bar['value'] = 100
#bar.grid(column=0, row=0)

canvas.pack()
root.bind('<KeyPress>', keyPress)
root.mainloop()
exit()
