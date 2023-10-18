user = int(input("enter the num"))
rev = 0
temp= user
while user!=0:
    rev +=rev*10+user%10
    user/=10
    if(rev==temp):
        print(rev,"palindrome")
    else:
        print(rev,"not palindrome")

