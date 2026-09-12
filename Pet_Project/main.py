from tkinter import HIDDEN, NORMAL, Tk, Canvas
root = Tk()
root.title("screen pet")

c = Canvas(root, width=400, height=400, bg='dark blue',highlightthickness=0)
c.pack()

c.body_color = 'skyblue1'
body = c.create_oval(35, 20, 365, 350, outline=c.body_color, fill=c.body_color)

eye_left = c.create_oval(130, 110, 160, 170, outline='black', fill='white')
eye_right = c.create_oval(230, 110, 260, 170, outline='black', fill='white')
pupil_left = c.create_oval(140, 145, 150, 155, outline='black', fill='black')
pupil_right = c.create_oval(240, 145, 250, 155, outline='black', fill='black')

mouth_normal = c.create_line(170, 250, 200, 272, 230, 250, smooth=1, width=2, state=NORMAL)
mouth_happy = c.create_line(170, 250, 200, 282, 230, 250, smooth=1, width=2, state=HIDDEN)
mouth_sad = c.create_line(170, 250, 200, 232, 230, 250, smooth=1, width=2, state=HIDDEN)

tounge_main = c.create_rectangle(170, 250, 230, 290, outline='red', fill='red', state=HIDDEN)
tounge_tip = c.create_oval(170, 285, 230, 300, outline='red', fill='red', state=HIDDEN)

cheek_left = c.create_oval(70, 180, 120, 230, outline='pink', fill='pink', state=HIDDEN)
cheek_right = c.create_oval(280, 180, 330, 230, outline='pink', fill='pink', state=HIDDEN)

def toggle_eyes():
    current_color = c.itemcget(eye_left, 'fill')
    new_color = c.body_color if current_color == 'white' else 'white'
    current_state = c.itemcget(pupil_left, 'state')
    new_state = NORMAL if current_state == HIDDEN else HIDDEN
    c.itemconfigure(pupil_left, state=new_state)
    c.itemconfigure(pupil_right, state=new_state)
    c.itemconfigure(eye_left, fill=new_color)
    c.itemconfigure(eye_right, fill=new_color)

def blink():
    toggle_eyes()
    root.after(250, toggle_eyes)
    root.after(3000, blink)

root.after(1000, blink)

def show_happy(event):
    if (20 <= event.x <=350) and (20 <= event.y <=350):
        c.itemconfigure(cheek_left, state=NORMAL)
        c.itemconfigure(cheek_right, state=NORMAL)
        c.itemconfigure(mouth_happy, state=NORMAL)
        c.itemconfigure(mouth_normal, state=HIDDEN)
        c.itemconfigure(mouth_sad, state=HIDDEN)
        c.happy_level = 1
    
c.bind('<Motion>', show_happy)

def hide_happy(event):
    if (20 <= event.x <=350) and (20 <= event.y <=350):
        c.itemconfigure(cheek_left, state=HIDDEN)
        c.itemconfigure(cheek_right, state=HIDDEN)
        c.itemconfigure(mouth_happy, state=HIDDEN)
        c.itemconfigure(mouth_normal, state=NORMAL)
        c.itemconfigure(mouth_sad, state=HIDDEN)
        return


def sad():
    if c.happy_level == 0:
        c.itemconfigure(mouth_happy, state=HIDDEN)
        c.itemconfigure(mouth_normal, state=HIDDEN)
        c.itemconfigure(mouth_sad, state=NORMAL)
    else:
        c.happy_level -= 1
    root.after(4000, sad)    

def toggle_tounge():
    if not c.tongue_out:
        c.itemconfigure(tounge_tip, state=NORMAL)
        c.itemconfigure(tounge_main, state=NORMAL)
        c.tongue_out = True
    else:
        c.itemconfigure(tounge_tip, state=HIDDEN)
        c.itemconfigure(tounge_main, state=HIDDEN)
        c.tongue_out = False

c.eyes_crossed = False
def toggle_pupil():
    if not c.eyes_crossed:
        c.move(pupil_left, 10, -5)
        c.move(pupil_right, -10, -5)
        c.eyes_crossed = True
    else:
        c.move(pupil_left, -10, 5)
        c.move(pupil_right, 10, 5)
        c.eyes_crossed = False

def cheeky(event):
    toggle_tounge()
    toggle_pupil()
    hide_happy(event)
    root.after(1000, toggle_tounge)
    root.after(1000, toggle_pupil)       
    return

left_ear = c.create_polygon(
    100, 180,
    30, -1,
    120, 88,
    fill="skyblue1",
    outline="skyblue1"
)

# Telinga kanan
right_ear = c.create_polygon(
    275, 180,
    350, -1,
    250, 88,
    fill="skyblue1",
    outline="skyblue1"
)

c.bind('<Double-1>', cheeky)                                      

root.after(1000, sad)

c.tongue_out = False



c.bind('<Leave>', hide_happy)

c.happy_level = 1

            
root.mainloop()