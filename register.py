from tkinter import Tk, Label, Frame, Entry, ttk, Checkbutton, Button, StringVar, messagebox, IntVar
from tkinter.ttk import Combobox

from PIL import Image, ImageTk
import pymysql

class Register:
    def __init__(self, root):
        self.root = root
        self.root.title("Registeration Window")
        self.root.geometry("1357x700+0+0")
        self.root.config(bg="white")
        # ===BG Image===
        self.bg = ImageTk.PhotoImage(file="images/862206.jpg")
        bg = Label(self.root, image=self.bg).place(x=0, y=0, relwidth=1, relheight=1)
        # ===Left Image===
        self.left = ImageTk.PhotoImage(file="images/harvey.jpg")
        left = Label(self.root, image=self.left).place(x=30, y=95, relwidth=0.33, relheight=0.73)

        # ====Register Frame====
        frame1: Frame = Frame(self.root, bg="white")
        frame1.place(x=480, y=100, width=700, height=500)

        title = Label(frame1, text="Register Here", font=("Arial", 20, "bold"), bg="white", fg="blue").place(x=50, y=30)

        # --------------Row1
        f_name = Label(frame1, text="First Name", font=("Arial", 15, "bold"), bg="white", fg="grey").place(x=50, y=100)
        self.txt_fname =Entry(frame1,font=("times new roman",15),bg="lightgray")
        self.txt_fname.place(x=50,y=130,width=250)

        l_name = Label(frame1, text="Last Name", font=("Arial", 15, "bold"), bg="white", fg="grey").place(x=370, y=100)
        self.txt_lname = Entry(frame1, font=("times new roman", 15), bg="lightgray")
        self.txt_lname.place(x=370, y=130, width=250)

        #--------------Row2
        contact = Label(frame1, text="Contact", font=("Arial", 15, "bold"), bg="white", fg="grey").place(x=50, y=155)
        self.txt_contact = Entry(frame1, font=("times new roman", 15), bg="lightgray")
        self.txt_contact.place(x=50, y=185, width=250)

        email = Label(frame1, text="Email", font=("Arial", 15, "bold"), bg="white", fg="grey").place(x=370, y=155)
        self.txt_email = Entry(frame1, font=("times new roman", 15), bg="lightgray")
        self.txt_email.place(x=370, y=185, width=250)

        # --------------Row3
        question = Label(frame1, text="Security Question", font=("Arial", 15, "bold"), bg="white", fg="grey").place(x=50, y=220)
        self.cmb_question = ttk.Combobox(frame1, font=("times new roman", 13),state='readonly')
        self.cmb_question['values']=("select","Your pet name","your birth place","your birth date")
        self.cmb_question.place(x=50, y=245, width=250)
        self.cmb_question.current(0)

        answer = Label(frame1, text="Answer", font=("Arial", 15, "bold"), bg="white", fg="grey").place(x=370, y=220)
        self.txt_answer = Entry(frame1, font=("times new roman", 15), bg="lightgray")
        self.txt_answer.place(x=370, y=245, width=250)

        # --------------Row4
        password = Label(frame1, text="Password", font=("Arial", 15, "bold"), bg="white", fg="grey").place(x=50, y=275)
        self.txt_password = Entry(frame1, font=("times new roman", 15), bg="lightgray")
        self.txt_password.place(x=50, y=300, width=250)

        cpassword = Label(frame1, text="Confirm Password", font=("Arial", 15, "bold"), bg="white", fg="grey").place(x=370, y=275)
        self.txt_cpassword = Entry(frame1, font=("times new roman", 15), bg="lightgray")
        self.txt_cpassword.place(x=370, y=300, width=250)

        #------terms--------
        self.var_chk=IntVar()
        chk=Checkbutton(frame1,text="I agree The terms and conditions",variable=self.var_chk,onvalue=1,offvalue=0, bg="white").place(x=50, y=340, width=250)

        self.btn_img=ImageTk.PhotoImage(file="images/regyy.jpg")
        btn_register = Button(frame1,image=self.btn_img,bd=0,cursor="hand2", command=self.register_data).place(x=50,y=420,relwidth=0.8, relheight=0.1)

        btn_2 = Button(self.root, text="Sing In",font=("arial",20), bd=0, cursor="hand2",command=self.login_window).place(x=130, y=500, relwidth=0.2, relheight=0.05)

    def login_window(self):
        self.root.destroy()
        import login

    def register_data(self):
        if self.txt_fname.get()=="" or self.txt_contact.get()=="" or self.txt_email.get()=="" or self.cmb_question.get()=="Select" or self.txt_answer.get()=="" or self.txt_password.get()=="" or self.txt_cpassword.get()=="":
            messagebox.showerror("Error","All Fields are compulsory",parent=self.root)
        elif self.txt_password.get()!=self.txt_cpassword.get():
            messagebox.showerror("Error", "Password And Confirm Password should be same", parent=self.root)
        elif self.var_chk.get()==0:
            messagebox.showerror("Error", "Please accept Tearms and conditions", parent=self.root)
        else:
            try:
                con=pymysql.connect(host="localhost",user="root",password="",database="employee2")
                cur=con.cursor()
                cur.execute("insert into employee (f_name,l_name,contact,email,question,answer,password) values(%s,%s,%s,%s,%s,%s,%s)",
                            (self.txt_fname.get(),
                             self.txt_lname.get(),
                             self.txt_contact.get(),
                             self.txt_email.get(),
                             self.cmb_question.get(),
                             self.txt_answer.get(),
                             self.txt_password.get()
                            ))
                con.commit()
                con.close()
                messagebox.showerror("Success", "Register successful", parent=self.root)

            except Exception as es:
                messagebox.showerror("Error",f"Error Due to:{str(es)}", parent=self.root)



root = Tk()
obj = Register(root)
root.iconbitmap(r"D:\Login_with_database\images\favicon.ico")
root.mainloop()