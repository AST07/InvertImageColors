'''
Invert Image Colors
Copyright (c) 2020 Aditya Singh Tejas
'''

from tkinter import * 
from tkinter import messagebox
from PIL import Image
import PIL.ImageOps   
from os import path,listdir
from tkinter.ttk import Entry

def invert(input_dir, output_dir):
	try:
		for img in sorted(listdir(input_dir)):
			image=Image.open(path.join(input_dir,img))
			inverted_image=PIL.ImageOps.invert(image.convert('RGB'))
			inverted_image.save(path.join(output_dir,f'Inverted {path.basename(img)}'))
	except Exception as e:
		print(e)
		messagebox.showerror('Error','Directory not found!')

root=Tk()
root.resizable(False,False)
root.title('Invert Image Colors')

head_label=Label(root,text='Invert Image Colors')
head_label.grid(row=0,column=0,columnspan=2,padx=10,pady=10)
input_label=Label(root,text='Input Directory')
input_label.grid(row=1,column=0,padx=20,pady=10)
input_dir=StringVar()
input_entry=Entry(root,textvariable=input_dir)
input_entry.grid(row=1,column=1,padx=20,pady=10)
output_label=Label(root,text='Output Directory')
output_label.grid(row=2,column=0,padx=20,pady=10)
output_dir=StringVar()
output_entry=Entry(root,textvariable=output_dir)
output_entry.grid(row=2,column=1,padx=20,pady=10)
sub_button=Button(root,text='Start',command=lambda:invert(input_dir.get(),output_dir.get()))
sub_button.grid(row=3,column=0,columnspan=2,padx=10,pady=10,ipadx=20)
cpyrt_label=Label(root,text='Copyright © 2020 Aditya Singh Tejas',bg='grey',fg='white')
cpyrt_label.grid(row=4,column=0,columnspan=2,sticky='nesw')

root.mainloop()