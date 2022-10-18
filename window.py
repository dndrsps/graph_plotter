import tkinter

class Window:

    def __init__(self):

        self.function_string = ['','']
        self.cons_a = 0
        self.cons_b = 0
        self.cons_c = 0
        self.cons_d = 0

        self.window = tkinter.Tk()
        self.window.title("Settings")
        self.slider = tkinter.Scale(self.window, from_=10, to=100, length=300, orient=tkinter.HORIZONTAL)
        self.window.geometry("500x150")
        label_1 = tkinter.Label(self.window, text="Size: ")
        label_2 = tkinter.Label(self.window, text="f(x) = ")
        label_3 = tkinter.Label(self.window, text="g(x) = ")
        label_4 = tkinter.Label(self.window, text="A = ")
        label_5 = tkinter.Label(self.window, text="B = ")
        label_6 = tkinter.Label(self.window, text="C = ")
        label_7 = tkinter.Label(self.window, text="D = ")
        entry_field_1 = tkinter.Entry(self.window, width=70)
        entry_field_2 = tkinter.Entry(self.window, width=70)
        entry_field_3 = tkinter.Entry(self.window, width=13)
        entry_field_4 = tkinter.Entry(self.window, width=13)
        entry_field_5 = tkinter.Entry(self.window, width=13)
        entry_field_6 = tkinter.Entry(self.window, width=13)
        def read_input():
            self.function_string[0] = entry_field_1.get()
            self.function_string[1] = entry_field_2.get()
            self.cons_a = entry_field_3.get()
            self.cons_b = entry_field_4.get()
            self.cons_c = entry_field_5.get()
            self.cons_d = entry_field_6.get()    
        entry_button_1 = tkinter.Button(self.window, text='Draw!', command = read_input)
        label_1.grid(row=0, column=0)
        self.slider.grid(row=0, column=1, columnspan=7)
        label_4.grid(row=1, column=0)
        label_5.grid(row=1, column=2)
        label_6.grid(row=1, column=4)
        label_7.grid(row=1, column=6)
        entry_field_3.grid(row=1, column=1)
        entry_field_4.grid(row=1, column=3)
        entry_field_5.grid(row=1, column=5)
        entry_field_6.grid(row=1, column=7)
        label_2.grid(row=2, column=0)
        label_3.grid(row=3, column=0)
        entry_field_1.grid(row=2, column=1, columnspan=7)
        entry_field_2.grid(row=3, column=1, columnspan=7)
        entry_button_1.grid(row=4, column=0, columnspan=8)
        

    def refresh(self):
        self.window.update()

    def get_data(self):

        return (self.function_string,
                self.cons_a,
                self.cons_b,
                self.cons_c,
                self.cons_d)


