class Solution:
    def reverseString(self, s: List[str]) -> None:

        s[:] = s[::-1]
        


#2. reverse string
# def reverseString(s):
#     s = s[::-1]
#     return s

# s = ['h', 'e', 'l']

# print(reverseString(s))
#이렇게 하면 왜 안되는거지??
#--> 쳐보니까 공간복잡도 때매 안된다고 함..
