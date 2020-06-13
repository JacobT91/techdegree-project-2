rows = range(4)
cols = range(10)

print([(x, y) for y in rows for x in cols])

print([(letter, number) for number in range(1, 5) for letter in 'abc'])

print({number: letter for letter, number in zip('abcdefghijklmnopqrstuvwxyz', range(1, 27))})