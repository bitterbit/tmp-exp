print "    *    "
print "   **   "
print "  ***  "
print " **** "
print "____________________________________"

print "    *    "
print "   ***   "
print "  *****  "
print " ******* "
print "*********"

print"________________________________"
print "*****"
print "*****"
print "*****"
print "*****"
print "*****"
print "*****"
print "*****"
print "*****"
print "*****"
print "*****"

print "*"*5
print "*****"
print "*****"
print "*****"
print "*****"
print "*****"
print "*****"
print "*****"
print "*****"
print "*****"

print "---------------------"

def rectangler_drawer(rectangler_height, rectangler_width):
    for i in range(rectangler_height):
        print "*"* (rectangler_width)

rectangler_drawer(3,3)

print "---------------"

def square (square_size):
    for x in range(square_size):
        print "*******"


square(1)
print "---------------"
square(3)
print "---------------"
square(5)
print "---------------"
