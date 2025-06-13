# LeetCode_007-Reverse-Integer
Given a number, reverse its digits.   If the reversed number is bigger than 32-bit integer range, return 0.  


## How I solved it
- I use a while loop to take each digit from the number.
- I use `% 10` to get the last digit.
- I use `// 10` to remove the last digit.
- I check if the result is too big.
- I handle the positive or negative sign.
