import cv2
from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector


class Details:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1530x800+0+0")
        self.root.title("Face Recognition System")

        # variables
        self.var_dep=StringVar()
        self.var_pos = StringVar()
        self.var_year = StringVar()
        self.var_EmpId = StringVar()
        self.var_name = StringVar()
        self.var_phone = StringVar()


        img1 = Image.open(r"C:\Users\hp\PycharmProjects\face-recognition\images\background images.jpg")
        img1 = img1.resize((1530, 800), Image.ANTIALIAS)
        self.photoimg1 = ImageTk.PhotoImage(img1)

        f_lbl = Label(self.root, image=self.photoimg1)
        f_lbl.place(x=0, y=0, width=1530, height=800)

        title_lbl = Label(text="ENTER YOUR DETAILS", font=("cursive", 33,"bold"), bg="darkblue",
                          fg="white")
        title_lbl.place(x=0, y=0, width=1530, height=40)

        main_frame=Frame(f_lbl,bd=2,bg="white")
        main_frame.place(x=20,y=55,width=1490,height=710)


        Left_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Person Details",font=("times new roman",12,"bold"))
        Left_frame.place(x=10,y=10,width=710,height=680)

        Info_frame = LabelFrame(Left_frame, bd=2, bg="white", relief=RIDGE, text="Enter Information",
                                font=("times new roman", 12, "bold"))
        Info_frame.place(x=5, y=5, width=690, height=200)
# department
        Dep_label=Label(Info_frame,text="Department",font=("times new roman",12,"bold"),bg="white")
        Dep_label.grid(row=0,column=0,padx=10)

        Dep_combo=ttk.Combobox(Info_frame,textvariable=self.var_dep,font=("times new roman",12,"bold"),width=17,state="readonly")
        Dep_combo["values"]=("Select Department","Software","IT","Production","Legal","Administrative")
        Dep_combo.current(0)
        Dep_combo.grid(row=0,column=1,padx=2,pady=10,sticky=W)

        Pos_label = Label(Info_frame, text="Position", font=("times new roman", 12, "bold"), bg="white")
        Pos_label.grid(row=0, column=2, padx=10)

        Pos_combo = ttk.Combobox(Info_frame, textvariable=self.var_pos,font=("times new roman", 13, "bold"), width=20, state="readonly")
        Pos_combo["values"] = ("Select Position", "Intern", "Junior", "Senior", "VP", "Director")
        Pos_combo.current(0)
        Pos_combo.grid(row=0, column=3, padx=2, pady=10 ,sticky=W)


        #year of joining

        Year_label = Label(Info_frame, text="Year of joining", font=("times new roman", 12, "bold"), bg="white")
        Year_label.grid(row=1, column=0, padx=10)

        Year_combo = ttk.Combobox(Info_frame, textvariable=self.var_year, font=("times new roman", 13, "bold"), width=20, state="readonly")
        Year_combo["values"] = ("Select Year", "2022-2023", "2021-2022", "2020-2021", "2019-2020", "2018-2019")
        Year_combo.current(0)
        Year_combo.grid(row=1, column=1, padx=2, pady=10, sticky=W)

        #employee id

        EmpId_label = Label(Info_frame, text="Employee ID", font=("times new roman", 12, "bold"), bg="white")
        EmpId_label.grid(row=1, column=2, padx=10)

        EmpId_entry=ttk.Entry(Info_frame,textvariable=self.var_EmpId,width=20,font=("times new roman", 12, "bold"))
        EmpId_entry.grid(row=1,column=3)

        # name
        Name_label = Label(Info_frame, text="Name", font=("times new roman", 12, "bold"), bg="white")
        Name_label.grid(row=2, column=0, padx=10)

        Name_entry = ttk.Entry(Info_frame, textvariable=self.var_name,width=20, font=("times new roman", 12, "bold"))
        Name_entry.grid(row=2, column=1)

        # phone number
        Phone_label = Label(Info_frame, text="Phone number", font=("times new roman", 12, "bold"), bg="white")
        Phone_label.grid(row=2, column=2, padx=10)

        Phone_entry = ttk.Entry(Info_frame,textvariable=self.var_phone, width=20, font=("times new roman", 12, "bold"))
        Phone_entry.grid(row=2, column=3)

        # radio button
        self.var_radio1=StringVar()
        radionbtn1=ttk.Radiobutton(Info_frame,variable=self.var_radio1,text="take Photo Sample", value="Yes")
        radionbtn1.grid(row=3,column=0)

        radionbtn2 = ttk.Radiobutton(Info_frame,variable=self.var_radio1, text="No Photo Sample", value="No")
        radionbtn2.grid(row=3, column=1)

        #bbuttons frame

        btn_frame=Frame(Left_frame,bd=2,relief=RIDGE)
        btn_frame.place(x=50,y=280,width=600,height=70)

        save_btn=Button(btn_frame,text="Save",command=self.add_data,font=("times new roman", 12, "bold"),width=16,height=3,bg="blue",fg="white")
        save_btn.grid(row=0,column=0)

        update_btn = Button(btn_frame, text="Update",command=self.update_data, font=("times new roman", 12, "bold"), width=16, height=3, bg="blue",
                          fg="white")
        update_btn.grid(row=0, column=1)

        delete_btn = Button(btn_frame, text="Delete",command=self.delete_data, font=("times new roman", 12, "bold"), width=16, height=3, bg="blue",
                          fg="white")
        delete_btn.grid(row=0, column=2)

        reset_btn = Button(btn_frame, text="Reset", command=self.reset_data,font=("times new roman", 12, "bold"), width=16, height=3, bg="blue",
                          fg="white")
        reset_btn.grid(row=0, column=3)



        btn2_frame = Frame(Left_frame, bd=2, relief=RIDGE)
        btn2_frame.place(x=50, y=350, width=600, height=70)

        takephoto_btn = Button(btn2_frame,command=self.generate_dataset , text="Take Photo Sample", font=("times new roman", 12, "bold"), width=66,
                               height=3, bg="blue",
                               fg="white")
        takephoto_btn.grid(row=1, column=0)





        Right_frame = LabelFrame(main_frame, bd=2, bg="white", relief=RIDGE, text="Person Details ",font=("times new roman", 12, "bold"))
        Right_frame.place(x=750, y=10, width=725, height=680)

        # serach sytem
        Search_frame = LabelFrame(Right_frame, bd=2, bg="white", relief=RIDGE, text="Database System",
                                font=("times new roman", 12, "bold"))
        Search_frame.place(x=10, y=5, width=680, height=70)

        #*****************table frame************
        table_frame =Frame(Right_frame, bd=2, bg="white", relief=RIDGE)
        table_frame.place(x=10, y=85, width=680, height=550)

        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame, orient=VERTICAL)

        self.employee_table=ttk.Treeview(table_frame, column=("dep","pos","year","EmpId","name","phone","photo"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.employee_table.xview)
        scroll_y.config(command=self.employee_table.yview)

        self.employee_table.heading("dep",text="Department")
        self.employee_table.heading("pos", text="Position")
        self.employee_table.heading("year", text="Year of Joining")
        self.employee_table.heading("EmpId", text="EMP ID")
        self.employee_table.heading("name", text="Name")
        self.employee_table.heading("phone", text="Phone Number")
        self.employee_table.heading("photo", text="Sample Photo")
        self.employee_table["show"]="headings"



        self.employee_table.pack(fill=BOTH,expand=1)
        self.employee_table.bind("<ButtonRelease>",self.get_cursor)
        self.fetch_data()


    def add_data(self):
        if self.var_dep.get()=="Select Department" or self.var_name.get()=="" or self.var_EmpId.get()=="":
            messagebox.showerror("Error","All field are required to fill",parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(host="localhost", username="root", password="Khanak@123",database="face_recognizer")
                my_cursor = conn.cursor()
                my_cursor.execute("insert into employee values(%s,%s,%s,%s,%s,%s,%s)", (
                                                                            self.var_dep.get(),
                                                                            self.var_pos.get(),
                                                                            self.var_year.get(),
                                                                            self.var_EmpId.get(),
                                                                            self.var_name.get(),
                                                                            self.var_phone.get(),
                                                                            self.var_radio1.get()

                                                                                                     ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success","Employee details has been added Successfully",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)

    # fetch data from the data base
    def fetch_data(self):
        conn = mysql.connector.connect(host="localhost", username="root", password="Khanak@123",database="face_recognizer")
        my_cursor = conn.cursor()
        my_cursor.execute("select * from employee")
        data=my_cursor.fetchall()

        if len(data)!=0:
            self.employee_table.delete(*self.employee_table.get_children())
            for i in data:
                self.employee_table.insert("",END,values=i)
                conn.commit()
            conn.close()

    # get cursor
    def get_cursor(self,event=""):
        cursor_focus=self.employee_table.focus()
        content=self.employee_table.item(cursor_focus)
        data=content["values"]

        self.var_dep.set(data[0]),
        self.var_pos.set(data[1]),
        self.var_year.set(data[2]),
        self.var_EmpId.set(data[3]),
        self.var_name.set(data[4]),
        self.var_phone.set(data[5]),
        self.var_radio1.set(data[6]),

    # update the data
    def update_data(self):
        if self.var_dep.get()=="Select Department" or self.var_name.get()=="" or self.var_EmpId.get()=="":
            messagebox.showerror("Error","All field are required to fill",parent=self.root)
        else:
            try:
                Update=messagebox.askyesno("Update", "Do you want to update this employee detail",parent=self.root)
                if Update>0:
                    conn = mysql.connector.connect(host="localhost", username="root", password="Khanak@123", database="face_recognizer")
                    my_cursor = conn.cursor()
                    my_cursor.execute("update employee set Dep=%s,Pos=%s,Year=%s,Name=%s,Phone=%s,PhotoSample=%s where Emp_Id=%s",(
                                                                            self.var_dep.get(),
                                                                            self.var_pos.get(),
                                                                            self.var_year.get(),
                                                                            self.var_name.get(),
                                                                            self.var_phone.get(),
                                                                            self.var_radio1.get(),
                                                                            self.var_EmpId.get()
                                                                        ))
                else:
                    if not Update:
                        return
                messagebox.showinfo("Success","Employee Details successfully updated",parent=self.root)
                conn.commit()
                self.fetch_data()
                conn.close()
            except Exception as es:
                messagebox.showerror("Error","f<Due To : {str(es)}>",parent=self.root)

    # delete
    def delete_data(self):
        if self.var_EmpId.get()=="":
            messagebox.showerror(("Error","Employee id must be required"),parent=self.root)
        else:
            try:
                delete=messagebox.askyesno("Employee delete page","Do you want to delete ths Employee data",parent=self.root)
                if delete>0:
                    conn = mysql.connector.connect(host="localhost", username="root", password="Khanak@123", database="face_recognizer")
                    my_cursor = conn.cursor()
                    sql="delete from employee where Emp_id=%s"
                    val=(self.var_EmpId.get(),)
                    my_cursor.execute(sql,val)
                else:
                    if not delete:
                     return

                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Delete", "Employee Details successfully deleted", parent=self.root)


            except Exception as es:
                messagebox.showerror("Error", f"<Due To : {str(es)}>", parent=self.root)

    #reset

    def reset_data(self):
        self.var_dep.set("Select Department")
        self.var_pos.set("Select Position")
        self.var_year.set("Select Year")
        self.var_EmpId.set("")
        self.var_name.set("")
        self.var_phone.set("")
        self.var_radio1.set("")


    # data set to take photo samples
    def generate_dataset(self):
        if self.var_dep.get()=="Select Department" or self.var_name.get()=="" or self.var_EmpId.get()=="":
            messagebox.showerror("Error","All field are required to fill",parent=self.root)
        else:
            try:
                    conn = mysql.connector.connect(host="localhost", username="root", password="Khanak@123", database="face_recognizer")
                    my_cursor = conn.cursor()
                    my_cursor.execute("select * from employee")
                    myresult=my_cursor.fetchall()
                    id=0
                    for x in myresult:
                        id+=1
                    my_cursor.execute("update employee set Dep=%s,Pos=%s,Year=%s,Name=%s,Phone=%s,PhotoSample=%s where Emp_Id=%s", (
                                                                                                            self.var_dep.get(),
                                                                                                            self.var_pos.get(),
                                                                                                            self.var_year.get(),
                                                                                                            self.var_name.get(),
                                                                                                            self.var_phone.get(),
                                                                                                            self.var_radio1.get(),
                                                                                                            self.var_EmpId.get()==id+1
                                                                                                        ))
                    conn.commit()
                    self.fetch_data()
                    self.reset_data()
                    conn.close()

                    # load face frontals

                    face_classifier=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
                    def face_cropped(img):
                        gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
                        faces=face_classifier.detectMultiScale(gray,1.3,5)
                        #scaling factor=1.3
                        #Minimum neighbor=5

                        for (x,y,w,h) in faces:
                            face_cropped=img[y:y+h,x:x+w]
                            return face_cropped

                    cap=cv2.VideoCapture(0)
                    img_id=0
                    while True:
                        ret, my_frame = cap.read()
                        if face_cropped(my_frame) is not None:
                            img_id += 1
                            face = cv2.resize(face_cropped(my_frame),(500, 500))  # Pass desired size as second argument
                            face = cv2.cvtColor(face, cv2.COLOR_BGR2GRAY)
                            file_name_path = "data/user." + str(id) + "." + str(img_id) + ".jpg"
                            cv2.imwrite(file_name_path, face)
                            cv2.putText(face, str(img_id), (50,50), cv2.FONT_HERSHEY_COMPLEX, 2, (0, 255, 0), 2)
                            cv2.imshow("Cropped Face", face)

                            if cv2.waitKey(1) == 13 or int(img_id) == 100:
                                break
                    cap.release()
                    cv2.destroyAllWindows()
                    messagebox.showinfo("Result","generating data sets completed!!!")

            except Exception as es:
                messagebox.showerror("Error", f"<Due To : {str(es)}>", parent=self.root)
                        


if __name__ == "__main__":
    root = Tk()
    obj = Details(root)
    root.mainloop()