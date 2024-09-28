import tkinter
from label import Label


def miles_to_kilometer():
    num = int(input.get()) * 1.609344
    label_3.config(text=f"{num:.2f}")


window = tkinter.Tk()
window.title("Conversor de Mi para Km")
window.config(padx=20, pady=20)

input = tkinter.Entry(width=7)
input.grid(column=2, row=0)

label_1 = Label(text="Mi.", column=3, row=0)
label_2 = Label(text="É igual a", column=0, row=1)
label_3 = Label(text="0", column=2, row=1)
label_4 = Label(text="Km.", column=3, row=1)

button = tkinter.Button(text="Calcular", command=miles_to_kilometer)
button.grid(column=2, row=2)

window.mainloop()
