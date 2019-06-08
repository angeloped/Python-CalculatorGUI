#!/usr/bin/python
#-*-coding: utf-8-*-
from __future__ import division
from Tkinter import *
import math


# default buttons and background colour #
activebackground=["#f9f9f9"]
activeforeground=["#000000"]
background=["#d9d9d9"]
disabledforeground=["#a3a3a3"]
foreground=["#000000"]
highlightbackground=["#d9d9d9"]
highlightcolor=["#000000"]
# entry colour #
_ety_background=["#a8a8a8"]
_ety_disabledforeground=["#d9d9d9"]
_ety_foreground=["#d9d9d9"]
_ety_highlightbackground=["#d9d9d9"]
_ety_highlightcolor=["#000000"]

# parse system colour configuration file
bg_links = {"activebackground":activebackground, "activeforeground":activeforeground, "background":background, "disabledforeground":disabledforeground, "foreground":foreground, "highlightbackground":highlightbackground, "highlightcolor":highlightcolor, "_ety_background":_ety_background, "_ety_disabledforeground":_ety_disabledforeground, "_ety_foreground":_ety_foreground, "_ety_highlightbackground":_ety_highlightbackground, "_ety_highlightcolor":_ety_highlightcolor}
with open("colour.conf") as f:
	for raw_colour_conf in f.read().split("<colour>")[1].split("</colour>")[0].replace("\"", "").split("\n"):
		colour_conf = raw_colour_conf.split("=")
		if len(colour_conf) == 2:
			bg_links[colour_conf[0]][0]=colour_conf[1]

class calc:
	def getandreplace(self):
		"""replace x with * and ÷ with /"""
		self.expression = self.e.get()
		self.newtext=self.expression.replace(self.newdiv,'/')
		self.newtext=self.newtext.replace('x','*')
	
	def equals(self):
		"""when the equal button is pressed"""
		self.getandreplace()
		try: 
			self.value= eval(self.newtext) #evaluate the expression using the eval function
		except SyntaxError or NameErrror:
			self.e.delete(0,END)
			self.e.insert(0,'Invalid Input!')
		else:
			self.e.delete(0,END)
			self.e.insert(0,self.value)
		
		# it means, it's done calculating... 
		self.done_output = True
	
	def squareroot(self):
		"""squareroot method"""
		self.getandreplace()
		try: 
			self.value= eval(self.newtext) #evaluate the expression using the eval function
		except SyntaxError or NameErrror:
			self.e.delete(0,END)
			self.e.insert(0,'Invalid Input!')
		else:
			self.sqrtval=math.sqrt(self.value)
			self.e.delete(0,END)
			self.e.insert(0,self.sqrtval)

	def square(self):
		"""square method"""
		self.getandreplace()
		try: 
			self.value= eval(self.newtext) #evaluate the expression using the eval function
		except SyntaxError or NameErrror:
			self.e.delete(0,END)
			self.e.insert(0,'Invalid Input!')
		else:
			self.sqval=math.pow(self.value,2)
			self.e.delete(0,END)
			self.e.insert(0,self.sqval)
	
	def clearall(self): 
		"""when clear button is pressed,clears the text input area"""
		self.e.delete(0,END)
	
	def clear1(self):
		if not self.e.get() == "Invalid Input!":
			self.txt=self.e.get()[:-1]
			self.e.delete(0,END)
			self.e.insert(0,self.txt)
		else:
			self.clearall()
	
	def action(self,argi):
		"""pressed button's value is inserted into the end of the text area"""
		if len(self.e.get()) > 0:
			operators_ = ["+", "x", "*", "-", "/", "%", ".", "(", ")"]
			if self.e.get()[-1] in operators_ and argi in operators_:
				argi = self.e.get()[:-1] + str(argi)
				self.e.delete(0,END)
		self.e.insert(END,argi)
	
	def __init__(self,master):
		"""Constructor method"""
		master.title('Calulator') 
		master.bind("<Escape>", lambda e:master.destroy())
		master.resizable(False, False)
		
		# window app positioning
		x,y=316,170
		# Gets both half the screen width/height and window width/height
		positionRight = int(master.winfo_screenwidth()/2 - x/2)
		positionDown = int(master.winfo_screenheight()/2 - y/2)
		master.geometry("{0}x{1}+{2}+{3}".format(x,y,positionRight, positionDown))
		
		master.configure(background=background)
		master.configure(highlightbackground=highlightbackground)
		master.configure(highlightcolor=highlightcolor)
		
		# indicator whether calculation done or not.
		# after getting output, the Entry must be cleared to start another calcualtion.
		self.done_output = False
		
		# state="readonly"
		self.e = Entry(master, font=("Helvetica",25,"normal"), relief="flat", justify="right", width=16)
		self.e.grid(row=0,column=0,columnspan=6,pady=3)
		
		self.e.configure(background=_ety_background)
		self.e.configure(disabledforeground=_ety_disabledforeground)
		self.e.configure(foreground=_ety_foreground)
		self.e.configure(highlightbackground=_ety_highlightbackground)
		self.e.configure(highlightcolor=_ety_highlightcolor)
		
		# entry bindings (to disable focus or direct typing)
		self.e.bind("<Key>",lambda e:master.focus())
		self.e.bind("<FocusIn>",lambda e:master.focus())
		
		self.div='÷'
		self.newdiv=self.div.decode('utf-8')
		
		#Generating Buttons
		b1 = Button(master,text="=",width=10,command=lambda:self.equals(), background="#000000", foreground="#00FF00")
		b1.grid(row=4, column=4,columnspan=2)
		b2 = Button(master,text='AC',width=3,command=lambda:self.clearall())
		b2.grid(row=1, column=4)
		b3 = Button(master,text='C',width=3,command=lambda:self.clear1())
		b3.grid(row=1, column=5)
		b4 = Button(master,text="+",width=3,command=lambda:self.action('+'))
		b4.grid(row=4, column=3)
		b5 = Button(master,text="x",width=3,command=lambda:self.action('x'))
		b5.grid(row=2, column=3)
		b6 = Button(master,text="-",width=3,command=lambda:self.action('-'))
		b6.grid(row=3, column=3)
		b7 = Button(master,text="÷",width=3,command=lambda:self.action(self.newdiv))
		b7.grid(row=1, column=3) 
		b8 = Button(master,text="%",width=3,command=lambda:self.action('%'))
		b8.grid(row=4, column=2)
		b9 = Button(master,text="7",width=3,command=lambda:self.action(7))
		b9.grid(row=1, column=0)
		b10 = Button(master,text="8",width=3,command=lambda:self.action(8))
		b10.grid(row=1, column=1)
		b11 = Button(master,text="9",width=3,command=lambda:self.action(9))
		b11.grid(row=1, column=2)
		b12 = Button(master,text="4",width=3,command=lambda:self.action(4))
		b12.grid(row=2, column=0)
		b13 = Button(master,text="5",width=3,command=lambda:self.action(5))
		b13.grid(row=2, column=1)
		b14 = Button(master,text="6",width=3,command=lambda:self.action(6))
		b14.grid(row=2, column=2)
		b15 = Button(master,text="1",width=3,command=lambda:self.action(1))
		b15.grid(row=3, column=0)
		b16 = Button(master,text="2",width=3,command=lambda:self.action(2))
		b16.grid(row=3, column=1)
		b17 = Button(master,text="3",width=3,command=lambda:self.action(3))
		b17.grid(row=3, column=2)
		b18 = Button(master,text="0",width=3,command=lambda:self.action(0))
		b18.grid(row=4, column=0)
		b19 = Button(master,text=".",width=3,command=lambda:self.action('.'))
		b19.grid(row=4, column=1)
		b20 = Button(master,text="(",width=3,command=lambda:self.action('('))
		b20.grid(row=2, column=4)
		b21 = Button(master,text=")",width=3,command=lambda:self.action(')'))
		b21.grid(row=2, column=5)
		b22 = Button(master,text="√",width=3,command=lambda:self.squareroot())
		b22.grid(row=3, column=4)
		b23 = Button(master,text="x²",width=3,command=lambda:self.square())
		b23.grid(row=3, column=5)
		
		for widget in [b1,b2,b3,b4,b5,b6,b7,b8,b9,b10,b11,b12,b13,b14,b15,b16,b17,b18,b19,b20,b21,b22,b23]:
			widget.configure(activebackground=activebackground)
			widget.configure(activeforeground=activeforeground)
			widget.configure(background=background)
			widget.configure(disabledforeground=disabledforeground)
			widget.configure(foreground=foreground)
			widget.configure(highlightbackground=highlightbackground)
			widget.configure(highlightcolor=highlightcolor)
		
		master.bind("<Key>", self.key)
	
	def key(self, event):
		# clear ouput
		if self.done_output:
			print("must clear all")
			self.clearall()
			self.done_output = False
		
		# event char selector
		if event.char.isdigit():
			self.action(int(event.char))
		elif event.char in ["\r", "="]:
			self.equals()
		elif event.char == "\x7f":
			self.clearall()
		elif event.char == "\x08":
			self.clear1()
		elif event.char in ["+", "x", "×", "*", "-", "/", "%", ".", "(", ")"]:
			self.action(event.char.replace("*","x").replace("×","x"))
		print("pressed", event.char)

#Main
root = Tk()
obj=calc(root) #object instantiated
root.mainloop()
