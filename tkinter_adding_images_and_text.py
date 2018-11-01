from tkinter import *

from PIL import Image, ImageTk

class Window(Frame):

    def __init__(self, master = None):
        Frame.__init__(self, master)

        self.master = master

        self.init_window()

    def init_window(self):

        self.master.title("GUI")

        self.pack(fill=BOTH, expand=1)

        #quitButton = Button(self, text="Quit", command=self.client_exit)
        #quitButton.place(x=0, y=0)

        menu = Menu(self.master)
        self.master.config(menu=menu)

        file = Menu(menu)
        file.add_command(label='New File')
        file.add_command(label='Open')
        file.add_command(label='Save')
        file.add_command(label='Save as')
        file.add_command(label='Print Windows')
        file.add_command(label='Exit', command=self.client_exit)
        menu.add_cascade(label='File', menu=file)

        edit = Menu(menu)
        edit.add_command(label='Show Image', command=self.showImg)
        edit.add_command(label='Show Text', command=self.showTxt)
        edit.add_command(label='Undo')
        edit.add_command(label='Redo')
        edit.add_command(label='Cut')
        edit.add_command(label='Copy')
        edit.add_command(label='Paste')
        edit.add_command(label='Select All')
        edit.add_command(label='Find')
        menu.add_cascade(label='Edit', menu=edit)

        formatt = Menu(menu)
        formatt.add_command(label='Toggle Tabs')
        formatt.add_command(label='Indent Region')
        formatt.add_command(label='Dedent Region')
        formatt.add_command(label='Format Paragraph')
        formatt.add_command(label='New Indent')
        menu.add_cascade(label='Format', menu=formatt)

        run = Menu(menu)
        run.add_command(label='Python Shell')
        run.add_command(label='Rub Module')
        run.add_command(label='Check Module')
        menu.add_cascade(label='Run', menu=run)

        options = Menu(menu)
        options.add_command(label='Configure IDLE')
        options.add_command(label='Code Context')
        menu.add_cascade(label='Options', menu=options)

        window = Menu(menu)
        window.add_command(label='Zoom')
        menu.add_cascade(label='Window', menu=window)

        helps = Menu(menu)
        helps.add_command(label='About IDLE')
        helps.add_command(label='IDLE Help')
        helps.add_command(label='Python Docs')
        helps.add_command(label='Turtle Demp')
        menu.add_cascade(label='Help', menu=helps)

    def showImg(self):
        load = Image.open('pic.jpg')
        render = ImageTk.PhotoImage(load)

        img = Label(self, image=render)
        img.image = render
        img.place(x=0,y=0)

    def showTxt(self):
        text = Label(self, text='Hey it is awesome!')
        text.pack()
    def client_exit(self):
        exit()
        
root = Tk()
root.geometry("400x300")

app = Window(root)

root.mainloop()
