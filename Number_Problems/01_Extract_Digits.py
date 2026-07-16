#1.COUNT DIGITS IN A NUMBER
n=5873
num=n
count=0
while num>0:
    count+=1
    num=num//10
print(count)

#2.REVERSE A NUMBER
n = 5873
num = n
reverse = 0
while num > 0:
    last_digit = num % 10
    reverse = reverse * 10 + last_digit
    num = num // 10
print(reverse)

#3.CHECK PALINDROME
n=1234
num=n
result=0
while num>0:
    id=num%10
    result=(result*10)+id
    num=num//10
print(n==result)

#4. ARMSTRONG NUMBER
n=153
num=n
total=0
nod=(len(str(n)))
while num>0:
    id=num%10
    total=total+(id**nod)
    num=num//10
print(total==n)