class Solution:
    def isPalindrome(self, s: str) -> bool:
            text = s.lower()
            text = text.replace(' ', '')
            text = re.sub('[^a-zA-Z0-9]', '',text)
            
            reverse_text = text[::-1]

            if text == reverse_text:
                return True
            else:
                return False
        