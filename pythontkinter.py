from tkinter import *
import os


def close1():
    window.withdraw()
    #second---------now this fuction will and call the func. open_window() which will open a new window and we also created--------
        # -----------close1() function which will hide our main window as we open our parent window----------

def multi():
    open_window()
    close1()


#first-------we have created a parent window and we linked this window to child window with the help of  button4 with a fuction as command -----------
window = Tk()

button1 = Button(text="Python", bg="black", fg="white",font=('Comic Sans MS', 40, 'overstrike'))
button1.pack()
button1.place(relx=.5, rely=.2, anchor="c")


button2 = Button(text="WELCOME TO TKINTER GUI BY ALFAIJ MANSURI", bg="black", fg="white",font=('Ariel', 20, 'italic'))
button2.pack()
button2.place(relx=.5, rely=.4, anchor="c")

button3 = Button(text="here we'll show you the poems of your fav. keywords", bg="black", fg="white",font=('Comic Sans MS', 20, 'italic'))
button3.pack()
button3.place(relx=.5, rely=.5, anchor="c")



button4 = Button(text="NEXT", bg="black", fg="white", font=('Ariel', 20, 'italic'), command = multi)
button4.pack()
button4.place(relx=.5, rely=.73, anchor="c")


button5 = Button(text="click NEXT for next page", bg="black", fg="white", font=('Times new roman', 12, 'bold'))
button5.pack()
button5.place(relx=.5, rely=0.9, anchor="c")


window.geometry("1800x1800+120+120")
window.configure(background='mediumspringgreen')




#-----------third -  we have created a new window that is child window ----------------------

def open_window():
    top = Toplevel()
    top.title("Top window")
    top.geometry("1800x1800+120+120")
    button = Button(top,text = " Choose your Favourite keywords and press sumit ",bg="black", fg="white",font=('Comic Sans MS', 40, 'underline'))
    button.place(relx=.5, rely=.2, anchor="c")
    button.pack(padx = 30 ,pady = 100)
    top.configure(background='mediumspringgreen')

    #--------we have created checkbuttons in our childwindow to open multiple files ---------
    #---------- A list to hold the checkbuttons and their associated variables---------
    buttons = []

    def ShowChoice():
        # Go through the list of checkbuttons and get each button/variable pair
        for button, var in buttons:
            # If var.get() is True, the checkbutton was clicked
            if var.get():
                # So, we open the file with a context manager
                with open(os.path.join("/home/kuldeep/poem", button["text"])) as file:
                    # And print its contents
                    for line in file:
                        print(line)

    for file in os.listdir("/home/kuldeep/poem"):
        if file.endswith(".txt"):
            # Create a variable for the following checkbutton
            var = IntVar()
            # Create the checkbutton
            button1 = Checkbutton(top, text=file, variable=var)
            button1.pack(anchor=W)
            # Add a tuple of (button, var) to the list buttons
            buttons.append((button1, var))
            # (file.read)

    submitButton = Button(top, text="Submit",bg = "black",fg = "white",font=('Ariel', 20, 'italic'), command=ShowChoice)
    submitButton.pack(padx=30,pady=40)



window.mainloop()


