class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        word_list = [x for x in re.sub(r'[^\w]', ' ', paragraph).lower().split() if x not in banned]
        return Counter(word_list).most_common(1)[0][0]


from collections import Counter
import re


paragraph = 'Bob hit a ball, the hit BALL flew far after it was hit.'
banned = ['hit']


# print(paragraph.lower())
#lower은 일단 리스트에선 반환이 안된다.
# 그냥 문자열 str 문자열에서만 lower()가 가능하다!

# split도! split 은 근데 바로 리스트로 반환해줌.
# print(paragraph.split())

#일단 그냥 문자열 나오면, 공백이랑, 알파벳, 숫자
#문자 어떻게 replace하고, 정규식으로 쪼갤 건지 고민부터 해야할듯
# 수요일날 일단 ㄱ



# word_list = [x for x in re.sub(r'[^\w]', ' ', paragraph).lower().split() if x not in banned]
#리스트 컴프리헨션 공부좀 해야겠다
# print(Counter(word_list).most_common(1)[0][0])
#most common 을 바탕으로 most_common() 파라미터 안에는
#상위 n개를 반환해준다!
# for i in paragraph:
#     paragraph = paragraph.lower()
#     paragraph = re.sub(r'[^\w]', ' ', paragraph)
#     # paragraph = paragraph.split()
#     # e_list.append(i)

# print(paragraph)
