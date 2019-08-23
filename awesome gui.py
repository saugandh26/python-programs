from tkinter import *
from tkinter import ttk

window = Tk()
window.title("Awesome meter")
window.iconbitmap('')
window.minsize(width=100, height=100)
label = ttk.Label(window, text="Enter a name:  ",)
label.pack(side="left",fill="both",expand="True") 

def popup():
	def leavemini():
		popup.destroy()
	popup = Tk()
	popup.wm_title("Result")
	if e1_value.get()=="":
		msg= "Please input name."
		md= "Okay"
	else:
		msg = e1_value.get()+" is Awesome."
		md= "I agree."
	label = Label(popup, text=msg,)
	label.pack(side="top", fill="x", pady=10)
	B1 = ttk.Button(popup, text=md, command = popup.destroy)
	B1.pack()
	popup.mainloop()
	
 

b1 = ttk.Button(window,text="Check",command=popup)
b1.pack(side="bottom",fill="both",expand="True")


e1_value= StringVar()
e1 = Entry(window,textvariable=e1_value)
e1.pack(side="right",fill="both",expand="True")


 
window.mainloop()
