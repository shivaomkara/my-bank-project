m=int(input("marks in maths:"))
s=int(input("marks in science:"))
e=int(input("marks in english:"))

total=m+s+e
avg=total/3
percentage=(total/300)*100
if percentage>90:
    grade='A'
elif percentage>80 and percentage<=90:
    grade="B"
elif percentage>70 and percentage<=80:
    grade="C"
else:
    grade="P"
print(f"total marks:{total} \n avg marks :{avg} \n grade:{grade}")


