# import dependencies
from dataclasses import dataclass
from typing import Any
import unittest

# import local modules
from prevent_flood import prevent_flood

from max_bits_hj86 import max_bits
from max_common_substr_hj75 import max_common_substr
from max_seeds import max_seeds
from max_team_members import max_team_members
from sudoku_hj44 import resolve_sudoku
from guess_number import guess_number
from alphabet_snake import snake_move


@dataclass
class NowcoderTestCase:
    expected: Any
    args: list[str]


# def parse_args_as_list_of_integers(sep:str|None=None):
#     return list(map(int, args().split(sep)))


def parse_args_as_list_of_integers(args: str, sep: str | None = None):
    return list(map(int, args.split(sep)))


# def parse_args_as_list_of_strings(sep:str|None=None):
#     return args().split(sep)


def parse_args_as_list_of_strings(args: str, sep: str | None = None):
    return args.split(sep)


# def parse_args_as_list_of_floats(sep:str|None=None):
#     return list(map(float, args().split(sep)))


# def expected_list_of_integers(lst: list[int]):
#     print(" ".join(map(str, lst)))


# def expected_list_of_strings(lst: list[str]):
#     print(" ".join(lst))


class NowcoderTestCases(unittest.TestCase):
    def test_case_prevent_flood(self):
        testcases = [
            NowcoderTestCase(
                expected=0,
                args=[
                    "2 2",
                    "**",
                    "**",
                ],
            ),
            NowcoderTestCase(
                expected=1,
                args=[
                    "3 3",
                    "***",
                    "*0*",
                    "***",
                ],
            ),
            NowcoderTestCase(
                expected=51,
                args=[
                    "19 18",
                    "*0**0**0**0**0****",
                    "*0*0************0*",
                    "0**0****0*******0*",
                    "***0*******0*****0",
                    "*******0*****0****",
                    "**0*0****0*****0**",
                    "0*****000*******0*",
                    "*0********0***0**0",
                    "**00**0***********",
                    "**0***********0**0",
                    "**0*****0****0*0**",
                    "******00*0********",
                    "****0***0******00*",
                    "*****0***00******0",
                    "*****0******0**0*0",
                    "*******00**0****0*",
                    "***0*0****0******0",
                    "****0**00**0******",
                    "******0*0*********",
                ],
            ),
        ]
        for tc in testcases:
            [x, y] = parse_args_as_list_of_integers(tc.args[0])
            matrix = [[item for item in list(row)] for row in tc.args[1:]]
            expected = prevent_flood(x, y, matrix)
            self.assertEqual(tc.expected, expected)

    def test_case_hj44(self):
        testcases: list[NowcoderTestCase] = [
            NowcoderTestCase(
                expected=[
                    [5, 9, 2, 4, 8, 1, 7, 6, 3],
                    [4, 1, 3, 7, 6, 2, 9, 8, 5],
                    [8, 6, 7, 3, 5, 9, 4, 1, 2],
                    [6, 2, 4, 1, 9, 5, 3, 7, 8],
                    [7, 5, 9, 8, 4, 3, 1, 2, 6],
                    [1, 3, 8, 6, 2, 7, 5, 9, 4],
                    [2, 7, 1, 5, 3, 8, 6, 4, 9],
                    [3, 8, 6, 9, 1, 4, 2, 5, 7],
                    [9, 4, 5, 2, 7, 6, 8, 3, 1],
                ],
                args=[
                    "0 9 2 4 8 1 7 6 3",
                    "4 1 3 7 6 2 9 8 5",
                    "8 6 7 3 5 9 4 1 2",
                    "6 2 4 1 9 5 3 7 8",
                    "7 5 9 8 4 3 1 2 6",
                    "1 3 8 6 2 7 5 9 4",
                    "2 7 1 5 3 8 6 4 9",
                    "3 8 6 9 1 4 2 5 7",
                    "0 4 5 2 7 6 8 3 1",
                ],
            ),
            NowcoderTestCase(
                expected=[
                    [7, 3, 5, 4, 6, 8, 1, 9, 2],
                    [2, 4, 9, 1, 5, 7, 6, 3, 8],
                    [6, 8, 1, 2, 3, 9, 4, 5, 7],
                    [3, 2, 8, 7, 4, 5, 9, 6, 1],
                    [9, 6, 7, 8, 1, 3, 2, 4, 5],
                    [5, 1, 4, 6, 9, 2, 7, 8, 3],
                    [4, 7, 6, 3, 8, 1, 5, 2, 9],
                    [1, 5, 3, 9, 2, 4, 8, 7, 6],
                    [8, 9, 2, 5, 7, 6, 3, 1, 4],
                ],
                args=[
                    "7 3 0 0 0 8 0 0 0",
                    "2 0 0 0 0 0 6 0 0",
                    "0 0 1 0 0 0 4 5 0",
                    "0 0 0 0 0 5 9 6 0",
                    "9 0 0 8 1 0 0 4 0",
                    "0 0 0 0 0 2 7 8 0",
                    "0 0 6 0 0 0 5 2 0",
                    "1 0 0 0 0 0 8 0 0",
                    "8 9 0 0 0 6 0 0 0",
                ],
            ),
        ]
        for tc in testcases:
            matrix = [parse_args_as_list_of_integers(row) for row in tc.args]
            expected = resolve_sudoku(matrix)
            self.assertAlmostEqual(expected, tc.expected)
            # for i in range(9):
            #     self.assertAlmostEqual(expected[i], tc.expected[i])

    def test_case_hj75(self):
        testcases: list[NowcoderTestCase] = [
            NowcoderTestCase(args=["awaabb", "aawbb"], expected=2),
            NowcoderTestCase(args=["asdfas", "werasdfaswer"], expected=6),
            NowcoderTestCase(args=["asdfghjk", "zxcvbnm"], expected=0),
        ]
        for tc in testcases:
            [s, t] = tc.args[0], tc.args[1]
            expected = max_common_substr(s, t)
            self.assertEqual(tc.expected, expected)

    def test_case_hj86(self):
        testcases: list[NowcoderTestCase] = [
            NowcoderTestCase(args=["200"], expected=2),
            NowcoderTestCase(args=["1023"], expected=10),
            NowcoderTestCase(args=["77"], expected=2),
        ]
        for tc in testcases:
            [n] = parse_args_as_list_of_integers(tc.args[0])
            expected = max_bits(n)
            self.assertEqual(tc.expected, expected)

    def test_case_max_seeds(self):
        testcases: list[NowcoderTestCase] = [
            NowcoderTestCase(args=["6", "12 13 14 36 35 34", "4"], expected=12),
        ]
        for tc in testcases:
            n = int(tc.args[0])
            seeds = parse_args_as_list_of_integers(tc.args[1])
            level = int(tc.args[2])
            expected = max_seeds(n, seeds, level)
            self.assertEqual(tc.expected, expected)

    def test_case_max_team_members(self):
        testcases: list[NowcoderTestCase] = [
            NowcoderTestCase(args=["1", "5 3", "8 3 5 1 6"], expected=[3]),
            NowcoderTestCase(
                args=[
                    "3",
                    "10 505",
                    "54604396 120637531 96469253 57030519 358520833 297841423 857285461 771064165 320380391 65255577",
                    "10 504",
                    "521557840 96033464 452668396 11812081 390867436 174826675 365181136 7501879 29638567 303828339",
                    "185 50638",
                    "458565889 340632163 16405177 468140625 327557847 24899317 5327591 158703835 1126189 23764026 76727407 250032226 418166832 311952403 676748689 157421057 184218305 70463327 43181019 899091707 473093596 467825906 10229009 106481776 533143041 74088895 129368149 7773433 22085589 119027425 208235064 4159804 234444673 324965215 516302777 77810945 196505371 345021545 131044046 223444475 237844135 59543023 318859621 27379651 61750081 196921022 690267121 277717726 189477337 223838002 833436592 332764466 64823707 28321401 194380816 144444056 231526285 278856531 185115001 60401132 9633255 300134899 1070641 483126177 182301761 505741482 40331683 4500163 474814954 175857557 513172297 54554748 54584645 6898585 77741761 252778373 24909919 791765209 181898111 132124631 216920407 54227289 24785909 31329001 52837531 173427281 172150861 706062232 176808456 418420979 56522849 4832965 37085177 395376619 241424854 529489273 477194081 98343376 30197368 381088531 10017181 173424232 137405351 684435640 142616477 207134251 504399301 677959437 305275278 204944993 231532645 678750453 3651601 118006279 389223751 31899583 550685281 53464321 221189736 319683469 85604113 31812865 515013019 210042913 43521103 143092216 48263338 322068826 4802450 294162127 441118876 299333049 712640545 190040476 88931868 250526625 653880585 961214149 88020016 633701981 554402114 157598841 102126201 744525379 391019245 261805405 427703055 237557601 137230237 200622521 212523733 449730424 876539665 376999953 339687847 536381631 215665978 18840158 472663305 107306892 432229043 228738457 842694607 55067502 328530399 606288775 856515056 590271859 36296966 113259067 240061981 73149490 802316209 66476319 231254101 517614553 4461745 104562606 425251 106989331 563876176 470983258 365087635 7648711 219968191",
                ],
                expected=[1, 1, 2],
            ),
        ]
        for tc in testcases:
            T = int(tc.args[0])
            teams = [parse_args_as_list_of_integers(arg) for arg in tc.args[1:]]
            result = max_team_members(T, teams)
            self.assertAlmostEqual(tc.expected, result)

    def test_case_guess_number(self):
        testcases: list[NowcoderTestCase] = [
            NowcoderTestCase(
                args=[
                    "6",
                    "4815 1A1B",
                    "5716 0A1B",
                    "7842 0A1B",
                    "4901 0A0B",
                    "8585 3A0B",
                    "8555 2A1B",
                ],
                expected='3585',
            ),
            NowcoderTestCase(args=["2", "4815 0A0B", "2999 3A0B"], expected="NA"),
        ]
        for tc in testcases:
            N = int(tc.args[0])
            numbers: list[list[str]] = []
            for i in range(1, N + 1):
                items = tc.args[i].split()
                numbers.append(items)
            result = guess_number(N, numbers)
            self.assertEqual(tc.expected, result)

    def test_case_snake_move(self):
        testcases: list[NowcoderTestCase] = [
            NowcoderTestCase(
                args=[
                    "5",
                    "S N A K E",
                    "5 5",
                    "S N A B D",
                    "E K F F E",
                    "C B D A L",
                    "E K E F K",
                    "S A R T A",
                ],
                expected=["0 0", "1 0", "1 4", "1 3", "0 3"],
            ),
            NowcoderTestCase(
                args=[
                    "4",
                    "B E A R",
                    "5 5",
                    "S N A B D",
                    "E K F F E",
                    "C B D A L",
                    "E K E F K",
                    "S A R T A",
                ],
                expected=["-1 -1"],
            ),
            NowcoderTestCase(
                args=[
                    "4",
                    "A B C D",
                    "4 4",
                    "D A D X",
                    "C B C X",
                    "D X D X",
                    "X X X X",
                ],
                expected=["1 0", "1 1", "0 1", "0 0"],
            ),
        ]
        for tc in testcases:
            steps = int(tc.args[0])
            alphabet = tc.args[1].split()
            [row, col] = [int(item) for item in tc.args[2].split()]
            matrix = [item.split() for item in tc.args[3:]]
            result = snake_move(steps, alphabet, row, col, matrix)
            # self.assertAlmostEqual(tc.expected, result)
            # x,y 反了…
            for i in range(len(result)):
                x, y = result[i]
                self.assertEqual(
                    tc.expected[i],
                    f"{y} {x}",
                    msg=f"Failed test case with args: {tc.args}",
                )


if __name__ == "__main__":
    _ = unittest.main()
