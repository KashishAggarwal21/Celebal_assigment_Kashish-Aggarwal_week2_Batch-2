def average(array):
    # Remove duplicates using a set
    distinct = set(array)
    # Compute the mean of distinct heights
    avg = sum(distinct) / len(distinct)
    # Round to 3 decimal places before returning
    return round(avg, 3)

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)
    
    
    
    
 
 
 
    
    
'''Sample Input:

STDIN                                       Function
-----                                       --------
10                                          arr[] size N = 10
161 182 161 154 176 170 167 171 170 174     arr = [161, 181, ..., 174] 

Sample Output:

169.375'''