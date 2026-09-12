from tkinter import Tk, messagebox, font, Label, Entry, Button

print('ask the expert - type word in bahasa')
root = Tk()
root.withdraw()
        
the_world = {}

def read_from_file():
    with

def custom_askstring(
    title,
    prompt,
    dialog_size="500x500",
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
        dialog_size="500x500",
        font_size=14,
        bg_color="lightgreen"
    )

    if query_bahasa_input:
        query_bahasa = query_bahasa_input.capitalize()


        if query_bahasa in the_world:
            result = the_world[query_bahasa]


            messagebox.showinfo(
                "Answer"
                "the bahasa"
                + query_bahasa
                + " is "
                + result
                + "!"
            )