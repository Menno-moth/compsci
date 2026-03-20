
import tkinter as tk 
from tkinter import ttk
import pickle
import csv
import os  # added

# --- get script folder and pkl path ---
#script_dir = os.path.dirname(os.path.abspath(__file__))
#pkl_path = os.path.join(script_dir, "products.pkl")


#class product:
 #   def __init__(self, id, name, price):
  #      self.id = id
   #     self.name = name
    #    self.price = price

    #def set_price(self, new_price):
     #   try:
      #      self.price = float(new_price)
       #     return True
        #except:
         #   return False
#
 #   def get_attributes(self):
  #      obj_att = [self.id, self.name, self.price]
   #     return obj_att
#

#def import_products():
 #   with open(os.path.join(script_dir, "products.csv"), mode='r', newline='') as file:
  #      my_products = list(csv.reader(file))
   # print(my_products)

    #my_objects = []
#    for row in range(len(my_products)):
#        temp = product(int(my_products[row][0]), my_products[row][1], float(my_products[row][2]))
 #       my_objects.append(temp)

  #  with open(pkl_path, 'wb+') as file:
  #      pickle.dump(my_objects, file)
  #      print("done")


#def save(entry_w, root):
 #   my_product = entry_w[0].get()
 #   price = entry_w[1].get()

    # load products safely
 #   if os.path.exists(pkl_path):
 #       with open(pkl_path, 'rb') as file:
 #           product_objects = list(pickle.load(file))
 #   else:
 #       product_objects = []

  #  final_object = len(product_objects) - 1 if product_objects else 0
  #  id = (product_objects[final_object].id + 1) if product_objects else 1
  #  temp = product(int(id), my_product, float(price))
 #   product_objects.append(temp)

   # with open(pkl_path, 'wb+') as file:
   #     pickle.dump(product_objects, file)

   # print("done")
   # root.destroy()
   # start()


#def edit_object(product_objects, listboxprod, root):
    #prod_index = listboxprod.curselection()[0]
   # my_product = product_objects[prod_index].get_attributes()
   # topframe = tk.Tk()
 #   my_labels = ["product", "price"]
 #   entry_w = []
 ##   for row in range(len(my_labels)):
 #       label = ttk.Label(topframe, text=my_labels[row])
 #       label.grid(row=row, column=0)
 #       entry = ttk.Entry(topframe)
 #       entry.delete(0, tk.END)
 #       entry.insert(0, my_product[row+1])
 #       entry.grid(row=row, column=1)
 #       entry_w.append(entry)
 #   button = ttk.Button(topframe, text="save", command=lambda: save_edit(product_objects, prod_index, entry_w, topframe, root))
 #   button.grid(row=row + 1, column=0)

 #   topframe.mainloop()


#def save_edit(product_objects, prod_index, entry_w, topframe, root):
   # a_product = entry_w[0].get()
   # a_price = entry_w[1].get()
   # my_object = product_objects[prod_index]
   # my_object.name = a_product
   # my_object.price = a_price

  #  with open(pkl_path, 'wb+') as file:
  #      pickle.dump(product_objects, file)

  #  topframe.destroy()
  #  root.destroy()
   # start()


#def delete_object(product_objects, listbox, root):
   # product_index = listbox.curselection()[0]
   # product_objects.pop(product_index)

   # with open(pkl_path, 'wb+') as file:
    #    pickle.dump(product_objects, file)

    #root.destroy()
    #start()


#def start():
   # root = tk.Tk()
   # topFrame = tk.Frame(root)
   # topFrame.grid(row=0, column=0)
   # midFrame = tk.Frame(root)
 #   botFrame = tk.Frame(root)
  #  botFrame.grid(row=2, column=1)
#
 #   my_labels = ["product", "price"]
 #   entry_w = []
 #   for row in range(len(my_labels)):
 #       label = ttk.Label(topFrame, text=my_labels[row])
 #       label.grid(row=row, column=0)
 #       entry = ttk.Entry(topFrame)
 #       entry.grid(row=row, column=1)
 #       entry_w.append(entry)
 #   button = ttk.Button(topFrame, text="save", command=lambda: save(entry_w, root))
 #   button.grid(row=row + 1, column=0)
#
 #   # load products safely
 #   if os.path.exists(pkl_path):
 #       with open(pkl_path, 'rb') as file:
#product_objects = list(pickle.load(file))
 #   else:
 #       product_objects = []
#
 #   product_list = []
 #   for obj in product_objects:
 #       product_list.append(obj.get_attributes())
#
 #   scrollbar = tk.Scrollbar(midFrame, orient=tk.VERTICAL)
 #   listboxprod = tk.Listbox(midFrame, yscrollcommand=scrollbar.set, height=15, width=60, exportselection=False)
 #   scrollbar.config(command=listboxprod.yview)
 #   for i in range(len(product_list)):
 #       listboxprod.insert(tk.END, product_list[i])
 #   listboxprod.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
 #   scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
#
 #   buttonedit = ttk.Button(botFrame, text="edit", command=lambda: edit_object(product_objects, listboxprod, root))
 #   buttonedit.grid(row=0, column=0)
 #   buttonedelete = ttk.Button(botFrame, text="delete", command=lambda: delete_object(product_objects, listboxprod, root))
 #   buttonedelete.grid(row=0, column=1)
##
 #   root.mainloop()


#start()

import tkinter as tk 
from tkinter import ttk
from tkinter import messagebox

# Servers' page
def server_login():
    main.withdraw()
    servers = tk.Toplevel ()
    servers.title("servers")
    servers.geometry("800x600")
    tk.Label(servers,text="This is the server' window!").pack(pady=20)
    logout = add_logout(servers)
    servers.bind("<Escape>", logout)

    servers.focus_force()    
    servers.grab_set()        
    servers.lift() 
    

# cooks' page
def cook_login():
    main.withdraw()
    cooks = tk.Toplevel ()
    cooks.title("cooks")
    cooks.geometry("800x600")
    tk.Label(cooks,text="This is the cooks' window!").pack(pady=20)
    logout = add_logout(cooks)
    cooks.bind("<Escape>", logout)

    cooks.focus_force()    
    cooks.grab_set()        
    cooks.lift() 

# menno's page
def manager_login():
    main.withdraw()
    manager = tk.Toplevel ()
    manager.title("manager")
    manager.geometry("800x600")
    tk.Label(manager,text="This is Menno's manager window!").pack(pady=20)
    logout = add_logout(manager)
    manager.bind("<Escape>", logout)
    

    manager.focus_force()    
    manager.grab_set()        
    manager.lift() 
    
# Function to validate the login
def validate_login():
    userid = username_entry.get()
    password = password_entry.get()

    if userid == "servers@cafemenno" and password == "cafemennoservers":
        server_login()
    elif userid == "cooks@cafemenno" and password == "cafemennocooks":
        cook_login()
    elif userid == "manager@cafemenno" and password == "cafemennomanagement":
        manager_login()
    else:
        messagebox.showerror("Login Failed", "Invalid username or password")

# Create the main window
main = tk.Tk()
main.title("Login")
main.geometry("800x600")

# Create and place the username label and entry
username_label = tk.Label(main, text="Userid:")
username_label.pack()

username_entry = tk.Entry(main)
username_entry.pack()

# Create and place the password label and entry
password_label = tk.Label(main, text="Password:")
password_label.pack()

password_entry = tk.Entry(main, show="*")  # Show asterisks for password
password_entry.pack()

def toggle_password():
    if password_entry.cget("show") == "*":
        password_entry.config(show="")
    else:
        password_entry.config(show="*")

show_password_var = tk.BooleanVar()

show_password = tk.Checkbutton(
    main,
    text="Show Password",
    variable=show_password_var,
    command=toggle_password
)
show_password.pack()

# login button
login_button = tk.Button(main, text="Login", command=validate_login)
login_button.pack()
main.bind("<Return>", lambda event: login_button.invoke()) # pressing enter triggers the logout button to be pressed

# logout button
def add_logout(window):
    def logout(event=None):
        window.destroy()
        main.deiconify()
        
        username_entry.delete(0, tk.END)
        password_entry.delete(0, tk.END)
        show_password_var.set(False)
        password_entry.config(show="*")

    logout_button = tk.Button(window, text="Log Out", command=logout, bg="red")
    logout_button.pack(side="bottom", anchor="w", padx=10, pady=10)

    window.bind("<Escape>", logout)

    return logout

# Start the Tkinter event loop
main.mainloop()

