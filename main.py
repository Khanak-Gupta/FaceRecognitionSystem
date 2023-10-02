import tkinter.messagebox
from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from details import Details
from train import Train
from face_recognizer import Face_recognizer
class Face_Recognition:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1530x800+0+0")
        self.root.title("Face Recognition System")


        img1=Image.open(r"C:\Users\hp\PycharmProjects\face-recognition\images\background images.jpg")
        img1=img1.resize((1530,800),Image.ANTIALIAS)
        self.photoimg1=ImageTk.PhotoImage(img1)

        f_lbl=Label(self.root,image=self.photoimg1)
        f_lbl.place(x=0,y=0,width=1530,height=800)

        title_lbl=Label(f_lbl,text="WELCOME TO FACE RECOGNITION SYSTEM",font=("cursive",35,"bold"),bg="white",fg="red")
        title_lbl.place(x=0,y=0,width=1530,height=40)

        img2= Image.open(r"C:\Users\hp\PycharmProjects\face-recognition\images\data entry.png")
        img2= img2.resize((260,220), Image.ANTIALIAS)
        self.photoimg2= ImageTk.PhotoImage(img2)

        b1=Button(f_lbl,image=self.photoimg2,command=self.details,cursor="hand2")
        b1.place(x=100,y=150,width=260,height=220)

        b1_1 = Button(f_lbl,text="Enter The Details",command=self.details,cursor="hand2",font=("cursive",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=100, y=350 , width=260, height=40)

        img3 = Image.open(r"C:\Users\hp\PycharmProjects\face-recognition\images\face detection.jpg")
        img3 = img3.resize((260, 220), Image.ANTIALIAS)
        self.photoimg3 = ImageTk.PhotoImage(img3)

        b2 = Button(f_lbl, image=self.photoimg3,command=self.face_recog,cursor="hand2")
        b2.place(x=450, y=150, width=260, height=220)

        b2_1 = Button(f_lbl, text="Face Detection",command=self.face_recog, cursor="hand2", font=("cursive", 15, "bold"), bg="darkblue",
                      fg="white")
        b2_1.place(x=450, y=350, width=260, height=40)

        img4 = Image.open(r"C:\Users\hp\PycharmProjects\face-recognition\images\data info.jpg")

        img4 = img4.resize((260, 220), Image.ANTIALIAS)
        self.photoimg4 = ImageTk.PhotoImage(img4)

        b3 = Button(f_lbl, image=self.photoimg4,command=self.train_data, cursor="hand2")
        b3.place(x=100, y=500, width=260, height=220)

        b3_1 = Button(f_lbl, text="Train DataSet",command=self.train_data, cursor="hand2", font=("cursive", 15, "bold"), bg="darkblue",
                      fg="white")
        b3_1.place(x=100, y=680, width=260, height=40)

        img5 = Image.open(r"C:\Users\hp\PycharmProjects\face-recognition\images\data exit.jpg")
        img5 = img5.resize((260, 220), Image.ANTIALIAS)
        self.photoimg5 = ImageTk.PhotoImage(img5)

        b4 = Button(f_lbl,command=self.Exit, image=self.photoimg5, cursor="hand2",)
        b4.place(x=450, y=500, width=260, height=220)

        b4_1 = Button(f_lbl,command=self.Exit, text="EXIT", cursor="hand2", font=("cursive", 15, "bold"), bg="darkblue",
                      fg="white")
        b4_1.place(x=450,y=680, width=260, height=40)

    def Exit(self):
        self.Exit = tkinter.messagebox.askyesno("Face Recognition System", "Do you want to exit this project")
        if self.Exit > 0:
            self.root.destroy()
        else:
            return
#************FUNCTIONS************

    def details(self):
        self.new_window=Toplevel(self.root)
        self.app=Details(self.new_window)

    def train_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Train(self.new_window)

    def face_recog(self):
        self.new_window=Toplevel(self.root)
        self.app=Face_recognizer(self.new_window)



if __name__ == "__main__":
    root = Tk()
    obj = Face_Recognition(root)
    root.mainloop()