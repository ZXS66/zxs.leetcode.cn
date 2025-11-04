# https://www.nowcoder.com/practice/06f09bafcf3740cf88c08629b0443a8e?channelPut=w251acm

import math
# from collections import deque

def max_seeds(n: int, seeds: list[int], level: int) -> int:
    queue:list[tuple[int, int]] = []
    for seed in seeds:
        if seed >= level:
            queue.append((seed, 1))  # (current_seed_level, current_seed_count)

    # result = 0
    # while queue:
    #     current_level, count = queue.popleft()
    #     if current_level == level:
    #         result += count
    #     elif current_level < level:
    #         continue
    #     else:
    #         next_seed = math.ceil(current_level / 3)
    #         queue.append((next_seed, count * 2))

    # 你可以进行收割，收割必须收割所有种下的小麦。
    def harvest(seed_level_count: list[tuple[int, int]]) -> tuple[list[tuple[int, int]], int, bool]:
        next_seeds = []
        max_result = 0
        can_harvest = False
        for seed_level, count in seed_level_count:
            next_seed = math.ceil(seed_level / 3)
            next_seeds.append((next_seed, count * 2))
            if seed_level == level:
                max_result += count
            elif seed_level > level:
                can_harvest = True

        return next_seeds, max_result, can_harvest

    flag = n > 0
    result = 0
    while flag:
        queue, res, flag = harvest(queue)
        result = max(result, res)

    return result
