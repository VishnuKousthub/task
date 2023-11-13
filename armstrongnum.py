n=153
sum=0
temp=n
while n > 0:
    digit = n%10
    sum += digit**3
    n//=10
if temp == sum:
    print("armstrong number")
else:
    print("not an armstrong number")