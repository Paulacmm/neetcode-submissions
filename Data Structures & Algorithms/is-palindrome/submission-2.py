class Solution:
    def isPalindrome(self, s: str) -> bool:
        sentence = []

        if len(s) == 1:
            return True

        for letter in s:
            if letter.isalnum():
                sentence.append(letter.lower())
        print(sentence)

        if sentence == sentence[::-1]:
            return True
        else:
            return False


