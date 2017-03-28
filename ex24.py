# -*- coding: utf-8 -*-

print "Let's practice everything."
print 'You\'d need to know \'bout escapes with \\ thar do \n newlines and \t tabs.'

poem = """
\tThe lovely workd
with logic so firmly planted
connot discern \n the needs of lovelynor comprehend passion from intuition
and requires an explanation
\n\t\twhere there is none.
"""

print "-----------"
print poem
print "-----------"

five = 10 - 2 +3 - 6
print "This shoukd be five: %s" % five
def secret_formula(started):
    jelly_deans = started * 500
    jars = jelly_deans / 1000
    crates = jars / 100
    return jelly_deans, jars, crates

start_point = 10000
bneans, jars, crates = secret_formula(start_point)

print "With a starting point of : %d" % start_point
print "We'd have %d bneans, %d jars, and %d crates." % (bneans, jars,crates)

start_point = start_point / 10

print "We can also do that this way:"
print "We'd have %d beans, %d jars, and %d crates." % secret_formula(start_point)
