from tkinter import Tk, messagebox, font, Label, Entry, Button

print('ask the expert - type word in bahasa')
root = Tk()
root.withdraw()
        
the_world = {}

def read_from_file():
    with open('Exam/translator.txt') as file:
        for line in file:
            line = line.rstrip('\n')
            bahasa, english = line.split('/')
            the_world[bahasa] = english
read_from_file()
print(the_world)

def write_to_file(indonesia, english):
    with open('Exam/translator.txt', 'a') as file:
        file.write('\n' + indonesia + '/' + english)


def custom_askstring(
    title,
    prompt,
    dialog_size="500x100",
    bg_color="lightblue",
    font_size=13,
    font_weight="bold"
):
    dialog = Tk()
    dialog.title(title)
    dialog.configure(bg=bg_color)

    custom_font = font.Font(size=font_size, weight=font_weight)

    label = Label(dialog, text=prompt, bg=bg_color)
    label.configure(font=custom_font)
    label.pack()

    entry = Entry(dialog, font=custom_font)
    entry.pack()

    def ok():
        dialog.result = entry.get()
        dialog.destroy()
    button = Button(dialog, text="OK", command=ok, bg=bg_color, font=custom_font)
    button.pack()
    dialog.geometry(dialog_size)
    dialog.eval('tk::PlaceWindow . center')

    entry.focus_set()

    dialog.wait_window()

    try:
        return dialog.result
    except AttributeError:
        return ""

while True:
    query_bahasa_input = custom_askstring(
        "translate",
        "type word in bahasa",
        dialog_size="500x200",
        font_size=14,
        bg_color="lightgreen"
    )

    if query_bahasa_input:
        query_bahasa = query_bahasa_input.lower()


        if query_bahasa in the_world:
            result = the_world[query_bahasa]


            messagebox.showinfo(
                "Answer",
                "The english of "
                + query_bahasa
                + " is "
                + result
                + "!"
            )
        else:
            new_bahasa = custom_askstring(
                "English of",
                "Teach me " +
                "I don't know the english of  " 
                + query_bahasa 
                +"?", 
                dialog_size="500x200",
                    bg_color="lightblue",
                    font_size=13,
                    font_weight="bold"
            )

            the_world[query_bahasa] = new_bahasa
            write_to_file(query_bahasa, new_bahasa)