from ctypes import resize
from  tkinter import *
import datetime
# from PIL import ImageTK,Image

tk = Tk()
tk.title('Voice Based Desktop Assistant ')
tk.geometry("700x700")
#-----------Screen Height & Width------------
screen_width = tk.winfo_screenwidth()
screen_height = tk.winfo_screenheight()

screen_centerx = screen_width / 2
screen_centery = screen_height / 2

tk.rowconfigure(0,weight=1)
tk.columnconfigure(0,weight=1)
# tk.state('zoomed')

page_1 = Frame(tk)
page_2 = Frame(tk)
page_3 = Frame(tk)

for frame in (page_1,page_2,page_3):
    frame.grid(row = 0,column = 0, sticky = 'nsew')


def show_frame(frame):
    frame.tkraise()
    
show_frame(page_1)

#------Page1-------
page_1.config(background='blue')
page_1_label1 = Label(page_1,text='31.0 C',font=('Arial',15,'bold'),fg='blue',padx=15,pady=8,bg='white')
page_1_label1.place(x=20,y=20)

# now = datetime.datetime.now()
# print("Current date time is :")
# time = now.strftime("%H:%M:%S")

page_1_label2 = Label(page_1,text = '9:00',font=('Arial',15,'bold'),fg='blue',padx=15,pady=8,bg='white')
page_1_label2.place(x = screen_width - 130,y=20)

#------Page1 Picture in Center-------
# center_pic = Image.open('center1.png')
center_pic = PhotoImage(file = 'center1.png')
playbtn_pic = PhotoImage(file = 'playBtn1.png')
wave_pic = PhotoImage(file = 'soundwave.png')

picture_btn = Button(page_1,image = center_pic,)
picture_btn.place(x = screen_centerx - 270 , y = screen_centery - 250)


next_btn = Button(page_1,text='Next',font=('Arial',15,'bold'),fg='blue',padx=15,pady=8,bg='white', command=lambda: show_frame(page_2))
next_btn.place(x = screen_width -300, y = screen_height - 140 )


#------Page2-------

# page_2_label1 = Label(page_2,text='Second Page',font=('Arial',15,'bold'),padx=15,pady=8,bg='white')
# page_2_label1.place(x=20,y=20)

# page_2_label2 = Label(page_2,image = wave_pic)
# page_2_label2.place(x= screen_centerx - 250 ,y=100)

# def send():
#     send = "You : " + ePage_2.get()
#     txtPage_2.insert(END, "\n" + send)
#     user = ePage_2.get().lower()
#     if (user == "hello"):
#         txtPage_2.insert(END, "\n" + "Captain: Hi there, how can I help?")
#     else:
#         txtPage_2.insert(END, "\n" + "Captain: Sorry! I dind't got you")
#     ePage_2.delete(0, END)

page_2.config(background='blue')
lablePage_2 = Label(page_2, bg="blue",font='Helvetica 22 bold', fg="white", text="Welcome on Desktop Voice Assisstant Home Page",  pady=10, width=80, height=1)
lablePage_2.grid(row=0)
 
txtPage_2 = Text(page_2, bg="blue",font='Helvetica 14 bold', fg="white" ,height= 31, width=138)
txtPage_2.grid(row=1, column=0, columnspan=2)
 
ePage_2 = Entry(page_2, bg="blue",font='Helvetica 18 bold', fg="white",width=70)
ePage_2.grid(row=2, column=0)
 
sendPage_2 = Button(page_2, text="Send",font='Helvetica 16 bold',  bg="blue",fg="white",width=6,).grid(row=2, column=1)
otherBtnPage_2 = Button(page_2, text="otherBtn",font='Helvetica 16 bold',  bg="blue",fg="white",width=6,).grid(row=2, column=1)

#command = 'send'
tk.mainloop()
