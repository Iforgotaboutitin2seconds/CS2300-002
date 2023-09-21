Teoh = 4
Kenyou = 6
value = 2

print("Teoh = " + str(Teoh))
print("Kenyou = " + str(Kenyou))

Mat1 = []
Mat2 = []
Mat3 = []
Mat4 = []

# Mat1
for i in range(Teoh):
    row = []
    for j in range(Kenyou):
        row.append(i * Kenyou + j + 1)
    Mat1.append(row)

for row in Mat1:
    print(row)
print()
# End Mat1

# Mat2
for i in range(Teoh):
    row = []
    row.append(value)
    value += 3
    Mat2.append(row)

for j in range(Kenyou - 1):
    for i in range(Teoh):
        Mat2[i].append(value)
        value += 3

for row in Mat2:
    print(row)
print()
# End Mat2

# Mat3
value = 10

for i in range(2):
    row = []
    for j in range(4):
        row.append(value)
        value -= 2
    Mat3.append(row)

for row in Mat3:
    print(row)
print()
# End Mat3

# Mat4
value = -6

for i in range(4):
    row = []
    row.append(value)
    value += 1.5
    Mat4.append(row)

for j in range(1):
    i = 0
    for i in range(4):
        Mat4[i].append(value)
        value += 1.5

for row in Mat4:
    print(row)
print()
# End Mat4


with open('kteoh_mat1.txt', 'w') as file:
    for row in Mat1:
        for element in row:
            file.write(str(element) + " ")
        file.write("\n")

with open('kteoh_mat2.txt', 'w') as file:
    for row in Mat2:
        for element in row:
            file.write(str(element) + " ")
        file.write("\n")

with open('kteoh_mat3.txt', 'w') as file:
    for row in Mat3:
        for element in row:
            file.write(str(element) + " ")
        file.write("\n")

with open('kteoh_mat4.txt', 'w') as file:
    for row in Mat4:
        for element in row:
            file.write(str(element) + " ")
        file.write("\n")
