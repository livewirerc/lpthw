# the below lines through line eight define the 'cheese_and_crackers' function,
# which prints out information about the number of cheese and crackers you have
# based on variable input from different sources.
def cheese_and_crackers(cheese_count, boxes_of_crackers):
    print "cheese_count in function: %d" % cheese_count
    print "You have %d cheeses!" % cheese_count
    print "you have %d boxes of crackahzzzzz, crackah!" % boxes_of_crackers
    print "Man, that's enough for a fuckin' party!"
    print "Get a blanket.\n"

# This line calls the above function with directly assigned variables
print "We can just give the functions numbers directly:"
cheese_and_crackers(20, 30)

# these lines set values to two variables, and then assigns those variables
# to the variables inherent in the function cheese_and_crackers
print "OR, we can use variables from our script:"
amount_of_cheese = 10
amount_of_crackers = 50

print "amount_of_cheese before function: %d" % amount_of_cheese
cheese_and_crackers(amount_of_cheese, amount_of_crackers)
print "amount_of_cheese after function: %d" % amount_of_cheese

# Similar to the first call, but with math equations assigned to the variables
print "We can even do math inside, too:"
cheese_and_crackers(10 + 20, 5 + 6)

# using variables defined above PLUS math. FANCY.
print "and we can combine the two, variables and math:"
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 10000)
