filename = raw_input("Holla at that filename: ")
# this assigns the prompt to 'prompt'
prompt = "> "
# This assigns the file listed as filename to the variable txt
txt = open(filename)

# this prints your filename, based on the filename variable
print "Here is you file %r:" % filename
# this actually prints the content of the file itself, which was assigned to txt
print txt.read()
txt.close()
