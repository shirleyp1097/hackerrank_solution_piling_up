from collections import deque

def my_function(this):

    
    while max(this) == this[0] or max(this) == this[-1]:
        if max(this) == this[0]:
            this.popleft()
        elif max(this) == this[-1]:
            this.pop()
        return "Yes"
        break
    else:
        return 'No'
    

for x in range(0, int(input())):
    size = int(input())
    my_list = deque([int(x) for x in input().replace(' ','')])
    print(my_function(my_list))