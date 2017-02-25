
dix = 'Test 1, \n3, \n4'

print "%r" % dix
print "%s" % dix

format = """
"%r" '%r' %s
"""
print format % ("foo", "bar", "baz")

tester = 'This line says my height: 5\' 10\"'

print "%r" % tester
print "%s" % tester
