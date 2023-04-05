class Solution:
    def isPalindrome(self, x: int) -> bool:
        var = x.__str__()
        return var[0:((len(var) - 1) / 2).__ceil__()] == var[:((len(var) - 1) / 2).__floor__():-1]


if __name__ == "__main__":
    s = Solution()
    print(s.isPalindrome(1001))  # True
    print(s.isPalindrome(12321))  # True
    print(s.isPalindrome(12231))  # False
    print(s.isPalindrome(1311))  # False

