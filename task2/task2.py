a = [[1,3], [2,2]]
b = [[3,3], [2,2]]
z = []
[z.append(x) for x in [*a, *b] if x not in z]
print(z)