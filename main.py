import tkinter as tk


class App(tk.Tk):
    def __init__(self):
        super().__init__()

        self.radio_value = tk.IntVar()

        self.title("conversion")

        self.upper_frame = tk.Frame(self, bg="black")
        self.upper_frame.pack()

        radio_one = tk.Radiobutton(self.upper_frame, text='2進数',
                                   variable=self.radio_value, value=1)
        radio_two = tk.Radiobutton(self.upper_frame, text='8進数',
                                   variable=self.radio_value, value=2)
        radio_three = tk.Radiobutton(self.upper_frame, text='16進数',
                                     variable=self.radio_value, value=3)
        button = tk.Button(self.upper_frame, text="変換", command=self.clicked)

        radio_one.pack(side=tk.LEFT)
        radio_two.pack(side=tk.LEFT)
        radio_three.pack(side=tk.LEFT)
        button.pack(side=tk.LEFT, pady=5, padx=5)

        self.lower_frame = tk.Frame(self, bg="black")
        self.entry = tk.Entry(self.lower_frame, font=("", 25), justify="center")
        self.entry.pack()
        self.lower_frame.pack()

    def clicked(self):
        i = int(self.entry.get())
        n = self.radio_value.get()

        if n == 1:
            self.entry.delete(0, tk.END)
            self.entry.insert(tk.END, bin(i))
        elif n == 2:
            self.entry.delete(0, tk.END)
            self.entry.insert(tk.END, oct(i))
        elif n == 3:
            self.entry.delete(0, tk.END)
            self.entry.insert(tk.END, hex(i))
        else:
            return


if __name__ == "__main__":
    app = App()
    app.mainloop()
