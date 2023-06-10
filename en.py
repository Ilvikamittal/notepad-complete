from tkinter import*
from PIL import ImageTk,Image
from tkinter import filedialog
import os
from tkinter import messagebox
root=Tk()

root.minsize(650,650)
root.maxsize(1000,1000)
root.title("Notepad")

open_img=ImageTk.PhotoImage(Image.open("open.png"))
save_img=ImageTk.PhotoImage(Image.open("save.png"))
exit_img=ImageTk.PhotoImage(Image.open("exit.jpg"))  

file_name=Label(root,text="File Name")          
file_name.place(relx=0.28,rely=0.03,anchor=CENTER)

input_file_name=Entry(root)
input_file_name.place(relx=0.46,rely=0.03,anchor=CENTER)

my_text=Text(root,width=80,height=35)
my_text.place(relx=0.5,rely=0.55,anchor=CENTER)

name=""
def open_file():
    print("opening file")
    global name
    my_text.delete(1.0, END)
    input_file_name.delete(0, END)
    text_file = filedialog.askopenfilename(title=" Open Text File", filetypes=(("Text Files", "*.txt"),))
    print(text_file)
    name = os.path.basename(text_file)
    format_name = name.split('.')[0]
    input_file_name.insert(END,format_name)
    root.title(format_name)
    text_file = open(name,'r')
    paragraph=text_file.read()
    my_text.insert(END,paragraph)
    text_file.close()

open_btn=Button(root,text="open",command=open_file,image=open_img)
open_btn.place(relx=0.05,rely=0.03,anchor=CENTER)

def save_file():
    print("saving file")
    input_name=input_file_name.get()
    file=open(input_name+".txt","w")
    data=my_text.get("1.0",END)
    file.write(data)
    input_file_name.delete(0,END)
    my_text.delete(1.0,END)
    messagebox.showinfo("information","File have been saved successfully") 
    
    

save_btn=Button(root,text="save",image=save_img,command=save_file)
save_btn.place(relx=0.12,rely=0.03,anchor=CENTER)

def exit_file():
    print("exiting file")
    root.destroy()

exit_btn=Button(root,text="exit",image=exit_img,command=exit_file)
exit_btn.place(relx=0.19,rely=0.03,anchor=CENTER)

root.mainloop()                

