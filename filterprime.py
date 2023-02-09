def prime2 (mylist):
    nums = mylist
    for i in range(2, 8):
        print (i) # added to make things explicit; it's not necessary
        nums = filter(lambda x: x == i or x % i, nums)
    return nums