from tkinter import *
from tkinter import messagebox
from tkinter import scrolledtext
import pyperclip
import tkinter.ttk as ttk

def textbox(result):
    root = Tk()
    #root.attributes("-toolwindow", 1)
    #root.resizable(1, 0)
    #ttk.Style().configure("BW.TLabel", foreground="white", background="black")
    root.protocol("WM_DELETE_WINDOW", quit)
    def close(event):
        if pyperclip.paste() == result:
            root.clipboard_clear()
            pyperclip.copy(result)
            pyperclip.paste()
            root.update()
            root.destroy()
        #root.withdraw() # if you want to bring it back
        sys.exit() # if you want to exit the entire thing

    root.bind('<Escape>', close)

    #root.withdraw()
    # try:
    #     MACS = root.clipboard_get().upper().splitlines()
    # except:
    #     messagebox.showerror("MACresolver", 'Error reading the Clipboard')
    #     quit()

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
    T.config(yscrollcommand=S.set, font=('Consolas', 12), width=250, height=50)
    #T.tag_add("here", "1.0", END)
    #T.tag_config("here", background="black", foreground="white")
    #root.update_idletasks()
    root.title(__name__)
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
# if __name__ == '__main__':
#     sys.exit(main())