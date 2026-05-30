class Solution:
    def isPalindrome(self, s: str) -> bool:
        check = []
        for elem in s:
            if (ord(elem) >= 65 and ord(elem) <= 90) or (ord(elem) >= 97 and ord(elem) <= 122) or (ord(elem) >= 48 and ord(elem) <= 57):
                check.append(elem.lower())

        left = 0
        right = len(check) - 1

        while left < right:
            if check[left] != check[right]:
                return False
            left += 1
            right -= 1

        return True