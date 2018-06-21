import tkinter as tk
import random

root = tk.Tk()
img1 = tk.PhotoImage(file = "rock.png")
img2 = tk.PhotoImage(file = "paper.png")
img3 = tk.PhotoImage(file = "scissor.png")
list1 = ['Rock','Paper','Scissor']
temp='xyz'

def countdown(count):
    # change text in label        
    label['text'] = "Wait for "+str(count)+" Sec  : "
    
    
    if count >= 0:
        # call countdown again after 1000ms (1s)
        root.after(1000, countdown, count-1)
    else :
        temp=display()
        f_read = open("temp.txt", "r")
        last_line = f_read.readlines()[-1]
        f_read.close()
        if temp == last_line.strip():
            label2['text']='DRAW!!'
        elif ((temp=='Scissor') and ('Rock' in last_line.strip())) or ((temp=='Rock') and ('Paper' in last_line.strip())) or ((temp=='Paper') and ('Scissor' in last_line.strip())):
            label2['text']='YOU WON!!'
        elif (last_line.strip()=='empty') or (last_line.strip()=='Invalid') :
            label2['text']='Invalid input'
        else:
            label2['text']=temp
        countdown(5)
        
label = tk.Label(root)
label1 = tk.Label(root)
label.place(x=35, y=10)
label1.place(x=35, y=40)
label2=tk.Label(root)
label2.place(x=35,y=70)

# call countdown first time    
countdown(5)

# root.after(0, countdown, 5) 

def display():
    temp = random.choice(list1)
    if temp=='Rock':
        label1['image']=img1
    elif temp=='Paper':
        label1['image']=img2
    else:
        label1['image']=img3
    return temp
    
root.mainloop()