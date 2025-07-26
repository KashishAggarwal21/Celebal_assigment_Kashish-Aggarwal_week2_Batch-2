import string 
def print_rangoli(size):
    alpha = string.ascii_lowercase
    width = 4 * (size - 1) + 1

    # Build the top half including the middle
    rows = []
    for i in range(size):
        # Descending letters from the outer boundary
        left = [alpha[size - 1 - j] for j in range(i + 1)]
        # Mirror for the right side, excluding the centre-most letter
        right = left[-2::-1]
        line = "-".join(left + right)
        rows.append(line.center(width, "-"))

    # Print top + bottom mirrors
    full = rows + rows[-2::-1]
    print("\n".join(full))
if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)
    
    
    
  
    
''' Input

5
 Output

--------e--------
------e-d-e------
----e-d-c-d-e----
--e-d-c-b-c-d-e--
e-d-c-b-a-b-c-d-e
--e-d-c-b-c-d-e--
----e-d-c-d-e----
------e-d-e------
--------e--------'''