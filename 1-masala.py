number = input("Enter a number: ")

digit_count = {}

for digit in number:
    if digit in digit_count:
        digit_count[digit] += 1
    else:
        digit_count[digit] = 1
for digit in sorted(digit_count):
    print(f"{digit} - {digit_count[digit]}")
