n=int(input("Enter the number of rows: "),base=10)

#Upper Triangle
for i in range(n):
    for j in range(n-i):
        print("*",end=" ")
    print()    


#Lower Triangle
for i in range(n):
    for j in range(n-i-1):
        print(" ",end="")
    for j in range(i+1):
        print("*",end="")
    print()


#Pyramid
for i in range(n):
    for j in range(n-i+1):
        print(' ',end="")
    for j in range(i+1):
        print('*',end=" ")
    print()

