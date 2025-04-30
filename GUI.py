from tkinter import*
from PIL import Image, ImageTk
import speechToText
import actions

root = Tk()
root.title("MORRIS")
root.geometry("550x675")
root.resizable(False, False)
root.config(bg="#6F8FAF")

def ask():
    val = speechToText.speech_to_text()
    if val is None:
        text.insert(END, "Bot<--- Sorry, I didn't catch that. Please try again.\n")
        return
    val2 = actions.Action(val)
    text.insert(END ,'User--->' + val+"\n" )
    if val2 != None:
        text.insert(END, "Bot<---" +str(val2)+"\n" )
    if val2 == "ok sir shutting down see you soon":
        root.destroy()

def send():
    send = entry.get()
    bot = actions.Action(send)
    text.insert(END ,'User--->' + send+"\n" )
    if bot != None:
        text.insert(END, "Bot<---" +str(bot)+"\n" )
    if bot == "ok sir":
        root.destroy()


def del_text():
    text.delete('1.0' , "end")
#frame
frame = LabelFrame(root, padx= 100, pady= 7, borderwidth= 3, relief= "raised")
frame.config(bg= "#6F8FAF")
frame.grid(row = 0, column = 1, padx = 55, pady = 10)

#text lable 
text_label = Label(frame, text="MORRIS", font=("Helvetica", 12, "bold"), bg="#356696")
text_label.grid( row = 0, column = 0 , padx = 20, pady = 10)

#image 
image = ImageTk.PhotoImage(Image.open("image/virtualAssistant.png"))
image_label = Label(frame, image= image)
image_label.grid(row = 1, column= 0, pady= 20)

#adding some Text widget
text = Text(root, font=('courire 10 bold'), bg ="#356696")
text.grid(row = 2, column= 0)
text.place(x = 100, y = 375, width=375, height= 100)

# entry widget
entry = Entry(root , justify= CENTER)
entry.place(x =100, y=500, width= 350, height= 30) 

# buttons

botton1 = Button(root, text= "ASK" , bg="#356696", pady= 18 , padx= 35, borderwidth= 4, relief= SOLID, command=ask)
botton1.place(x= 70, y= 575)

botton2 = Button(root, text= "SEND" , bg="#356696", pady= 18 , padx= 35, borderwidth= 4, relief= SOLID, command=send)
botton2.place(x= 400, y= 575)

botton3 = Button(root, text= "DELETE" , bg="#356696", pady= 18 , padx= 35, borderwidth= 4, relief= SOLID, command=del_text)
botton3.place(x= 225, y= 575)



root.mainloop()
