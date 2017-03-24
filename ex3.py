# -*- coding utf-8 -*-

#常见数学符号
# +    plus
# -    minus
# /    slash    除法取整
# *    asterisk
# %    percent  除法取余
# <    less-than
# >    greater-than
# <=   less-than-equal
# >=   greater-than-equal


print "I will now count my chickens:"

print "Hens", 25 + 30/6.
print "Roosters", 100 - 25 * 3 % 4

print "Now I will count the eggs:"

print 3 + 2 + 1 - 5 + 4 % 2 - 1 / 4 +6

print "Is it true that 3 + 2 < 5 - 7?"

print 3 + 2 < 5 - 7

print "What is 3 + 2?", 3 + 2
print "Oh, that's why it's False."

print "How about some more."

print "Is it greater?", 5 > -2
print "Is it greater or equal?", 5 >= -2
print "Is it less or equal?", 5 <=-2


print "%s,,,,,,%d" % ("dsfasd", 5)

print "." * 10 ,

print "a" + "b" + "c"

print """
There's something going on here.
With the three double-quotes.
We'll be able to type as much as we like.
Even 4 lines if we want, or 5, or 6.
"""



print "%s" % '6.656'
print "%r" % 6.336

print "dasfsf",
age = raw_input("input your age:")
print age
