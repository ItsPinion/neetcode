class Solution:
    def isPalindrome(self, s: str) -> bool:
        front = 0
        back = len(s) - 1

        while front < back:
            print(s[front], s[back])
            if not s[front].isalnum():
                front += 1
                continue
            if not s[back].isalnum():
                back -= 1
                continue

            if s[front].lower() != s[back].lower():
                return False

            front += 1
            back -= 1

        return True


solution = Solution()
print(solution.isPalindrome("A man, a plan, a canal: Panama"))  # Output: True
print(solution.isPalindrome("race a car"))  # Output: False
