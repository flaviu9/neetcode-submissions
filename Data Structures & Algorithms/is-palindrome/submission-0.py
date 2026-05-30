class Solution:
    def isPalindrome(self, s: str) -> bool:
        isPal = False
        check = []
        for elem in s:
            if (ord(elem) >= 65 and ord(elem) <= 90) or (ord(elem) >= 97 and ord(elem) <= 122) or (ord(elem) >= 48 and ord(elem) <= 57):
                check.append(  elem.lower()  )

        if check == check[::-1]:
            isPal = True

        return isPal

