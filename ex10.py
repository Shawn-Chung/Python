# -*- coding: utf-8 -*-


#This is all of the escape sequences Python supports.

# \\    \
# \'    '
# \"    "
# \a    bell
# \b    backspace
# \f    formfeed
# \n    linefeed
# \N{name}    character named name in the unicode database
# \r    CR
# \t    TAB
# \uxxxx    character with 16-bit hex value xxxx
# \uxxxxxxxx    character with 32-bit hex value xxxxxxxx
# \v    vertical tab
# \ooo    character with octal value ooo
# \xhh    character with hex value hh

print "u'\u4fdc"
print "u'\ukd7309e3"
print "\x09"
tabby_cat = "\tI'm tabbed in."
persian_cat = "I'm split\non a line."
backslash_cat = "I'm \\ a \\ cat."

fat_cat = """
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
"""

print tabby_cat
print persian_cat
print backslash_cat
print fat_cat
