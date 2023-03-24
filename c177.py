from tkinter import *
root=Tk()
root.title("private variable login page")
root.geometry("600x400")

name_label=Label(root,text="Name : ")
name_label.place(relx=0.3,rely=0.1,anchor=CENTER)
textbox_1=Entry(root)
textbox_1.place(relx=0.5,rely=0.1,anchor=CENTER)
password_label=Label(root,text="password : ")
password_label.place(relx=0.3,rely=0.2,anchor=CENTER)
textbox_2=Entry(root)
textbox_2.place(relx=0.5,rely=0.2,anchor=CENTER)
captcha_label=Label(root,text="captcha : ")
captcha_label.place(relx=0.3,rely=0.3,anchor=CENTER)
textbox_3=Entry(root)
textbox_3.place(relx=0.5,rely=0.3,anchor=CENTER)
user_name_label=Label(root)
user_name_label.place(relx=0.5,rely=0.5,anchor=CENTER)
user_password_label=Label(root)
user_password_label.place(relx=0.5,rely=0.6,anchor=CENTER)
user_captcha_label=Label(root)
user_captcha_label.place(relx=0.5,rely=0.7,anchor=CENTER)

class userDB():
    def __init__(self):
        self.__username="Rudra"
        self.__password="rg_08_10"
        self.__captcha="08r"
    def showuser(self):
        user_name_label["text"]="Name : "+self.__username
        user_password_label["text"]="password : "+self.__password
        user_captcha_label["text"]="captcha : "+self.__captcha
obj1=userDB()
        
def addUser():
    global obj1
    obj1.username=textbox_1.get()
    obj1.password=textbox_2.get()
    obj1.captcha=textbox_3.get()
    print("details updated")
    
btn1=Button(root,text="update login details",command=addUser)    
btn1.place(relx=0.3,rely=0.4,anchor=CENTER)

btn2=Button(root,text="show profile",command=obj1.showuser)
btn2.place(relx=0.7,rely=0.4,anchor=CENTER)

root.mainloop()
