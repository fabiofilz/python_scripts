#############################
# String Indexing
#############################
s = 'Hello World'

# Show first element (in this case a letter)
s[0]
# H

s[1]
# e

# Grab everything past the first term all the way to the length of s which is len(s)
s[1:]
# 'ello World'

# Grab everything UP TO the 3rd index
s[:3]
# 'Hel'

#Everything - usually used to duplicate an object
s[:]

# Last letter (one index behind 0 so it loops back around)
s[-1]
# d

# Grab everything but the last letter
s[:-1]
# 'Hello Worl'

# Grab everything, but go in steps size of 1
s[::1]
'Hello World'

# Grab everything, but go in step sizes of 2
s[::2]
# 'HloWrd'

# We can use this to print a string backwards
s[::-1]
# 'dlroW olleH'

# Invert phase
text = 'My name is Fabio'
inverted_phase = ' '.join(text.split()[::-1])
print(inverted_phase)

inverted_list = text.split()[::-1]
inverted_text = ' '.join(inverted_list)
print(inverted_text)
