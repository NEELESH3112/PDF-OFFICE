from tkinter import *
from PIL import ImageTk, Image, ImageFilter
from PIL import ImageEnhance
from tkinter import filedialog
import tkinter.messagebox as tmg

rot = 1
flipp = 1

def harry(event):
    pass

class imageedi:
    def __init__(self):
        self.bt1 = None
        self.bt2 = None
        self.bt3 = None
        self.bt5 = None
        self.bt6 = None
        self.bt7 = None
        self.bt8 = None
        self.bt9 = None
        self.bt10 = None
        self.bt11 = None
        self.bt12 = None
        self.bt13 = None
        self.save = None
        self.filex = None
        self.open_image = None
        self.root = Tk()
        self.root.title("BUILD 2 LEARN PDF OFFICE")
        self.root.geometry("1240x660")
        self.root.iconbitmap("3.ico")
        self.root.resizable(width=False, height=False)
        self.imgg = Image.open("Background 3.png")
        self.img = self.imgg.resize((1240, 660))
        self.img = ImageTk.PhotoImage(self.img)
        self.my_canvas = Canvas(self.root)
        self.my_canvas.place(x=0, y=0, relheight=1, relwidth=1)
        self.my_canvas.create_image(0, 0, image=self.img, anchor="nw")
        self.b1 = Button(self.root, text='START EXPLORING', bg='sky blue',command=self.mainpg, height=2, width=20,
                         font="Helvetica 16 bold")
        self.b1.place(x=920, y=150)
        self.root.bind('<Button-1>', harry)
        self.root.mainloop()

    def filt(self, filte):
        global saveimg
        global originalimg
        self.fimg = originalimg.resize((500, 500))
        self.fimg = self.fimg.filter(filte)
        saveimg = self.fimg.copy()
        self.fimg = ImageTk.PhotoImage(self.fimg)
        self.panel = Label(self.root, image=self.fimg)
        self.panel.image = self.fimg
        self.panel.place(x=700, y=50)
        originalimg = saveimg.copy()

    def orgim(self):
        global saveimg
        self.orgi = Image.open(self.filex)
        self.orgi = self.orgi.resize((500, 500))
        saveimg = self.orgi.copy()
        self.orgi = ImageTk.PhotoImage(self.orgi)
        self.panel = Label(self.root, image=self.orgi)
        self.panel.image = self.orgi
        self.panel.place(x=700, y=50)

    def mainpg(self, main=0):
        global saveimg
        self.my_canvas.delete("all")
        self.b1.place_forget()
        self.imgg1 = Image.open('mainbackground.png')
        self.img1 = self.imgg1.resize((1240, 660), Image.ANTIALIAS)
        self.img1 = ImageTk.PhotoImage(self.img1)
        self.my_canvas = Canvas(self.root)
        self.my_canvas.place(x=0, y=0, relheight=1, relwidth=1)
        self.my_canvas.create_image(0, 0, image=self.img1, anchor="nw")
        self.my_canvas.create_rectangle(700, 50, 1200, 550, fill="")
        self.my_canvas.place()
        if (main == 0):
            self.uploadbut = Button(self.root, text='UPLOAD FILE', command=self.open_image, height=2, width=12,
                                    font="Helvetica 10 bold")
            self.uploadbut.place(x=926, y=264)
        elif (main == 1):
            self.open_file(2)
        elif (main == 2):
            self.uploadbut = Button(self.root, text='UPLOAD FILE', command=self.open_image, height=2, width=12,
                                    font="Helvetica 10 bold")
            self.uploadbut.place(x=926, y=264)
            saveimg = 0
        self.f1 = Image.open('7.png')
        self.f1 = self.f1.resize((90,90), Image.ANTIALIAS)
        self.f1 = ImageTk.PhotoImage(self.f1)
        self.bt1 = Button(self.root, text='PDF TO WORD', image=self.f1, command=self.bt1, height=100, width=90,
                                font="Helvetica 10 bold", compound=TOP)
        self.bt1.place(x=370, y=230)
        self.f2 = Image.open('6.png')
        self.f2 = self.f2.resize((85, 85), Image.ANTIALIAS)
        self.f2 = ImageTk.PhotoImage(self.f2)
        self.bt2 = Button(self.root, text='JPG TO PDF', image=self.f2, command=self.bt2, height=100, width=90,
                                font="Helvetica 10 bold", compound=TOP)
        self.bt2.place(x=370, y=50)
        self.f3 = Image.open('5.png')
        self.f3 = self.f3.resize((85, 85), Image.ANTIALIAS)
        self.f3 = ImageTk.PhotoImage(self.f3)
        self.bt3 = Button(self.root, text='PNG TO PDF', image=self.f3, command=self.bt3, height=100, width=90,
                              font="Helvetica 10 bold", compound=TOP)
        self.bt3.place(x=200, y=50)
        self.f4 = Image.open('saveimage.png')
        self.f4 = self.f4.resize((85, 85), Image.ANTIALIAS)
        self.f4 = ImageTk.PhotoImage(self.f4)
        self.savebut = Button(self.root, text='SAVE', image=self.f4, command=self.save, height=100, width=90,
                              font="Helvetica 10 bold", compound=TOP)
        self.savebut.place(x=200, y=230)
        self.removebut = Button(self.root, text='REMOVE FILE', command=lambda: self.mainpg(2), height=1, width=12,
                                font="Helvetica 10 bold", compound=TOP)
        self.removebut.place(x=1000, y=600)
        self.f5 = Image.open('9.png')
        self.f5 = self.f5.resize((85, 85), Image.ANTIALIAS)
        self.f5 = ImageTk.PhotoImage(self.f5)
        self.bt5 = Button(self.root, text='EXCEL TO PDF', image=self.f5, command=self.bt5, height=100,
                                width=90, font="Helvetica 10 bold", compound=TOP)
        self.bt5.place(x=200, y=410)

        self.f6 = Image.open('8.png')
        self.f6 = self.f6.resize((85, 85), Image.ANTIALIAS)
        self.f6 = ImageTk.PhotoImage(self.f6)
        self.bt6 = Button(self.root, text='PDF TO PPT', image=self.f6, command=self.bt6, height=100,
                                  width=90, font="Helvetica 10 bold", compound=TOP)
        self.bt6.place(x=370, y=410)

        self.f7 = Image.open('10.png')
        self.f7 = self.f7.resize((85, 85), Image.ANTIALIAS)
        self.f7 = ImageTk.PhotoImage(self.f7)
        self.bt7 = Button(self.root, text='E SIGN PDF', image=self.f7, command=self.bt7, height=100,
                                  width=90, font="Helvetica 10 bold", compound=TOP)
        self.bt7.place(x=525, y=50)

        self.f8 = Image.open('11.jpg')
        self.f8 = self.f8.resize((85, 85), Image.ANTIALIAS)
        self.f8 = ImageTk.PhotoImage(self.f8)
        self.bt8 = Button(self.root, text='UNLOCK PDF', image=self.f8, command=self.bt8, height=100,
                          width=90, font="Helvetica 10 bold", compound=TOP)
        self.bt8.place(x=525, y=230)

        self.f9 = Image.open('12.jpg')
        self.f9 = self.f9.resize((85, 85), Image.ANTIALIAS)
        self.f9 = ImageTk.PhotoImage(self.f9)
        self.bt9 = Button(self.root, text='MERGE PDF', image=self.f9, command=self.bt9, height=100,
                          width=90, font="Helvetica 10 bold", compound=TOP)
        self.bt9.place(x=525, y=410)

        self.f10 = Image.open('12.jpg')
        self.f10 = self.f10.resize((85, 85), Image.ANTIALIAS)
        self.f10 = ImageTk.PhotoImage(self.f10)
        self.bt10 = Button(self.root, text='MERGE PDF', image=self.f10, command=self.bt10, height=100,
                          width=90, font="Helvetica 10 bold", compound=TOP)
        self.bt10.place(x=525, y=410)

        self.f11 = Image.open('13.png')
        self.f11 = self.f11.resize((85, 85), Image.ANTIALIAS)
        self.f11 = ImageTk.PhotoImage(self.f11)
        self.bt11 = Button(self.root, text='YTDOWNLOAD', image=self.f11, command=self.bt11, height=100,
                           width=90, font="Helvetica 10 bold", compound=TOP)
        self.bt11.place(x=35, y=50)

        self.f12 = Image.open('14.jpg')
        self.f12 = self.f12.resize((85, 85), Image.ANTIALIAS)
        self.f12 = ImageTk.PhotoImage(self.f12)
        self.bt12 = Button(self.root, text='WORD TO PDF', image=self.f12, command=self.bt12, height=100,
                           width=90, font="Helvetica 10 bold", compound=TOP)
        self.bt12.place(x=35, y=225)

        self.f13 = Image.open('15.png')
        self.f13 = self.f13.resize((85, 85), Image.ANTIALIAS)
        self.f13 = ImageTk.PhotoImage(self.f13)
        self.bt13 = Button(self.root, text='IMAGE - ICON', image=self.f13, command=self.bt13, height=100,
                           width=90, font="Helvetica 10 bold", compound=TOP)
        self.bt13.place(x=35, y=410)

    def open_file(self, param):
        pass


if __name__ == '__main__':
    gu = imageedi()

