from tkinter import *
import numpy as np
from tkinter.messagebox import *
import random

class binary():
	def __init__(self):
		self.master=Tk()
		self.master.title('Sorting and searching')
		self.master.configure(padx=15,pady=5)

		#partie menu
		def about():
			showinfo("Tentang Binary Search","Binary search adalah metode pencarian suatu data atau elemen di dalam suatu array dengan kondisi data dalam keadaan terurut. Proses pencarian binary search hanya dapat dilakukan pada sekumpulan data yang sudah diurutkan terlebih dahulu.")
		def reset():
			self.e.delete(0, END)
			self.e2.delete(0,END)
			self.v.set("")
			self.v2.set("")
		menubar = Menu(self.master)
		menu1 = Menu(menubar, tearoff=0)
		menu1.add_command(label="about",command=about)
		menubar.add_cascade(label="help", menu=menu1)
		menu2 = Menu(menubar, tearoff=0)
		menu2.add_command(label="restart",command=reset)
		menubar.add_cascade(label="reset",menu=menu2)

		self.master.config(menu=menubar)

		self.champ_label2 = Label(self.master, text ="Silakan masukkan item dari array yang diurutkan \n (Dipisahkan oleh spasi):")
		self.champ_label2.grid(row=1)

		self.e = Entry(self.master,width=30)
		self.e.grid(row=2)

		self.new = Label(self.master,text= 'Silahkan masukkan item pencarian: ')
		self.new.grid(row=4)

		self.e2 = Entry(self.master,width=10)

		self.e2.grid(row=4,column=2)

		self.b = Button(self.master, text="urutkan",fg='blue', width=10,command=self.binary)
		self.b.grid(row=5)

		self.b2 =Button(self.master, text="keluar", width=10,command=self.master.destroy)
		self.b2.grid(row=10)

		self.v2 = StringVar()
		self.v = StringVar()

		self.master.mainloop()

	def binary(self):

		self.string = self.e.get()
		self.arr = self.string.split()
		self.arr= [int(i) for i in self.arr]

		self.arr2=sorted(self.arr)

		self.lresult = Label(self.master,textvariable=self.v)
		self.lresult.grid(row=6)


		#mencari dari input yg sudah urut
		if(np.array_equal(self.arr,self.arr2)):
			#print(ok)
			self.target=self.e2.get()
			self.target=int(self.target)

			self.first = 0
			self.last = len(self.arr)-1
			self.found = False

			while(self.first<=self.last and not self.found):
				self.mid = (self.first + self.last)//2
				if self.arr[self.mid]== self.target :
					self.found = True
					self.v.set('Found.')
					#print(self.mid)
					self.ltext = Label(self.master,text= "Berada di posisi :")
					self.ltext.grid(row=7)
					self.ltest = Label(self.master,textvariable=self.v2)
					self.ltest.grid(row=7,column=2)
					self.v2.set(self.mid)
				else:
					if self.target < self.arr[self.mid]:
						self.last = self.mid - 1
					else:
						self.first = self.mid + 1
			#print(self.found)
			if (self.found==False):
				showwarning('warning', 'Not Found!!')
				self.v.set('Not Found!!')
				self.v2.set('')
				self.ltext.configure(text='')
			return self.found


		#mencari dari input yg belum urut, yg kemudian diurutkan dgn bubble sort

		else:
			showwarning('warning', 'Your List is Not sorted!!')
			self.v.set('Your List has been Sorted')
			self.v2.set('')

			
			temp = self.e.get()
			temp_arr = temp.split()
			temp_arr = [int(i) for i in temp_arr]
			new = ''

			#Bubble sort
			n = len(temp_arr)
			for i in range(n):
				for j in range(0, n-i-1):
					if temp_arr[j] > temp_arr[j+1] :
						temp_arr[j], temp_arr[j+1] = temp_arr[j+1], temp_arr[j] 


			#untuk nampung list yang tdk urut

			for i in temp_arr:
				new = new + str(i) + ' '

			self.e.delete(0, END)
			self.e.insert(END, new)

			self.target=self.e2.get()
			self.target=int(self.target)

			self.first = 0
			self.last = len(temp_arr)-1
			self.found = False

			while(self.first<=self.last and not self.found):
				self.mid = (self.first + self.last)//2
				if temp_arr[self.mid]== self.target :
					self.found = True
					self.v.set('Found.')
					#print(self.mid)
					self.ltext = Label(self.master,text= "The position of the item is :")
					self.ltext.grid(row=7)
					self.ltest = Label(self.master,textvariable=self.v2)
					self.ltest.grid(row=7,column=2)
					self.v2.set(self.mid)
				else:
					if self.target < temp_arr[self.mid]:
						self.last = self.mid - 1
					else:
						self.first = self.mid + 1
			#print(self.found)
			if (self.found==False):
				showwarning('warning', 'Not Found!!')
				self.v.set('Not Found!!')
				self.v2.set('')
			return self.found
binary()
				