import tkinter as tk
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

class Exit(Player):
    def __init__(this):
       super().__init__('#F0FC53') 

class Enemy(Player):
    def __init__(this, color = 'red'):
       super().__init__(color)

class EnemyD(Enemy):
    def __init__(this):
       super().__init__('pink')

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

class Semen(Player):
    def checkPos(this, other):
        return ((this.x == other.x) and (this.y == other.y))

    def __init__(this):
       super().__init__('#32F366')
       
def keyPress(event):
    print(event)
    keys = {37,38.39,40,65,68,83,87}
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
        print('Game over')
    enemies = enemies_d + enemies_s
    for enemy in enemies:
        if player.checkPos(enemy):
            print('YOU DIED!')
            print('Game over')
            break

def addEnemies():
    for i in range(10):
        enemy = Enemy()
        enemies_s.append(enemy)
    for i in range(6):
        enemy = EnemyD()
        enemies_d.append(enemy)
    
master = tk.Tk()
step = 60
N_X = 10
N_Y = 10
enemies_s = []
enemies_d = []
canvas = tk.Canvas(master,bg='#00FFFF',height = step*N_X,width=step*N_Y)

addEnemies()
player = Semen()
exit_g = Exit()

canvas.pack()
master.bind('<KeyPress>', keyPress)
master.mainloop()
