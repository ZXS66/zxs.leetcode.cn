import unittest
import json
from dataclasses import dataclass
from min_stack_155 import MinStack

from two_sum_1 import Solution as Solution_1
from integer_to_roman_12 import Solution as Solution_12
from roman_to_integer_13 import Solution as Solution_13
from longest_common_prefix_14 import Solution as Solution_14
from letter_combinations_of_a_phone_number_17 import Solution as Solution_17
from valid_parentheses_20 import Solution as Solution_20
from generate_parentheses_22 import Solution as Solution_22
from find_the_index_of_the_first_occurrence_in_a_string_28 import (
    Solution as Solution_28,
)
from substring_with_concatenation_of_all_words_30 import Solution as Solution_30
from combination_sum_39 import Solution as Solution_39
from trapping_rain_water_42 import Solution as Solution_42
from permutations_46 import Solution as Solution_46
from group_anagrams_49 import Solution as Solution_49
from n_queens_51 import Solution as Solution_51
from n_queens_ii_52 import Solution as Solution_52
from merge_intervals_56 import Solution as Solution_56
from insert_interval_57 import Solution as Solution_57
from length_of_last_word_58 import Solution as Solution_58
from simplify_path_71 import Solution as Solution_71
from set_matrix_zeroes_73 import Solution as Solution_73
from minimum_window_substring_76 import Solution as Solution_76
from combinations_77 import Solution as Solution_77
from word_search_79 import Solution as Solution_79
from best_time_to_buy_and_sell_stock_121 import Solution as Solution_121
from valid_palindrome_125 import Solution as Solution_125
from word_ladder_127 import Solution as Solution_127
from longest_consecutive_sequence_128 import Solution as Solution_128
from evaluate_reverse_polish_notation_150 import Solution as Solution_150
from reverse_words_in_a_string_151 import Solution as Solution_151
from majority_element_169 import Solution as Solution_169
from happy_number_202 import Solution as Solution_202
from isomorphic_strings_205 import Solution as Solution_205
from implement_trie_prefix_tree_208 import Trie
from design_add_and_search_words_data_structure_211 import WordDictionary
from contains_duplicate_ii_219 import Solution as Solution_219
from basic_calculator_224 import Solution as Solution_224
from summary_ranges_228 import Solution as Solution_228
from valid_anagram_242 import Solution as Solution_242
from game_of_life_289 import Solution as Solution_289
from word_pattern_290 import Solution as Solution_290
from ransom_note_383 import Solution as Solution_383
from is_subsequence_392 import Solution as Solution_392
from minimum_genetic_mutation_433 import Solution as Solution_433
from minimum_number_of_arrows_to_burst_balloons_452 import Solution as Solution_452
from super_egg_drop_877 import Solution as Solution_877
from distance_between_bus_stops_1184 import Solution as Solution_1184
from egg_drop_with_2_eggs_and_n_floors_1884 import Solution as Solution_1884
from time_needed_to_buy_tickets_2073 import Solution as Solution_2073
from minimum_time_to_complete_trips_2187 import Solution as Solution_2187
from maximize_number_of_subsequences_in_a_string_2207 import Solution as Solution_2207
from number_of_excellent_pairs_2354 import Solution as Solution_2354
from node_with_highest_edge_score_2374 import Solution as Solution_2374
from take_k_of_each_character_from_left_and_right_2516 import Solution as Solution_2516
from points_that_intersect_with_cars_2848 import Solution as Solution_2848
from find_the_number_of_good_pairs_ii_3164 import Solution as Solution_3164
from minimum_average_of_smallest_and_largest_elements_3194 import Solution as Solution_3194
from maximum_height_of_a_triangle_3200 import Solution as Solution_3200


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

    def test_case_12(self):
        testcases = [
            LeetcodeTestCase(input=3749, output="MMMDCCXLIX"),
            LeetcodeTestCase(input=58, output="LVIII"),
            LeetcodeTestCase(input=1994, output="MCMXCIV"),
        ]
        sln = Solution_12()
        for tc in testcases:
            output = sln.intToRoman(tc.input)
            self.assertEqual(tc.output, output)

    def test_case_13(self):
        testcases = [
            LeetcodeTestCase(input="III", output=3),
            LeetcodeTestCase(input="IV", output=4),
            LeetcodeTestCase(input="IX", output=9),
            LeetcodeTestCase(input="LV", output=55),
            LeetcodeTestCase(input="LVIII", output=58),
            LeetcodeTestCase(input="MCMXCIV", output=1994),
        ]
        sln = Solution_13()
        for tc in testcases:
            output = sln.romanToInt(tc.input)
            self.assertEqual(tc.output, output)

    def test_case_14(self):
        testcases = [
            LeetcodeTestCase(input=["flower", "flow", "flight"], output="fl"),
            LeetcodeTestCase(input=["dog", "racecar", "car"], output=""),
            LeetcodeTestCase(input=["a"], output="a"),
            LeetcodeTestCase(input=[""], output=""),
        ]
        sln = Solution_14()

    def test_case_17(self):
        testcases = [
            LeetcodeTestCase(
                input="23",
                output=[
                    "ad",
                    "ae",
                    "af",
                    "bd",
                    "be",
                    "bf",
                    "cd",
                    "ce",
                    "cf",
                ],
            ),
            LeetcodeTestCase(
                input="",
                output=[],
            ),
            LeetcodeTestCase(
                input="2",
               output=["a", "b", "c"]
            )
        ]
        sln = Solution_17()
        for tc in testcases:
            output = sln.letterCombinations(tc.input)
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

    def test_case_22(self):
        testcases = [
            LeetcodeTestCase(input=3, output=["((()))", "(()())", "(())()", "()(())", "()()()"]),
            LeetcodeTestCase(input=1, output=["()"]),
        ]
        sln = Solution_22()
        for tc in testcases:
            output = sln.generateParenthesis(tc.input)
            self.assertEqual(len(tc.output), len(output))

    def test_case_28(self):
        testcases = [
            LeetcodeTestCase(
                input={"haystack": "sadbutsad", "needle": "sad"}, output=0
            ),
            LeetcodeTestCase(
                input={"haystack": "leetcode", "needle": "leeto"}, output=-1
            ),
        ]
        sln = Solution_28()
        for tc in testcases:
            output = sln.strStr(tc.input["haystack"], tc.input["needle"])
            self.assertEqual(tc.output, output)

    def test_case_30(self):
        testcases = [
            LeetcodeTestCase(
                input={
                    "s": "barfoothefoobarman",
                    "words": ["foo", "bar"],
                },
                output=[0, 9],
            ),
            LeetcodeTestCase(
                input={
                    "s": "wordgoodgoodgoodbestword",
                    "words": ["word", "good", "best", "word"],
                },
                output=[],
            ),
            LeetcodeTestCase(
                input={
                    "s": "barfoofoobarthefoobarman",
                    "words": ["bar", "foo", "the"],
                },
                output=[6, 9, 12],
            ),
            LeetcodeTestCase(
                input={
                    "s": "wordgoodgoodgoodbestword",
                    "words": ["word", "good", "best", "good"],
                },
                output=[8],
            ),
            LeetcodeTestCase(
                input={
                    "s": "lingmindraboofooowingdingbarrwingmonkeypoundcake",
                    "words": ["fooo", "barr", "wing", "ding", "wing"],
                },
                output=[13],
            ),
        ]
        sln = Solution_30()
        for tc in testcases:
            output = sln.findSubstring(tc.input["s"], tc.input["words"])
            self.assertEqual(str(tc.output), str(output))

    def test_case_39(self):
        testcases = [
            LeetcodeTestCase(input={"candidates": [2,3,6,7], "target": 7}, output=[[2,2,3],[7]]),
            LeetcodeTestCase(input={"candidates": [2,3,5], "target": 8}, output=[[2,2,2,2],[2,3,3],[3,5]]),
            LeetcodeTestCase(input={"candidates": [2], "target": 1}, output=[])
        ]
        sln = Solution_39()
        for tc in testcases:
            output = sln.combinationSum(tc.input["candidates"], tc.input["target"])
            self.assertEqual(len(tc.output), len(output))

    def test_case_42(self):
        testcases = [
            LeetcodeTestCase(input=[0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1], output=6),
            LeetcodeTestCase(input=[4, 2, 0, 3, 2, 5], output=9),
        ]
        sln = Solution_42()
        for tc in testcases:
            output = sln.trap(tc.input)
            self.assertEqual(tc.output, output)

    def test_case_46(self):
        testcases = [
            LeetcodeTestCase(input=[1, 2, 3], output=[[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]),
            LeetcodeTestCase(input=[0,1], output=[[0,1],[1,0]]),
            LeetcodeTestCase(input=[1], output=[[1]]),
        ]
        sln = Solution_46()
        for tc in testcases:
            output = sln.permute(tc.input)
            self.assertEqual(len(tc.output), len(output))

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

    def test_case_51(self):
        testcases = [
            LeetcodeTestCase(input=1, output=[["Q"]]),
            LeetcodeTestCase(input=4, output=[[".Q..","...Q","Q...","..Q."],["..Q.","Q...","...Q",".Q.."]]),
        ]
        sln = Solution_51()
        for tc in testcases:
            output = sln.solveNQueens(tc.input)
            self.assertEqual(len(tc.output), len(output))

    def test_case_52(self):
        testcases = [
            LeetcodeTestCase(input=1, output=1),
            LeetcodeTestCase(input=4, output=2),
        ]
        sln = Solution_52()
        for tc in testcases:
            output = sln.totalNQueens(tc.input)
            self.assertEqual(tc.output, output)

    def test_case_56(self):
        testcases = [
            LeetcodeTestCase(
                input=[[1, 3], [2, 6], [8, 10], [15, 18]],
                output=[[1, 6], [8, 10], [15, 18]],
            ),
            LeetcodeTestCase(input=[[1, 4], [4, 5]], output=[[1, 5]]),
        ]
        sln = Solution_56()
        for tc in testcases:
            output = sln.merge(tc.input)
            self.assertEqual(str(tc.output), str(output))

    def test_case_57(self):
        testcases = [
            LeetcodeTestCase(
                input={"intervals": [[1, 3], [6, 9]], "newInterval": [2, 5]},
                output=[[1, 5], [6, 9]],
            ),
            LeetcodeTestCase(
                input={
                    "intervals": [[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]],
                    "newInterval": [4, 8],
                },
                output=[[1, 2], [3, 10], [12, 16]],
            ),
            LeetcodeTestCase(
                input={"intervals": [[1, 5]], "newInterval": [6, 8]},
                output=[[1, 5], [6, 8]],
            ),
            LeetcodeTestCase(
                input={"intervals": [[1, 5]], "newInterval": [0, 0]},
                output=[[0, 0], [1, 5]],
            ),
            LeetcodeTestCase(
                input={"intervals": [[3, 5], [12, 15]], "newInterval": [6, 6]},
                output=[[3, 5], [6, 6], [12, 15]],
            ),
        ]
        sln = Solution_57()
        for tc in testcases:
            output = sln.insert(tc.input["intervals"], tc.input["newInterval"])
            self.assertEqual(str(tc.output), str(output))

    def test_case_58(self):
        testcases = [
            LeetcodeTestCase(input="Hello World", output=5),
            LeetcodeTestCase(input="   fly me   to   the moon  ", output=4),
            LeetcodeTestCase(input="luffy is still joyboy", output=6),
        ]
        sln = Solution_58()
        for tc in testcases:
            output = sln.lengthOfLastWord(tc.input)
            self.assertEqual(tc.output, output)

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

    def test_case_73(self):
        testcases = [
            LeetcodeTestCase(
                input=[[1, 1, 1], [1, 0, 1], [1, 1, 1]],
                output=[[1, 0, 1], [0, 0, 0], [1, 0, 1]],
            ),
            LeetcodeTestCase(
                input=[[0, 1, 2, 0], [3, 4, 5, 2], [1, 3, 1, 5]],
                output=[[0, 0, 0, 0], [0, 4, 5, 0], [0, 3, 1, 0]],
            ),
        ]
        sln = Solution_73()
        for tc in testcases:
            sln.setZeroes(tc.input)
            self.assertEqual(str(tc.output), str(tc.input))

    def test_case_76(self):
        testcases = [
            LeetcodeTestCase(input={"s": "ADOBECODEBANC", "t": "ABC"}, output="BANC"),
            LeetcodeTestCase(input={"s": "a", "t": "a"}, output="a"),
            LeetcodeTestCase(input={"s": "a", "t": "aa"}, output=""),
        ]
        sln = Solution_76()
        for tc in testcases:
            output = sln.minWindow(tc.input["s"], tc.input["t"])
            self.assertEqual(tc.output, output)

    def test_case_77(self):
        testcases = [
            LeetcodeTestCase(input={"n":4,"k":2}, output=[
                [2,4],
                [3,4],
                [2,3],
                [1,2],
                [1,3],
                [1,4],
            ]),
            LeetcodeTestCase(input={"n":1,"k":1}, output=[[1]]),
        ]
        sln = Solution_77()
        for tc in testcases:
            output = sln.combine(tc.input["n"], tc.input["k"])
            # self.assertEqual(str(tc.output), str(output))
            self.assertEqual(len(tc.output),len(output))

    def test_case_79(self):
        testcases = [
            LeetcodeTestCase(
                input={
                    "board": [
                        ["A", "B", "C", "E"],
                        ["S", "F", "C", "S"],
                        ["A", "D", "E", "E"],
                    ],
                    "word": "ABCCED",
                },
                output=True,
            ),
            LeetcodeTestCase(
                input={"board": [["C","A","A"],["A","A","A"],["B","C","D"]], "word": "AAB"},
                output=True,
            ),
            LeetcodeTestCase(
                input={"board": [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "word": "ABCB"},
                output=False,
            ),
            LeetcodeTestCase(
                input={"board": [["A","B","C","E"],["S","F","E","S"],["A","D","E","E"]], "word": "ABCESEEEFS"},
                output=True,
            ),
        ]
        sln = Solution_79()
        for tc in testcases:
            output = sln.exist(tc.input["board"], tc.input["word"])
            self.assertEqual(tc.output, output)

    def test_case_121(self):
        testcases: list[LeetcodeTestCase] = [
            LeetcodeTestCase(input=[7, 1, 5, 3, 6, 4], output=5),
            LeetcodeTestCase(input=[7, 6, 4, 3, 1], output=0),
            LeetcodeTestCase(input=[2, 4, 1], output=2),
        ]
        sln = Solution_121()
        for tc in testcases:
            output = sln.maxProfit(tc.input)
            self.assertEqual(tc.output, output)

    def test_case_125(self):
        testcases: list[LeetcodeTestCase] = [
            LeetcodeTestCase(input="A man, a plan, a canal: Panama", output=True),
            LeetcodeTestCase(input="race a car", output=False),
            LeetcodeTestCase(input=" ", output=True),
            LeetcodeTestCase(input="0P", output=False),
        ]
        sln = Solution_125()
        for tc in testcases:
            output = sln.isPalindrome(tc.input)
            self.assertEqual(tc.output, output)

    def test_case_127(self):
        testcases: list[LeetcodeTestCase] = [
            LeetcodeTestCase(
                input={
                    "beginWord": "hit",
                    "endWord": "cog",
                    "wordList": ["hot", "dot", "dog", "lot", "log", "cog"],
                },
                output=5,
            ),
            LeetcodeTestCase(
                input={
                    "beginWord": "hit",
                    "endWord": "cog",
                    "wordList": ["hot", "dot", "dog", "lot", "log"],
                },
                output=0,
            ),
        ]
        sln = Solution_127()
        for tc in testcases:
            output = sln.ladderLength(
                tc.input["beginWord"], tc.input["endWord"], tc.input["wordList"]
            )
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

    def test_case_151(self):
        testcases = [
            LeetcodeTestCase(input="the sky is blue", output="blue is sky the"),
            LeetcodeTestCase(input="  hello world  ", output="world hello"),
            LeetcodeTestCase(input="a good   example", output="example good a"),
        ]
        sln = Solution_151()
        for tc in testcases:
            output = sln.reverseWords(tc.input)
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

    def test_case_169(self):
        testcases: list[LeetcodeTestCase] = [
            LeetcodeTestCase(input=[3, 2, 3], output=3),
            LeetcodeTestCase(input=[2, 2, 1, 1, 1, 2, 2], output=2),
        ]
        sln = Solution_169()
        for tc in testcases:
            output = sln.majorityElement(tc.input)
            self.assertEqual(tc.output, output)

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

    def test_case_208(self):
        trie = Trie()
        trie.insert("apple")
        ret1 = trie.search("apple")
        self.assertTrue(ret1)
        ret2 = trie.search("app")
        self.assertFalse(ret2)
        ret3 = trie.startsWith("app")
        self.assertTrue(ret3)
        trie.insert("app")
        ret4 = trie.search("app")
        self.assertTrue(ret4)

    def test_case_211(self):
        wordDictionary = WordDictionary()
        wordDictionary.addWord("bad")
        wordDictionary.addWord("dad")
        wordDictionary.addWord("mad")
        self.assertFalse(wordDictionary.search("pad"))
        self.assertTrue(wordDictionary.search("bad"))
        self.assertTrue(wordDictionary.search(".ad"))
        self.assertTrue(wordDictionary.search("b.."))

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

    def test_case_228(self):
        testcases: list[LeetcodeTestCase] = [
            LeetcodeTestCase(input=[0, 1, 2, 4, 5, 7], output=r'["0->2", "4->5", "7"]'),
            LeetcodeTestCase(
                input=[0, 2, 3, 4, 6, 8, 9], output='["0", "2->4", "6", "8->9"]'
            ),
        ]
        sln = Solution_228()
        for tc in testcases:
            output = sln.summaryRanges(tc.input)
            output = json.dumps(output)
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

    def test_case_289(self):
        testcases: list[LeetcodeTestCase] = [
            LeetcodeTestCase(
                input=[[0, 1, 0], [0, 0, 1], [1, 1, 1], [0, 0, 0]],
                output=[[0, 0, 0], [1, 0, 1], [0, 1, 1], [0, 1, 0]],
            ),
            LeetcodeTestCase(input=[[1, 1], [1, 0]], output=[[1, 1], [1, 1]]),
        ]
        sln = Solution_289()
        for tc in testcases:
            sln.gameOfLife(tc.input)
            self.assertEqual(str(tc.output), str(tc.input))

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

    def test_case_392(self):
        testcases: list[LeetcodeTestCase] = [
            LeetcodeTestCase(input={"s": "abc", "t": "ahbgdc"}, output=True),
            LeetcodeTestCase(input={"s": "axc", "t": "ahbgdc"}, output=False),
        ]
        sln = Solution_392()
        for tc in testcases:
            output = sln.isSubsequence(
                s=tc.input["s"],
                t=tc.input["t"],
            )
            self.assertEqual(tc.output, output)

    def test_case_433(self):
        testcases: list[LeetcodeTestCase] = [
            LeetcodeTestCase(
                input={"start": "AACCGGTT", "end": "AACCGGTA", "bank": ["AACCGGTA"]},
                output=1,
            ),
            LeetcodeTestCase(
                input={
                    "start": "AACCGGTT",
                    "end": "AAACGGTA",
                    "bank": ["AACCGGTA", "AACCGCTA", "AAACGGTA"],
                },
                output=2,
            ),
            LeetcodeTestCase(
                input={
                    "start": "AAAAACCC",
                    "end": "AACCCCCC",
                    "bank": ["AAAACCCC", "AAACCCCC", "AACCCCCC"],
                },
                output=3,
            ),
        ]
        sln = Solution_433()
        for tc in testcases:
            output = sln.minMutation(
                tc.input["start"],
                tc.input["end"],
                tc.input["bank"],
            )
            self.assertEqual(tc.output, output)

    def test_case_452(self):
        testcases: list[LeetcodeTestCase] = [
            LeetcodeTestCase(input=[[10, 16], [2, 8], [1, 6], [7, 12]], output=2),
            LeetcodeTestCase(input=[[1, 2], [3, 4], [5, 6], [7, 8]], output=4),
            LeetcodeTestCase(input=[[1, 2], [2, 3], [3, 4], [4, 5]], output=2),
        ]
        sln = Solution_452()
        for tc in testcases:
            output = sln.findMinArrowShots(points=tc.input)
            self.assertEqual(tc.output, output)

    def test_case_877(self):
        testcases: list[LeetcodeTestCase] = [
            LeetcodeTestCase(input={"k":1,"n":2}, output=2),
            LeetcodeTestCase(input={"k":2,"n":4}, output=3),
            LeetcodeTestCase(input={"k":2,"n":6}, output=3),
            LeetcodeTestCase(input={"k":3,"n":2}, output=2),
            LeetcodeTestCase(input={"k":3,"n":3}, output=2),
            LeetcodeTestCase(input={"k":3,"n":14}, output=4),
        ]
        sln = Solution_877()
        for tc in testcases:
            output = sln.superEggDrop(tc.input["k"], tc.input["n"])
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

    def test_case_1884(self):
        testcases: list[LeetcodeTestCase] = [
            LeetcodeTestCase(input=2, output=2),
            LeetcodeTestCase(input=100, output=14),
        ]
        sln = Solution_1884()
        for tc in testcases:
            output = sln.twoEggDrop(tc.input)
            self.assertEqual(tc.output, output)

    def test_case_2073(self):
        testcases: list[LeetcodeTestCase] = [
            LeetcodeTestCase(input={"tickets": [2, 3, 2], "k": 2}, output=6),
            LeetcodeTestCase(input={"tickets": [5, 1, 1, 1], "k": 0}, output=8),
        ]
        sln = Solution_2073()
        for tc in testcases:
            output = sln.timeRequiredToBuy(
                tickets=tc.input["tickets"],
                k=tc.input["k"],
            )
            self.assertEqual(tc.output, output)

    def test_case_2187(self):
        testcases: list[LeetcodeTestCase] = [
            LeetcodeTestCase(input={"time": [1, 2, 3], "totalTrips": 5}, output=3),
            LeetcodeTestCase(input={"time": [2], "totalTrips": 1}, output=2),
        ]
        sln = Solution_2187()
        for tc in testcases:
            output = sln.minimumTime(tc.input["time"], tc.input["totalTrips"])
            self.assertEqual(tc.output, output)

    def test_case_2207(self):
        testcases: list[LeetcodeTestCase] = [
            LeetcodeTestCase(input={"text": "abdcdbc", "pattern": "ac"}, output=4),
            LeetcodeTestCase(input={"text": "aabb", "pattern": "ab"}, output=6),
        ]
        sln = Solution_2207()
        for tc in testcases:
            output = sln.maximumSubsequenceCount(tc.input["text"], tc.input["pattern"])
            self.assertEqual(tc.output, output)

    def test_case_2354(self):
        testcases: list[LeetcodeTestCase] = [
            LeetcodeTestCase(input={"nums": [1, 2, 3, 1], "k": 3}, output=5),
            LeetcodeTestCase(input={"nums": [5, 1, 1], "k": 10}, output=0),
        ]
        sln = Solution_2354()
        for tc in testcases:
            output = sln.countExcellentPairs(tc.input["nums"], tc.input["k"])
            self.assertEqual(tc.output, output)

    def test_case_2374(self):
        testcases: list[LeetcodeTestCase] = [
            LeetcodeTestCase(input=[1, 0, 0, 0, 0, 7, 7, 5], output=7),
            LeetcodeTestCase(input=[2, 0, 0, 2], output=0),
        ]
        sln = Solution_2374()
        for tc in testcases:
            output = sln.edgeScore(tc.input)
            self.assertEqual(tc.output, output)

    def test_case_2516(self):
        testcases: list[LeetcodeTestCase] = [
            LeetcodeTestCase(input={"s": "aabaaaacaabc", "k": 2}, output=8),
            LeetcodeTestCase(input={"s": "a", "k": 1}, output=-1),
        ]
        sln = Solution_2516()
        for tc in testcases:
            output = sln.takeCharacters(tc.input["s"], tc.input["k"])
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

    def test_case_3164(self):
        testcases: list[LeetcodeTestCase] = [
            LeetcodeTestCase(
                input={"nums1": [1, 3, 4], "nums2": [1, 3, 4], "k": 1}, output=5
            ),
            LeetcodeTestCase(
                input={"nums1": [1, 2, 4, 12], "nums2": [2, 4], "k": 3}, output=2
            ),
        ]
        sln = Solution_3164()
        for tc in testcases:
            output = sln.numberOfPairs(
                tc.input["nums1"], tc.input["nums2"], tc.input["k"]
            )
            self.assertEqual(tc.output, output)

    def test_case_3194(self):
        testcases = [
            LeetcodeTestCase(input=[7,8,3,4,15,13,4,1], output=5.5),
            LeetcodeTestCase(input=[1,2,3,7,8,9], output=5.0),
        ]
        sln = Solution_3194()
        for tc in testcases:
            output = sln.minimumAverage(tc.input)
            self.assertEqual(tc.output, output)

    def test_case_3200(self):
        testcases: list[LeetcodeTestCase] = [
            LeetcodeTestCase(input={"red": 2, "blue": 3}, output=2),
            LeetcodeTestCase(input={"red": 2, "blue": 4}, output=3),
            LeetcodeTestCase(input={"red": 1, "blue": 2}, output=2),
            LeetcodeTestCase(input={"red": 1, "blue": 1}, output=1),
            LeetcodeTestCase(input={"red": 10, "blue": 1}, output=2),
        ]
        sln = Solution_3200()
        for tc in testcases:
            output = sln.maxHeightOfTriangle(tc.input['red'], tc.input['blue'])
            self.assertEqual(tc.output,output)


if __name__ == "__main__":
    unittest.main()
