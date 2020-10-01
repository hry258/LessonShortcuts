
import tkinter as tk, os, webbrowser

window = tk.Tk()
window.title("Lesson_shortcuts")
positionRight = int(window.winfo_screenwidth()/2 - window.winfo_reqwidth()/2)
positionDown = int(window.winfo_screenheight()/3 - window.winfo_reqheight()/2)
window.geometry(f"350x600+{positionRight - 100}+{positionDown}")

homework_frame = tk.Frame(master=window)
base_frame = tk.Frame(master=window)

# Main frame widgets:

button_portal = tk.Button(text="Portal E-Learning", master=base_frame, width=25, height=2)
button1 = tk.Button(text="Lesson 1", master=base_frame, width=25, height=2)
button2 = tk.Button(text="Lesson 2", master=base_frame, width=25, height=2)
button3 = tk.Button(text="Lesson 3", master=base_frame, width=25, height=2)
button4 = tk.Button(text="Lesson 4", master=base_frame, width=25, height=2)
button5 = tk.Button(text="Lesson 5", master=base_frame, width=25, height=2)
button6 = tk.Button(text="Lesson 6", master=base_frame, width=25, height=2)
button7 = tk.Button(text="Lesson 7", master=base_frame, width=25, height=2)
button8 = tk.Button(text="Lesson 8", master=base_frame, width=25, height=2)
button_PyCharm = tk.Button(text="PyCharm", master=base_frame, width=25, height=2)
button_meeting = tk.Button(text="Google meet", master=base_frame, width=25, height=2)
button_homework = tk.Button(text="Create homework folder", master=base_frame, width=25, height=2)
button_portal.pack(pady=2)
button_meeting.pack(pady=2)
button_homework.pack(pady=2)
button1.pack(pady=2)
button2.pack(pady=2)
button3.pack(pady=2)
button4.pack(pady=2)
button5.pack(pady=2)
button6.pack(pady=2)
button7.pack(pady=2)
button8.pack(pady=2)
button_PyCharm.pack(pady=2)
base_frame.pack()

# Homework frame widgets:

homework_ent = tk.Entry(master=homework_frame, width=30)
homework_button = tk.Button(text="Create", master=homework_frame, width=25, height=2)
back_button = tk.Button(text="Back", master=homework_frame, width=25, height=2)
error_message = tk.Label(master=homework_frame, text="Folder already exists!", width=25, height=2)
files_created_message = tk.Label(master=homework_frame, text="Files created!", width=25, height=2)
homework_button.pack(pady=2)
homework_ent.pack(pady=2)
back_button.pack(pady=2)

# Functions for buttons:

def create_h_folder(event):
    week = homework_ent.get()
    try:
        os.mkdir(f"C:\\Users\\user\\PycharmProjects\\Bit2\\Tema {week}\\")
    except:
        error_message.pack()
    else:
        for i in range(1, 5):
            open(f"C:\\Users\\user\\PycharmProjects\\Bit2\\Tema {week}\\Tema {week}.{i}.py", "w")
        files_created_message.pack()
    homework_ent.delete(0, tk.END)

def delete_entry(event):
    homework_ent.delete(0, tk.END)
    error_message.pack_forget()
    files_created_message.pack_forget()

def open_homework(event):
    base_frame.pack_forget()
    homework_frame.pack()
    homework_ent.insert(0, "Enter week number")

def close_homework(event):
    homework_frame.pack_forget()
    base_frame.pack()
    files_created_message.pack_forget()

def lesson1(event):
    webbrowser.open("https://lcp.bitacad.net/book/python-advanced/1")

def lesson2(event):
    webbrowser.open("https://lcp.bitacad.net/book/python-advanced/2")

def lesson3(event):
    webbrowser.open("https://lcp.bitacad.net/book/python-advanced/3")

def lesson4(event):
    webbrowser.open("https://lcp.bitacad.net/book/python-advanced/4")

def lesson5(event):
    webbrowser.open("https://lcp.bitacad.net/book/python-advanced/5")

def lesson6(event):
    webbrowser.open("https://lcp.bitacad.net/book/python-advanced/6")

def lesson7(event):
    webbrowser.open("https://lcp.bitacad.net/book/python-advanced/7")

def lesson8(event):
    webbrowser.open("https://lcp.bitacad.net/book/python-advanced/8")

def pyCharm(event):
    os.startfile("C:\\Users\\user\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\Programs\\JetBrains Toolbox\\PyCharm Community.lnk")

def portal(event):
    webbrowser.open("https://portal.bitacad.net/my/")

def google_meet(event):
    webbrowser.open("https://meet.google.com/kiq-awnh-pmk?authuser=0")

# Binding buttons to functions:

button1.bind("<Button-1>", lesson1)
button2.bind("<Button-1>", lesson2)
button3.bind("<Button-1>", lesson3)
button4.bind("<Button-1>", lesson4)
button5.bind("<Button-1>", lesson5)
button6.bind("<Button-1>", lesson6)
button7.bind("<Button-1>", lesson7)
button8.bind("<Button-1>", lesson8)
button_PyCharm.bind("<Button-1>", pyCharm)
button_portal.bind("<Button-1>", portal)
button_meeting.bind("<Button-1>", google_meet)
button_homework.bind("<Button-1>", open_homework)
back_button.bind("<Button-1>", close_homework)
homework_ent.bind("<Button-1>", delete_entry)
homework_button.bind("<Button-1>", create_h_folder)

window.mainloop()