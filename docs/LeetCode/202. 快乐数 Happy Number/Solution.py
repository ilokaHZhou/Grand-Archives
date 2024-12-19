class Solution:
    def isHappy(self, n: int) -> bool:
        # 由于可以无限循环，有些数变着变着就会重复自身陷入循环，始终变不到1
        # 所以用set来记录
        record = set()
        while n not in record:
            record.add(n)
            new_num = 0
            n_str = str(n)
            for i in n_str:
                new_num = int(i) ** 2
            if new_num == 1:
                return True
            else:
                n = new_num
        return False