import os
os.system('cls')


from collections import defaultdict
def solution(id_list, report, k):
    #신고 누적을 위한 dict
    status = dict.fromkeys(id_list, 0)

    #신고 추적을 위한 dict
    report_who = defaultdict(list)

    for info in report :
        from_, to_ = info.split()
        if to_ not in report_who[from_] :
            status[to_] += 1
            report_who[from_].append(to_)

    answer = []

    for id in id_list :
        cnt = 0
        for reported in report_who[id] :
            if status[reported] >= k:
                cnt += 1
        answer.append(cnt)
    return answer

print(solution(["con", "ryan"],["ryan con", "ryan con", "ryan con", "ryan con"] , 3))
print(solution(["muzi", "frodo", "apeach", "neo"], ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"], 2))