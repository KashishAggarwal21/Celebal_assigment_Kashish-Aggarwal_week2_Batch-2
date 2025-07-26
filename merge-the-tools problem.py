def merge_the_tools(string, k):
    # Process each substring of length k
    for i in range(0, len(string), k):
        substring = string[i:i+k]
        seen = set()
        result = []
        for c in substring:
            if c not in seen:
                seen.add(c)
                result.append(c)
        print("".join(result))

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)
    
    
    
    
    
'''Sample Input:

STDIN       Function
-----       --------
AABCAAADA   s = 'AABCAAADA'
3           k = 3

Sample Output:
AB
CA
AD'''