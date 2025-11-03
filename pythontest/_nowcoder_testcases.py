# import dependencies
from dataclasses import dataclass
import sys
from typing import Any, Literal
import unittest

# import local modules
from prevent_flood import prevent_flood

from sudoku_hj44 import resolve_sudoku
from max_common_substr_hj75 import max_common_substr
from max_bits_hj86 import max_bits


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
                expected=0, args=[
                    "2 2",
                    "**",
                    "**",
                ]
            ),
            NowcoderTestCase(
                expected=1,
                args=[
                    "3 3",
                    "***",
                    "*0*",
                    "***",
                ]
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
"******0*0*********"
                ]
            ),
        ]
        for tc in testcases:
            [x, y]=parse_args_as_list_of_integers(tc.args[0])
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
                args=["0 9 2 4 8 1 7 6 3",
"4 1 3 7 6 2 9 8 5",
"8 6 7 3 5 9 4 1 2",
"6 2 4 1 9 5 3 7 8",
"7 5 9 8 4 3 1 2 6",
"1 3 8 6 2 7 5 9 4",
"2 7 1 5 3 8 6 4 9",
"3 8 6 9 1 4 2 5 7",
"0 4 5 2 7 6 8 3 1"],
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
                args=["7 3 0 0 0 8 0 0 0",
"2 0 0 0 0 0 6 0 0",
"0 0 1 0 0 0 4 5 0",
"0 0 0 0 0 5 9 6 0",
"9 0 0 8 1 0 0 4 0",
"0 0 0 0 0 2 7 8 0",
"0 0 6 0 0 0 5 2 0",
"1 0 0 0 0 0 8 0 0",
"8 9 0 0 0 6 0 0 0"],
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
            expected = max_common_substr(s,t)
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


if __name__ == "__main__":
    unittest.main()
