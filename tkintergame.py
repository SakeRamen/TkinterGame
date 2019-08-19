import tkinter as tk
import random

def randomPoz(top):
    return random.randint(1,top-1)*step
    
master = tk.Tk()
step = 60
N_X = 10
N_Y = 10
canvas = tk.Canvas(master,bg='#BACE72',height = step*N_X,width=step*N_Y)

player_pos = (randomPoz(N_X), randomPoz(N_Y))
exit_pos   = (randomPoz(N_X), randomPoz(N_Y))
