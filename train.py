import cv2
from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import os
import numpy as np

class Train:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1530x800+0+0")
        self.root.title("Face Recognition System")

        img1 = Image.open(r"C:\Users\hp\PycharmProjects\face-recognition\images\background images.jpg")
        img1 = img1.resize((1530, 800), Image.ANTIALIAS)
        self.photoimg1 = ImageTk.PhotoImage(img1)

        f_lbl = Label(self.root, image=self.photoimg1)
        f_lbl.place(x=0, y=0, width=1530, height=800)

        #button
        b1 = Button(self.root,text="Train Data",command=self.train_classifier, cursor="hand2",font=("times new roman",17,"bold"),bg="darkblue",fg="white")
        b1.place(x=0, y=0, width=1530, height=60)


    def train_classifier(self):
        data_dir=("data")
        path=[os.path.join(data_dir,file) for file in os.listdir(data_dir)]

        faces=[]
        ids=[]

        for image in path:
            img=Image.open(image).convert('L')  #gray scale image
            imageNp=np.array(img,'uint8')
            id=int(os.path.split(image)[1].split('.')[1])

            faces.append(imageNp)
            ids.append(id)
            cv2.imshow("TRAIN",imageNp)
            cv2.waitKey(1)==13
        ids=np.array(ids)

        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.train(faces,ids)
        clf.write("classifier.xml")
        cv2.destroyAllWindows()
        messagebox.showinfo("Result","training of data set completed!!")



if __name__ == "__main__":
    root = Tk()
    obj = Train(root)
    root.mainloop()