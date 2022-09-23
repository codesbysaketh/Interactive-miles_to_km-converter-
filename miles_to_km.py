import tkinter


def converter():
    output_box_km.config(text=f"{1.6*(int(input_box_m.get()))}")


window = tkinter.Tk()
window.title("Miles to Km Converter")
window.config(padx=20, pady=20)
window.minsize(width=250, height=140)

input_box_m = tkinter.Entry()
input_box_m.grid(column=1, row=0)

label1 = tkinter.Label(text="is equal to ")
label1.grid(column=0, row=1)

label_m = tkinter.Label(text="Miles")
label_m.grid(column=2, row=0)

label_km = tkinter.Label(text="Kilometers")
label_km.grid(column=2, row=1)

output_box_km = tkinter.Label(text="-")
output_box_km.grid(column=1, row=1)

button = tkinter.Button(text="calculate", command=converter)
button.grid(column=1, row=2)
button.config(width=7, height=1)

window.mainloop()
