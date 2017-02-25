name = 'Jason Abels'
age = 37 # not a lie
height = 71.5 # inches
weight = 220 # lbs
eyes = 'Hazel'
teeth = 'White'
hair = 'Gray'
height_in_cm = height * 2.54
weight_in_kg = weight * .45

print "Let's talk about %s." % name
print "He's %f inches tall." % height
print "he's %d pounds heavy." % weight
print "Actually that's not too heavy."
print "He's got %s eyes and %s hair." % (eyes, hair)
print "his teath are usually %s depending on the coffee." % teeth

# this line is tricky, try to get it exactly right
print "If I add %d, %f, and %d I get %d." % (
age, height, weight, age + height + weight
)

print "My weight of %d pounds equals roughly %d Kilograms, and my height of %d inches equals %d centinmeters." % (weight, weight * 0.45, height, height * 2.54)
print "I weigh %d Kilos and am %d centimeters tall." % (weight_in_kg, height_in_cm)
