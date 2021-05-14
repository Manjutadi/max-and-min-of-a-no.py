#max and min of no
n=int(input())
max=0
min=9
while n:
    r=n%10
    n=n//10
    if r>max:
        max=r
    elif r<min:
        min=r
print(max,min)
