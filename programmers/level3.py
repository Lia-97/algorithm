# 여행경로
# def solution(tickets):
#     airport = {}
#
#     for ticket in tickets:
#         if ticket[0] in airport:
#             airport[ticket[0]].append(ticket[1])
#
#         else:
#             airport[ticket[0]] = [ticket[1]]
#
#     # 딕셔너리 안에 있는 value 를 알파벳 순으로 정렬한다
#     for ap in airport:
#         airport[ap].sort()
#
#     def dfs():
#         stack = ['ICN']
#         path = []
#         while stack:
#             top = stack[-1]
#             if top not in airport or len(airport[top]) == 0:
#                 path.append(stack.pop())
#             else:
#                 stack.append(airport[top].pop(0))
#         return path[::-1]
#
#     answer = dfs()
#     return answer

# 네트워크

