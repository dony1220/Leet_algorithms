class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        word_list = [x for x in re.sub(r'[^\w]', ' ', paragraph).lower().split() if x not in banned]
        return Counter(word_list).most_common(1)[0][0]
