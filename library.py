from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image
from tkinter import messagebox
import cx_Oracle
import loginquery as query




class Login:
    def __init__(self, root):
        self.root = root
        self.root.title("Library System")
        self.root.geometry("910x607+100+50")
        self.root.resizable(False,False)

        #========== BG Image ==============#
        path_to_file = "C:/Users/reals/OneDrive/Desktop/CPSPROJECT/285-2850805_black-framed-eyeglasses-on-book-beside-cappuccino-coffee.jpg"
        self.bg=ImageTk.PhotoImage(Image.open(path_to_file))
        self.bg_image = Label(self.root, image=self.bg).place(x=0, y=0, relwidth=1, relheight=1)

        #=========== Login Frame ===========
        frame_login = Frame(self.root, bg="White")
        frame_login.place(x=45, y=100, height=380, width=400)

        title= Label(frame_login, text="Library System", font=("Impact", 40, "bold"), fg="#0B547C", bg="white").place(x=40, y=30)
        title_description= Label(frame_login, text="Login Below", font=("Arial", 15, "bold"), fg="#317EA9", bg="white").place(x=130, y=100)

        user_label = Label(frame_login, text="Username", font=("Gaudy old style", 15, "bold"), fg="gray", bg="white").place(x=40, y=140)
        self.txt_user = Entry(frame_login, font=("times new roman", 15), bg = "lightgray")
        self.txt_user.place(x=40, y=170, width = 335, height=35)

        password_label= Label(frame_login, text="Password", font=("Gaudy old style", 15, "bold"), fg="gray", bg="white").place(x=40, y=220)
        self.txt_password = Entry(frame_login, font=("times new roman", 15), bg = "lightgray")
        self.txt_password.place(x=40, y=260, width = 335, height=35)

        create_account_btn = Button(frame_login, text="Create Account?",font=("times new roman", 15), bd=0, fg="#0B547C", bg="white", command = self.create_account).place(x=40,y=300)

        login_btn = Button(self.root, text="Login", fg="white", bg="#0B547C", font=("Arial", 15, "bold"), command=self.login).place(x=120, y=460, width=250, height=40)

        #create_account_btn = Button(self.root, text="Create Account", fg="white", bg="#0B547C", font=("Arial", 15, "bold")).place(x=650, y = 25, width=250, height=40)



    def login(self):
        dsnStr = cx_Oracle.makedsn("oracle.scs.ryerson.ca", "1521", "orcl")
        db = cx_Oracle.connect(user="sbalolia", password="05257621", dsn=dsnStr)
        cursor = db.cursor()
        try:
            cursor.execute(query.login_check.format(self.txt_user.get(), self.txt_password.get()))
            tables = cursor.fetchall()
            for table in tables:
                print(table)
            if table[0] != "" and table[1] != "":
                print("LOGGED IN SUCCESFULLY")
                self.root.destroy()
                import customer.py
        except:
            messagebox.showerror("Error", "INCORRECT USERNAME OR PASSWORD", parent = self.root)
        if self.txt_password.get() == "" or self.txt_user.get()=="":
            messagebox.showerror("Error", "All fields are required", parent = self.root)
       

    def create_account(self):
        self.root.destroy()
        import CreateAccount


#
# class CreateAccount:
#     def __init__(self, )




root = Tk()
obj = Login(root)
root.mainloop()
