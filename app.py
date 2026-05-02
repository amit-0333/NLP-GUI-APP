from tkinter import *
from mydb import Database
from tkinter import messagebox
from myapi import API

class NLPApp:

    def __init__(self):

        ## database obj
        self.dbo=Database()
        self.apio=API()

        ##login ka gui load karna
        self.root=Tk()## created obj of tkinter
        self.root.title('NLPApp')## name of app heading
        #self.root.iconbitmap('path') ## changes icon in app
        self.root.geometry('350x600') ## changes orientation
        self.root.configure(bg='pink') # hex code of any color by html hexcolor

        self.login_gui()
        self.root.mainloop()## hold app for long terms otherwise close immediately

    def login_gui(self):
        self.clear()
        heading=Label(self.root,text='NLPApp',bg='pink',fg='white') ## changes name of app btw screen not heading of app background and foreground
        heading.pack(pady=(30,30)) ## change location of app name in screen
        heading.configure(font=('verdana',24,'italic')) ## changes font style of name app

        label1=Label(self.root,text='Enter Email',bg='pink',fg='purple')## label is used to crete input var name or like that
        label1.pack(pady=(10,10))

        self.email_input=Entry(self.root,width=40)
        self.email_input.pack(pady=(5,5),ipady=4)

        label2=Label(self.root,text='Enter Password',bg='pink',fg='purple')##,width=15,height=3
        label2.pack(pady=(10,10))

        self.pass_input=Entry(self.root,width=40,show='*')
        self.pass_input.pack(pady=(5,5),ipady=4)

        login_btn=Button(self.root,text='Login Here',bg='beige',fg='purple',width=25,height=2,command=self.perform_login)
        login_btn.pack(pady=(10,10))

        label3=Label(self.root,text='Not a Member',bg='pink',fg='purple')##,width=15,height=3
        label3.pack(pady=(20,10))

        redirect_btn=Button(self.root,text='Register Now!',bg='beige',fg='purple',command=self.register_gui)
        redirect_btn.pack(pady=(1,10))

    def register_gui(self):
        ## clear the xisting gui
        self.clear()

        heading=Label(self.root,text='NLPApp',bg='pink',fg='white') ## changes name of app btw screen not heading of app background and foreground
        heading.pack(pady=(30,30)) ## change location of app name in screen
        heading.configure(font=('verdana',24,'italic')) ## changes font style of name app

        label0=Label(self.root,text='Enter Name',bg='pink',fg='purple')## label is used to crete input var name or like that
        label0.pack(pady=(10,10))

        self.name_input=Entry(self.root,width=40)
        self.name_input.pack(pady=(5,5),ipady=4)

        label1=Label(self.root,text='Enter Email',bg='pink',fg='purple')## label is used to crete input var name or like that
        label1.pack(pady=(10,10))

        self.email_input=Entry(self.root,width=40)
        self.email_input.pack(pady=(5,5),ipady=4)

        label2=Label(self.root,text='Enter Password',bg='pink',fg='purple')##,width=15,height=3
        label2.pack(pady=(10,10))

        self.pass_input=Entry(self.root,width=40,show='*')
        self.pass_input.pack(pady=(5,5),ipady=4)

        register_btn=Button(self.root,text='Register',bg='beige',fg='purple',width=25,height=2,command=self.perform_registration)
        register_btn.pack(pady=(10,10))

        label3=Label(self.root,text='Already a Member',bg='pink',fg='purple')##,width=15,height=3
        label3.pack(pady=(20,10))

        redirect_btn=Button(self.root,text='Login Now!',bg='beige',fg='purple',command=self.login_gui)
        redirect_btn.pack(pady=(1,10))

    def perform_registration(self):
        name=self.name_input.get()
        email=self.email_input.get()
        password=self.pass_input.get()

        response=self.dbo.add_data(name,email,password)

        if response:
            messagebox.showinfo('Success','registration successfull u can login now')
        else:
            messagebox.showerror('Error','email already exists')

    def perform_login(self):
        email=self.email_input.get()
        password=self.pass_input.get()

        response=self.dbo.search(email,password)

        if response:
            messagebox.showinfo('Success','Login Successfull')
            self.home_gui()
        else:
            messagebox.showerror('Error','incorrect email and password combination')

    def home_gui(self):
        self.clear()

        heading=Label(self.root,text='NLPApp',bg='pink',fg='white') 
        heading.pack(pady=(30,30)) 
        heading.configure(font=('verdana',24,'italic')) 

        sentiment_btn=Button(self.root,text='Sentiment Analysis',bg='beige',fg='purple',width=25,height=2,command=self.sentiment_gui)
        sentiment_btn.pack(pady=(10,10))

        ner_btn=Button(self.root,text='Named Entity Recoginition ',bg='beige',fg='purple',width=25,height=2,command=self.ner_gui)
        ner_btn.pack(pady=(10,10))

        emotion_btn=Button(self.root,text='Emotion Detection',bg='beige',fg='purple',width=25,height=2,command=self.emotion_gui)
        emotion_btn.pack(pady=(10,10))

        logout_btn=Button(self.root,text='Log Out',bg='beige',fg='purple',command=self.login_gui)
        logout_btn.pack(pady=(1,10))

    def sentiment_gui(self):
        self.clear()

        heading=Label(self.root,text='NLPApp',bg='pink',fg='white') 
        heading.pack(pady=(30,30)) 
        heading.configure(font=('verdana',24,'italic')) 

        heading1=Label(self.root,text='Sentiment Analysis',bg='pink',fg='white') 
        heading1.pack(pady=(10,20)) 
        heading1.configure(font=('verdana',20,'italic')) 

        label1=Label(self.root,text='Enter Text',bg='pink',fg='purple')
        label1.pack(pady=(10,10))

        self.sentiment_input = Text(self.root, width=40, height=5)
        self.sentiment_input.pack(pady=(5,5))

        sentiment_btn=Button(self.root,text='Analyze Sentiment',bg='beige',fg='purple',width=25,height=2,command=self.do_sentiment_analysis)
        sentiment_btn.pack(pady=(10,10))


        self.sentiment_result = Label(
                            self.root,
                            text='',
                            bg='pink',
                            fg='purple',
                            wraplength=300,
                            justify='left'
                                            )
        self.sentiment_result.pack(pady=(10,10))  
        self.sentiment_result.config(font=('verdana',12)) 

        goBack_btn=Button(self.root,text='Go Home',bg='beige',fg='purple',width=15,height=2,command=self.home_gui)
        goBack_btn.pack(pady=(10,10))

    def do_sentiment_analysis(self):
        text = self.sentiment_input.get("1.0", "end").strip()
        if not text.strip():
            messagebox.showerror("Error", "Please enter some text")
            return
        result=self.apio.sentiment_analysis(text)

        print(result)

        self.sentiment_result.config(text=result)


    def emotion_gui(self):
        self.clear()

        heading=Label(self.root,text='NLPApp',bg='pink',fg='white') 
        heading.pack(pady=(30,30)) 
        heading.configure(font=('verdana',24,'italic')) 

        heading1=Label(self.root,text='Emotion Detection',bg='pink',fg='white') 
        heading1.pack(pady=(10,20)) 
        heading1.configure(font=('verdana',20,'italic')) 

        label1=Label(self.root,text='Enter Text',bg='pink',fg='purple')
        label1.pack(pady=(10,10))

        self.emotion_input = Text(self.root, width=40, height=5)
        self.emotion_input.pack(pady=(5,5))

        emotion_btn=Button(self.root,text='Detect Emotion',bg='beige',fg='purple',width=25,height=2,command=self.do_emotion_analysis)
        emotion_btn.pack(pady=(10,10))


        self.emotion_result = Label(
                            self.root,
                            text='',
                            bg='pink',
                            fg='purple',
                            wraplength=300,
                            justify='left'
                                            )
        self.emotion_result.pack(pady=(10,10))  
        self.emotion_result.config(font=('verdana',12)) 

        goBack_btn=Button(self.root,text='Go Home',bg='beige',fg='purple',width=15,height=2,command=self.home_gui)
        goBack_btn.pack(pady=(10,10))



    def do_emotion_analysis(self):
        text = self.emotion_input.get("1.0", "end").strip()
        print("INPUT TEXT:", repr(text))

        if not text:
            messagebox.showerror("Error", "Please enter some text")
            return

        result = self.apio.emotion_analysis(text)

        print(result)

        self.emotion_result.config(text=result)
        # print("BUTTON CLICKED")
        text = self.emotion_input.get("1.0", "end").strip()
        print("INPUT TEXT:", repr(text))


    def ner_gui(self):
        self.clear()

        heading = Label(self.root, text='NLPApp', bg='pink', fg='white')
        heading.pack(pady=(30,30))
        heading.config(font=('verdana',24,'italic'))

        heading1 = Label(self.root, text='Named Entity Recognition', bg='pink', fg='white')
        heading1.pack(pady=(10,20))
        heading1.config(font=('verdana',20,'italic'))

        label1 = Label(self.root, text='Enter Text', bg='pink', fg='purple')
        label1.pack(pady=(10,10))

        # ✅ multi-line input
        self.ner_input = Text(self.root, width=40, height=5)
        self.ner_input.pack(pady=(5,5))

        ner_btn = Button(
            self.root,
            text='Extract Entities',
            bg='beige',
            fg='purple',
            width=25,
            height=2,
            command=self.do_ner
        )
        ner_btn.pack(pady=(10,10))

        self.ner_result = Label(
            self.root,
            text='',
            bg='pink',
            fg='purple',
            wraplength=300,
            justify='left'
        )
        self.ner_result.pack(pady=(10,10))
        self.ner_result.config(font=('verdana',12))

        goBack_btn = Button(
            self.root,
            text='Go Home',
            bg='beige',
            fg='purple',
            width=15,
            height=2,
            command=self.home_gui
        )
        goBack_btn.pack(pady=(10,10))


    def do_ner(self):
        text = self.ner_input.get("1.0", "end").strip()

        if not text:
            messagebox.showerror("Error", "Please enter some text")
            return

        result = self.apio.ner(text)

        print(result)

        self.ner_result.config(text=result)



        


    



    def clear(self):
        for i in self.root.pack_slaves():
            i.destroy()



    


nlp=NLPApp()
