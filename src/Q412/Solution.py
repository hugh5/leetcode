from typing import List
"""
Given an integer n, return a string array answer (1-indexed) where:
    answer[i] == "FizzBuzz" if i is divisible by 3 and 5.
    answer[i] == "Fizz" if i is divisible by 3.
    answer[i] == "Buzz" if i is divisible by 5.
    answer[i] == i (as a string) if none of the above conditions are true.
"""

class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        answer = []
        for i in range(1,n+1):
            current = ""
            if i % 3 == 0:
                current += "Fizz"
            if i % 5 == 0:
                current += "Buzz"
            if current == "":
                current = i.__str__()
            answer.append(current)
        return answer

if __name__ == '__main__':
    s = Solution()
    print(s.fizzBuzz(15))