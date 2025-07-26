from collections import Counter
if __name__ == '__main__':
    x = int(input().strip())  # number of shoes 
    shoe_counts = Counter(map(int, input().split()))
    n = int(input().strip())  # number of customers
    
    total_earnings = 0
    for _ in range(n):
        size, price = map(int, input().split())
        if shoe_counts[size] > 0:
            total_earnings += price
            shoe_counts[size] -= 1
    
    print(total_earnings)
    
    
 
 
    
''' Sample Input
10
2 3 4 5 6 8 7 6 5 18
6
6 55
6 45
6 55
4 40
18 60
10 50

Sample Output
200
'''