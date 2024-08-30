def is_happy(number):
    seen = set()
    while number != 1 and number not in seen:
        seen.add(number)
        number = sum(int(x) ** 2 for x in str(number))
    return number == 1

limit = int(input("Enter the limit: "))
print("Happy numbers:")
for num in range(1, limit + 1):
    if is_happy(num):
        print(num)
