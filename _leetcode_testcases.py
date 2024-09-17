import unittest
from dataclasses import dataclass

from group_anagrams_49 import Solution as Solution_49
from isomorphic_strings_205 import Solution as Solution_205
from valid_anagram_242 import Solution as Solution_242
from word_pattern_290 import Solution as Solution_290
from ransom_note_383 import Solution as Solution_383
from distance_between_bus_stops_1184 import Solution as Solution_1184
from points_that_intersect_with_cars_2848 import Solution as Solution_2848


@dataclass
class LeetcodeTestCase:
    input: any
    output: any


class Leetcode_testcases(unittest.TestCase):

    def test_case_49(self):
        testcases = [
            LeetcodeTestCase(input=["eat", "tea", "tan", "ate", "nat", "bat"], output=[["bat"],["nat","tan"],["ate","eat","tea"]]),
            LeetcodeTestCase(input=[""], output=[""]),
            LeetcodeTestCase(input=["a"], output=["a"]),
        ]
        sln = Solution_49()
        print(f"{'#'*8} runing testing of problem 49 {'#'*8}'")
        for tc in testcases:
            print(f"input: {tc.input}, expected output: {tc.output}")
            output = sln.groupAnagrams(tc.input)
            print(f"output: {output}")
            # self.assertEqual(str(tc.output), str(output))

    def test_case_205(self):
        testcases: list[LeetcodeTestCase] = [
            LeetcodeTestCase(input={"s": "egg", "t": "add"}, output=True),
            LeetcodeTestCase(input={"s": "foo", "t": "bar"}, output=False),
            LeetcodeTestCase(input={"s": "paper", "t": "title"}, output=True),
        ]
        sln = Solution_205()
        print(f"{'#'*8} runing testing of problem 205 {'#'*8}'")
        for tc in testcases:
            print(f"input: {tc.input}, expected output: {tc.output}")
            output = sln.isIsomorphic(tc.input["s"], tc.input["t"])
            print(f"output: {output}")
            self.assertEqual(tc.output, output)
        print(f"{'#'*8} ✔️  all test passed for problem 205! {'#'*8}")


    def test_case_242(self):
        testcases: list[LeetcodeTestCase] = [
            LeetcodeTestCase(input={"s": "anagram", "t": "nagaram"}, output=True),
            LeetcodeTestCase(input={"s": "rat", "t": "car"}, output=False),
        ]
        sln = Solution_242()
        for tc in testcases:
            print(f"input: {tc.input}, expected output: {tc.output}")
            output = sln.isAnagram(
                s=tc.input["s"],
                t=tc.input["t"],
            )
            print(f"output: {output}")
            self.assertEqual(tc.output, output)
            print("-" * 32)


    def test_case_290(self):
        testcases: list[LeetcodeTestCase] = [
            LeetcodeTestCase(input={"pattern": "abba", "s": "dog cat cat dog"}, output=True),
            LeetcodeTestCase(input={"pattern": "abba", "s": "dog cat cat fish"}, output=False),
            LeetcodeTestCase(input={"pattern": "aaaa", "s": "dog cat cat dog"}, output=False),
        ]
        sln = Solution_290()
        print(f"{'#'*8} runing testing of problem 290 {'#'*8}'")
        for tc in testcases:
            print(f"input: {tc.input}, expected output: {tc.output}")
            output = sln.wordPattern(
                pattern=tc.input["pattern"],
                s=tc.input["s"],
            )
            print(f"output: {output}")


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
        print(f"{'#'*8} runing testing of problem 383 {'#'*8}'")
        for tc in testcases:
            print(f"input: {tc.input}, expected output: {tc.output}")
            output = sln.canConstruct(
                ransomNote=tc.input["ransomNote"], magazine=tc.input["magazine"]
            )
            print(f"output: {output}")
            self.assertEqual(tc.output, output)
            print("-" * 32)
        print(f"{'#'*8} ✔️  all test passed for problem 383! {'#'*8}")

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
        print(f"{'#'*8} runing testing of problem 1184 {'#'*8}'")
        for tc in testcases:
            print(f"input: {tc.input}, expected output: {tc.output}")
            output = sln.distanceBetweenBusStops(
                distance=tc.input["distance"],
                start=tc.input["start"],
                destination=tc.input["destination"],
            )
            print(f"output: {output}")
            self.assertEqual(tc.output, output)
            print("-" * 32)
        print(f"{'#'*8} ✔️  all test passed for problem 1184! {'#'*8}")

    def test_case_2848(self):
        testcases: list[LeetcodeTestCase] = [
            LeetcodeTestCase(input=[[3, 6], [1, 5], [4, 7]], output=7),
            LeetcodeTestCase(input=[[1, 3], [5, 8]], output=7),
        ]
        sln = Solution_2848()
        print(f"{'#'*8} runing testing of problem 2848 {'#'*8}'")
        for tc in testcases:
            print(f"input: {tc.input}, expected output: {tc.output}")
            output = sln.numberOfPoints(tc.input)
            print(f"output: {output}")
            self.assertEqual(tc.output, output)
            print("-" * 32)
        print(f"{'#'*8} ✔️  all test passed for problem 2848! {'#'*8}")


if __name__ == "__main__":
    unittest.main()
