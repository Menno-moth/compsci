import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkinter import PhotoImage

# Frame switch function
def show_frame(frame):
    frame.tkraise()


# Logout function
def Add_Logout(window):
    def Logout(event=None):
        show_frame(Login)
        Username_Entry.delete(0, tk.END)
        Password_Entry.delete(0, tk.END)
        Show_Password_Var.set(False)
        Password_Entry.config(show="*")

    Logout_Button = tk.Button(window, text="Log Out", command=Logout, bg="red")
    Logout_Button.pack(side="bottom", anchor="w", padx=10, pady=10)

    window.bind("<Escape>", Logout)
    return Logout


# Server / Cook / Manager frames
def Server_Login():
    show_frame(Servers)

def Cook_Login():
    show_frame(Cooks)

def Manager_Login():
    show_frame(Manager)


# Login validation
def Validate_Login():
    User_ID = Username_Entry.get()
    Password = Password_Entry.get()

    if User_ID == "service@cafemenno" and Password == "cafemennoservice":
        Server_Login()
    elif User_ID == "kitchen@cafemenno" and Password == "cafemennokitchen":
        Cook_Login()
    elif User_ID == "management@cafemenno" and Password == "cafemennomanagement":
        Manager_Login()
    else:
        messagebox.showerror("Login Failed", "Invalid username or password")

# Password toggle
def Toggle_Password():
    if Password_Entry.cget("show") == "*":
        Password_Entry.config(show="")
    else:
        Password_Entry.config(show="*")


# Main window
Main = tk.Tk()
Main.title("Cafe System")
Main.geometry("800x600")

Show_Password_Var = tk.BooleanVar()

# Login Frame
Login = tk.Frame(Main)

Username_Label = tk.Label(Login, text="Userid:")
Username_Label.pack()

Username_Entry = tk.Entry(Login)
Username_Entry.pack()

Password_Label = tk.Label(Login, text="Password:")
Password_Label.pack()

Password_Entry = tk.Entry(Login, show="*")
Password_Entry.pack()

Show_Password = tk.Checkbutton(
    Login,
    text="Show Password",
    variable=Show_Password_Var,
    command=Toggle_Password
)
Show_Password.pack()

Login_Button = tk.Button(Login, text="Login", command=Validate_Login)
Login_Button.pack()

# Bind Enter key to login
Main.bind("<Return>", lambda event: Login_Button.invoke())


# server frame's frames
Food_Order = tk.Frame(Main)
tk.Label(Food_Order, text="This is the Food_Order window!").pack(pady=20)

Back_Button = tk.Button(Food_Order, text="Back", command=lambda: show_frame(Servers)) # make back button into a function like logout later
Back_Button.pack(side="bottom", anchor="w", padx=10, pady=10)

Drink_Order = tk.Frame(Main)
tk.Label(Drink_Order, text="This is the Drink_Order window!").pack(padx = 20, pady = 20)

Back_Button = tk.Button(Drink_Order, text="Back", command=lambda: show_frame(Servers))
Back_Button.pack(side="bottom", anchor="w", padx=10, pady=10)


# Server Frame
Servers = tk.Frame(Main)
tk.Label(Servers, text="This is the servers' window!").pack(pady=20)
Logout_Server = Add_Logout(Servers)
Order_Food = tk.Button(Servers, text="Food", command=lambda: show_frame(Food_Order)).pack()
Order_Drink = tk.Button(Servers, text="drink", command=lambda: show_frame(Drink_Order)).pack()
Servers.bind("<Escape>", Logout_Server)

# Cook Frame
Cooks = tk.Frame(Main)
tk.Label(Cooks, text="This is the Cooks' window!").pack(pady=20)
Logout_Cook = Add_Logout(Cooks)
Cooks.bind("<Escape>", Logout_Cook)

# Manager Frame
Manager = tk.Frame(Main)
tk.Label(Manager, text="This is Menno's manager window!").pack(pady=20)
Logout_Manager = Add_Logout(Manager)
Manager.bind("<Escape>", Logout_Manager)


# place frames into main window and stack them on tpo of each other
for frame in (Login, Servers, Cooks, Manager, Food_Order, Drink_Order):
    frame.place(relwidth=1, relheight=1)

# Start on login
show_frame(Login)


Main.mainloop()