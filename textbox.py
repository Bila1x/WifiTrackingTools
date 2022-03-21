from tkinter import *
import tkinter.ttk as ttk
import sys

def textbox(result):
    root = Tk()
    root.protocol("WM_DELETE_WINDOW", quit)

    def close(event):
        sys.exit()

    root.bind('<Escape>', close)

    w = 0
    lines = result.splitlines()
    for line in lines:
        if len(line) > w: w = len(line)

    S = ttk.Scrollbar(root)
    T = Text(root, bg='black', fg='white', insertbackground='white')
    S.pack(side=RIGHT, fill=Y)
    T.pack()
    T.insert(END, result)
    S.config(command=T.yview)
    T.config(yscrollcommand=S.set, font=('Consolas', 12), width=250, height=100)
    root.title('Query')
    root.wm_attributes('-toolwindow', 'True')
    if w < 20: w = 20
    if w > 190: w = 190
    width = w * 10
    if len(lines) < 20: h = 25 + int(len(lines)*24)
    else: h = 500
    height = h
    x = (root.winfo_screenwidth() // 2) - (width // 2)
    y = (root.winfo_screenheight() // 2) - (height // 2)
    root.geometry('{}x{}+{}+{}'.format(width, height, x, y))
    T.focus_set()
    mainloop()

if __name__ == '__main__':
    sys.exit()
