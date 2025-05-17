from tkinter import *
from PIL import Image,ImageTk
import webbrowser
class Home_page:


    def __init__(self, root):
        self.root=root
        self.root.geometry("1600x800+0+0")
        self.root.maxsize(0,0)
        #root.minsize(1500,900)ww
        self.root.title("Graphical Password Interface")
        self.root.bg=Image.open(r"D:/Graphical-Password-Authentication-System-master/pic/home.jpg")
        self.root.resizeA = root.bg.resize((1550, 800), Image.Resampling.LANCZOS)
        self.root.photo= ImageTk.PhotoImage(self.root.resizeA)
        root.bg_image=Label(root,image=self.root.photo).place(x=0,y=0)
        self.root.wm_attributes("-transparentcolor", 'red')
        my_text1= Label(root,text="Welcome!", font=("time new roman", 30,"bold"),fg="blue").place(x=650,y=50)
        my_text2= Label(root,text="Graphical Password Authentication System", font=("time new roman", 25,"bold"),bg="white",fg="#E67E22").place(x=390,y=150)

        Reg = Button(self.root, text="Registration",cursor="hand2", font=("time new roman", 13), border=5, bg="blue", fg="white",
                     command=self.reg).place(x=100, y=450, width=180, height=40)
        Sign_in = Button(self.root, text="Sign In", cursor="hand2", font=("time new roman", 13), border=5, bg="blue",
                         fg="white",
                         command=self.signup).place(x=500, y=450, width=180, height=40)


        sign_in = Button(self.root, text="Profile", cursor="hand2", font=("time new roman", 13), border=5, bg="blue",
                         fg="white",
                         command=self.portfolio).place(x=900, y=450, width=150, height=40)
        sign_in = Button(self.root, text="GPAS", cursor="hand2", font=("time new roman", 13), border=5, bg="blue",
                         fg="white",
                         command=self.about1).place(x=1300, y=450, width=150, height=40)

    def reg(self):
        self.root.destroy()
        import registration_page




    def signup(self):
        self.root.destroy()
        import login_page

    def portfolio(self):
            self.window4 = Toplevel()
            self.window4.title("About Me")
            self.window4.geometry('1530x800+0+0')
            self.window4.config(bg='pink')
            self.window4.resizable(False, False)
            self.window4.bg = Image.open(r"D:/Graphical-Password-Authentication-System-master/pic/bg333.jpg")
            self.window4.resizeA = self.window4.bg.resize((1530, 800), Image.Resampling.LANCZOS)
            self.window4.photo = ImageTk.PhotoImage(self.window4.resizeA)

            self.window4.bg2 = Image.open(r"C:/Users/sushree sujata/Downloads/IMG_20250122_130711.jpg")
            self.window4.resizeB = self.window4.bg2.resize((150, 180), Image.Resampling.LANCZOS)
            self.window4.photo1 = ImageTk.PhotoImage(self.window4.resizeB)

            canvas = Canvas(self.window4)
            canvas.create_image(0, 0, image=self.window4.photo, anchor=NW)
            canvas.create_image(120, 220, image=self.window4.photo1)
            canvas.create_text(640, 60, text="Welcome to My Profile!", fill='white',
                               font=("times new roman", 25, "bold"))
            canvas.create_text(450, 145, text="Hey, I'm Sushree Sujata Sahoo.", fill='white',
                               font=("calibri", 25, "bold"))
            canvas.create_text(460, 190,
                               text="Aspiring Cloud Engineer | Web Developer \n📍 Bhubaneswar | ✉ sushreesujatasaoo@gmail.com",
                               fill='white', font=("calibri", 15))
            canvas.create_text(275, 240, text="About Me", fill='black', font=("calibri", 18, "bold"))
            canvas.create_text(690, 280,
                               text="I am a passionate and dedicated Web Developer, skilled in HTML, CSS, JavaScript, PHP, Java, SQL, AWS Services. \nI love solving real-world problems through technology and continuously strive to learn and innovate.",
                               fill='white', font=("calibri", 15))
            canvas.create_text(100, 360, text="Projects", fill='black', font=("calibri", 22, "bold"))
            canvas.create_text(270, 400, text="-  Graphical Password Authentication System", fill='white',
                               font=("calibri", 18, "bold"))
            canvas.create_text(610, 430,
                               text="Developed a secure login system using images and text, enhancing traditional password security with visual-based authentication.",
                               fill='white', font=("calibri", 15))
            canvas.create_text(205, 470, text="-  Online Food Ordering Website", fill='white',
                               font=("calibri", 18, "bold"))
            canvas.create_text(548, 500,
                               text="Built a web-based solution called FoodyMood to order food online, browse menus, track location and place orders.",
                               fill='white', font=("calibri", 15))

            canvas.create_text(118, 550, text="Contact Me", fill='black', font=("calibri", 22, "bold"))
            canvas.pack(fill="both", expand=True)

            def facebook():
                webbrowser.open("https://www.facebook.com/profile.php?id=61555001709782")

            def instagram():
                webbrowser.open("https://www.facebook.com/profile.php?id=61555001709782")

            def linkedin():
                webbrowser.open("https://www.linkedin.com/in/swatisnigdhapanigrahi")

            self.bg10 = Image.open(r"D:/Graphical-Password-Authentication-System-master/pic/facebook.jpg")
            self.resizeJ = self.bg10.resize((40, 40), Image.Resampling.LANCZOS)
            self.photo10 = ImageTk.PhotoImage(self.resizeJ)

            self.bg11 = Image.open(r"D:/Graphical-Password-Authentication-System-master/pic/instagram.jpg")
            self.resizeK = self.bg11.resize((40, 40), Image.Resampling.LANCZOS)
            self.photo11 = ImageTk.PhotoImage(self.resizeK)

            self.bg12 = Image.open(r"D:/Graphical-Password-Authentication-System-master/pic/linkedin1.jpg")
            self.resizeL = self.bg12.resize((40, 40), Image.Resampling.LANCZOS)
            self.photo12 = ImageTk.PhotoImage(self.resizeL)

            Next = Button(self.window4, image=self.photo10, font=("time new roman", 13, "bold"), border=2,
                          command=facebook).place(x=50, y=580, width=30, height=30)
            Next = Button(self.window4, image=self.photo11, font=("time new roman", 13, "bold"), border=2,
                          command=instagram).place(x=100, y=580, width=30, height=30)
            Next = Button(self.window4, image=self.photo12, font=("time new roman", 13, "bold"), border=2,
                          command=linkedin).place(x=150, y=580, width=30, height=30)


    def about1(self):
            self.window4 = Toplevel()
            self.window4.title("About GPAS")
            self.window4.geometry('1530x800+0+0')
            self.window4.config(bg='black')
            self.window4.resizable(False, False)
            self.window4.bg = Image.open(r"D:/Graphical-Password-Authentication-System-master/pic/bg444.jpg")
            self.window4.resizeA = self.window4.bg.resize((1530, 800), Image.Resampling.LANCZOS)
            self.window4.photo = ImageTk.PhotoImage(self.window4.resizeA)

            canvas = Canvas(self.window4)
            canvas.create_image(0, 0, image=self.window4.photo, anchor=NW)
            canvas.create_text(400, 60, text="About Graphical Password Authentication System (GPAS)", fill='white',
                               font=("calibri", 22, "bold"))
            canvas.create_text(600, 140,
                               text="A Graphical Password Authentication System is a security method where users select or interact with images, patterns, or visual \nelements instead of typing traditional text-based passwords. It enhances security by leveraging human memory for visuals, making"
                                    "\nit harder for attackers to guess or steal passwords through common methods like brute force or key-logging. This system is often \nused in areas needing stronger, more user-friendly authentication."
                                    "  \n  ", fill='white', font=("calibri", 15))
            canvas.create_text(140, 220, text="Schemes used:", fill='white', font=("calibri", 22, "bold"))
            canvas.create_text(150, 270, text="~  Text-based Scheme", fill='white', font=("calibri", 18, "bold"))
            canvas.create_text(600, 320,
                               text="Using text-based security in a Graphical Password Authentication System involves adding text elements, such as labels, hints, or \npasscodes, to support and strengthen the graphical authentication process. This is the first level of security in which users have"
                                    "\nto register or login before moving to further process.", fill='white',
                               font=("calibri", 15))
            canvas.create_text(150, 400, text="~  Color-based Scheme", fill='white', font=("calibri", 18, "bold"))
            canvas.create_text(600, 450,
                               text="Using color-based security in a Graphical Password Authentication System involves integrating colors as an additional layer of \nsecurity. Users may select specific colors, remember color patterns, enhancing both security and usability. This method increases"
                                    "\npassword complexity and makes it more difficult for attackers to guess the authentication sequence.",
                               fill='white', font=("calibri", 15))
            canvas.create_text(150, 530, text="~  Image-based Scheme", fill='white', font=("calibri", 18, "bold"))
            canvas.create_text(600, 580,
                               text="Using image-based security in a Graphical Password Authentication System involves selecting, recognizing, or interacting with \nsome images to authenticate a user. This method enhances both the security and user experience, making it harder for attackers"
                                    "\nto guess or steal passwords through traditional methods.", fill='white',
                               font=("calibri", 15))
            canvas.pack(fill="both", expand=True)


root=Tk()
obj=Home_page(root)
root.mainloop()