class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        int_min = -2 ** 31
        int_max = 2 ** 31 - 1
        r = 0 

        sign = -1 if x < 0 else 1
        x = abs(x)  # 取絕對值
        
        while True:  # x 變成 0 就跳
            if x == 0:
                break

            digits = x % 10
            x = x // 10  # 整除

            if r > (int_max // 10):
                return 0
            
            r = r * 10 + digits

        return r * sign

        