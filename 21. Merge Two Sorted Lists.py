def mergeTwoLists(x, y):
    r = x + y
    r.sort()
    print(r)


l1 = map(int, input().split())
l2 = map(int, input().split())
mergeTwoLists(l1, l2)
