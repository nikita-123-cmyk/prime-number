def in_prime_numb(n,start,end)
for n in range(start,end):
    if n>1:
        is_prime=True
        for i in range(2,n):
            if n%i==0:
                print(f"{n}is not a prime number")
                return False
            break
        if is_prime:
            print(f"{n}is a prime number")
            break

        n=49 , start=2, end=50
        in_prime_numb(n,start,end)
