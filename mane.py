def mane_function(n):
    print (n)
    if n > 5:
        return
    mane_function (n + 1)
mane_function (1)
print ("get result 123456 for mane_function(1)")
mane_function (2)
print ("get result 23456 for mane_function(2)")
mane_function (3)
print ("get result 3456 for mane_function(3)")
mane_function (4)
print ("get result 456 for mane_function(4)")
print ("So added new code line to mane....")
print ("Comment that cannot see changes from test branch")


#when come to test branch cannot see two added last code lines from master"

def test_function(j, k):
    return j * k
print (test_function (3, 7))
print (test_function (8, 9))


