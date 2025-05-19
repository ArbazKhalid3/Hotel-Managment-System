from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
import mysql.connector
import hotel  # assumes hotel.py contains start_hotel_system()

# === Database connection ===
def connect_db():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="Shahroz123#",
        database="management"
    )

class LoginSystem:
    def __init__(self, root):
        self.root = root
        self.root.title("Hotel Login System")

        # Set window size to 1366x768
        width = 1366
        height = 768

        # Get screen width and height
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()

        # Calculate position x and y coordinates
        x = (screen_width // 2) - (width // 2)
        y = (screen_height // 2) - (height // 2)

        # Set geometry and disable resizing
        self.root.geometry(f"{width}x{height}+{x}+{y}")
        self.root.resizable(False, False)

        # === Load & Resize Background Image ===
        bg_image = Image.open(r"C:\Users\Shahroz\Desktop\Hotel_Managment_system\pics for hotel man\hotel 3.jpeg")
        bg_image = bg_image.resize((1366, 768), Image.LANCZOS)
        self.bg = ImageTk.PhotoImage(bg_image)

        bg_lbl = Label(self.root, image=self.bg)
        bg_lbl.place(x=0, y=0, width=1366, height=768)

        # === Frame for Login/Register ===
        self.frame = Frame(self.root, bg="white")
        self.frame.place(x=508, y=150, width=350, height=500)  # Center frame on new resolution

        self.login_form()


    def login_form(self):
        for widget in self.frame.winfo_children():
            widget.destroy()

        Label(self.frame, text="Login", font=("Arial", 20, "bold"), bg="white", fg="black").pack(pady=10)

        Label(self.frame, text="Email", font=("Arial", 12), bg="white").pack(pady=5)
        self.username = Entry(self.frame, font=("Arial", 12))
        self.username.pack()

        Label(self.frame, text="Password", font=("Arial", 12), bg="white").pack(pady=5)
        self.password = Entry(self.frame, font=("Arial", 12), show="*")
        self.password.pack()

        Button(self.frame, text="Login", command=self.login, font=("Arial", 12, "bold"), bg="black", fg="gold").pack(pady=10)
        Button(self.frame, text="Forgot Password?", command=self.forgot_password, font=("Arial", 10), bg="white", fg="blue", bd=0).pack()
        Button(self.frame, text="Register Now", command=self.register_form, font=("Arial", 10), bg="white", fg="green", bd=0).pack()

    def register_form(self):
        for widget in self.frame.winfo_children():
            widget.destroy()

        Label(self.frame, text="Register", font=("Arial", 20, "bold"), bg="white", fg="black").pack(pady=10)

        Label(self.frame, text="First Name", font=("Arial", 12), bg="white").pack(pady=2)
        self.first_name = Entry(self.frame, font=("Arial", 12))
        self.first_name.pack()

        Label(self.frame, text="Last Name", font=("Arial", 12), bg="white").pack(pady=2)
        self.last_name = Entry(self.frame, font=("Arial", 12))
        self.last_name.pack()

        Label(self.frame, text="Contact No.", font=("Arial", 12), bg="white").pack(pady=2)
        self.contact_no = Entry(self.frame, font=("Arial", 12))
        self.contact_no.pack()

        Label(self.frame, text="Email", font=("Arial", 12), bg="white").pack(pady=2)
        self.email = Entry(self.frame, font=("Arial", 12))
        self.email.pack()

        Label(self.frame, text="Password", font=("Arial", 12), bg="white").pack(pady=2)
        self.reg_password = Entry(self.frame, font=("Arial", 12), show="*")
        self.reg_password.pack()

        Label(self.frame, text="Confirm Password", font=("Arial", 12), bg="white").pack(pady=2)
        self.confirm_password = Entry(self.frame, font=("Arial", 12), show="*")
        self.confirm_password.pack()

        Button(self.frame, text="Register", command=self.register, font=("Arial", 12, "bold"), bg="black", fg="gold").pack(pady=10)
        Button(self.frame, text="Back to Login", command=self.login_form, font=("Arial", 10), bg="white", fg="blue", bd=0).pack()

    def forgot_password(self):
        messagebox.showinfo("Info", "Feature under development.")

    def login(self):
        email = self.username.get()
        password = self.password.get()

        if not email or not password:
            messagebox.showerror("Error", "All fields are required")
            return

        try:
            conn = connect_db()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM admins WHERE email=%s AND password=%s", (email, password))
            row = cursor.fetchone()
            conn.close()

            if row:
                messagebox.showinfo("Success", "Login successful!")
                self.root.destroy()
                hotel.start_hotel_system()
            else:
                messagebox.showerror("Error", "Invalid email or password")

        except Exception as e:
            messagebox.showerror("Database Error", str(e))

    def register(self):
        fn = self.first_name.get()
        ln = self.last_name.get()
        contact = self.contact_no.get()
        email = self.email.get()
        password = self.reg_password.get()
        confirm = self.confirm_password.get()

        if not fn or not ln or not contact or not email or not password or not confirm:
            messagebox.showerror("Error", "All fields are required")
            return
        if password != confirm:
            messagebox.showerror("Error", "Passwords do not match")
            return

        try:
            conn = connect_db()
            cursor = conn.cursor()
            cursor.execute("INSERT INTO admins (first_name, last_name, contact_no, email, password) VALUES (%s, %s, %s, %s, %s)",
                           (fn, ln, contact, email, password))
            conn.commit()
            conn.close()
            messagebox.showinfo("Success", "User registered successfully!")
            self.login_form()

        except mysql.connector.IntegrityError:
            messagebox.showerror("Error", "Email already exists")
        except Exception as e:
            messagebox.showerror("Database Error", str(e))


if __name__ == "__main__":
    root = Tk()
    app = LoginSystem(root)
    root.mainloop()
