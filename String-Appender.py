#!/usr/bin/python

""" Lambda clousures """

def string_appender(name, append_str):
	return "%s_%s" % (name, append_str)

if __name__ == '__main__':
	name_list = ["kenny", "hippo", "peter", "kelly", "john", "bob"]
	funcs = []
	for n in name_list:
		# solution:
		# using a default parameter to store the value of name 
		# in a variable which is local to lambda's scope
		funcs.append( lambda n=n: string_appender(n, 'char') )

	# Don't modify the code below:
	for f in funcs:
		print(f())
