'''
def function():
	print("I am the Bad Boy !!!")
	function()
	'''

'''
def sum(a,b):
	print(a+b)
sum(21,22)
'''

'''
def abc():
	a=10
abc()
print(a) #Error (Scope factor)'''

a=10
def function():
	print(a)
function()
