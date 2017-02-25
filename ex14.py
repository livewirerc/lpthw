from sys import argv

script, user_name, goofy_name = argv
prompt = '"" '

print "Hi %s the %s, I'm the %s script." % (user_name, goofy_name, script)
print "I'd like to ask you a few questions (nerd)."
print "Do you like me %s the %s?" % (user_name, goofy_name)
likes = raw_input(prompt)

print "Where do you live %s?" % user_name
lives = raw_input(prompt)

print "What kind of computer do you have? Nerd."
computer = raw_input(prompt)

print """
Alright %s, so you said %r about liking me.
You live in %r. Not sure where that is because I'm a stupid script.
And you have a %r computer. If it ain't a PC, it ain't shit.
As to that whole 'The %s' business, I think it's cheezy affectation.
""" % (user_name, likes, lives, computer, goofy_name)
