from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from PIL import ImageTk, Image, ImageFilter
from tkPDFViewer import tkPDFViewer as pdfviewer
import pyttsx3
import PyPDF2
from fpdf import FPDF
import tkinter.messagebox as tmg
from fpdf import FPDF

def position(event):
    x,y=event.x,event.y
    print("x={},y={}".format(x,y))

def bgimagedit(imgaddress):
    imgeddit = Image.open(imgaddress)
    imgeddit = imgeddit.resize((1240, 660))
    imgeddit = ImageTk.PhotoImage(imgeddit)
    return(imgeddit)

class mainwin:
    def __init__ (self):
        #some needed variable
        self.pdfviewnum=0
        self.amain=0
        #windows
        self.root=Tk()
        self.root.geometry("500x500")
        self.root.title("BUILD 2 LEARN PDF OFFICE CONVERTER")
        self.root.geometry("1240x660")
        self.root.iconbitmap("3.ico")
        self.my_canvas = Canvas(self.root)
        self.root.bind('<Button-1>',position)
        self.startingpg()
        self.root.mainloop()
    def openfilename(self):  
        self.filename = filedialog.askopenfilename(title ='pen')
        return self.filename
    def mulfilename(self):
        mulfile = filedialog.askopenfilenames(parent=self.root,title='Choose a file')
        return(mulfile)
    def outputfilename(self):
        savefile = filedialog.asksaveasfile(defaultextension=".pdf")
        return(savefile.name)
    def buttonimgedd(self,butimgaddress,size):
        self.buttonimgedit = Image.open(butimgaddress)
        self.buttonimgedit = self.buttonimgedit.resize((size,size), Image.ANTIALIAS)
        self.buttonimgedit = ImageTk.PhotoImage(self.buttonimgedit)
        return(self.buttonimgedit)
    def startingpg(self):
        self.my_canvas = Canvas(self.root)
        self.my_canvas.place(x=0, y=0, relheight=1, relwidth=1)
        self.bgimg =bgimagedit("Background 3.png")
        self.my_canvas.create_image(0, 0, image=self.bgimg, anchor="nw")
        self.my_canvas.place()
        self.startbut=Button(self.root, text='START EXPLORING', bg='sky blue',command=self.frontpage, height=2, width=20,
                         font="Helvetica 16 bold")
        self.startbut.place(x=920, y=150)

    def frontpage(self):
        self.my_canvas.delete("all")
        self.startbut.place_forget()
        if (self.amain==1):
            self.pdfadbookbut.place_forget()
        self.mainimg =bgimagedit('mainbackground.png')
        self.my_canvas = Canvas(self.root)
        self.my_canvas.place(x=0, y=0, relheight=1, relwidth=1)
        self.my_canvas.create_image(0, 0, image=self.mainimg, anchor="nw")
        self.my_canvas.place()
        #buttons
        self.pdfviewbutimg = self.buttonimgedd('pdfviewerimage.png',90)

        self.pdfviewbut = Button(self.my_canvas, text='PDF VIEWER', image=self.pdfviewbutimg, command=self.pdfviewerpg, height=100,
                                  width=90, font="Helvetica 10 bold", compound=TOP)
        
        self.pdfviewbut.place(x=200, y=130)
        #imgtopdf button
        self.imgtopdfbutimg = self.buttonimgedd('6.png',90)

        self.imgtopdfbut = Button(self.my_canvas, text='IMG TO PDF', image=self.imgtopdfbutimg, command=self.imgtopdf, height=100,
                                  width=90, font="Helvetica 10 bold", compound=TOP)
        
        self.imgtopdfbut.place(x=530, y=130)
        #merge button
        self.pdfmerbutimg = self.buttonimgedd('mergesplitimage.png',90)

        self.pdfmerbut = Button(self.my_canvas, text='MERGE', image=self.pdfmerbutimg, command=self.pdfMerge, height=100,
                                  width=90, font="Helvetica 10 bold", compound=TOP)
        
        self.pdfmerbut.place(x=840, y=350)
        #split button
        self.pdfsplibutimg = self.buttonimgedd('mergesplitimage.png',90)

        self.pdfsplbut = Button(self.my_canvas, text='notworking', image=self.pdfsplibutimg, command=self.pdfsplit, height=100,
                                  width=90, font="Helvetica 10 bold", compound=TOP)
        
        #pdftotext
        self.pdftotextbutimg = self.buttonimgedd('6.png',90)

        self.pdftotextbut = Button(self.my_canvas, text='PDF2WORD', image=self.pdftotextbutimg, command=self.pdftoword, height=100,
                                  width=90, font="Helvetica 10 bold", compound=TOP)
        
        self.pdftotextbut.place(x=200,y=350)
        #texttopdf
        self.texttopdfbutimg = self.buttonimgedd('6.png',90)

        self.texttopdfbut = Button(self.my_canvas, text='WORD2PDF', image=self.texttopdfbutimg, command=self.wordtopdf, height=100,
                                  width=90, font="Helvetica 10 bold", compound=TOP)
        
        self.texttopdfbut.place(x=530, y=350)
        #button 1
        self.PDFPROTECTbutimg = self.buttonimgedd('protectpdfimage.jpg',90)
        
        self.PDFPROTECTbut = Button(self.my_canvas, text='PDF PROTECT', image=self.PDFPROTECTbutimg, command=self.pdfprotectpg, height=100, width=90,
                                font="Helvetica 10 bold", compound=TOP)
        
        self.PDFPROTECTbut.place(x=840, y=130)
    def pdfMerge(self):
        pdftopdfpath=self.mulfilename()
        pdflist=list(pdftopdfpath)
        print(pdflist)
        merger=PyPDF2.PdfFileMerger()
        for pdf in pdflist:
            merger.append(pdf)

        merger.write(self.outputfilename())
        merger.close()
        suc=tmg.showinfo("Infomation",'successfully merged')

    def pdfsplit(self):
        pdf = PyPDF2.PdfFileReader(self.openfilename())

        pages = [0,2]
        pdfWriter = PyPDF2.PdfFileWriter()

        for page_num in pages:
            pdfWriter.addPage(pdf.getPage(page_num))

        with open(self.outputfilename, 'wb') as f:
            pdfWriter.write(f)
        f.close()
        suc=tmg.showinfo("Infomation",'successfully split')
    def pdftoword(self):
        pdffileobj=open(self.openfilename(),'rb')
        pdfreader=PyPDF2.PdfFileReader(pdffileobj)
        x=pdfreader.numPages
        pageobj=pdfreader.getPage(x-1) 
        text=pageobj.extractText()

        file1=open(self.outputfilename(),"a")
        file1.writelines(text)
        file1.close()
        suc=tmg.showinfo("Infomation",'successfully merged')
    def wordtopdf(self):
        pdf = FPDF()   
        pdf.add_page()
        pdf.set_font("Arial", size = 15)
        #open the text file which is in python folder or save some text file in python folder and open it.
        f = open(self.openfilename(), "r")
  
        for x in f:
            pdf.cell(200, 10, txt = x, ln = 1, align = 'C')
        pdf.output("test.pdf")
        suc=tmg.showinfo("Infomation",'successfully merged')
    def pdfprotectpg(self):
        self.my_canvas.delete("all")
        self.pdfviewbut.place_forget()
        self.imgtopdfbut.place_forget()
        self.pdfmerbut.place_forget()
        self.pdfsplbut.place_forget()
        self.imgtopdfbut.place_forget()
        self.texttopdfbut.place_forget()
        self.PDFPROTECTbut.place_forget()
        self.backbut1()
        #button1
        self.pdfencryptbutimg = self.buttonimgedd('mergesplitimage.png',90)

        self.pdfencryptbut = Button(self.my_canvas, text='ENCRYPT', image=self.pdfencryptbutimg, command=self.pdfprotectencrypt, height=100,
                                  width=90, font="Helvetica 10 bold", compound=TOP)
        
        self.pdfencryptbut.place(x=330, y=220)
        
        #button2
        self.pdfdecryptbutimg = self.buttonimgedd('mergesplitimage.png',90)

        self.pdfdecryptbut = Button(self.my_canvas, text='DECRYPT', image=self.pdfdecryptbutimg, command=self.pdfprotectdecrypt, height=100,
                                  width=90, font="Helvetica 10 bold", compound=TOP)
        
        self.pdfdecryptbut.place(x=860, y=220)

    def pdfprotectencrypt(self):
        pdf_reader=PyPDF2.PdfFileReader(self.openfilename())
        pdf_writer=PyPDF2.PdfFileWriter()
        pdf_writer.appendPagesFromReader(pdf_reader)
        pdf_writer.encrypt(user_pwd="supersecret")
        output_path=self.outputfilename()
        with open(output_path,mode='wb') as output_file:
            pdf_writer.write(output_file)
        print('DONE')
        try:
            pdf_reader=PyPDF2.PdfFileReader(output_path)
            print('OK')
            pdftest=pdf_reader.getPage(0)
        except:
            suc=tmg.showinfo("Infomation",'SUCESSFULLLY ENCRYPT')
            
    def pdfprotectdecrypt(self):
        pdf_reader=PyPDF2.PdfFileReader(self.openfilename())
        pdf_reader.decrypt(password="supersecret")
        try:
            pdftest1=pdf_reader.getPage(0)
            suc=tmg.showinfo("Infomation",'sucessfully decrypyed')
        except:
            print('error')




    def pdfviewerpg(self):
        self.my_canvas.delete("all")
        self.imgtopdfbut.place_forget()
        self.pdfviewbut.place_forget()
        self.my_canvas = Canvas(self.root)
        self.my_canvas.place(x=300,y=0, relheight=1, relwidth=1)
        self.backbut()
        pdfobject = pdfviewer.ShowPdf()
        pdfviewloc = pdfobject.pdf_view(self.my_canvas,pdf_location = self.openfilename(),width = 75, height = 75)
        # Placing Pdf in my gui.
        pdfviewloc.pack(side=LEFT)
        self.my_canvas.mainloop()
    def Entrybox(self):
        self.root2=Tk()
        self.root2.title('box')
        self.root.geometry("50x50")
        self.entry1=Entry(self.root2,text='enter pages numbers i.e 1,2,3')
        return (self.entry1)
    def backbut1(self):
        #backbutton
        self.backimg= self.buttonimgedd('backimgicon.png',90)
        self.backbut=Button(self.root,text="BACK",image=self.backimg,command=self.frontpage,height=100,width=100,compound=TOP)
        self.backbut.place(x=0,y=0)
        
    def backbut(self):
        #backbutton
        self.backimg= self.buttonimgedd('backimgicon.png',90)
        self.backbut=Button(self.root,text="BACK",image=self.backimg,command=self.frontpage,height=100,width=100,compound=TOP)
        self.backbut.place(x=0,y=0)
        #audiobook button
        self.pdfadbookbutimg = self.buttonimgedd('audiobookimage.png',90)

        self.pdfadbookbut = Button(self.root, text='AUDIOBOOK', image=self.pdfadbookbutimg, command=self.audiobook, height=100,
                                  width=90, font="Helvetica 10 bold", compound=TOP)
        
        self.pdfadbookbut.place(x=940, y=25)
        self.amain=1

    def audiobook(self):
        file=open(self.filename,'rb')
        pdfReader=PyPDF2.PdfFileReader(file)
        text=""
        for pagenum in range(pdfReader.numPages):
            pageobj=pdfReader.getPage(pagenum)
            text+=pageobj.extractText()

        file.close()

        engine=pyttsx3.init(driverName='sapi5')
        engine.setProperty('rate',150)
        engine.say(text)
        engine.runAndWait()
    def imgtopdf(self):
        imgtopdfpath=self.mulfilename()
        imglist=list(imgtopdfpath)
        img1path=imglist.pop(0)
        img1=Image.open(img1path)
        img1.convert('RGB')
        imgtopdfimglt=[]
        if(len(imglist)>1):
            for impath in imglist: 
                image=Image.open(impath)
                image.convert('RGB')
                imgtopdfimglt.append(image)
            img1.convert('RGB').save(self.outputfilename(),save_all=True,append_images=imgtopdfimglt)
            suc=tmg.showinfo("Infomation",'successfully converted')
        else:
            img1.convert('RGB').save(self.outputfilename())
            suc=tmg.showinfo("Infomation",'successfully converted')

if __name__ == '__main__':
    gu = mainwin()



