# # 1
# a = int(input("first leg"))
# b = int(input("second leg"))
# print("output" + (a**2 + b**2)**0.5)


# # 2
# c = int(input("Number"))
# print(c // 10 % 10)


# # 3
# a = int(input("Number"))
# print(a + (a+1) % 2 + 1)


# # 8
# a = int(input())
# b = int(input())
# c = int(input())
# if a + b > c and a + c > b and b + c > a:
#     print("YES")
# else:
#     print("NO")


# # 6
# a = int(input())
# b = int(input())
# c = int(input())
# min_num = 0
# if a >= b >= c or a >= c >= b:
#     min_num = a
# elif b >= a >= c or b >= c >= a:
#     min_num = b
# elif c >= b >= a or c >= a >= b:
#     min_num = c
# print(min_num)
# they expected max value i tried to find min value for 30 minutes


# # 5
# a = int(input())
# b = int(input())
# if a > b:
#     print(1)
# elif b > a:
#     print(2)
# elif a == b:
#     print(0)


# # 9
# a = int(input())
# b = int(input())
# c = int(input())
# if a == b == c:
#     print(3)
# elif a == c or a == b or b == c:
#     print(2)
# else:
#     print(0)


# # 10
# a = int(input())
# b = int(input())
# c = int(input())
# temp_c = 0
# temp_b = 0
# temp_a = 0
# if a <= b <= c:
#     temp_c = c
#     temp_b = b
#     temp_a = a
# elif a <= c <= b:
#     temp_c = b
#     temp_b = c
#     temp_a = a
# elif c <= a <= b:
#     temp_c = b
#     temp_b = a
#     temp_a = c
# elif c <= b <= a:
#     temp_c = a
#     temp_b = b
#     temp_a = c
# elif b <= a <= c:
#     temp_c = c
#     temp_b = a
#     temp_a = b
# elif b <= c <= a:
#     temp_c = a
#     temp_b = c
#     temp_a = b
# print(temp_a, temp_b, temp_c)


# # 7
# a = int(input())
# b = int(input())
# c = int(input())
# d = int(input())
# if a == c or b == d:
#     print("YES")
# else:
#     print("NO")


# # max
# a = int(input())
# b = int(input())
# max_value = 0
# if a > b:
#     max_value = a
# elif b > a:
#     max_value = b
# elif a == b:
#     max_value = a
# print(max_value)


# problem solving
# a = input()
# b = input()
# c = input()
# a = float(a)
# b = float(b)
# c = float(c)
# dis = b ** 2 - 4 * a * c
# if a != 0:
#     if dis > 0:
#         x1 = (-b + dis**0.5)/(2*a)
#         x2 = (-b - dis**0.5)/(2*a)
#         print(x1, x2)
#     elif dis == 0:
#         x1 = -b / 2*a
#         print(x1)
# kak napisat' return 0?

# triangle
a = float(input())
b = float(input())
c = float(input())
cosa = (b**2 + c**2 - a**2)/(2*b*c)
if cosa > 0:
    print("acute")
elif cosa < 0:
    print("obtuse")
elif cosa == 0:
    print("right")
elif a + b < c or a + c < b or b + c < a or b + a < c:
    print("impossible")

