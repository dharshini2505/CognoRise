import random
letters=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','Q','R','S','T','U','V','W','X','Y','Z']
numbers=['0','1','2','3','4','5','6','7','8','9']
symbols=['!','@','#','$','%','^','&','*','(',')','-','+','_','=']
print("----PASSWORD GENERATOR--------")
n_letters=int(input("Enter the letters you want:"))
n_numbers=int(input("Enter the numbers you want:"))
n_symbols=int(input("Enter the symbols you want:"))
password=""
for i in range(1,n_letters+1):
    char=random.choice(letters)
    password += char
for i in range(1,n_numbers+1):
    char=random.choice(numbers)
    password += char
for i in range(1,n_symbols+1):
    char=random.choice(symbols)
    password += char
print(password)

