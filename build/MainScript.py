from tkinter import *
import customtkinter as ctk

from PIL import Image  # Import Image from Pillow for loading images
import random

from ctypes import *
from BlurWindow.blurWindow import *

from pathlib import Path
from tkinter import Tk, Canvas, Entry, Button, PhotoImage, ttk, messagebox,filedialog, Toplevel, Label
import tkinter as tk

BASE_DIR = Path(__file__).resolve().parent
EMPLOYEE_FILE_PATH = BASE_DIR / "data" / "employees.json" 
import employee_manager as em
import pywinstyles
import json
import os

# Define the assets path relative to the base directory
ASSETS_PATH = BASE_DIR / "assets" / "frame0"

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)
window =  ctk.CTk()

# Hide the default title bar
window.overrideredirect(True)
window.config(bg='black')
# Update the window before applying the blur effect
window.update()
# Get the window handle and apply blur effect
hWnd = windll.user32.GetForegroundWindow()
global username

# # Set window transparency
# window.wm_attributes("-transparent", 'green')

# Create the main window
#root = ctk.CTk()

window.geometry("818x536")

button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))

# Function to apply blur with custom color
def apply_color(hex_color):
    hWnd = windll.user32.GetForegroundWindow()
    blur(hWnd, hexColor=hex_color)






#===========================================================================================


def open_second_page():
  
    
    OUTPUT_PATH = Path(__file__).parent
    ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\mrxcr\OneDrive\Desktop\Tkinter-Designer-master\build\assets\frame1")


    def relative_to_assets(path: str) -> Path:
        return ASSETS_PATH / Path(path)
    GG = False
    if GG == True:
        return

    
    canvas = Canvas(
        window,
        bg = "black",
        height = 818,
        width = 1020,
        bd = 0,
        highlightthickness = 0,
        relief = "ridge"
    )

    canvas.place(x = 0, y = 30)

  
    Tabl_canvas = Canvas(
        window,
        bg = "black",
        height = 692.2831420898438,
        width = 519.1370544433594,
        bd = 0,
        highlightthickness = 0,
        relief = "ridge"
    )
    Tabl_canvas.place(x=18, y=110) 
  


    ##=================Table============================================
    # Create a rounded frame for the table
    table_frame = ctk.CTkFrame(Tabl_canvas, corner_radius=0, fg_color="#2b2b2b") 
    table_frame.pack( fill="both", expand=False)
   # Create the Treeview widget (table)
    tree = ttk.Treeview(table_frame, columns=("Name", "Age", "ID", "Salary","Gender","Number","Email","Years of Exp."), show='headings', height=13)

    # Function to load data from JSON file and insert into the table
    def load_json_data(file_path, treeview):
        with open(file_path, 'r') as json_file:
            data = json.load(json_file)
            # Clear existing data
            for row in treeview.get_children():
                treeview.delete(row)
            # Insert new data into the treeview
            for item in data:
                treeview.insert("", "end", values=(item["Name"], item["Age"], item["ID"], item["Salary"],item["Gender"], item["Number"], item["Email"], item["Years of Exp."]))

    # Function to display employees in the tkinter Treeview

    def Reset_Table(treeview):
        employees = load_json_data(EMPLOYEE_FILE_PATH, treeview)

 

    # Customize style for Treeview
    style = ttk.Style()
    style.theme_use("default")
    style.configure("Treeview", 
                    background="black", 
                    foreground="#a1a1a1", 
                    rowheight=40, 
                    fieldbackground="#a1a1a1", 
                    bordercolor="#a1a1a1", 
                    borderwidth=0,
                    font=("Poppins", 11))
    style.configure("Treeview.Heading", 
                    background="#a1a1a1", 
                    foreground="black", 
                    relief="flat",        

                    font=("Poppins", 12, "bold"))
    style.map('Treeview', 
            background=[('selected', '#a1a1a1')],  # Custom color for selected item
            foreground=[('selected', 'black')])    # Text color when selected
    style.map("Treeview.Heading",
            background=[('active', '#0d0d0d'),  # Color when hovering over the header
                        ('pressed', '#0d0d0d')],  # Color when the header is clicked (pressed)
            foreground=[('pressed', 'white')])  # Text color when the header is pressed

 
    # Define the column headings
    tree.heading("Name", text="Name")
    tree.heading("Age", text="Age")
    tree.heading("ID", text="ID")
    tree.heading("Salary", text="Salary")
    tree.heading("Gender", text="Gender")
    tree.heading("Number", text="Number")
    tree.heading("Email", text="Email")
    tree.heading("Years of Exp.", text="Years of Exp.")
    style.configure("Treeview", rowheight=40)
    # Set column widths and alignment
    tree.column("Name", anchor="center", width=111)
    tree.column("Age", anchor="center", width=111)
    tree.column("ID", anchor="center", width=111)
    tree.column("Salary", anchor="center", width=111)
    tree.column("Gender", anchor="center", width=111)
    tree.column("Number", anchor="center", width=111)
    tree.column("Email", anchor="center", width=111)
    tree.column("Years of Exp.", anchor="center", width=111)

    # Pack the Treeview widget into the rounded frame
    tree.pack(fill="both", expand=False)
    #tree.selection_set(30)
   

    # Load data from the JSON file and populate the table
    load_json_data(EMPLOYEE_FILE_PATH, tree)
    first_item = tree.get_children()[0]  # Get the first item (index 0)
    
    # Select the first item
    tree.selection_set(first_item)

    # Function to import employee data from a JSON file
    def import_employees():
        file_path = filedialog.askopenfilename(defaultextension=".json", filetypes=[("JSON files", "*.json")])
        if not file_path:
            return

        with open(file_path, 'r') as file:
            employees = json.load(file)
        em.save_employees(employees)
        Reset_Table(tree)

    # Function to export employee data to a JSON file
    def export_employees():
        file_path = filedialog.asksaveasfilename(defaultextension=".json", filetypes=[("JSON files", "*.json")])
        if not file_path:
            return

        employees = load_json_data(EMPLOYEE_FILE_PATH, tree)
        with open(file_path, 'w') as file:
            json.dump(employees, file, indent=4)
        print(f"Employees exported to {file_path}.")
    #==================================================================

    def search():
        query = Search_entry.get().lower()  # Get the search query and convert to lowercase
        
        if query == "":
            # If the search query is empty, show all items
            Reset_Table(tree)
            return
        
        any_match = False
        for item in tree.get_children():
            # Get the values of the current item
            values = tree.item(item, 'values')
            # Check if the query is in any of the columns
            if any(query in str(value).lower() for value in values):
            # tree.item(item, tags='show')
                any_match = True
            else:
            # tree.item(item, tags='hide')
                tree.delete(item)
        
        # Update the visibility of rows
        tree.tag_configure('show', background='white')
        tree.tag_configure('hide', background='lightgrey')
        
        # Detach items that are hidden
        for item in tree.get_children():
            if 'hide' in tree.item(item, 'tags'):
                tree.detach(item)
        
        # Optionally, show a message if no items match
        if not any_match:
            print("No matches found.")


    def reset():
        Search_entry.delete(0, tk.END)  # Clear the search entry
        Reset_Table(tree)  # Reload and display all employee data
        tree.selection_remove(tree.selection())  # Deselect any selected item

            

    # Create a frame for the search bar and buttons
    search_frame = tk.Frame(window, bg="white")
    search_frame.place(x=285, y=window.winfo_height() - 460) 


    # Create a search button

    #=================================================================


    def toggle_form():
        if form_frame.winfo_viewable():  # If form is visible, hide it
            form_frame.pack_forget()
            ColordFrame.pack_forget()
           
       
            _CancelBTN.pack_forget()
            _CancelBTN.place(x=185,y=1000)
            # show_button.configure(text="Show Form")
        else:  # Otherwise, show it
          
            form_frame.pack(side="right", ipadx=0)
            ColordFrame.pack(side="right", ipadx=0)
       
            _CancelBTN.pack()

            _CancelBTN.place(x=530,y=455)

                


          

    selected_item = tree.selection()
    # if not selected_item:
    #     print("select item first")
        
    # if selected_item:
    #     print(tree.item(selected_item[0])['ID'])

    id_var_Selected = tk.IntVar()


    def on_item_click(event):
        # Get the selected item
        selected_item = tree.focus()  # Returns the selected item's ID
        item_values = tree.item(selected_item, 'values')  # Get the values of the item
        print("Selected item contents:", item_values[2])  # Print the item contents
        
        # Use .set() to assign the value to IntVar
        id_var_Selected.set(item_values[2])
        FillEntryFileds()

        # To verify, print the value from IntVar
        print("Stored ID in IntVar:", id_var_Selected.get())


    

    # Bind a click event to the Treeview
    tree.bind('<ButtonRelease-1>', on_item_click)  # ButtonRelease-1 is the left-click event



    Search_entry = ctk.CTkEntry(canvas, fg_color="transparent",width=220, height=30, placeholder_text="Search",corner_radius=45,border_width=1,border_color="#999999")
    Search_entry.pack(pady=20, padx=20)

    Search_entry.place(x=15+36, y=20)
    def on_enter(event):
        search_text = Search_entry.get()
        search()
        print(f"Search for: {search_text}")
    # Bind the Enter key event to the entry widget
    Search_entry.bind("<Return>", on_enter)


    #Resets the Table if the search filed is empty
    global ResetIt  # Declare it as global at the beginning
    ResetIt = False

    if Search_entry.get() != "":
        ResetIt = True  # No need to declare again inside the if block
            
    if ResetIt == True and Search_entry.get() == "":
        Reset_Table()
        ResetIt = False

    button_image_1 = PhotoImage(
        file=relative_to_assets("button_1.png"))

    _SearchBTN = ctk.CTkButton(canvas, 
                    text="", 
                    image=button_image_1, 
                    fg_color="transparent",    # No background color
                    hover_color="black", # No hover color
                    border_width=0,   # Remove border
                    corner_radius=0,
                    background_corner_colors=None,
                    bg_color="transparent",
                    
                    command= search
                    )  # No corner radius
    _SearchBTN.pack(pady=20, padx=20)
    pywinstyles.set_opacity(_SearchBTN, color="black")
    _SearchBTN.place(
        x=185+38,
        y=16,
    )
    button_image_9 = PhotoImage(
    file=relative_to_assets("BackBtn.png"))
    def restart_window():
        #Here Chat GPT
        pass
    

    _BackBTN = ctk.CTkButton(canvas, 
                    text="", 
                    image=button_image_9, 
                    fg_color="transparent",    # No background color
                    hover_color="black", # No hover color
                    border_width=0,   # Remove border
                    corner_radius=0,
                    background_corner_colors=None,
                    bg_color="transparent",
                    
                    command= lambda: LoginMenuCreate()
                    )  # No corner radius
    _BackBTN.pack(pady=20, padx=20)
    pywinstyles.set_opacity(_BackBTN, color="black")
    _BackBTN.place(
        x=-41,
        y=16,
    )


    button_image_2 = PhotoImage(
        file=relative_to_assets("button_2.png"))

    _AddBTN = ctk.CTkButton(canvas, 
                    text="", 
                    image=button_image_2, 
                    fg_color="transparent",    # No background color
                    hover_color="black", # No hover color
                    border_width=0,   # Remove border
                    corner_radius=0,
                    background_corner_colors=None,
                    bg_color="transparent",
                    command= lambda: (functext_var.set("Add") ,ResetEntryFileds(),toggle_form(), print(functext_var.get()))#(em.add_employee(name_var.get(),age_var.get(),id_var.get(),salary_var.get()),Reset_Table(tree)) ,
                    )  # No corner radius
    _AddBTN.pack(pady=20, padx=20)
    pywinstyles.set_opacity(_AddBTN, color="black")
    _AddBTN.place(
        x=702,
        y=419 -90 -90 -90 -90,


    )



    button_image_3 = PhotoImage(
        file=relative_to_assets("button_3X.png"))

    def FillEntryFileds ():
        employees = em.load_employees()
        matched_employees = [e for e in employees if int(e["ID"]) == int(id_var_Selected.get())]
        #print(matched_employees)
        employee = matched_employees[0]

        NameEntry.delete(0, 'end')
        NameEntry.insert(0, employee["Name"])
        
        AgeEntry.delete(0, 'end')
        AgeEntry.insert(0, employee["Age"])
        
        IDEntry.delete(0, 'end')
        IDEntry.insert(0, employee["ID"])
        
        SalaryEntry.delete(0, 'end')
        SalaryEntry.insert(0, employee["Salary"])
        
        NumberEntry.delete(0, 'end')
        NumberEntry.insert(0, employee["Number"])
        
        EmailEntry.delete(0, 'end')
        EmailEntry.insert(0, employee["Email"])
        
        YOXEntry.delete(0, 'end')
        YOXEntry.insert(0, employee["Years of Exp."])

        
    def ResetEntryFileds ():
        if functext_var.get() == "Add":

            NameEntry.delete(0, 'end')
            
            AgeEntry.delete(0, 'end')
            
            IDEntry.delete(0, 'end')
            
            SalaryEntry.delete(0, 'end')
            
            NumberEntry.delete(0, 'end')
            
            EmailEntry.delete(0, 'end')
            
            YOXEntry.delete(0, 'end')
        
        


    _EditBTN = ctk.CTkButton(canvas, 
                    text="", 
                    image=button_image_3, 
                    fg_color="transparent",    # No background color
                    hover_color="black", # No hover color
                    border_width=0,   # Remove border
                    corner_radius=0,
                    background_corner_colors=None,
                    bg_color="transparent",
                    command=lambda: (functext_var.set("Edit") ,FillEntryFileds (),toggle_form(), print(functext_var.get())) #print#
                    )  # No corner radius
    _EditBTN.pack(pady=20, padx=20)
    pywinstyles.set_opacity(_EditBTN, color="black")
    _EditBTN.place(
        x=702,
        y=419 - 90 -90 -90,

    )


    button_image_4 = PhotoImage(
        file=relative_to_assets("button_4X.png"))

    _importBTN = ctk.CTkButton(canvas, 
                    text="", 
                    image=button_image_4, 
                    fg_color="transparent",    # No background color
                    hover_color="black", # No hover color
                    border_width=0,   # Remove border
                    corner_radius=0,
                    background_corner_colors=None,
                    bg_color="transparent",
                    command=lambda: import_employees()
                    )  # No corner radius
    _importBTN.pack(pady=20, padx=20)
    pywinstyles.set_opacity(_importBTN, color="black")
    _importBTN.place(
        x=702,
        y=419 - 90,
      
    )

    button_image_5 = PhotoImage(
        file=relative_to_assets("button_5X.png"))

    _DeleteBTNq = ctk.CTkButton(canvas, 
                       text="", 
                       image=button_image_5, 
                       fg_color="transparent",    # No background color
                       hover_color="black", # No hover color
                       border_width=0,   # Remove border
                       corner_radius=0,
                       background_corner_colors=None,
                       bg_color="transparent",
                       command=lambda:(em.delete_employee(id_var_Selected.get()),Reset_Table(tree))
                       )  # No corner radius
    _DeleteBTNq.pack(pady=20, padx=20)
    pywinstyles.set_opacity(_DeleteBTNq, color="black")
    _DeleteBTNq.place(
        x=702,
      
        y=419 - 90 - 90,

    )

    button_image_6 = PhotoImage(
        file=relative_to_assets("button_6Xx.png"))

    _ExportBTN = ctk.CTkButton(canvas, 
                    text="", 
                    image=button_image_6, 
                    fg_color="transparent",    # No background color
                    hover_color="black", # No hover color
                    border_width=0,   # Remove border
                    corner_radius=0,
                    background_corner_colors=None,
                    bg_color="transparent",
                    command= lambda: export_employees()
                    )  # No corner radius
    _ExportBTN.pack(pady=20, padx=20)
    pywinstyles.set_opacity(_ExportBTN, color="black")
    _ExportBTN.place(
        x=702,
        y=419,
    )
   
    
   #===============================================================
    
    # Function to toggle the form's visibility

            # show_button.configure(text="Hide Form")
    

    # # Main button to show/hide the form
    # show_button = ctk.CTkButton(
    #     canvas,
    #     text="Show Form",
    #     command=toggle_form,
    #     width=200,
    #     height=50
    # )
    # show_button.pack()
    

    # Frame to hold the form widgets (initially hidden)
    form_frame = ctk.CTkFrame(window, width=350, height=1000,bg_color="black",fg_color="black")
    
    form_frame.pack_forget()  # Hide the frame at the beginning

    ColordFrame = ctk.CTkFrame(window, width=1, height=1000,bg_color="transparent",fg_color="transparent")
    functext_var = tk.StringVar()
    name_var = tk.StringVar()
    age_var = tk.StringVar()
    id_var = tk.StringVar()
    salary_var = tk.StringVar()
    
    gender_var = tk.StringVar()
    number_var = tk.StringVar()
    email_var = tk.StringVar()
    yox_var = tk.StringVar()


    # Add form elements to the frame
    NameEntry = ctk.CTkEntry(form_frame,textvariable= name_var,fg_color="transparent", width=190, height=30, placeholder_text="Name", corner_radius=45, border_width=1, border_color="#bababa")
    NameEntry.pack(pady=10)

    AgeEntry = ctk.CTkEntry(form_frame,textvariable= age_var, fg_color="transparent", width=190, height=30, placeholder_text="Age", corner_radius=45, border_width=1, border_color="#bababa")
    AgeEntry.pack(pady=10)

    IDEntry = ctk.CTkEntry(form_frame,textvariable= id_var, fg_color="transparent", width=190, height=30, placeholder_text="ID", corner_radius=45, border_width=1, border_color="#bababa")
    IDEntry.pack(pady=10)

    SalaryEntry = ctk.CTkEntry(form_frame,textvariable= salary_var, fg_color="transparent", width=190, height=30, placeholder_text="Salary", corner_radius=45, border_width=1, border_color="#bababa")
    SalaryEntry.pack(pady=10)

    # GenderEntry = ctk.CTkEntry(form_frame, fg_color="transparent", width=190, height=30, placeholder_text="Gender", corner_radius=45, border_width=1, border_color="#bababa")
    # GenderEntry.pack(pady=10)

    # Function to display selected gender
    def SelectGender():
        selected_gender = gender_combobox.get()
        gender_var.set(selected_gender)
        print("Gender in IntVar:", gender_var.get())


    

    
   

    # Create a CTkComboBox for gender selection
    gender_combobox = ctk.CTkComboBox(
        master=form_frame,
        values=["Male", "Female", "Other"],  # Gender options
        fg_color="black",
        width=190,
        height=30,
        corner_radius=45, 
        border_width=1, 
        border_color="#bababa"
    )
    gender_combobox.pack(pady=10)


    NumberEntry = ctk.CTkEntry(form_frame,textvariable= number_var, fg_color="transparent", width=190, height=30, placeholder_text="Number", corner_radius=45, border_width=1, border_color="#bababa")
    NumberEntry.pack(pady=10)

    EmailEntry = ctk.CTkEntry(form_frame,textvariable= email_var, fg_color="transparent", width=190, height=30, placeholder_text="Email", corner_radius=45, border_width=1, border_color="#bababa")
    EmailEntry.pack(pady=10)

    YOXEntry = ctk.CTkEntry(form_frame,textvariable= yox_var, fg_color="transparent", width=190, height=30, placeholder_text="Search", corner_radius=45, border_width=1, border_color="#bababa")
    YOXEntry.pack(pady=10)



    NameText = ctk.CTkLabel(form_frame,height=20, text="Name")
    NameText.place(x=100,y=0)

    AgeText = ctk.CTkLabel(form_frame,height=20, text="Age")
    AgeText.place(x=108,y=51.3)

    IDText = ctk.CTkLabel(form_frame,height=20, text="ID")
    IDText.place(x=113,y=51.3+51.3)

    SalaryText = ctk.CTkLabel(form_frame,height=20, text="Salary")
    SalaryText.place(x=100,y=51.3+51.3+51.3)

    GenderText = ctk.CTkLabel(form_frame,height=20, text="Gender")
    GenderText.place(x=100,y=51.3+51.3+51.3+51.3)

    NumberText = ctk.CTkLabel(form_frame,height=20, text="Number")
    NumberText.place(x=100,y=51.3+51.3+51.3+51.3+51.3)

    EmailText = ctk.CTkLabel(form_frame,height=20, text="Email")
    EmailText.place(x=100,y=51.3+51.3+51.3+51.3+51.3+51.3)


    YOXText = ctk.CTkLabel(form_frame,height=20, text="Years of Exp.")
    YOXText.place(x=86,y=51.3+51.3+51.3+51.3+51.3+51.3+51.3)

    button_image_1 = PhotoImage(
        file=relative_to_assets("ConfirmBTN.png"))
    _ConfirmBTN = ctk.CTkButton(form_frame, 
                        text="", 
                        image=button_image_1, 
                        fg_color="transparent",    # No background color
                        hover_color="black", # No hover color
                        border_width=0,   # Remove border
                        corner_radius=0,
                        background_corner_colors=None,
                        bg_color="transparent",
                        
                        
                        command=lambda:(SelectGender(),em.add_employee(functext_var.get(),name_var.get(),age_var.get(),id_var.get(),salary_var.get(),gender_var.get(),number_var.get(),email_var.get(),yox_var.get()),     (em.edit_employee(functext_var.get(),id_var_Selected.get(),name_var.get(),age_var.get(),id_var.get(),salary_var.get(),gender_var.get(),number_var.get(),email_var.get(),yox_var.get()))    ,Reset_Table(tree),ResetEntryFileds()) ,
                        )  # No corner radius
    _ConfirmBTN.pack(pady=20, padx=20)
    pywinstyles.set_opacity(_ConfirmBTN, color="black")


    button_image_2 = PhotoImage(
        file=relative_to_assets("CancelBTN.png"))
  
    _CancelBTN = ctk.CTkButton(window, 
                        text="", 
                        width=40,
                        image=button_image_2, 
                        fg_color="black",    # No background color
                        hover_color="black", # No hover color
                        border_width=0,   # Remove border
                        corner_radius=0,
                        background_corner_colors=None,
                        bg_color="transparent",
                        
                        command=lambda: toggle_form()
                        )  # No corner radius


    #_CancelBTN.pack(pady=20, padx=20)
    pywinstyles.set_opacity(_CancelBTN, color="black")

    _CancelBTN.pack_forget()



   # window.resizable(False, False)
    #window.mainloop()






def LoginMenuCreate():
        
    canvas = Canvas(
        window,
        bg="black",
        height=700,
        width=1200,
        bd=0,
        highlightthickness=0,
  
        
        relief="ridge"
    )
    canvas.place(relx=0, rely=0.05)

    # background_img = PhotoImage(file=relative_to_assets("Dialog2.png"))

    # background_label = canvas.create_image(0, 0, anchor="nw", image=background_img)



    # background_img = PhotoImage(file=relative_to_assets("GlassPanel.png"))
    # background_label =canvas.create_image(100, 100, anchor="nw", image=background_img)

    # pywinstyles.set_opacity(background_label, color="red")


    increasey = 5
    canvas.place(x=0, y=0)
    canvas.create_text(
        388,
        140+increasey,
        anchor="nw",
        text="Login",
        fill="white",
        font=("Poppins", 30 * -1,"bold")
    )

    UserEntry2 = ctk.CTkEntry(canvas, fg_color="transparent",width=240, height=35, placeholder_text="Enter username",corner_radius=45,border_width=1,border_color="#999999")

    UserEntry2.pack(pady=20, padx=20)

    UserEntry2.place(x=309, y=141+30+10+increasey)


    # Function to return random special character
    def get_random_special_char():
        special_chars = '@!#$%&'
        return random.choice(special_chars)

    # Function to update the entry dynamically with random mask characters

    def update_show_char(*args):

        input_text = PassEntry2.get()  # Get the current input text
        masked_text = ''.join([get_random_special_char() for _ in input_text])  # Generate random special chars for each character
        PassEntry2.delete(0, "end")  # Clear the entry
        PassEntry2.insert(0, masked_text)  # Insert the masked text
    
    def returnPassEntry2():
        #return PassEntry2.get()  # Get the current input text
        print(PassEntry2.get())
    


    # Create the password entry (no show argument needed here, we handle it manually)
    PassEntry2 = ctk.CTkEntry(
        canvas,
        fg_color="transparent",
        width=240,
        height=35,
        placeholder_text="Enter password",
        corner_radius=45,
        border_width=1,
        border_color="#999999",
        show="*"
    )
    PassEntry2.pack(pady=20, padx=20)

    # Bind the entry to update the show characters every time the user types
   # PassEntry2.bind("<KeyRelease>", (returnPassEntry2(),update_show_char))

    PassEntry2.place(x=309, y=220+30+increasey)



    def login():
        username = UserEntry2.get()
        password = PassEntry2.get()
        
        # Replace with your actual username and password
        correct_username = "admin"
        correct_password = "123456"
        
        if username == correct_username and password == correct_password:
            # Open the second page
            open_second_page()
        else:
            # You can add a message box or some error indication here
            messagebox.showwarning("Erorr","Wrong Password!")
            print(returnPassEntry2())



    Login_BTN_button = ctk.CTkButton(canvas,bg_color="black", text="Login",fg_color="#835ADC", command=login,width=240,height=35,corner_radius=45,hover_color="#6344a6")

    # Position the button in the window
    Login_BTN_button.place(x=430, y=308+20+increasey, anchor="center")  # Center the button
    pywinstyles.set_opacity(Login_BTN_button, color="black")



    canvas.create_text(
        388,
        188+10+increasey,
        anchor="nw",
        text="Username",
        fill="#999999"  ,
        font=("Poppins", 16 * -1)
    )

    canvas.create_text(
        388,
        288+increasey,
        anchor="nw",
        text="Password",
        fill="#999999",
        font=("Poppins", 16 * -1)
    )



blur(hWnd, "#21212140","#21212140")  # Adjust the blur hex color here

# Function to allow window dragging
def move_app(event):
    window.geometry(f"+{event.x_root}+{event.y_root}")

# Create a custom title bar frame
title_bar = tk.Frame(window, bg="#141414", relief="raised", bd=0)
title_bar.pack(fill=tk.X)

# Create a flat button
close_button = ctk.CTkButton(
    title_bar,
    text="X",
    width=24,
    command=window.quit,
    fg_color="#141414",  # Background color
    hover_color="#d1d1d1",  # Hover color
    text_color="#d1d1d1",  # Text color
    border_width=0,  # Removes border
    text_color_disabled="black",
    corner_radius=0
)
close_button.pack(side=tk.RIGHT)
close_button.bind("<Enter>", lambda event: close_button.configure(text_color="#141414",fg_color="#d1d1d1")) 
close_button.bind("<Leave>", lambda event: close_button.configure(text_color="#d1d1d1",fg_color="#141414"))    

# Add a label for the custom title
title = tk.Label(title_bar, text="Database mangment", bg="#141414", fg="#d1d1d1", relief="flat",font=
                 ("Poppins", 12),padx=10)
title.pack(side=tk.LEFT)
# Helvetica
# Verdana
# Tahoma
# Trebuchet MS
# Serif Fonts:

# Times New Roman
# Georgia
# Garamond
# Baskerville
# Monospace Fonts:

# Courier New
# Lucida Console
# Consolas
# Menlo
# Display Fonts:

# Impact
# Comic Sans MS
# Arial Black

# Bind the window movement to the title bar
title_bar.bind("<B1-Motion>", move_app)

LoginMenuCreate()


#window.resizable(False, False)
window.mainloop()
