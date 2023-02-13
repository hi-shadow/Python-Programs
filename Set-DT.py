s1 = set()
print(type(s1))
s1.add(1)
s1.add(1)
s1.add(1)
s1.add(2)

print(s1.union({12, 33, 1}))
print(s1)
