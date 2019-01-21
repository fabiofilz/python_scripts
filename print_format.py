##################################
# Print format
##################################

# Formatting with placeholders
######################################################3
print("I'm going to inject %s here." %'something')

print("I'm going to inject %s text here, and %s text here." %('some','more'))

x, y = 'some', 'more'
print("I'm going to inject %s text here, and %s text here."%(x,y))

# Format conversion methods.
######################################################3
print('He said his name was %s.' %'Fred')
# He said his name was Fred.
print('He said his name was %r.' %'Fred')   # __repr__()
# He said his name was 'Fred'.


# Padding and Precision of Floating Point Numbers
######################################################3

print('Floating point numbers: %5.2f' %(13.144))
# Floating point numbers: 13.14

print('Floating point numbers: %1.0f' %(13.144))
# Floating point numbers: 13

print('Floating point numbers: %1.5f' %(13.144))
# Floating point numbers: 13.14400

print('Floating point numbers: %10.2f' %(13.144))
# Floating point numbers:      13.14

print('Floating point numbers: %25.2f' %(13.144))
# Floating point numbers:                     13.14

print('First: %s, Second: %5.2f, Third: %r' %('hi!',3.1415,'bye!'))
# First: hi!, Second:  3.14, Third: 'bye!'


# Formatting with the .format() method. The .format() method has several advantages over the %s placeholder method:
######################################################

print('Insert another string with curly brackets: {}'.format('The inserted string'))
# 'Insert another string with curly brackets: The inserted string'

# 1. Inserted objects can be called by index position:
print('The {2} {1} {0}'.format('fox','brown','quick'))
# The quick brown fox

# 2. Inserted objects can be assigned keywords:
print('First Object: {a}, Second Object: {b}, Third Object: {c}'.format(a=1,b='Two',c=12.3))
# First Object: 1, Second Object: Two, Third Object: 12.3

#3. Inserted objects can be reused, avoiding duplication:
print('A %s saved is a %s earned.' %('penny','penny'))
# A penny saved is a penny earned.

print('A {p} saved is a {p} earned.'.format(p='penny'))
# A penny saved is a penny earned.

# Alignment, padding and precision with .format()
######################################################
print('{0:8} | {1:9}'.format('Fruit', 'Quantity'))
print('{0:8} | {1:9}'.format('Apples', 3.))
print('{0:8} | {1:9}'.format('Oranges', 10))
# Fruit    | Quantity 
# Apples   |       3.0
# Oranges  |        10


print('{0:<8} | {1:^8} | {2:>8}'.format('Left','Center','Right'))
print('{0:<8} | {1:^8} | {2:>8}'.format(11,22,33))
# Left     |  Center  |    Right
# 11       |    22    |       33


print('{0:=<8} | {1:-^8} | {2:.>8}'.format('Left','Center','Right'))
print('{0:=<8} | {1:-^8} | {2:.>8}'.format(11,22,33))
# Left==== | -Center- | ...Right
# 11====== | ---22--- | ......33

print('{a:=<8} | {b:-^8} | {c:.>8}'.format(a='Left', b='Center', c='Right'))
print('{a:=<8} | {b:-^8} | {c:.>8}'.format(a=11, b=22, c=33))
# Left==== | -Center- | ...Right
# 11====== | ---22--- | ......33

print('This is my ten-character, two-decimal number:%10.2f' %13.579)
print('This is my ten-character, two-decimal number:{0:10.4f}'.format(13.579))
# This is my ten-character, two-decimal number:     13.58
# This is my ten-character, two-decimal number:   13.5800

# Formatted String Literals (f-strings)
######################################################
name = 'Fred'
print(f"He said his name is {name}.")
# He said his name is Fred.


print(f"He said his name is {name!r}")   # __repr__()
# He said his name is 'Fred'

# Float formatting follows "result: {value:{width}.{precision}}"
num = 23.45678
print("My 10 character, four decimal number is:{0:10.4f}".format(num))
# My 10 character, four decimal number is:   23.4568
print(f"My 10 character, four decimal number is:{num:{10}.{6}}")
# My 10 character, four decimal number is:   23.4568

num = 23.45
print("My 10 character, four decimal number is:{0:10.4f}".format(num))
# My 10 character, four decimal number is:   23.4500
print(f"My 10 character, four decimal number is:{num:{10}.{6}}")
# My 10 character, four decimal number is:     23.45

num = 23.45
print("My 10 character, four decimal number is:{0:10.4f}".format(num))
# My 10 character, four decimal number is:   23.4500
print(f"My 10 character, four decimal number is:{num:10.4f}")
# My 10 character, four decimal number is:   23.4500



# FUNCTION
######################################################
def format_f(name, age):
    return f'He said his name is {name} and he is {age} years old.'

def format_per(name, age):
    return 'He said his name is %s and he is %s years old.' % (name, age)

def format_string(name, age):
    return 'He said his name is ' + name + ' and he is ' + str(
        age) + ' years old.'

def format_format(name, age):
    return 'He said his name is {} and he is {} years old.'.format(name, age)

from string import Template
template = Template('He said his name is $name and he is $age years old.')

def format_template(name, age):
    return template.substitute(name=name, age=age)

print(format_f('Fabio f', '21'))
print(format_per('Fabio per', '21'))
print(format_string('Fabio string', '21'))
print(format_format('Fabio format', '21'))
print(format_template('Fabio template', '21'))
# He said his name is Fabio f and he is 21 years old.
# He said his name is Fabio per and he is 21 years old.
# He said his name is Fabio string and he is 21 years old.
# He said his name is Fabio format and he is 21 years old.
# He said his name is Fabio template and he is 21 years old.

# Plural
######################################################
print("%(pronome)s %(verb)s a %(noun)s." % {"pronome": "This", "noun": "test", "verb": "is"})
print("%(pronome)s %(verb)s %(noun)s." % {"pronome": "These", "noun": "testes", "verb": "are"})
# This is a test.
# These are testes.


######################################################
# PERFORMANCE COMPARATION
######################################################
import timeit

format = """
def format(name, age):
    return f'He said his name is {name} and he is {age} years old.'
""", """
def format(name, age):
    return 'He said his name is %s and he is %s years old.' % (name, age)
""", """
def format(name, age):
    return 'He said his name is ' + name + ' and he is ' + str(
        age) + ' years old.'
""",  """
def format(name, age):
    return 'He said his name is {} and he is {} years old.'.format(name, age)
""", """
from string import Template

template = Template('He said his name is $name and he is $age years old.')

def format(name, age):
    return template.substitute(name=name, age=age)
"""

test = """
def test():
    for name in ('Fred', 'Barney', 'Gary', 'Rock', 'Perry', 'Jackie'):
        for age in range (20, 200):
            format(name, age)
"""

for fmt in format:
    print(timeit.timeit('test()', fmt + test, number=10000))


# 3.496802750999997
# 4.316503745999995
# 5.855094422999997
# 5.4657661229999945
# 40.785825333999995


