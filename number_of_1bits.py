'''
Write a function that takes the binary representation of a positive integer and returns the number of 
set bits it has (also known as the Hamming weight).

 

Example 1:
Input: n = 11
Output: 3
Explanation:
The input binary string 1011 has a total of three set bits.

Example 2:
Input: n = 128
Output: 1
Explanation:
The input binary string 10000000 has a total of one set bit.

Example 3:
Input: n = 2147483645
Output: 30
Explanation:
The input binary string 1111111111111111111111111111101 has a total of thirty set bits.

Constraints:
1 <= n <= 2^31 - 1

Follow up: If this function is called many times, how would you optimize it?

'''
def hammingWeight(n):
    # Convert integer to binary string
    binStr = bin(n)[2:]
    
    # Convert binary string to list of integers
    binList = [int(x) for x in binStr]

    # Return the sum of the list
    return sum(binList)

# Some Test cases
if __name__ == "__main__":
    
    # Examples
    input = [
        (11, 3),
        (128, 1),
        (2147483645, 30)
        
    ]

    for idx, (n, expected) in enumerate(input):
        print("\nExample", idx, ":")
        print("Input:", n)
        print("Output:", hammingWeight(n))
        print("Expected:", expected)