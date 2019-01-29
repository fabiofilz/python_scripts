# rangelist = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
rangelist = [1, 2]
for number in rangelist:
    # Check if number is one of
    # the numbers in the tuple.
    if number in (3, 4, 7, 9):
        # "Break" terminates a for without
        # executing the "else" clause.
        print('Break')
        break
    else:
        # "Continue" starts the next iteration
        # of the loop. It's rather useless here,
        # as it's the last statement of the loop.
        print('Continue')
        continue
else:
    # The "else" clause is optional and is
    # executed only if the loop didn't "break".
    print('FOR ELSE')


##### FOR
for x in [0, 1, 2, 3, 4, 5]:
    print('inside: ', x)
else:
    print('outside: ')

#### WHILE
x = 0
while x < 6:
    print('inside: ', x)
    x = x + 1   
else:
    print('outside: ')


