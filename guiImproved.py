from tkinter import *
from PIL import Image, ImageTk
import speechToText
import actions

root = Tk()
root.title("MORRIS - Your Virtual Assistant")
root.geometry("600x750")
root.resizable(False, False)
root.config(bg="#1A202C")

def ask():
    val = speechToText.speech_to_text()
    if val is None:
        text.insert(END, "Bot<--- Sorry, I didn't catch that. Please try again.\n")
        return
    val2 = actions.Action(val)
    text.insert(END, 'User---> ' + val + "\n")
    if val2 is not None:
        text.insert(END, "Bot<--- " + str(val2) + "\n")
    if val2 == "ok sir shutting down see you soon":
        root.destroy()

def send():
    user_input = entry.get()
    bot_response = actions.Action(user_input)
    text.insert(END, 'User---> ' + user_input + "\n")
    entry.delete(0, END)
    if bot_response is not None:
        text.insert(END, "Bot<--- " + str(bot_response) + "\n")
    if bot_response == "ok sir shutting down see you soon":
        root.destroy()

def del_text():
    text.delete('1.0', "end")


header_frame = Frame(root, bg="#2D3748", relief=RAISED, bd=2)
header_frame.place(x=50, y=20, width=500, height=80)

header_label = Label(
    header_frame, 
    text="MORRIS - Your Virtual Assistant", 
    font=("Helvetica", 16, "bold"), 
    bg="#2D3748", 
    fg="#F7FAFC"
)
header_label.pack(expand=True)


image = Image.open("virtualAssistant.png").resize((200, 200), Image.Resampling.LANCZOS)
image_tk = ImageTk.PhotoImage(image)
image_label = Label(root, image=image_tk, bg="#1A202C")
image_label.place(x=200, y=110)


text = Text(root, font=("Courier", 10, "bold"), bg="#2D3748", fg="#E2E8F0", wrap=WORD)
text.place(x=50, y=350, width=500, height=200)

entry = Entry(root, font=("Helvetica", 12), justify=CENTER, bg="#4A5568", fg="#E2E8F0", insertbackground="#E2E8F0")
entry.place(x=50, y=570, width=400, height=40)


ask_button = Button(
    root, text="ASK", bg="#3182CE", fg="#F7FAFC", font=("Helvetica", 12, "bold"), 
    pady=10, padx=20, borderwidth=2, relief=SOLID, command=ask
)
ask_button.place(x=70, y=630)

send_button = Button(
    root, text="SEND", bg="#38A169", fg="#F7FAFC", font=("Helvetica", 12, "bold"), 
    pady=10, padx=20, borderwidth=2, relief=SOLID, command=send
)
send_button.place(x=260, y=630)

delete_button = Button(
    root, text="CLEAR", bg="#E53E3E", fg="#F7FAFC", font=("Helvetica", 12, "bold"), 
    pady=10, padx=20, borderwidth=2, relief=SOLID, command=del_text
)
delete_button.place(x=450, y=630)


root.mainloop()
