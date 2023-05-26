from tkinter import *
import random as r


# functions
def destroy():
    window.destroy()
def game(usr_inp):
    pc_choices = ['Rock', 'Paper', "Scissor"]
    global pc_pick, n
    n = 0
    pc_pick = r.choices(pc_choices)
    win = 'You won | pc loses'
    lose = 'You lose | pc Won'
    tie = 'Its an Tie'
    pc_pick = pc_pick[0]
    print(pc_pick)
    if usr_inp == pc_pick:
        if usr_inp == 'Rock':
            label_pc.configure(image=rock_img)
            label_player.configure(image=rock_img)
        elif usr_inp == 'Scissor':
            label_pc.configure(image=scissor_img)
            label_player.configure(image=scissor_img)
        elif usr_inp == 'Paper':
            label_pc.configure(image=pap_img)
            label_player.configure(image=pap_img)
        print('Tie')
        label_pc.configure(text=pc_pick)
        label_player.configure(text=usr_inp)
        lbl_cmt.configure(text=tie)
        n = 1
    elif usr_inp == 'Rock':
        label_player.configure(image=rock_img)
        if pc_pick == 'Paper':
            print(lose)
            n = 2
            label_pc.configure(image=pap_img)
            lbl_cmt.configure(text=lose)
        elif pc_pick == 'Scissor':
            print(win)
            n = 3
            label_pc.configure(image=scissor_img)
            lbl_cmt.configure(text=win)
    elif usr_inp == 'Paper':
        label_player.configure(image=pap_img)
        if pc_pick == 'Rock':
            print(win)
            n = 3
            label_pc.configure(image=rock_img)
            lbl_cmt.configure(text=win)
        elif pc_pick == 'Scissor':
            print(lose)
            n = 2
            label_pc.configure(image=scissor_img)
            lbl_cmt.configure(text=lose)
    elif usr_inp == 'Scissor':
        label_player.configure(image=scissor_img)
        if pc_pick == 'Paper':
            print(win)
            n = 3
            label_pc.configure(image=pap_img)
            lbl_cmt.configure(text=win)
        elif pc_pick == 'Rock':
            print(lose)
            n = 2
            label_pc.configure(image=rock_img)
            lbl_cmt.configure(text=lose)
    print(n)
    
def move_app(e):
    window.geometry(f'+{e.x_root}+{e.y_root}')    
