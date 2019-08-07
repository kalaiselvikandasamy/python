def prime(n):
    for i in range(2,n):
        if(n%i==0):
            print("it is not prime")
        else:
            print("it is prime")
prime(5)
