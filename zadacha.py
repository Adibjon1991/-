# arr = input().split()
# new_arr = []
# for el in arr:
#     new_arr.append(int(el))
#     print(new_arr)


# numbers = input().split()
# numbers = list(map(int, numbers))
# unique_numbers = set(numbers)

# print(unique_numbers)


a = int(input())
b = int(input())
c = int(input())
if a < b + c and b < a + c and c < a + b:
    print('YES')
else:
    print('NO!')

