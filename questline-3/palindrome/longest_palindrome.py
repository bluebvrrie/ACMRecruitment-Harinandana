def longest_palindrome(s):
    if not s:
        return ""

    start = end = 0  

    def word(left, right):
        
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return left + 1, right - 1  #adjusted elaments that are now 1 step away

    for i in range(len(s)):
        # Odd-length palindrome
        left1, right1 = word(i, i)
        # Even-length palindrome 
        left2, right2 = word(i, i + 1)

        if right1 - left1 > end - start:
            start, end = left1, right1
        if right2 - left2 > end - start:
            start, end = left2, right2

    return s[start:end + 1]

text = input("Enter a string: ")
print("Longest palindromic substring:", longest_palindrome(text))
