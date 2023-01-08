def mane_function(n):
    print (n)
    if n > 5:
        return
    mane_function (n + 1)
mane_function (1)
print ("get result 123456 for mane_function(1)")
mane_function (2)
print ("get result 23456 for mane_function(2)")