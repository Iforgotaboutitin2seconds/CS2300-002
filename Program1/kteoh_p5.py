r = [-1, -2]
s = [-3, 3]
u = [2, -1]
v = [3, 1]
w = [1, 3]


def match(vector):
    if vector == 'r':
        vector = r
    if vector == 's':
        vector = s
    if vector == 'u':
        vector = u
    if vector == 'v':
        vector = v
    if vector == 'w':
        vector = w
    return vector


def write(result, filename):
    with open(filename, 'w') as file:
        file.write(str(result))


def dot(vector1, vector2):
    result = [vector1[0]+vector2[0], vector1[1]+vector2[1]]
    return result


print("You have 5 vectors")
print("r = " + str(r))
print("s = " + str(s))
print("u = " + str(u))
print("v = " + str(v))
print("w = " + str(w))
v1 = input("Enter the first vector: ")
v2 = input("Enter the second vector: ")
vector1 = match(v1)
vector2 = match(v2)
result = dot(vector1, vector2)

write(result, "kteoh_p5_out" + v1 + v2 + ".txt")
