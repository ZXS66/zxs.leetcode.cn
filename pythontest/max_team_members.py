# https://www.nowcoder.com/practice/60c417b02a3b49708dbb634956bb65fe?channelPut=w251acm


def max_team_members(T: int, teams: list[list[int]]) -> list[int]:
    max_members = [1] * T

    for i in range(T):
        n, k = teams[i * 2]
        a = teams[i * 2 + 1]
        a.sort()

        leftIdx = 0
        for rightIdx in range(1, n):
            if a[rightIdx] - a[leftIdx] <= k:
                continue
            else:
                leftIdx += 1
            count = rightIdx - leftIdx + 1
            if count > max_members[i]:
                max_members[i] = count

    return max_members
