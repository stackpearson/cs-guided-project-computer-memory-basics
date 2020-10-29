# Given an integer, write a function that reverses the bits (in binary) and returns the integer result.

# Examples:

# csReverseIntegerBits(417) -> 267
# 417 in binary is 110100001. Reversing the binary is 100001011, which is 267 in decimal.
# csReverseIntegerBits(267) -> 417
# csReverseIntegerBits(0) -> 0

def csReverseIntegerBits(n):
    #convert n to binary
    #convert binary to string & reverse it
    #convert reversed string to binary
    #convert back to decimal
    bit_n = ''.join([bin(n)])
    bin_string = bit_n[2:]
    reversed_char = int(bin_string[::-1], 2)
    return reversed_char
    
print(csReverseIntegerBits(417))