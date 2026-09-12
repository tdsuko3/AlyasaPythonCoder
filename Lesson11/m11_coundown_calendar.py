from tkinter import Tk, Canvas  
from datetime import datetime

root = Tk()
c = Canvas(root, width=800, height=500, bg='green')
c.pack()
c.create_text(100, 50, anchor='w', fill='orange', font='arial 28 underline', text = 'my coundown calendar')

root.mainloop()

def get_event():
    list_event = []
    with open('m11_event.txt') as file:
        for line in line:
            line = line.rstrip('\n')
            current_event = line.split(',')
            event_date = datetime.strptime(current_event[1], '%d/%m/%y')
            current_event = 