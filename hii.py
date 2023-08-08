temp=temp.next
		if i==1:
			print("Element found")
		else:
			print("Element not found")
		self.call()
	     	
	     	
	def remo_given_ele(self,ele):
		if self.head.data is None:
			print("there is thong to delete")
			return
		b=self.head
		while b is not None:
			if b.next.data==ele:
				break
			else:
				b=b.next
		b.next=b.next.next
		self.size-=1
		self.call()
	  
	  
	def remofromanyposition(self,pos):
		if self.head.data is None:
			print("there is thong to delete")
			return
		n=self.head
		i=1
		while i<pos-1 and self.head is not None:
			n=n.next
			i=i+1
		n.next=n.next.next
		self.size-=1
		self.call()

	def traverse(self):
		if self.head.data is None:
			print("List has no elements")
			return
		temp=self.head
		while temp is not None:
			print(temp.data)
			temp=temp.next
		self.call()
	    
	    
	    
	def max_among(self):
		max=self.head.data
		m=self.head.next
		while m is not None:
			if max < m.data:
				max=m.data
			m=m.next
		print("max element is", max)
		self.call()
		

	def mean(self):
		b=0
		count=0
		m=self.head
		while m is not None :
			b=b+m.data
			count+=1
			m=m.next
		print("the mean is ", b/count)
		self.call()


	def sorting(self):
		for i in range (0,self.size):
			p=self.head
			while p.next is not None:
				if p.data>p.next.data:
					p.data,p.next.data=p.next.data,p.data
				p=p.next
		self.call()


	def reverse(self):
		l=[]
		m=self.head
		while m is not None:
			l.append(m.data)
			m=m.next
		l.reverse()
		print("reverse of a stack is")	
		for i in range (len(l)):
			print(l[i])
		self.call()
	
		
	def call(self):
		print("select an option:\n 1) continue\n 2)quit")
		a=int(input("Enter choice:"))
		if a==1:
			print("""enter choice:\n 1) To see list\n 2) For insertion at starting\n 3) For insertion at end\n 4) For insertion at any position\n 5) For deletion of first element\n 6) For deletion of last element\n 7) For deletion of element at any position\n 8) To find maximum among elements\n 9) To find mean of the elements\n 10) To sort element\n 11) To reverse the linked list\n 12) To exit  """)
		else:
			print("thank u")
			return 
		b=int(input("Enter choice:"))
		if b==1:
			self.traverse()
		elif b==2:
			d=int(input("enter the element to be inserted:"))
			self.addfirst(d)
		elif b==3:
			d=int(input("enter the element to be inserted:"))
			self.add_end(d)
		elif b==4:
			d=int(input("enter the element to be inserted:"))
			f=int(input("enter the position:"))
			self.insert_at_given_positon(d,f)
		elif b==5:
			self.remofirst()
		elif b==6:
			self.remolast()
		elif b==7:
			f=int(input("enter the position:"))
			self.remove_from_given_position(f)
		elif b==8:
			self.max_among()
		elif b==9:
			self.mean()
		elif b==10:
			self.sort_elements()
		elif b==11:
			self.reverse()
		else:
	   		print(-1)
			
    		
    		
    		
    		
#drivers code 			
dl=Singlelinkedlist()
dl.call()	 


