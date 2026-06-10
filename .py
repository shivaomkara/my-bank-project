# string="happy birthday"
# print(string[1::-1])
# string=input()
# s2=string.lower()
# a=s2.count("a")
# e=s2.count("e")
# i=s2.count("i")
# o=s2.count("o")
# u=s2.count("u")
# print(f"number of vowels:{a+e+i+o+u}")

# t =input()
# reverse = t[::-1]
# if reverse == t:
#     print("true")
# else:
#     print("false")

# m=int(input("marks in maths:"))
# s=int(input("marks in sciences"))
# e=int(input("marks in english:"))
# total=m+s+e
# avg=total/3
# percentage=(total/300)*100
# grade=" "
# if percentage>90:
#     grade="A"
# elif percentage>80 and percentage<=90:
#     grade="B"
# elif percentage>70 and percentage<=80:
#     grade="C"
# else:
#     grade="p"
# print(f"total marks:{total} \n avg marks:{avg} \n grade:{grade}")


# a=input()
# x,y,z=a.split(",")
# num1=int(x)
# num2=int(y)
# num3=int(z)
# great=0
# if num1>num2:
#     if num1>num3:
#         great=num1
#     else:
#         great=num3
# elif num2>num1:
#     if num2>num3:
#         great=num2
#     else:
#         great=num3
# elif num3>num1:
#     if num3>num2:
#         great=num3
#     else:
#         great=num2
# print(great)

# a = input()
# x, y, z = a.split(",")

# num1 = int(x)
# num2 = int(y)
# num3 = int(z)

# if num1 >= num2 and num1 >= num3:
#     great = num1
# elif num2 >= num1 and num2 >= num3:
#     great = num2
# else:
#     great = num3

# print(great)
year=int(input())
leap=False
if year%100==0 and year%400!=0:
    leap=False
elif year%4==0:
    leap =True
else:
    leap=False
print(leap)

