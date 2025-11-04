from typing import Literal


def guess_number(N: int, numbers: list[list[str]]) -> str:
    def verify_guess(num: str) -> bool:
        for guess, result in numbers:
            if compare(num, guess) != result:
                return False
        return True

    def compare(num: str, myguess: str) -> str:
        num_of_A, num_of_B = 0, 0
        yes_digits_no_location: set[str] = set()
        for i in range(4):
            if num[i] == myguess[i]:
                num_of_A += 1
            else:
                yes_digits_no_location.add(num[i])
        num_of_B = len(
            [
                j
                for j in range(4)
                if num[j] != myguess[j] and myguess[j] in yes_digits_no_location
            ]
        )

        return f"{num_of_A}A{num_of_B}B"

    # 暴力解决
    ans: list[str] = []
    for i in range(10000):
        candidate = str(i).zfill(4)
        if verify_guess(candidate):
            ans.append(candidate)
            if len(ans) > 1:
                break

    return ans[0] if len(ans) == 1 else "NA"
