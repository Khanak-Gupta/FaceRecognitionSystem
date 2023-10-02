import cv2
from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import os



class Face_recognizer:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1530x800+0+0")
        self.root.title("Face Recognition System")

        img1 = Image.open(r"C:\Users\hp\PycharmProjects\face-recognition\images\background1 images.jpg")
        img1 = img1.resize((1200, 800), Image.ANTIALIAS)
        self.photoimg1 = ImageTk.PhotoImage(img1)

        f_lbl = Label(self.root, image=self.photoimg1)
        f_lbl.place(x=5, y=5, width=1530, height=800)

        b1 = Button(f_lbl, text="Click Here",command=self.face_recog, cursor="hand2",font=("times new roman", 18, "bold"), bg="green", fg="white")
        b1.place(x=690, y=80, width=150, height=50)

        #face-recognization
    def face_recog(self):
        def draw_boundary(img,classifier,scaleFactor, minNeighbors, color, text, clf):
            gray_image = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
            features=classifier.detectMultiScale(gray_image,scaleFactor,minNeighbors)

            coord=[]

            for (x,y,w,h) in features:
                cv2.rectangle(img,(x,y),(x+w,y+h),(0, 255, 0),3)
                id,predict = clf.predict(gray_image[y:y+h, x:x+w])
                # confidence predict
                confidence = int((100*(1-predict/300)))

                conn = mysql.connector.connect(host="localhost", username="root", password="Khanak@123", database="face_recognizer")
                my_cursor=conn.cursor()

                my_cursor.execute("select Name from employee where Emp_Id="+str(id))
                n=my_cursor.fetchone()
                n="+".join(n)

                my_cursor.execute("select Dep from employee where Emp_Id="+str(id))
                d=my_cursor.fetchone()
                d="+".join(d)

                my_cursor.execute("select Pos from employee where Emp_Id="+str(id))
                p=my_cursor.fetchone()
                p="+".join(p)


                if confidence>69:
                    cv2.putText(img, f"Name:{n}", (x,y-55),cv2.FONT_HERSHEY_COMPLEX,1,(0,0,255),2)
                    cv2.putText(img, f"Department:{d}",(x,y-30),cv2.FONT_HERSHEY_COMPLEX,1,(0,0,255),2)
                    cv2.putText(img, f"Position:{p}", (x,y-5), cv2.FONT_HERSHEY_COMPLEX,1,(0,0,255),2)
                else:
                    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 2)
                    cv2.putText(img, "Unknown Face (Intruder)", (x,y-5), cv2.FONT_HERSHEY_COMPLEX, 1, (255,0,255),2)

                coord = [x, y, w, h]

            return coord

        def recognize(img,clf,facecascade):
            coord=draw_boundary(img,facecascade,1.1,10,(255,255,255),"Face",clf)
            return img

        facecascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.read("classifier.xml")

        video_cap=cv2.VideoCapture(0,cv2.CAP_DSHOW)

        while True:
            ret,img = video_cap.read()
            img=recognize(img,clf,facecascade)
            cv2.imshow('Webcam',img)
            if cv2.waitKey(1)==13:
                break


if __name__ == "__main__":
    root = Tk()
    obj = Face_recognizer(root)
    root.mainloop()
