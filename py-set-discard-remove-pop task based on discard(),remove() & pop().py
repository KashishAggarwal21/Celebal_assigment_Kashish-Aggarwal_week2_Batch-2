if __name__ == '__main__':
    input()  
    # Read, reverse, then convert to set
    initial = list(map(int, input().split()))
    initial.reverse()
    s = set(initial)
    
    for _ in range(int(input().strip())):
        cmd = input().split()
        op = cmd[0]
        if op == 'pop':
            s.pop()
        elif op == 'remove':
            try:
                s.remove(int(cmd[1]))
            except KeyError:
                pass
        else:  # discard
            s.discard(int(cmd[1]))
    
    print(sum(s))
    
    
 
 
    
'''Sample Input:

9
1 2 3 4 5 6 7 8 9
10
pop
remove 9
discard 9
discard 8
remove 7
pop 
discard 6
remove 5
pop 
discard 5

Sample Output:

4
'''
