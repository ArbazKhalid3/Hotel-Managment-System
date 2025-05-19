from tkinter import *
from tkinter import scrolledtext
from PIL import Image, ImageTk
from PIL.Image import Resampling
from customer import Cust_Win
from room import Roombooking
from details import DetailsRoom
from report import print_developer_report
import io
import sys


class HotelManagmentSystem:
    def __init__(self, root):
        self.root = root
        self.root.title("Hotel Management System")
        self.root.geometry("1550x800+0+0")

        # =========== Top Image =============
        img1 = Image.open(r"C:\Users\Shahroz\Desktop\Hotel_Managment_system\pics for hotel man\macau skyline.jpg")
        img1 = img1.resize((1550, 140), Resampling.LANCZOS)
        self.photoimg1 = ImageTk.PhotoImage(img1)
        lblimg = Label(self.root, image=self.photoimg1, bd=4, relief=RIDGE)
        lblimg.place(x=0, y=0, width=1550, height=140)

        # =========== Logo Image =============
        img2 = Image.open(r"C:\Users\Shahroz\Desktop\Hotel_Managment_system\pics for hotel man\logo pic.jpg")
        img2 = img2.resize((230, 140), Resampling.LANCZOS)
        self.photoimg2 = ImageTk.PhotoImage(img2)
        lblimg = Label(self.root, image=self.photoimg2, bd=4, relief=RIDGE)
        lblimg.place(x=0, y=0, width=230, height=140)

        # ========== Title ==============
        lbl_title = Label(self.root, text="Hotel Management System", font=("times new roman", 40, "bold"),
                          bg="black", fg="gold", bd=4, relief=RIDGE)
        lbl_title.place(x=0, y=140, width=1550, height=50)

        # ============== Main Frame ===============
        main_frame = Frame(self.root, bd=4, relief=RIDGE)
        main_frame.place(x=0, y=190, width=1550, height=620)

        # ================ Menu ==================
        lbl_menu = Label(main_frame, text="MENU", font=("times new roman", 20, "bold"), bg="black", fg="gold", bd=4, relief=RIDGE)
        lbl_menu.place(x=0, y=0, width=230)

        # =============== Button Frame ==============
        btn_frame = Frame(main_frame, bd=4, relief=RIDGE)
        btn_frame.place(x=0, y=35, width=228, height=190)

        cust_btn = Button(btn_frame, text="CUSTOMER", command=self.cust_details, width=22, font=("times new roman", 14, "bold"), bg="black", fg="gold", bd=0, cursor="hand1")
        cust_btn.grid(row=0, column=0)

        room_btn = Button(btn_frame, text="ROOM", command=self.roombooking, width=22, font=("times new roman", 14, "bold"), bg="black", fg="gold", bd=0, cursor="hand1")
        room_btn.grid(row=1, column=0)

        detail_btn = Button(btn_frame, text="DETAILS", command=self.details_room, width=22, font=("times new roman", 14, "bold"), bg="black", fg="gold", bd=0, cursor="hand1")
        detail_btn.grid(row=2, column=0)

        report_btn = Button(btn_frame, text="REPORT", command=self.show_report, width=22, font=("times new roman", 14, "bold"), bg="black", fg="gold", bd=0, cursor="hand1")
        report_btn.grid(row=3, column=0)

        logout_btn = Button(btn_frame, text="LOGOUT", command=self.logout, width=22, font=("times new roman", 14, "bold"), bg="black", fg="gold", bd=0, cursor="hand1")
        logout_btn.grid(row=4, column=0)

        # ============ Right Side Image ============
        img3 = Image.open(r"C:\Users\Shahroz\Desktop\Hotel_Managment_system\pics for hotel man\inside 1.jpeg")
        img3 = img3.resize((1310, 590), Resampling.LANCZOS)
        self.photoimg3 = ImageTk.PhotoImage(img3)
        lblimg1 = Label(main_frame, image=self.photoimg3, bd=4, relief=RIDGE)
        lblimg1.place(x=225, y=0, width=1310, height=590)

        # ============== Bottom Images ===============
        img4 = Image.open(r"C:\Users\Shahroz\Desktop\Hotel_Managment_system\pics for hotel man\hotel 1.jpeg")
        img4 = img4.resize((230, 210), Resampling.LANCZOS)
        self.photoimg4 = ImageTk.PhotoImage(img4)
        lblimg1 = Label(main_frame, image=self.photoimg4, bd=4, relief=RIDGE)
        lblimg1.place(x=0, y=225, width=230, height=210)

        img5 = Image.open(r"C:\Users\Shahroz\Desktop\Hotel_Managment_system\pics for hotel man\food.jpg")
        img5 = img5.resize((230, 190), Resampling.LANCZOS)
        self.photoimg5 = ImageTk.PhotoImage(img5)
        lblimg1 = Label(main_frame, image=self.photoimg5, bd=4, relief=RIDGE)
        lblimg1.place(x=0, y=420, width=230, height=190)

    def cust_details(self):
        self.new_window = Toplevel(self.root)
        self.app = Cust_Win(self.new_window)

    def roombooking(self):
        self.new_window = Toplevel(self.root)
        self.app = Roombooking(self.new_window)

    def details_room(self):
        self.new_window = Toplevel(self.root)
        self.app = DetailsRoom(self.new_window)

    def logout(self):
        self.root.destroy()

    def show_report(self):
     report_window = Toplevel(self.root)
     report_window.title("Developer Report")
     report_window.geometry("1130x513+230+220")
     report_window.configure(bg="black")  # Set window background

     txt = scrolledtext.ScrolledText(
        report_window,
        wrap=WORD,
        font=("Consolas", 11),
        bg="black",           # Background color
        fg="gold",            # Text color
        insertbackground="white",  # Cursor color
        borderwidth=0,        # Remove border for flat look
     )
     txt.pack(expand=True, fill=BOTH, padx=10, pady=10)

     buffer = io.StringIO()
     sys.stdout = buffer
     print_developer_report()
     sys.stdout = sys.__stdout__
     txt.insert(END, buffer.getvalue())
     txt.configure(state='disabled')



def start_hotel_system():
    root = Tk()
    app = HotelManagmentSystem(root)
    root.mainloop()


if __name__ == "__main__":
    start_hotel_system()
