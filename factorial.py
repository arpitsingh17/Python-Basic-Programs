def fact(n):

    if n>=0:
        if n==0:
            return 1
        else:
            if n==1:
                return n
            else:
                return n*fact(n-1)



print fact(5)
