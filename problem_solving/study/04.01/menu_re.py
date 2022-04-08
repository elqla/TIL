from itertools import combinations
from collections import Counter

def solution(orders, course):
    answer = []
    for c in course:
        menu = []
        for order in orders:
            menu += [''.join(sorted(combination)) for combination in combinations(order, c)]
        count_menu = Counter(menu).most_common()
        answer += [food for food, cnt in count_menu if cnt >1 and  cnt == count_menu[0][1]]

    return sorted(answer)


orders = ["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"]
course = [2, 3, 4]
a = solution(orders, course)
print(a)