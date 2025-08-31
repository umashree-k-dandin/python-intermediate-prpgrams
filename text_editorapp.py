import tkinter as tk
from tkinter import filedialog,messagebox,font

# this function is used to create a new file
def new_file():
    text.delete(1.0,tk.END)
    
#this function is used to open file
def open_file():
    file_path=filedialog.askopenfile(defaultextension=".txt",filetypes=[("Text files","*.txt")])
    if file_path:
        with open(file_path,'r') as file:
            text.delete(1.0,tk.END)
            text.insert(tk.END ,file.read())

# this function is used to save the file
def save_file():
    content=text.get(1.0,tk.END).strip()
    if not content:
        messagebox.showwarning("warning","file is Empty,Nothing to Save ")
        return
    file_path=filedialog.asksaveasfilename(defaultextension=".txt",filetypes=[("Text files","*.txt")]).strip()
    if file_path:
        with open(file_path,'w') as file:
            file.write(text.get(1.0,tk.END).strip())
        messagebox.showinfo("info","Files Save succesfully!!")
    
    


#this is to create the window
root=tk.Tk()
root.title(" Text Editor")
root.geometry("800x600")

root.grid_rowconfigure(1,weight=1)
root.grid_columnconfigure(0,weight=1)

menu=tk.Menu(root)
root.config(menu=menu)
file_menu=tk.Menu(menu)
menu.add_cascade(label="File",menu=file_menu)
file_menu.add_command(label="New",command=new_file)
file_menu.add_command(label="open",command=open_file)
file_menu.add_command(label="save",command=save_file)
file_menu.add_separator()
file_menu.add_command(label="Exit",command=root.quit)



text =tk.Text(root,wrap=tk.WORD,font=("Helvetica",12),fg="black",background="light blue")
text.pack(expand=tk.YES, fill=tk.BOTH)

root.mainloop()
