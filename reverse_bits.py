'''
Reverse bits of a given 32 bits unsigned integer.

Note:
Note that in some languages, such as Java, there is no unsigned integer type.
In this case, both input and output will be given as a signed integer type.
They should not affect your implementation, as the integer's internal binary representation is the same,
whether it is signed or unsigned.
In Java, the compiler represents the signed integers using 2's complement notation.
Therefore, in Example 2 above, the input represents the signed integer -3 and the output represents the signed integer -1073741825.
 

Example 1:
Input: n = 00000010100101000001111010011100
Output:    964176192 (00111001011110000010100101000000)
Explanation: The input binary string 00000010100101000001111010011100 represents the unsigned integer 43261596,
so return 964176192 which its binary representation is 00111001011110000010100101000000.

Example 2:
Input: n = 11111111111111111111111111111101
Output:   3221225471 (10111111111111111111111111111111)
Explanation: The input binary string 11111111111111111111111111111101 represents the unsigned integer 4294967293,
so return 3221225471 which its binary representation is 10111111111111111111111111111111.
 

Constraints:
The input must be a binary string of length 32
 

Follow up: If this function is called many times, how would you optimize it?

'''
def reverseBits(n):
    tmp = str(n)
    while len(tmp) < 32:
        tmp = '0' + tmp
    
    bString = ''
    for i in range(32):
        bString = tmp[i] + bString
        
    return int(bString, 2)

# Same as the normal reverseBits but takes an int as input
def reverseBitsInt(n):
    # Convert integer to binary string
    tmp = bin(n)[2:]
    
    tmp = '0' * (32 - len(tmp)) + tmp 
    
    bString = ''
    for i in range(32):
        bString = tmp[i] + bString
        
    return int(bString, 2)

# Some Test cases
if __name__ == "__main__":
    
    # Examples
    input = [
        ('00000010100101000001111010011100', '964176192'),
        ('11111111111111111111111111111101', '3221225471')
        
    ]

    for idx, (n, expected) in enumerate(input):
        print("\nExample", idx, ":")
        print("Input:", n)
        print("Output:", reverseBits(int(n)))
        print("Expected:", expected)