from tkinter import *
import random
import time

my_book=Tk()
my_book.title('吃豆子')
my_canvas=Canvas(my_book,width=1000,height=1000,background='white')
my_canvas.pack()

food=[]

def pos_object(a):
    return my_canvas.coords(a)

wall1=my_canvas.create_rectangle(random.randint(0,500),random.randint(0,500),random.randint(0,500),random.randint(500,1000),fill='blue')
wall2=my_canvas.create_rectangle(random.randint(500,1000),random.randint(0,500),random.randint(500,1000),random.randint(500,1000),fill='blue')

text=my_canvas.create_text(980,20,text=str(len(food)))

def crash(pos_object1,pos_object2):
    if pos_object1[3] >= pos_object2[1] and pos_object1[1] <= pos_object2[3] and pos_object1[2] >= pos_object2[0] and pos_object1[0] <= pos_object2[3]:
        return True #重合
    else:
        return False #不重合

while len(food) < 9:
    x=random.randint(10,990)
    y=random.randint(10,990)
    pellet=my_canvas.create_oval(x,y,x+10,y+10,fill='yellow')
    
    if crash(pos_object(pellet),pos_object(wall1)) or crash(pos_object(pellet),pos_object(wall2)):
        my_canvas.delete(pellet)
        continue
    else:
        food.append(pellet)
        my_canvas.itemconfig(text,text=str(len(food)))
    


##state='r'
pac_man=my_canvas.create_arc(20,20,70,70,start=30,extent=300,fill='yellow',outline='orange')

def move(event):
            
    if event.keysym == "Up":
        my_canvas.itemconfig(pac_man,start=120)
        if (not crash(pos_object(pac_man),pos_object(wall1))) and (not crash(pos_object(pac_man),pos_object(wall2))):
            my_canvas.move(pac_man, 0, -10)
            

    elif event.keysym == "Down":
        my_canvas.itemconfig(pac_man,start=300)
        if (not crash(pos_object(pac_man),pos_object(wall1))) and (not crash(pos_object(pac_man),pos_object(wall2))):
            my_canvas.move(pac_man, 0, 10)

        
    elif event.keysym == "Left":
        my_canvas.itemconfig(pac_man,start=210)
        if (not crash(pos_object(pac_man),pos_object(wall1))) and (not crash(pos_object(pac_man),pos_object(wall2))):
            my_canvas.move(pac_man, -10, 0)

        
    elif event.keysym == "Right":
        my_canvas.itemconfig(pac_man,start=30)
        if (not crash(pos_object(pac_man),pos_object(wall1))) and (not crash(pos_object(pac_man),pos_object(wall2))):
            my_canvas.move(pac_man, 10, 0)

my_canvas.bind_all("<KeyPress-Up>",move) 
my_canvas.bind_all("<KeyPress-Down>",move)
my_canvas.bind_all("<KeyPress-Left>",move)
my_canvas.bind_all("<KeyPress-Right>",move)

for i in range(len(food)):
    if crash(pos_object(pac_man),pos_object(food[i])):
        my_canvas.delete(food[i])
        del food[i]
    if len(food) == 0:
        my_canvas.create_text(480,490,text='Yon Win!')
        break

        
##def up(event):
##    global state
##    if state !='u':
##        my_canvas.itemconfig(pac_man,start=120)
##        state='u'
##    my_canvas.move(pac_man,0,-10)
##my_canvas.bind_all('<Up>',up)
##state='u'
##def down(event):
##    global state
##    if state !='d':
##        my_canvas.itemconfig(pac_man,start=300)
##        state='d'
##    my_canvas.move(pac_man,0,10)
##my_canvas.bind_all('<Down>',down)
##def left(event):
##    global state
##    if state !='l':
##        my_canvas.itemconfig(pac_man,start=210)
##        state='l'
##    my_canvas.move(pac_man,-10,0)
##my_canvas.bind_all('<Left>',left)
##def right(event):
##    global state
##    if state !='r':
##        my_canvas.itemconfig(pac_man,start=30)
##        state='r'
##    my_canvas.move(pac_man,10,0)
##my_canvas.bind_all('<Right>',right)
##hideorshow=[0,0,0,0,0,0,0,0,0]
##while True:
##    bn=0
##    pos_pac_man=my_canvas.coords(pac_man)
##    for x in range(len(food)):
##        pos_food=my_canvas.coords(food[x])
##        if pos_pac_man[2]>pos_food[0] and pos_food[2]>pos_pac_man[0] and pos_pac_man[3]>pos_food[1] and pos_food[3]>pos_pac_man[1]:
##            my_canvas.itemconfig(food[x],state='hidden')
##            hideorshow[x]=1
##    for i in range(9):
##            if hideorshow[i]==0:
##                bn+=1
##    if bn==0:
##        win=my_canvas.create_text(100,100,text='You win!')
##    my_canvas.itemconfig(text,text=str(bn))
##    my_canvas.update()
##    time.sleep(0.01)
##
my_book.mainloop()
