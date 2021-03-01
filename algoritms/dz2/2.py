number = int(input("введите число"))


def nums(num, count=0):
    if num < 1:
        return count
    else:
        if num % 10 % 2 == 0:
            count += 1
        num //= 10
        return nums(num, count)


chnum = nums(number)

print(f"колв-во четных чисел = {chnum} , а нечетных= {len(str(number)) - chnum}")
