import mysql.connector
from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk
from tkinter import messagebox
from demologin import Login_u

class RegistrationForm:
    def __init__(self, root):
        self.root = root
        self.root.title("REGISTER PAGE")
        self.root.geometry("500x600+0+0")

        # Establishing database connection
        self.conn = mysql.connector.connect(
            host="localhost",
            user="root",  # Replace with your MySQL username
            password="",  # Replace with your MySQL password
            database="cafemanagement"
        )
        self.cursor = self.conn.cursor()

        # Background image
        img1 = Image.open("C:/Users/sattu/OneDrive/Desktop/py/registerbgimg.jpg")
        img1 = img1.resize((500, 600))
        self.photoimg1 = ImageTk.PhotoImage(img1)
        lblimg1 = Label(self.root, image=self.photoimg1, bd=4, relief=SUNKEN)
        lblimg1.place(x=0, y=0, width=500, height=600)

        # Main frame
        main_frame = Frame(self.root, bd=0, relief=RIDGE, bg="white")
        main_frame.place(x=40, y=90, width=350, height=440)

        # Heading
        lbl_title = Label(main_frame, text="REGISTER HERE!!", font=("times new roman", 12, "bold"), bg="white", fg="green")
        lbl_title.place(x=30, y=30, width=140, height=50)

        # Fullname Entry
        lbl_fullname = Label(main_frame, text="Full Name *", font=("times new roman", 15, "bold"), bg="white", fg="black")
        lbl_fullname.place(x=0, y=60, width=200, height=50)
        self.fullname_entry = ttk.Entry(main_frame, font=("times new roman", 15, "italic"))
        self.fullname_entry.place(x=10, y=100, width=250, height=30)

        # Username Entry
        lbl_username = Label(main_frame, text="Username *", font=("times new roman", 15, "bold"), bg="white", fg="black")
        lbl_username.place(x=0, y=130, width=200, height=50)
        self.username_entry = ttk.Entry(main_frame, font=("times new roman", 15, "italic"))
        self.username_entry.place(x=10, y=170, width=250, height=30)

        # Password Entry
        lbl_password = Label(main_frame, text="Password *", font=("times new roman", 15, "bold"), bg="white", fg="black")
        lbl_password.place(x=0, y=200, width=200, height=50)
        self.password_entry = ttk.Entry(main_frame, show='*', font=("times new roman", 15, "italic"))
        self.password_entry.place(x=10, y=240, width=250, height=30)

        # Gender Selection
        lbl_gender = Label(main_frame, text="Gender", font=("times new roman", 15, "bold"), bg="white")
        lbl_gender.place(x=0, y=280, width=100, height=30)
        self.gender_var = StringVar()
        self.gender_var.set("Male")
        male_radio = Radiobutton(main_frame, text="Male", font=("times new roman", 15, "bold"), bg="white", variable=self.gender_var, value="Male")
        male_radio.place(x=100, y=280)
        female_radio = Radiobutton(main_frame, text="Female", font=("times new roman", 15, "bold"), bg="white", variable=self.gender_var, value="Female")
        female_radio.place(x=200, y=280)

        # Mobile Number Entry
        lbl_number = Label(main_frame, text="Mobile Number *", font=("times new roman", 15, "bold"), bg="white", fg="black")
        lbl_number.place(x=0, y=310, width=200, height=50)
        self.number_entry = ttk.Entry(main_frame, font=("times new roman", 15, "italic"))
        self.number_entry.place(x=10, y=350, width=250, height=30)

        # Register Button
        register_btn = Button(main_frame, bd=1, relief=RIDGE, text="REGISTER", font=("times new roman", 17, "bold"), bg="black", fg="white", command=self.register)
        register_btn.place(x=30, y=400, width=150, height=30)

        # Login Button
        login_btn = Button(main_frame, bd=1, relief=RIDGE, text="LOGIN", font=("times new roman", 17, "bold"), bg="black", fg="white", command=self.login)
        login_btn.place(x=200, y=400, width=130, height=30)

        # Logo image
        img2 = Image.open("C:/Users/sattu/OneDrive/Desktop/py/cappucino.jpeg")
        img2 = img2.resize((80, 70))
        self.photoimg2 = ImageTk.PhotoImage(img2)
        lblimg2 = Label(main_frame, image=self.photoimg2, relief=SUNKEN)
        lblimg2.place(x=250, y=10, width=60, height=70)

    def register(self):
        fullname = self.fullname_entry.get()
        username = self.username_entry.get()
        password = self.password_entry.get()  # Retrieve password
        gender = self.gender_var.get()
        mobile_number = self.number_entry.get()
        
        # Inserting data into the database
        query = "INSERT INTO register (fn, un, pass, gender, mobileno) VALUES (%s, %s, %s, %s, %s)"
        data = (fullname, username, password, gender, mobile_number)
        self.cursor.execute(query, data)
        self.conn.commit()

        # Show success message box
        messagebox.showinfo("Success", "Registration Successful!")

        # Redirect to login page
        self.open_login_page()

    def open_login_page(self):
        self.root.destroy()  # Close registration window
        login_window = Tk()
        login_page = Login_u(login_window)
        login_window.mainloop()

    def login(self):
        # Add your login logic here
        pass

class LoginPage:
    def __init__(self, root):
        self.root = root
        self.root.title("LOGIN PAGE")
        self.root.geometry("500x600+0+0")

        # Add your login page GUI here

if __name__ == "__main__":
    root = Tk()
    new = RegistrationForm(root)
    root.mainloop()
