import speech_recognition as sr
from tkinter import *

def start():
    r  = sr.Recognizer()
    mic = sr.Microphone(device_index=1)
    with mic as source:
        r.adjust_for_ambient_noise(source)
        print('speak....')
        audio=r.record(source=mic, duration=10)

        try:
            text=r.recognize_google(audio)
            print('you said:',text)

        except:
            print('sorry your voice can not recognise')
            text='sorry your voice can not recognise'
    global Text
    Text = Label(frame, text=text, font=('arial', 15), fg='cyan', bg='gray14', wraplength=500)
    Text.grid(row=3, column=0, columnspan=3)

def Clear():
    global Text
    Text['text']=''

#GUI Programming
win=Tk()
win.title('Voice 2 Text')

frame=Frame(win,relief=SUNKEN,bg="gray15",bd=10)
frame.pack()

Title=Label(frame,text='Voice 2 Text',font=('arial',30,'bold'),fg='green2',bg='gray14').grid(row=1,columnspan=3)

Record_btn= Button(frame,text='Record ',bd=5,fg='white',bg='black',font=('arial',20,'bold'),relief=SUNKEN,padx=8,pady=8,command=lambda:start())
Record_btn.grid(row=2,column=0,sticky='W')

Clear_btn= Button(frame,text='Clear ',bd=5,fg='white',bg='black',font=('arial',20,'bold'),relief=SUNKEN,padx=8,pady=8,command=lambda:Clear())
Clear_btn.grid(row=2,column=1,sticky='E')

win.mainloop()