import time
from tkinter import *
from tkinter import ttk
from calendar import month_name
from tkinter import scrolledtext
from tkinter import messagebox
from tkinter import filedialog
import mysql.connector
import threading



def main():

    root  = Tk()

    root.title("Title")
    root.geometry("960x540+250+100")
    root.iconbitmap("../Tkinter/coin.ico")
    # root.resizable(False,False)

    # def login():
    #     print(email.get())
    #     print(password.get())

    #root.attributes("-topmost",1) # The root is always at the top
    #root.lower() # The root is spawned in background
    #root.lift() # The root is spawned in foreground

    photo = PhotoImage(file ="coffee-icon.png")

    #label = Label(text = "I'm under the water\n please help me", padx = 10, pady = 10, font = ("Helvetica",24), cursor = "plus", justify = "center",image = photo ,compound = "left")
    #label.pack()

    #status = StringVar()
    #checkButton= Checkbutton(text = "Text", font = ("helvetica",20), command = lambda: print(status.get()), variable = status, onvalue = "True", offvalue = "False")
    #checkButton.pack()

    ''' ]---------radioButton------
    
    size_selected = StringVar()
    sizes = (
        ("Small","S"),
        ("Medium","M"),
        ("Large","L"),
    )

    for size in sizes:
        radioButton = Radiobutton(text = size[0], value = size[1], variable = size_selected)
        radioButton.pack()

    button = Button(text = "Help", command = lambda: print(size_selected.get()), image = photo,compound = "left", padx = 10, pady = 10)
    button.pack()
    '''

    ''' 
    #--------------Login page---------------
    
    email_label = ttk.Label(text = "Email")
    email_label.pack()

    email = StringVar()
    email_entry = ttk.Entry(textvariable = email)
    email_entry.focus()
    email_entry.pack()

    password_label = ttk.Label(text = "Password")
    password_label.pack()

    password = StringVar()
    password_entry = ttk.Entry(textvariable = password, show = "*")
    password_entry.pack()

    btn = ttk.Button(text = "Login", command = login)
    btn.pack(padx = 10, pady = 20)
    '''

    ''' #----------------- multiple frames--------------------------------
    
    frame1 = Frame(root, background = "green", height = 200, width = 100 )
    frame2 = Frame(root, background = "white", height = 200, width = 100 )
    frame3 = Frame(root, background = "red", height = 200, width = 100 )
    frame1.pack(fill = BOTH, expand = True, side = LEFT)
    frame2.pack(fill = BOTH, expand = True,  side = LEFT)
    frame3.pack(fill = BOTH, expand = True, side = LEFT)

    label1 = ttk.Label(frame1, text = "Text 1", background = frame1["background"])
    label2 = ttk.Label(frame2, text = "Text 2",background = frame2["background"])
    label3 = ttk.Label(frame3, text = "Text 3",background = frame3["background"])
    label1.pack()
    label2.pack()
    label3.pack()
    '''

    ''' #----------------------comboBox--------------------------
    
    selected_month = StringVar()
    comboBox = ttk.Combobox(root, textvariable = selected_month)
    comboBox["values"] = [month_name[m] for m in range(1,12)]
    comboBox["state"] = "readonly"

    def print_month(event):
        print(selected_month.get())

    comboBox.bind("<<ComboboxSelected>>", print_month)

    comboBox.pack(fill = X)
    '''

    '''  #---------------------gridLayout-------------------
    
    root.columnconfigure(0, weight = 1)
    root.columnconfigure(1, weight = 1)

    frame1 = Frame(root, background= "red", height = 200, width = 200)
    frame2 = Frame(root, background= "yellow", height = 200, width = 200)
    frame3 = Frame(root, background= "green", height = 200, width = 200)

    frame1.grid(column = 0, row = 0, rowspan = 2)
    frame2.grid(column = 1, row = 0)
    frame3.grid(column = 1, row = 1)
    '''

    '''#------------------------------ lisBox with scrollBar-----------------------------------
    
    root.columnconfigure(0,weight = 1)
    root.rowconfigure(0, weight = 1)

    months = ("jan", "feb", "mar", "apr", "may", "jun", "jul","aug", "sep", "oct", "nov", "dec",
              "jan", "feb", "mar", "apr", "may", "jun", "jul","aug", "sep", "oct", "nov", "dec",
              "jan", "feb", "mar", "apr", "may", "jun", "jul","aug", "sep", "oct", "nov", "dec")

    selected_moth = StringVar(value = months)

    listbox = Listbox(root, listvariable = selected_moth, selectmode = "extended")
    listbox.grid(column = 0, row = 0, sticky = "nwes")

    scrollBar = ttk.Scrollbar(root, orient = "vertical", command = listbox.yview)
    scrollBar.grid(row = 0, column = 0, sticky = "nse")

    listbox["yscrollcommand"] = scrollBar.set
    '''

    '''#-------------- scrolledText with scrollBar (textArea)--------------------
    
    scrolltxt = scrolledtext.ScrolledText(root, width = 50, height = 10)
    scrolltxt.pack(fill = BOTH, expand = True, side = LEFT)
    '''

    ''' #------------------noteBook---------------------
    
    noteBook = ttk.Notebook(root)
    noteBook.pack(fill = BOTH, expand = True)

    frame1 = Frame(noteBook, background = "orange")
    frame1.pack(fill = BOTH, expand = True)
    frame2 = Frame(noteBook, background = "yellow")
    frame2.pack(fill = BOTH, expand = True)

    noteBook.add(frame1, text = "Frame 1")
    noteBook.add(frame2, text = "Frame 2")
    '''

    ''' #-----------------------table with scrollBar--------------------------
    
    columns = ("name", "last_name", "email")
    table = ttk.Treeview(root, columns = columns, show = "headings")

    table.heading("name", text= "Name" )
    table.heading("last_name", text = "Last name")
    table.heading("email", text ="Email")

    rows = []

    for n in range(1,25):
        rows.append((f"name {n}",f"last name {n}", f"email {n}"))

    for row in rows:
        table.insert("", END,values = row)

    table.grid(row =0, column =0, sticky = "nswe")

    scrollBar = ttk.Scrollbar(root, orient = VERTICAL, comman = table.yview)
    scrollBar.grid(row = 0, column = 1, sticky = "ns")
    table.configure(yscrollcommand = scrollBar.set)
    '''

    ''' #-----------------Menu---------------------
     
    menuBar = Menu(root)
    root.config(menu = menuBar)


    file_menu = Menu(menuBar, tearoff = 0)
    file_menu.add_command(label = "Open")
    file_menu.add_command(label = "Edit")

    other_menu = Menu(file_menu, tearoff = 0)
    other_menu.add_command(label = "Preferences")
    other_menu.add_command(label = "Tool")
    file_menu.add_cascade(label = "Other", menu = other_menu)
    file_menu.add_separator()
    file_menu.add_command(label = "Exit", command = root.quit)



    menuBar.add_cascade(label = "FIle", menu = file_menu)
    '''

    '''
    frame = Frame(root, background = "grey")
    frame.pack(fill = BOTH, expand = True)

    ctx_menu = Menu(root, tearoff = 0)
    ctx_menu.add_command(label = "Cut")
    ctx_menu.add_command(label = "Copy")
    ctx_menu.add_command(label = "Pase")
    ctx_menu.add_separator()
    ctx_menu.add_command(label = "Run")

    def ctx_menu_popup(event):
        try:
            ctx_menu.tk_popup(event.x_root, event.y_root)
        finally:
            ctx_menu.grab_release()

    frame.bind("<Button-3>", ctx_menu_popup)
    '''

    '''#------------------------- MessageBox -------------------------------------------
    
    def show_info_message():
        messagebox.showinfo(title = "Info message", message = "This is a info message")

    def show_ask_message():
        res = messagebox.askyesno(title="Ask message", message="Do you want to exit?")

        if(res):
            root.destroy()

    btn1 = ttk.Button(text = "Info", command = show_info_message)
    btn2 = ttk.Button(text = "Ask", command = show_ask_message)

    btn1.pack(fill = X)
    btn2.pack(fill = X)
    '''

    ''' #-----------------------------fileDialog------------------------------------
    
    def read_file():
       filetypes = (("Tutti i file", "*.*"),("Documenti di testo","*.txt"))
       file_name = filedialog.askopenfilename(title = "Open file", initialdir = "C:\\Users\Davide\\OneDrive\\Documenti\\Utilities\\gameUtilites\\Demon's Souls", filetype = filetypes)

       with open(file_name, "r",encoding="utf-8") as file:
            for line in file:
                print(line, end = "")
       file.close()


    def save_file():
        f = filedialog.asksaveasfile(mode = "w",title = "Save file", defaultextension = ".txt")
        data = "Test"
        f.write(data)
        f.close()


    open_btn = ttk.Button(text = "open", command = read_file)
    open_btn.pack(expand = True)

    write_btn = ttk.Button(text = "write", command = save_file)
    write_btn.pack(expand = True)
    '''

     #----------------------- Select data from dataBase with Threading --------------------------------------
    
    root.rowconfigure(0,weight = 1)
    root.rowconfigure(1,weight = 1)
    root.columnconfigure(0, weight=1)
    root.columnconfigure(1, weight=1)

    def create_table_from_db():
        connection = mysql.connector.connect(
            host = "localhost",
            user = "root",
            password = "",
            database = "pysql"
        )
        frame = Frame(root)
        frame.grid(row = 0,column = 0, columnspan = 2)

        cursor = connection.cursor()
        cursor.execute("SELECT first_name, last_name, gender FROM employees")
        employees = cursor.fetchall()

        columns = ("first_name", "last_name", "gender")
        table = ttk.Treeview(frame, columns = columns, show = "headings")
        table.heading("first_name", text = "First name")
        table.heading("last_name", text = "Last name")
        table.heading("gender", text = "Gender")

        for employee in employees:
            table.insert("", END, values = employee)

        table.grid(row = 0, column =0, sticky = "nws", columnspan = 1)

        scrollBar = ttk.Scrollbar(frame, orient=VERTICAL, comman=table.yview)
        scrollBar.grid(row=0, column=1, sticky="ns")
        table.configure(yscrollcommand=scrollBar.set)
        print("Thread excecuted")

    btn_select = ttk.Button(root, text = "Select", command = lambda: threading.Thread(target=create_table_from_db).start())
    btn_select.grid(column = 0, row = 1, sticky = "e")

    btn_sleep = ttk.Button(root, text = "Sleep", command = lambda: print("Sleeping..."))
    btn_sleep. grid(column = 1, row = 1, sticky = "w")

    root.mainloop()

if __name__ == "__main__":
    main()