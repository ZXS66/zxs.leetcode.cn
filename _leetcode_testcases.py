import unittest
from dataclasses import dataclass
from min_stack_155 import MinStack

from two_sum_1 import Solution as Solution_1
from valid_parentheses_20 import Solution as Solution_20
from group_anagrams_49 import Solution as Solution_49
from simplify_path_71 import Solution as Solution_71
from longest_consecutive_sequence_128 import Solution as Solution_128
from evaluate_reverse_polish_notation_150 import Solution as Solution_150
from happy_number_202 import Solution as Solution_202
from isomorphic_strings_205 import Solution as Solution_205
from contains_duplicate_ii_219 import Solution as Solution_219
from basic_calculator_224 import Solution as Solution_224
from valid_anagram_242 import Solution as Solution_242
from word_pattern_290 import Solution as Solution_290
from ransom_note_383 import Solution as Solution_383
from distance_between_bus_stops_1184 import Solution as Solution_1184
from node_with_highest_edge_score_2374 import Solution as Solution_2374
from points_that_intersect_with_cars_2848 import Solution as Solution_2848


@dataclass
class LeetcodeTestCase:
    input: any
    output: any


class Leetcode_testcases(unittest.TestCase):

    def test_case_1(self):
        testcases = [
            LeetcodeTestCase(
                input={"nums": [2, 7, 11, 15], "target": 9}, output=[0, 1]
            ),
            LeetcodeTestCase(input={"nums": [3, 2, 4], "target": 6}, output=[1, 2]),
            LeetcodeTestCase(input={"nums": [3, 3], "target": 6}, output=[0, 1]),
        ]
        sln = Solution_1()
        for tc in testcases:
            output = sln.twoSum(tc.input["nums"], tc.input["target"])
            self.assertEqual(str(tc.output), str(output))

    def test_case_20(self):
        testcases = [
            LeetcodeTestCase(input="()", output=True),
            LeetcodeTestCase(input="()[]{}", output=True),
            LeetcodeTestCase(input="(]", output=False),
            LeetcodeTestCase(input="([])", output=True),
            LeetcodeTestCase(input="([)]", output=False),
            LeetcodeTestCase(input="{[]}", output=True),
        ]
        sln = Solution_20()
        for tc in testcases:
            output = sln.isValid(tc.input)
            self.assertEqual(tc.output, output)

    def test_case_49(self):
        testcases = [
            LeetcodeTestCase(
                input=["eat", "tea", "tan", "ate", "nat", "bat"],
                output=[["bat"], ["nat", "tan"], ["ate", "eat", "tea"]],
            ),
            LeetcodeTestCase(input=[""], output=[""]),
            LeetcodeTestCase(input=["a"], output=["a"]),
        ]
        sln = Solution_49()
        for tc in testcases:
            output = sln.groupAnagrams(tc.input)
            # self.assertEqual(str(tc.output), str(output))

    def test_case_71(self):
        testcases = [
            LeetcodeTestCase(input="/home/", output="/home"),
            LeetcodeTestCase(input="/home//foo/", output="/home/foo"),
            LeetcodeTestCase(
                input="/home/user/Documents/../Pictures", output="/home/user/Pictures"
            ),
            LeetcodeTestCase(input="/../", output="/"),
            LeetcodeTestCase(input="/.../a/../b/c/../d/./", output="/.../b/d"),
        ]
        sln = Solution_71()
        for tc in testcases:
            output = sln.simplifyPath(tc.input)
            self.assertEqual(tc.output, output)

    def test_case_128(self):
        testcases: list[LeetcodeTestCase] = [
            LeetcodeTestCase(input=[100, 4, 200, 1, 3, 2], output=4),
            LeetcodeTestCase(input=[0, 3, 7, 2, 5, 8, 4, 6, 0, 1], output=9),
            LeetcodeTestCase(input=[], output=0),
        ]
        sln = Solution_128()
        for tc in testcases:
            output = sln.longestConsecutive(tc.input)
            self.assertEqual(tc.output, output)

    def test_case_150(self):
        testcases = [
            LeetcodeTestCase(input=["2", "1", "+", "3", "*"], output=9),
            LeetcodeTestCase(input=["4", "13", "5", "/", "+"], output=6),
            LeetcodeTestCase(
                input=[
                    "10",
                    "6",
                    "9",
                    "3",
                    "+",
                    "-11",
                    "*",
                    "/",
                    "*",
                    "17",
                    "+",
                    "5",
                    "+",
                ],
                output=22,
            ),
            LeetcodeTestCase(input=[1, 2, 3, 4, 5], output=5),
        ]
        sln = Solution_150()
        for tc in testcases:
            output = sln.evalRPN(tc.input)
            self.assertEqual(tc.output, output)

    def test_case_155(self):
        minStack = MinStack()
        minStack.push(-2)
        minStack.push(0)
        minStack.push(-3)
        self.assertEqual(minStack.getMin(), -3)  # 返回 -3.
        minStack.pop()
        self.assertEqual(minStack.top(), 0)  # 返回 0.
        self.assertEqual(minStack.getMin(), -2)  # 返回 -2.

    def test_case_202(self):
        testcases: list[LeetcodeTestCase] = [
            LeetcodeTestCase(input=19, output=True),
            LeetcodeTestCase(input=2, output=False),
        ]
        sln = Solution_202()
        for tc in testcases:
            output = sln.isHappy(tc.input)
            self.assertEqual(tc.output, output)

    def test_case_205(self):
        testcases: list[LeetcodeTestCase] = [
            LeetcodeTestCase(input={"s": "egg", "t": "add"}, output=True),
            LeetcodeTestCase(input={"s": "foo", "t": "bar"}, output=False),
            LeetcodeTestCase(input={"s": "paper", "t": "title"}, output=True),
        ]
        sln = Solution_205()
        for tc in testcases:
            output = sln.isIsomorphic(tc.input["s"], tc.input["t"])
            self.assertEqual(tc.output, output)

    def test_case_219(self):
        testcases: list[LeetcodeTestCase] = [
            LeetcodeTestCase(input={"nums": [1, 2, 3, 1], "k": 3}, output=True),
            LeetcodeTestCase(input={"nums": [1, 0, 1, 1], "k": 1}, output=True),
            LeetcodeTestCase(input={"nums": [1, 2, 3, 1, 2, 3], "k": 2}, output=False),
            LeetcodeTestCase(input={"nums": [99, 99], "k": 2}, output=True),
        ]
        sln = Solution_219()
        for tc in testcases:
            output = sln.containsNearbyDuplicate(
                nums=tc.input["nums"],
                k=tc.input["k"],
            )
            self.assertEqual(tc.output, output)

    def test_case_224(self):
        testcases: list[LeetcodeTestCase] = [
            LeetcodeTestCase(input="1 + 1", output=2),
            LeetcodeTestCase(input=" 2-1 + 2 ", output=3),
            LeetcodeTestCase(input="(1+(4+5+2)-3)+(6+8)", output=23),
            LeetcodeTestCase(input="-(2 + 3)", output=-5),
            LeetcodeTestCase(input="1-(     -2)", output=3),
            LeetcodeTestCase(input="-(-2)+4", output=6),
        ]
        sln = Solution_224()
        for tc in testcases:
            output = sln.calculate(tc.input)
            self.assertEqual(tc.output, output)

    def test_case_242(self):
        testcases: list[LeetcodeTestCase] = [
            LeetcodeTestCase(input={"s": "anagram", "t": "nagaram"}, output=True),
            LeetcodeTestCase(input={"s": "rat", "t": "car"}, output=False),
        ]
        sln = Solution_242()
        for tc in testcases:
            output = sln.isAnagram(
                s=tc.input["s"],
                t=tc.input["t"],
            )
            self.assertEqual(tc.output, output)

    def test_case_290(self):
        testcases: list[LeetcodeTestCase] = [
            LeetcodeTestCase(
                input={"pattern": "abba", "s": "dog cat cat dog"}, output=True
            ),
            LeetcodeTestCase(
                input={"pattern": "abba", "s": "dog cat cat fish"}, output=False
            ),
            LeetcodeTestCase(
                input={"pattern": "aaaa", "s": "dog cat cat dog"}, output=False
            ),
        ]
        sln = Solution_290()
        for tc in testcases:
            output = sln.wordPattern(
                pattern=tc.input["pattern"],
                s=tc.input["s"],
            )
            self.assertEqual(tc.output, output)

    def test_case_383(self):
        testcases: list[LeetcodeTestCase] = [
            LeetcodeTestCase(input={"ransomNote": "a", "magazine": "b"}, output=False),
            LeetcodeTestCase(
                input={"ransomNote": "aa", "magazine": "ab"}, output=False
            ),
            LeetcodeTestCase(
                input={"ransomNote": "aa", "magazine": "aab"}, output=True
            ),
        ]
        sln = Solution_383()
        for tc in testcases:
            output = sln.canConstruct(
                ransomNote=tc.input["ransomNote"], magazine=tc.input["magazine"]
            )
            self.assertEqual(tc.output, output)

    def test_case_1184(self):
        testcases: list[LeetcodeTestCase] = [
            LeetcodeTestCase(
                input={"distance": [1, 2, 3, 4], "start": 0, "destination": 1}, output=1
            ),
            LeetcodeTestCase(
                input={"distance": [1, 2, 3, 4], "start": 0, "destination": 2}, output=3
            ),
            LeetcodeTestCase(
                input={"distance": [1, 2, 3, 4], "start": 0, "destination": 3}, output=4
            ),
            LeetcodeTestCase(
                input={"distance": [1, 2, 3, 4], "start": 2, "destination": 3}, output=3
            ),
        ]
        sln = Solution_1184()
        for tc in testcases:
            output = sln.distanceBetweenBusStops(
                distance=tc.input["distance"],
                start=tc.input["start"],
                destination=tc.input["destination"],
            )
            self.assertEqual(tc.output, output)

    def test_case_2374(self):
        testcases: list[LeetcodeTestCase] = [
            LeetcodeTestCase(input=[1,0,0,0,0,7,7,5], output=7),
            LeetcodeTestCase(input=[2,0,0,2], output=0),
        ]
        sln = Solution_2374()
        for tc in testcases:
            output = sln.edgeScore(tc.input)
            self.assertEqual(tc.output, output)

    def test_case_2848(self):
        testcases: list[LeetcodeTestCase] = [
            LeetcodeTestCase(input=[[3, 6], [1, 5], [4, 7]], output=7),
            LeetcodeTestCase(input=[[1, 3], [5, 8]], output=7),
        ]
        sln = Solution_2848()
        for tc in testcases:
            output = sln.numberOfPoints(tc.input)
            self.assertEqual(tc.output, output)


if __name__ == "__main__":
    unittest.main()
