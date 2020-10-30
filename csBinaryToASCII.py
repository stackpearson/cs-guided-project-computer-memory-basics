# Every eight bits in the binary string represents one character on the ASCII table.

# Examples:

# csBinaryToASCII("011011000110000101101101011000100110010001100001") -> "lambda"
# 01101100 -> 108 -> "l"
# 01100001 -> 97 -> "a"
# 01101101 -> 109 -> "m"
# 01100010 -> 98 -> "b"
# 01100100 -> 100 -> "d"
# 01100001 -> 97 -> "a"
# csBinaryToASCII("") -> ""
# Notes:

# The input string will always be a valid binary string.
# Characters can be in the range from "00000000" to "11111111" (inclusive).
# In the case of an empty input string, your function should return an empty string.


def csBinaryToASCII(binary):
    #seperate string into sub strings 8 chars in length
    if len(binary) > 0:
        sliced_list = [(binary[i:i+8]) for i in range(0, len(binary), 8)]

        char_list = []

        for i in sliced_list:
            char_list.append(chr(int(i[:8], 2)))

        return ''.join(char_list)
    else:
        return ''

print(csBinaryToASCII("011011000110000101101101011000100110010001100001"))
print(csBinaryToASCII(""))