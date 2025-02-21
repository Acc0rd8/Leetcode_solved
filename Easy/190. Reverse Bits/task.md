# 190. Reverse Bits #

Reverse bits of a given 32 bits unsigned integer.


__Note:__

- Note that in some languages, such as Java, there is no unsigned integer type. In this case, both input and output will be given as a signed integer type. They should not affect your implementation, as the integer's internal binary representation is the same, whether it is signed or unsigned.
- In Java, the compiler represents the signed integers using 2's complement notation. Therefore, in Example 2 above, the input represents the signed integer -3 and the output represents the signed integer -1073741825.
 

__Example 1:__

> __Input:__ n = 00000010100101000001111010011100
> __Output:__    964176192 (00111001011110000010100101000000)
> __Explanation:__ The input binary string 00000010100101000001111010011100 represents the unsigned integer 43261596, so return 964176192 which its binary representation is 00111001011110000010100101000000.

__Example 2:__

> __Input:__ n = 11111111111111111111111111111101
> __Output:__   3221225471 (10111111111111111111111111111111)
> __Explanation:__ The input binary string 11111111111111111111111111111101 represents the unsigned integer 4294967293, so return 3221225471 which its binary representation is 10111111111111111111111111111111.
 

__Constraints:__

- The input must be a binary string of length 32
