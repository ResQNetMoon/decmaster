from sys import argv
def parse_arg(argname):
	ssl = False
	for i in argv:
		if ssl:
			return i
			break
		if i == argname:
			ssl = True
def isset_arg(argname):
	for i in argv:
		if i == argname:
			return True
			break
	return False
