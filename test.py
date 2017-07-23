import os
os.chdir("..")
os.chdir('src')
errors = 0
with open('__init__.py') as init:
	try:
		eval(str(init))
	except:
		errors += 1
print(str(errors), "errors raised while excecuting __init__.py")
