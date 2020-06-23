from tkinter import *


def main():
    root = Tk()

    w = Canvas(
        root,
        width=200,
        height=200,
        background="white"
    )
    w.pack()

    w.create_text(100, 50, text='神農本草經')

    mainloop()
if __name__ == '__main__':
    main()