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

   #we have created a text box ,here our poem will appear
    T = Text(top, height=10, width=100)
    T.pack()
    #blacnk = Button(top, text="",bg="mediumspringgreen").pack(anchor=CENTER)

    def opencrazy():
        f = open("crazy.txt")
        # t is a Text widget
        T.insert(END, f.read())

    crazy = Button(top, text="Crazy", fg="black", bg="salmon", font=('Ariel', 10, 'bold'), command=opencrazy).pack(anchor=CENTER)


    def openalone():
        f= open("alone.txt")
        T.insert(END, f.read())

    alone = Button(top, text="Alone", fg="black", bg="red", font=('Ariel', 10, 'bold'), command=openalone).pack(anchor=CENTER)



    def opennight():
        f= open("night.txt")
        T.insert(END,f.read())

    night = Button(top, text="night", fg="black", bg="yellow", font=('Ariel', 10, 'bold'), command=opennight).pack(anchor=CENTER)


    def opengirl():
        f = open("alone.txt")
        T.insert(END,f.read())

    girl = Button(top, text="girl", fg="black", bg="brown3", font=('Ariel', 10, 'bold'), command=opengirl).pack(anchor=CENTER)



    def opentrust():
        f = open("trust.txt")
        T.insert(END,f.read())

    trust = Button(top, text="trust", fg="black", bg="orange2", font=('Ariel', 10, 'bold'), command=opentrust).pack(anchor=CENTER)

    def opennature():
        f= open("nature.txt")
        T.insert(END,f.read())

    nature = Button(top, text="nature", fg="black", bg="light goldenrod", font=('Ariel', 10, 'bold'), command=opennature).pack(anchor=CENTER)

    def openmoney():
        f = open("money.txt")
        T.insert(END,f.read())

    money = Button(top, text="money", fg="black", bg="SteelBlue2", font=('Ariel', 10, 'bold'), command=openmoney).pack(anchor=CENTER)


    def openmemory():
        f = open("memory.txt")
        T.insert(END ,f.read())

    memory = Button(top, text="memory", fg="black", bg="light sea green", font=('Ariel', 10, 'bold'), command=openmemory).pack(anchor=CENTER)


    def openkiss():
        f = open("kiss.txt")
        T.insert(END,f.read())

    kiss = Button(top, text="kiss", fg="black", bg="dark slate gray", font=('Ariel', 10, 'bold'), command=openkiss).pack(anchor=CENTER)


    def openhope():
        f = open("hope.txt")
        T.insert(END,f.read())

    hope = Button(top,text="hope",fg ="black",bg="light coral",font=('Ariel',10,'bold'),command = openhope).pack(anchor=CENTER)


    def openjoy():
        f = open("joy.txt")
        T.insert(END,f.read())

    joy = Button(top,text = "joy",fg = "black",bg = "dark khaki",font=('Ariel',10,'bold'),command=openjoy).pack(anchor=CENTER)



    def openfuture():
        f = open("future.txt")
        T.insert(END,f.read())

    future = Button(top,text ="future",fg="black",bg="pink",font=('Ariel',10,'bold'),command=openfuture).pack(anchor=CENTER)


    def openfriend():
        f = open("friend.txt")
        T.insert(END,f.read())

    friend = Button(top,text="friend",fg="black",bg="orange",font=('Ariel',10,'bold'),command=openfriend).pack(anchor=CENTER)




window.mainloop()


