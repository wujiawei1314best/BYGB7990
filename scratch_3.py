size =int(input("Enter your size number:"))


for i in range(size):
    for j in range(size-i):
        print('*',end='')
    print()

