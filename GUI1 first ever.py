from tkinter import *
# from PIL import Image

root=Tk()
root.title('Hotel')
root.geometry("400x400")

def suitewindow():
    swin=Toplevel(root)
    swin.title("Your Personalized Suite")
    swin.geometry("400x400")

    label=Label(swin,text=('Suite Chracteristics'),font='Magneto')
    label.pack()

    viewbutton=Button(swin,text='View',font=('Algerian'),command=viewtype)
    viewbutton.pack()

    close_button = Button(swin, text="Close", command=swin.destroy, font=("Arial", 10),)
    close_button.pack()

def viewtype():
    vt=Toplevel(root)
    vt.title(" view ")

    label=Label(vt,text='The View That Suits You',font='Magneto')
    label.pack()

    

def open_new_interface():
    # Create a new window
    new_window = Toplevel(root)
    new_window.title("Rooms Interface")
    new_window.geometry("300x300")  # Set the dimensions of the new window

    # Add content to the new window
    label = Label(new_window, text="Welcome: Choose your Stay!", font=("Showcard Gothic", 12))
    label.pack(pady=20)

    buttonsuite=Button(new_window, text="SUITE",font=('Copperplate Gothic Light',10,'bold'),fg='red',bg='white',command=suitewindow)
    buttonsuite.pack()

    buttonsr=Button(new_window, text="Single Room",font=('Copperplate Gothic Light',10,'bold'),fg='red',bg='white')
    buttonsr.pack()

    buttondr=Button(new_window, text="Double Room",font=('Copperplate Gothic Light',10,'bold'),fg='red',bg='white')
    buttondr.pack()

    # Add a close button
    close_button = Button(new_window, text="Close", command=new_window.destroy, font=("Arial", 10))
    close_button.pack(pady=10)
    

photo=PhotoImage(file='C:/Users/AMARTYA/Downloads/mymy.gif',width=100)
mylabel=Label(root,image=photo,bg='green')
mylabel.pack()
label=Label(root,text="Hotel Reservation System",width=20,height=1,fg='red',bg='yellow',font=('Monotype Corsiva', 15, 'bold'))
label.pack()
buttonr=Button(root, text="ROOMS", font=("Showcard Gothic", 10, 'bold'), padx=10, pady=5, command=open_new_interface)
buttoncr=Button(root,text="Cancel Reservation",font=("Showcard Gothic",10),padx=5,pady=5)
buttonbr=Button(root,text="Book a Room",font=("Showcard Gothic",10),padx=5,pady=5)
buttonquit=Button(root,text="Exit",font=("Showcard Gothic",10),padx=5,pady=5,fg='yellow',bg='black',command=root.quit)


buttonr.pack()
buttoncr.pack()
buttonbr.pack()
buttonquit.pack()

root.mainloop()
