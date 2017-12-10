#!/usr/bin/python
# CheckiO challenge

def say_hi(name, age):
	"""
		Hi!
	"""
	return 'Hi. My name is %s and I\'m %d years old' % (name, age)

if __name__ == '__main__':
	assert say_hi("Alex", 32) == "Hi. My name is Alex and I\'m 32 years old", "First"
	assert say_hi("Frank", 68) == "Hi. My name is Frank and I\'m 68 years old", "Second"
	print "Done. Time to Check."
	print say_hi("Alex", 32)
	print say_hi("Frank", 68)

