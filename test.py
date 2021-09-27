import time
import tkinter as tk


class MainFrame(tk.Frame):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.label = tk.Label(self, text='not running')
        self.label.pack()
        self.listbox = tk.Listbox(self)
        self.listbox.pack()
        self.button = tk.Button(
            self, text='blocking task', command=self.on_button)
        self.button.pack(pady=15)
        self.pack()

    def on_button(self):
        print('Button clicked')
        self.blocking_code()

    def blocking_code(self):
        self.label['text'] = 'running'

        for number in range(5):
            self.listbox.insert(tk.END, number)
            print(number)
            time.sleep(1)

        self.label['text'] = 'not running'


if __name__ == '__main__':
    app = tk.Tk()
    main_frame = MainFrame()
    app.mainloop()