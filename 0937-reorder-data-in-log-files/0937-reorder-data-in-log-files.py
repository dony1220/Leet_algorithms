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
#3. log-lambda

# logs = ["dig1 8 1 5 1",
#         "let1 art can",
#         "dig2 3 6",
#         "let2 own kit dig",
#         "let3 art zero"]



# # letter_logs = []
# # #숫자 담는 리스트
# # digit_logs = []
# #문자로 즉 letter로 구성된 리스트를 담을거임

# # for log in logs:
# #     letter_logs = [log for log in logs if log.split()[1].isalpha()]
# #     digit_logs = [log for log in logs if log.split()[1].isdigit()]
# #근데 만약에 아 짜증나네
# #문자열을 lambda로 ㅈ조질시 사전순으로 정렬된다.ㅇㅇ
# #사전순으로 정렬되면서 , lambda를 뭘로 기준으로 잡을지 하면 될 듯?

# # print(sorted(logs, key=lambda x : x))
# l = []
# d = []

# # 그니까 -> dig, let 이라는 식별자가 존재해요 맞죠?
# # 그러니까 split 했을 때 -> 식별자 다음 꺼가 이게
# # 숫자냐 , 문자냐로 리스트를 하나하나 추가하면 되는거지 ㅇㅈ?
# # 그러고 
# for log in logs:
#     l = [log for log in logs if log.split()[1].isalpha()]
#     d = [log for log in logs if log.split()[1].isdigit()]
#     # 자 근데 여기서 식별자 제외, 동일한 경우에 식별자로 정렬ㅇㅇ
#     l.sort(key=lambda x: (x.split()[1:], x.split()[0]))
#     # x.split()[1: ] 식별자 이후 기준으로 정렬하되
#     # x.split()[0] 동일시? -> 식별자 기준으로 정렬한다
#     #right?
# print(l+d)
# # 몇 시간을 쓴거임 대체? 진짜 빡대가리임
        
