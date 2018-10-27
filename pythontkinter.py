from tkinter import *
import os #The functions that the OS module provides allows you to interface with the underlying operating system that Python is running on
import glob  #The glob module finds all the pathnames matching a specified pattern

HEADING_FONT = ('Comic Sans MS', 40, 'bold')
SUBHEADING_FONT = ('Comic Sans MS', 25, 'bold')
BUTTON_FONT = ('Ariel', 20, 'italic')
PARAGRAPH_FONT = ('Times new roman', 12, 'bold')

#defining main window and using Label and Button widget to make buttons and labels in our main window
#setting command to option_window in our Button to jump to our next window
def main():
    window = Tk()
    window.geometry("1800x1800+120+120")
    Label(text="Python", bg="black", fg="white", font=HEADING_FONT).pack()
    Label(text="WELCOME TO TKINTER GUI BY ALFAIJ MANSURI",bg="black", fg="white", font=SUBHEADING_FONT).pack()
    Label(text="here we'll show you the poems of your fav. keywords", bg="black", fg="white", font=SUBHEADING_FONT).pack()
    Button(text="NEXT", bg="black", fg="white", font=BUTTON_FONT,command=lambda: option_window(window)).pack()
    Label(text="click NEXT for next page", bg="black", fg="white", font=PARAGRAPH_FONT).pack()
    window.configure(background='mediumspringgreen')


#defining a func. which automatically destroys the window when user close the window forcefully
    def on_closing():
        window.destroy()

    window.protocol("WM_DELETE_WINDOW", on_closing)
    window.mainloop()

def option_window(prev):
    prev.withdraw()    #using prev.withdraw() we hides our previous window i.e main window when our new window in opened
    top = Toplevel()   #creating a new window using Toplevel()
    top.geometry("1800x1800+120+120") #setting windows geometry same as top window so that it opens in same size as main window
    top.title("Top window")   #defining title of window
    Label(top, text=" Choose your Favourite keywords and press submit ",bg="black", fg="white", font=SUBHEADING_FONT).pack()
    top.configure(background='mediumspringgreen')

    states = {}
    file_paths = glob.glob('textfiles/*.txt') #This glob module finds all the pathnames which ends with .txt in our desired folder

    def submit(context):
        final_list = []
        for st in states.keys():#checking states of keys if the state of key is '1' i.e ON then it will append our file in the final list
                if states[st].get() == 1:
                    final_list.append(st)
        context.withdraw() #it will hide our top level window when our next top level window will open
        poem_window(final_list) # we are calling our poem_window in which we will show our text files which are been selected by our user

    for filepath in file_paths:
        states[filepath] = IntVar()  #The control variable that tracks the current state of the checkbutton. i.e ON or OFF
        Checkbutton(top, text=filepath[10:-4], variable=states[filepath]).pack() #making checkbutton same name as our file name
    Button(top, text="Submit", command=lambda: submit(top)).pack() #making submit button and settingn command = submit which will call the submit(context)
                                                                #funtion and then sumit function will append all the files which has ON value .


def poem_window(files): #definig funtion to show our poems
    top = Toplevel() # making a new window which will open when above submit button is clicked
    top.geometry("1800x1800+120+120")
    top.title(','.join(map(lambda x: x[10:-4], files)))  #setting the title of our top level same as the check butttons name  eselcted
    Label(top, text="The Poem",bg="black", fg="white", font=HEADING_FONT)
    top.configure(background='mediumspringgreen')
    t = Text(top, font=PARAGRAPH_FONT) #making a text box in our top level in which our poems will appear
    for file in files:  #opening the selected files in read mode and then inserting them them into textbox
        f = open(file, 'r')
        t.insert(END, f.read())
        f.close()
        t.pack()


if __name__ == '__main__':
    main()
