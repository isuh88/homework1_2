div = 2
switch = 0
def prime_determine(n):
    global div
    global switch
    if n == 1:
        print(n, 'is not a prime number')
    elif n == 2:
        print(n, 'is a prime number')
    elif div <= (n/2):
            if (n % div) == 0:
                print(n, 'is not a prime number')
                switch = 1
            else:
                div += 1
                prime_determine(n)
    else:
        if switch == 0:
            print(n, 'is a prime number')

prime_determine(int(input("Enter a number: ")))