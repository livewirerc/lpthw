from sys import argv

script, filename = argv

print "We're going to erase %r." % filename
print "If you don't want that, hit Ctril-C (^C)."
print "If you do want that, hit Return (Enter)."

raw_input("?")

print "Opening the file..."
target = open(filename, 'w')

print "Truncating the file. Goodbye!"
target.truncate()

print "Now I'm going to ask you for three lines."

line1 = raw_input("Line 1, please: ")
line2 = raw_input("Line 2, if you would: ")
line3 = raw_input("Line 3, to round things out: ")

out = "%s\n%s\n%s\n" % (line1, line2, line3)

print "I'm going to write these to the file."

target.write(out)

# target.write("%s\n%s\n%s\n" % (line1, line2, line3))

# target.write(line1)
# target.write("\n")
# target.write(line2)
# target.write("\n")
# target.write(line3)
# target.write("\n")

print "And finally, we close it."
target.close()
