class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        for log in logs:
            l = [log for log in logs if log.split()[1].isalpha()]
            d = [log for log in logs if log.split()[1].isdigit()]
            # 자 근데 여기서 식별자 제외, 동일한 경우에 식별자로 정렬ㅇㅇ
            l.sort(key=lambda x: (x.split()[1:], x.split()[0]))
            # x.split()[1: ] 식별자 이후 기준으로 정렬하되
            # x.split()[0] 동일시? -> 식별자 기준으로 정렬한다
            #rightㅅ
        return l+d
        