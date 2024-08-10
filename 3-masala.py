s = input("Sonni kiriting: ")
count = 0

for char in s:
    if char == '0':
        count += 1
    else:
        break

print(count)
