from typing import Any, List
import unittest
from dataclasses import dataclass

from _models import ListNode, TreeNode
from _utils import build_tree_from_preorder_list
from min_stack_155 import MinStack

from two_sum_1 import Solution as Solution_1
from median_of_two_sorted_arrays_4 import Solution as Solution_4
from integer_to_roman_12 import Solution as Solution_12
from roman_to_integer_13 import Solution as Solution_13
from longest_common_prefix_14 import Solution as Solution_14
from letter_combinations_of_a_phone_number_17 import Solution as Solution_17
from valid_parentheses_20 import Solution as Solution_20
from generate_parentheses_22 import Solution as Solution_22
from merge_k_sorted_lists_23 import (
    Solution as Solution_23,
    buildListNode as buildListNode_23,
)
from find_the_index_of_the_first_occurrence_in_a_string_28 import (
    Solution as Solution_28,
)
from substring_with_concatenation_of_all_words_30 import Solution as Solution_30
from longest_valid_parentheses_32 import Solution as Solution_32
from search_in_rotated_sorted_array_33 import Solution as Solution_33
from find_first_and_last_position_of_element_in_sorted_array_34 import (
    Solution as Solution_34,
)
from search_insert_position_35 import Solution as Solution_35
from combination_sum_39 import Solution as Solution_39
from first_missing_positive_41 import Solution as Solution_41
from trapping_rain_water_42 import Solution as Solution_42
from permutations_46 import Solution as Solution_46
from group_anagrams_49 import Solution as Solution_49
from n_queens_51 import Solution as Solution_51
from n_queens_ii_52 import Solution as Solution_52
from maximum_subarray_53 import Solution as Solution_53
from merge_intervals_56 import Solution as Solution_56
from insert_interval_57 import Solution as Solution_57
from length_of_last_word_58 import Solution as Solution_58
from simplify_path_71 import Solution as Solution_71
from set_matrix_zeroes_73 import Solution as Solution_73
from search_a_2d_matrix_74 import Solution as Solution_74
from sort_colors_75 import Solution as Solution_75
from minimum_window_substring_76 import Solution as Solution_76
from combinations_77 import Solution as Solution_77
from subsets_78 import Solution as Solution_78
from word_search_79 import Solution as Solution_79
from largest_rectangle_in_histogram_84 import Solution as Solution_84
from convert_sorted_array_to_binary_search_tree_108 import Solution as Solution_108
from best_time_to_buy_and_sell_stock_121 import Solution as Solution_121
from valid_palindrome_125 import Solution as Solution_125
from word_ladder_127 import Solution as Solution_127
from longest_consecutive_sequence_128 import Solution as Solution_128
from binary_tree_preorder_traversal_144 import Solution as Solution_144
from sort_list_148 import Solution as Solution_148, buildListNode_148
from evaluate_reverse_polish_notation_150 import Solution as Solution_150
from reverse_words_in_a_string_151 import Solution as Solution_151
from maximum_product_subarray_152 import Solution as Solution_152
from find_minimum_in_rotated_sorted_array_153 import Solution as Solution_153
from find_peak_element_162 import Solution as Solution_162
from majority_element_169 import Solution as Solution_169
from happy_number_202 import Solution as Solution_202
from isomorphic_strings_205 import Solution as Solution_205
from implement_trie_prefix_tree_208 import Trie
from design_add_and_search_words_data_structure_211 import WordDictionary
from word_search_ii_212 import Solution as Solution_212
from kth_largest_element_in_an_array_215 import Solution as Solution_215
from contains_duplicate_ii_219 import Solution as Solution_219
from basic_calculator_224 import Solution as Solution_224
from summary_ranges_228 import Solution as Solution_228
from valid_anagram_242 import Solution as Solution_242
from perfect_squares_279 import Solution as Solution_279
from game_of_life_289 import Solution as Solution_289
from word_pattern_290 import Solution as Solution_290
from range_sum_query_immutable_303 import NumArray
from ransom_note_383 import Solution as Solution_383
from is_subsequence_392 import Solution as Solution_392
from decode_string_394 import Solution as Solution_394
from partition_equal_subset_sum_416 import Solution as Solution_416
from construct_quad_tree_427 import Solution as Solution_427
from minimum_genetic_mutation_433 import Solution as Solution_433
from minimum_number_of_arrows_to_burst_balloons_452 import Solution as Solution_452
from subarray_sum_equals_k_560 import Solution as Solution_560
from longest_harmonious_subsequence_594 import Solution as Solution_594
from daily_temperatures_739 import Solution as Solution_739
from open_the_lock_752 import Solution as Solution_752
from partition_labels_763 import Solution as Solution_763
from super_egg_drop_877 import Solution as Solution_877
from smallest_range_i_908 import Solution as Solution_908
from smallest_range_ii_910 import Solution as Solution_910
from maximum_sum_circular_subarray_918 import Solution as Solution_918
from rotting_oranges_994 import Solution as Solution_994
from longest_common_subsequence_1143 import Solution as Solution_1143
from distance_between_bus_stops_1184 import Solution as Solution_1184
from find_lucky_integer_in_an_array_1394 import Solution as Solution_1394
from egg_drop_with_2_eggs_and_n_floors_1884 import Solution as Solution_1884
from time_needed_to_buy_tickets_2073 import Solution as Solution_2073
from kth_smallest_product_of_two_sorted_arrays_2040 import Solution as Solution_2040
from find_subsequence_of_length_k_with_the_largest_sum_2099 import (
    Solution as Solution_2099,
)
from minimum_time_to_complete_trips_2187 import Solution as Solution_2187
from maximize_number_of_subsequences_in_a_string_2207 import Solution as Solution_2207
from find_all_k_distant_indices_in_an_array_2200 import Solution as Solution_2200
from number_of_excellent_pairs_2354 import Solution as Solution_2354
from node_with_highest_edge_score_2374 import Solution as Solution_2374
from maximum_matching_of_players_with_trainers_2410 import Solution as Solution_2410
from take_k_of_each_character_from_left_and_right_2516 import Solution as Solution_2516
from points_that_intersect_with_cars_2848 import Solution as Solution_2848
from minimum_deletions_to_make_string_k_special_3085 import Solution as Solution_3085
from find_the_number_of_good_pairs_ii_3164 import Solution as Solution_3164
from count_days_without_meetings_3169 import Solution as Solution_3169
from count_pairs_that_form_a_complete_day_i_3184 import Solution as Solution_3184
from minimum_operations_to_make_binary_array_elements_equal_to_one_3191 import (
    Solution as Solution_3191,
)
from minimum_operations_to_make_binary_array_elements_equal_to_one_ii_3192 import (
    Solution as Solution_3192,
)
from minimum_average_of_smallest_and_largest_elements_3194 import (
    Solution as Solution_3194,
)
from maximum_height_of_a_triangle_3200 import Solution as Solution_3200
from find_the_k_th_character_in_string_game_i_3304 import Solution as Solution_3304
from find_the_k_th_character_in_string_game_ii_3307 import Solution as Solution_3307
from reschedule_meetings_for_maximum_free_time_ii_3440 import Solution as Solution_3440


from sudoku_hj44 import Solution as Solution_hj44
from max_common_substr_hj75 import Solution as Solution_hj75
from max_bits_hj86 import Solution as Solution_hj86


@dataclass
class LeetcodeTestCase:
    input: Any
    output: Any


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

    def test_case_4(self):
        testcases = [
            LeetcodeTestCase(input={"nums1": [1, 3], "nums2": [2]}, output=2.0),
            LeetcodeTestCase(input={"nums1": [1, 2], "nums2": [3, 4]}, output=2.5),
            LeetcodeTestCase(input={"nums1": [], "nums2": [3, 4]}, output=3.5),
            LeetcodeTestCase(input={"nums1": [2], "nums2": []}, output=2.0),
        ]
        sln = Solution_4()
        for tc in testcases:
            output = sln.findMedianSortedArrays(tc.input["nums1"], tc.input["nums2"])
            self.assertEqual(tc.output, output)

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
            LeetcodeTestCase(input="2", output=["a", "b", "c"]),
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
            LeetcodeTestCase(
                input=3, output=["((()))", "(()())", "(())()", "()(())", "()()()"]
            ),
            LeetcodeTestCase(input=1, output=["()"]),
        ]
        sln = Solution_22()
        for tc in testcases:
            output = sln.generateParenthesis(tc.input)
            self.assertEqual(len(tc.output), len(output))

    def test_case_23(self):
        testcases = [
            LeetcodeTestCase(
                input=[[1, 4, 5], [1, 3, 4], [2, 6]], output=[1, 1, 2, 3, 4, 4, 5, 6]
            ),
            LeetcodeTestCase(input=[], output=[]),
            LeetcodeTestCase(input=[[]], output=[]),
            LeetcodeTestCase(input=[[], []], output=[]),
            LeetcodeTestCase(input=[[], [1]], output=[1]),
        ]
        sln = Solution_23()
        for tc in testcases:
            lists: List = [buildListNode_23(input) for input in tc.input]
            output = sln.mergeKLists(lists)
            if tc.output:
                self.assertIsNotNone(output)
            else:
                self.assertIsNone(output)

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

    def test_case_32(self):
        testcases = [
            LeetcodeTestCase(input="(()", output=2),
            LeetcodeTestCase(input=")()())", output=4),
            LeetcodeTestCase(input="", output=0),
        ]
        sln = Solution_32()
        for tc in testcases:
            output = sln.longestValidParentheses(tc.input)
            self.assertEqual(tc.output, output)

    def test_case_33(self):
        testcases = [
            LeetcodeTestCase(
                input={"nums": [4, 5, 6, 7, 0, 1, 2], "target": 0}, output=4
            ),
            LeetcodeTestCase(
                input={"nums": [4, 5, 6, 7, 0, 1, 2], "target": 3}, output=-1
            ),
            LeetcodeTestCase(input={"nums": [1], "target": 0}, output=-1),
        ]
        sln = Solution_33()
        for tc in testcases:
            output = sln.search(tc.input["nums"], tc.input["target"])
            self.assertEqual(tc.output, output)

    def test_case_34(self):
        testcases = [
            LeetcodeTestCase(
                input={"nums": [5, 7, 7, 8, 8, 10], "target": 8}, output=[3, 4]
            ),
            LeetcodeTestCase(
                input={"nums": [5, 7, 7, 8, 8, 10], "target": 6}, output=[-1, -1]
            ),
            LeetcodeTestCase(input={"nums": [], "target": 0}, output=[-1, -1]),
        ]
        sln = Solution_34()
        for tc in testcases:
            output = sln.searchRange(tc.input["nums"], tc.input["target"])
            self.assertListEqual(tc.output, output)

    def test_case_35(self):
        testcases = [
            LeetcodeTestCase(input={"nums": [1, 3, 5, 6], "target": 5}, output=2),
            LeetcodeTestCase(input={"nums": [1, 3, 5, 6], "target": 2}, output=1),
            LeetcodeTestCase(input={"nums": [1, 3, 5, 6], "target": 7}, output=4),
        ]
        sln = Solution_35()
        for tc in testcases:
            output = sln.searchInsert(tc.input["nums"], tc.input["target"])
            self.assertEqual(tc.output, output)

    def test_case_39(self):
        testcases = [
            LeetcodeTestCase(
                input={"candidates": [2, 3, 6, 7], "target": 7}, output=[[2, 2, 3], [7]]
            ),
            LeetcodeTestCase(
                input={"candidates": [2, 3, 5], "target": 8},
                output=[[2, 2, 2, 2], [2, 3, 3], [3, 5]],
            ),
            LeetcodeTestCase(input={"candidates": [2], "target": 1}, output=[]),
        ]
        sln = Solution_39()
        for tc in testcases:
            output = sln.combinationSum(tc.input["candidates"], tc.input["target"])
            self.assertEqual(len(tc.output), len(output))

    def test_case_41(self):
        testcases = [
            LeetcodeTestCase(input=[1, 2, 0], output=3),
            LeetcodeTestCase(input=[3, 4, -1, 1], output=2),
            LeetcodeTestCase(input=[7, 8, 9, 11, 12], output=1),
            LeetcodeTestCase(input=[2, 2], output=1),
        ]
        sln = Solution_41()
        for tc in testcases:
            output = sln.firstMissingPositive(tc.input)
            self.assertEqual(tc.output, output)

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
            LeetcodeTestCase(
                input=[1, 2, 3],
                output=[
                    [1, 2, 3],
                    [1, 3, 2],
                    [2, 1, 3],
                    [2, 3, 1],
                    [3, 1, 2],
                    [3, 2, 1],
                ],
            ),
            LeetcodeTestCase(input=[0, 1], output=[[0, 1], [1, 0]]),
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
            LeetcodeTestCase(
                input=4,
                output=[
                    [".Q..", "...Q", "Q...", "..Q."],
                    ["..Q.", "Q...", "...Q", ".Q.."],
                ],
            ),
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

    def test_case_53(self):
        testcases = [
            LeetcodeTestCase(input=[-2, 1, -3, 4, -1, 2, 1, -5, 4], output=6),
            LeetcodeTestCase(input=[1], output=1),
            LeetcodeTestCase(input=[5, 4, -1, 7, 8], output=23),
        ]
        sln = Solution_53()
        for tc in testcases:
            output = sln.maxSubArray(tc.input)
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

    def test_case_74(self):
        testcases = [
            LeetcodeTestCase(
                input={
                    "matrix": [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]],
                    "target": 3,
                },
                output=True,
            ),
            LeetcodeTestCase(
                input={
                    "matrix": [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]],
                    "target": 13,
                },
                output=False,
            ),
        ]
        sln = Solution_74()
        for tc in testcases:
            output = sln.searchMatrix(tc.input["matrix"], tc.input["target"])
            self.assertEqual(tc.output, output)

    def test_case_75(self):
        testcases = [
            LeetcodeTestCase(input=[2, 0, 2, 1, 1, 0], output=[0, 0, 1, 1, 2, 2]),
            LeetcodeTestCase(input=[2, 0, 1], output=[0, 1, 2]),
            LeetcodeTestCase(input=[0], output=[0]),
            LeetcodeTestCase(input=[1], output=[1]),
        ]
        sln = Solution_75()
        for tc in testcases:
            sln.sortColors(tc.input)
            self.assertEqual(str(tc.output), str(tc.input))
            self.assertAlmostEqual(tc.output, tc.input)

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
            LeetcodeTestCase(
                input={"n": 4, "k": 2},
                output=[
                    [2, 4],
                    [3, 4],
                    [2, 3],
                    [1, 2],
                    [1, 3],
                    [1, 4],
                ],
            ),
            LeetcodeTestCase(input={"n": 1, "k": 1}, output=[[1]]),
        ]
        sln = Solution_77()
        for tc in testcases:
            output = sln.combine(tc.input["n"], tc.input["k"])
            # self.assertEqual(str(tc.output), str(output))
            self.assertEqual(len(tc.output), len(output))

    def test_case_78(self):
        testcases = [
            LeetcodeTestCase(
                input=[1, 2, 3],
                output=[[], [1], [2], [3], [1, 2], [1, 3], [2, 3], [1, 2, 3]],
            ),
            LeetcodeTestCase(input=[0], output=[[], [0]]),
        ]
        sln = Solution_78()
        for tc in testcases:
            output = sln.subsets(tc.input)
            # self.assertAlmostEqual(tc.output, output)
            self.assertEqual(len(tc.output), len(output))

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
                input={
                    "board": [["C", "A", "A"], ["A", "A", "A"], ["B", "C", "D"]],
                    "word": "AAB",
                },
                output=True,
            ),
            LeetcodeTestCase(
                input={
                    "board": [
                        ["A", "B", "C", "E"],
                        ["S", "F", "C", "S"],
                        ["A", "D", "E", "E"],
                    ],
                    "word": "ABCB",
                },
                output=False,
            ),
            LeetcodeTestCase(
                input={
                    "board": [
                        ["A", "B", "C", "E"],
                        ["S", "F", "E", "S"],
                        ["A", "D", "E", "E"],
                    ],
                    "word": "ABCESEEEFS",
                },
                output=True,
            ),
        ]
        sln = Solution_79()
        for tc in testcases:
            output = sln.exist(tc.input["board"], tc.input["word"])
            self.assertEqual(tc.output, output)

    def test_case_84(self):
        testcases = [
            LeetcodeTestCase(input=[2, 1, 5, 6, 2, 3], output=10),
            LeetcodeTestCase(input=[2, 4], output=4),
            LeetcodeTestCase(input=[0], output=0),
            LeetcodeTestCase(input=[1, 2, 3, 4], output=6),
        ]
        sln = Solution_84()
        for tc in testcases:
            output = sln.largestRectangleArea(tc.input)
            self.assertEqual(tc.output, output)

    def test_case_108(self):
        testcases = [
            LeetcodeTestCase(input=[-10, -3, 0, 5, 9], output=3),
            LeetcodeTestCase(input=[1, 3], output=2),
        ]
        sln = Solution_108()
        for tc in testcases:
            output = sln.sortedArrayToBST(tc.input)
            self.assertIsNotNone(output)

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

    def test_case_144(self):
        testcases: list[LeetcodeTestCase] = [
            LeetcodeTestCase(input=[1, None, 2, None, None, 3], output=[1, 2, 3]),
            LeetcodeTestCase(
                input=[1, 2, 3, 4, 5, None, 8, None, None, 6, 7, None, None, 9],
                output=[1, 2, 4, 5, 6, 7, 3, 8, 9],
            ),
            LeetcodeTestCase(input=[], output=[]),
            LeetcodeTestCase(input=[1], output=[1]),
        ]
        sln = Solution_144()
        for tc in testcases:
            root = build_tree_from_preorder_list(tc.input)
            output = sln.preorderTraversal(root)
            self.assertEqual(tc.output, output)

    def test_case_148(self):
        testcases = [
            LeetcodeTestCase(
                input=[4, 2, 1, 3],
                output=[1, 2, 3, 4],
            ),
            LeetcodeTestCase(
                input=[0, -1],
                output=[-1, 0],
            ),
            LeetcodeTestCase(
                input=[-1, 5, 3, 4, 0],
                output=[-1, 0, 3, 4, 5],
            ),
        ]
        sln = Solution_148()
        for tc in testcases:
            input = buildListNode_148(tc.input)
            output = sln.sortList(input)
            self.assertIsNotNone(output)
            if output is not None and output.next is not None:
                self.assertLess(output.val, output.next.val)

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

    def test_case_152(self):
        testcases: list[LeetcodeTestCase] = [
            LeetcodeTestCase(input=[2, 3, -2, 4], output=6),
            LeetcodeTestCase(input=[-2, 0, -1], output=0),
            LeetcodeTestCase(input=[-2, 3, -4], output=24),
            LeetcodeTestCase(input=[-1, -2, -9, -6], output=108),
            LeetcodeTestCase(input=[3, -1, 4], output=4),
            LeetcodeTestCase(input=[2, -5, -2, -4, 3], output=24),
        ]
        sln = Solution_152()
        for tc in testcases:
            output = sln.maxProduct(tc.input)
            self.assertEqual(tc.output, output)

    def test_case_153(self):
        testcases: list[LeetcodeTestCase] = [
            LeetcodeTestCase(input=[3, 4, 5, 1, 2], output=1),
            LeetcodeTestCase(input=[4, 5, 6, 7, 0, 1, 2], output=0),
            LeetcodeTestCase(input=[11, 13, 15, 17], output=11),
        ]
        sln = Solution_153()
        for tc in testcases:
            output = sln.findMin(tc.input)
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

    def test_case_162(self):
        testcases: list[LeetcodeTestCase] = [
            LeetcodeTestCase(input=[1, 2, 3, 1], output=2),
            LeetcodeTestCase(input=[1, 2, 1, 3, 5, 6, 4], output=5),  # output=1 or 5
            LeetcodeTestCase(input=[1, 2, 3, 4, 5, 6, 7, 8, 9], output=8),
            LeetcodeTestCase(input=[1, 3, 2, 1], output=1),
        ]
        sln = Solution_162()
        for tc in testcases:
            output = sln.findPeakElement(tc.input)
            self.assertEqual(tc.output, output)

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

    def test_case_212(self):
        testcases: list[LeetcodeTestCase] = [
            LeetcodeTestCase(
                input={
                    "words": ["oath", "pea", "eat", "rain"],
                    "board": [
                        ["o", "a", "a", "n"],
                        ["e", "t", "a", "e"],
                        ["i", "h", "k", "r"],
                        ["i", "f", "l", "v"],
                    ],
                },
                output=["oath", "eat"],
            ),
            LeetcodeTestCase(
                input={"words": ["abcb"], "board": [["a", "b"], ["c", "d"]]},
                output=[],
            ),
            LeetcodeTestCase(
                input={
                    "words": ["oa", "oaa"],
                    "board": [
                        ["o", "a", "b", "n"],
                        ["o", "t", "a", "e"],
                        ["a", "h", "k", "r"],
                        ["a", "f", "l", "v"],
                    ],
                },
                output=["oa", "oaa"],
            ),
            LeetcodeTestCase(
                input={"words": ["aaa"], "board": [["a", "a"]]}, output=[]
            ),
            LeetcodeTestCase(
                input={
                    "words": [
                        "ab",
                        "cb",
                        "ad",
                        "bd",
                        "ac",
                        "ca",
                        "da",
                        "bc",
                        "db",
                        "adcb",
                        "dabc",
                        "abb",
                        "acb",
                    ],
                    "board": [["a", "b"], ["c", "d"]],
                },
                output=["ab", "ac", "bd", "ca", "db"],
            ),
            LeetcodeTestCase(
                input={
                    "words": ["aba", "baa", "bab", "aaab", "aaa", "aaaa", "aaba"],
                    "board": [["a", "b"], ["a", "a"]],
                },
                output=["aba", "aaa", "aaab", "baa", "aaba"],
            ),
        ]
        sln = Solution_212()
        for tc in testcases:
            output = sln.findWords(
                board=tc.input["board"],
                words=tc.input["words"],
            )
            self.assertEqual(len(tc.output), len(output))

    def test_case_215(self):
        testcases: list[LeetcodeTestCase] = [
            LeetcodeTestCase(input={"nums": [3, 2, 1, 5, 6, 4], "k": 2}, output=5),
            LeetcodeTestCase(
                input={"nums": [3, 2, 3, 1, 2, 4, 5, 5, 6], "k": 4}, output=4
            ),
        ]
        sln = Solution_215()
        for tc in testcases:
            output = sln.findKthLargest(
                nums=tc.input["nums"],
                k=tc.input["k"],
            )
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

    def test_case_228(self):
        testcases: list[LeetcodeTestCase] = [
            LeetcodeTestCase(input=[0, 1, 2, 4, 5, 7], output=["0->2", "4->5", "7"]),
            LeetcodeTestCase(
                input=[0, 2, 3, 4, 6, 8, 9], output=["0", "2->4", "6", "8->9"]
            ),
        ]
        sln = Solution_228()
        for tc in testcases:
            output = sln.summaryRanges(tc.input)
            self.assertAlmostEqual(tc.output, output)

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

    def test_case_279(self):
        testcases: list[LeetcodeTestCase] = [
            LeetcodeTestCase(input=12, output=3),
            LeetcodeTestCase(input=13, output=2),
            LeetcodeTestCase(input=16, output=1),
            LeetcodeTestCase(input=17, output=2),
        ]
        sln = Solution_279()
        for tc in testcases:
            output = sln.numSquares(tc.input)
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

    def test_case_303(self):
        nArray = NumArray([-2, 0, 3, -5, 2, -1])
        self.assertEqual(nArray.sumRange(0, 2), 1)  # sum of nums[0..2] = -2 + 0 + 3 = 1
        self.assertEqual(
            nArray.sumRange(2, 5), -1
        )  # sum of nums[2..5] = 3 + -5 + 2 + -1
        self.assertEqual(
            nArray.sumRange(0, 5), -3
        )  # sum of nums[0..5] = -2 + 0 + 3 + -5 + 2 + -1 = -3

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

    def test_case_394(self):
        testcases: list[LeetcodeTestCase] = [
            LeetcodeTestCase(input="3[a]2[bc]", output="aaabcbc"),
            LeetcodeTestCase(input="3[a2[c]]", output="accaccacc"),
            LeetcodeTestCase(input="2[abc]3[cd]ef", output="abcabccdcdcdef"),
            LeetcodeTestCase(input="abc3[cd]xyz", output="abccdcdcdxyz"),
        ]
        sln = Solution_394()
        for tc in testcases:
            output = sln.decodeString(tc.input)
            self.assertEqual(tc.output, output)

    def test_case_416(self):
        testcases: list[LeetcodeTestCase] = [
            LeetcodeTestCase(input=[1, 5, 11, 5], output=True),
            LeetcodeTestCase(input=[1, 2, 3, 5], output=False),
            LeetcodeTestCase(input=[2, 2, 3, 5], output=False),
        ]
        sln = Solution_416()
        for tc in testcases:
            output = sln.canPartition(tc.input)
            self.assertEqual(tc.output, output)

    def test_case_427(self):
        testcases: list[LeetcodeTestCase] = [
            LeetcodeTestCase(
                input=[[0, 1], [1, 0]], output=[[0, 1], [1, 0], [1, 1], [1, 1], [1, 0]]
            ),
            LeetcodeTestCase(
                input=[
                    [1, 1, 1, 1, 0, 0, 0, 0],
                    [1, 1, 1, 1, 0, 0, 0, 0],
                    [1, 1, 1, 1, 1, 1, 1, 1],
                    [1, 1, 1, 1, 1, 1, 1, 1],
                    [1, 1, 1, 1, 0, 0, 0, 0],
                    [1, 1, 1, 1, 0, 0, 0, 0],
                    [1, 1, 1, 1, 0, 0, 0, 0],
                    [1, 1, 1, 1, 0, 0, 0, 0],
                ],
                output=[
                    [0, 1],
                    [1, 1],
                    [0, 1],
                    [1, 1],
                    [1, 0],
                    None,
                    None,
                    None,
                    None,
                    [1, 0],
                    [1, 0],
                    [1, 1],
                    [1, 1],
                ],
            ),
        ]
        sln = Solution_427()
        for tc in testcases:
            output = sln.construct(tc.input)
            self.assertIsNotNone(output)

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

    def test_case_560(self):
        testcases: list[LeetcodeTestCase] = [
            LeetcodeTestCase(input={"nums": [1, 1, 1], "k": 2}, output=2),
            LeetcodeTestCase(input={"nums": [1, 2, 3], "k": 3}, output=2),
        ]
        sln = Solution_560()
        for tc in testcases:
            output = sln.subarraySum(tc.input["nums"], tc.input["k"])
            self.assertEqual(tc.output, output)

    def test_case_594(self):
        testcases: list[LeetcodeTestCase] = [
            LeetcodeTestCase(input={"nums": [1, 3, 2, 2, 5, 2, 3, 7]}, output=5),
            LeetcodeTestCase(input={"nums": [1, 2, 3, 4]}, output=2),
            LeetcodeTestCase(input={"nums": [1, 1, 1, 1]}, output=0),
        ]
        sln = Solution_594()
        for tc in testcases:
            output = sln.findLHS(tc.input["nums"])
            self.assertEqual(tc.output, output)

    def test_case_739(self):
        testcases: list[LeetcodeTestCase] = [
            LeetcodeTestCase(
                input=[73, 74, 75, 71, 69, 72, 76, 73], output=[1, 1, 4, 2, 1, 1, 0, 0]
            ),
            LeetcodeTestCase(input=[30, 40, 50, 60], output=[1, 1, 1, 0]),
            LeetcodeTestCase(input=[30, 60, 90], output=[1, 1, 0]),
        ]
        sln = Solution_739()
        for tc in testcases:
            output = sln.dailyTemperatures(tc.input)
            self.assertAlmostEqual(tc.output, output)

    def test_case_752(self):
        testcases: List[LeetcodeTestCase] = [
            LeetcodeTestCase(
                input={
                    "deadends": ["0201", "0101", "0102", "1212", "2002"],
                    "target": "0202",
                },
                output=6,
            ),
            LeetcodeTestCase(input={"deadends": ["8888"], "target": "0009"}, output=1),
            LeetcodeTestCase(
                input={
                    "deadends": [
                        "8887",
                        "8889",
                        "8878",
                        "8898",
                        "8788",
                        "8988",
                        "7888",
                        "9888",
                    ],
                    "target": "8888",
                },
                output=-1,
            ),
        ]
        sln = Solution_752()
        for tc in testcases:
            output = sln.openLock(tc.input["deadends"], tc.input["target"])
            self.assertEqual(tc.output, output)

    def test_case_763(self):
        testcases: list[LeetcodeTestCase] = [
            LeetcodeTestCase(input="ababcbacadefegdehijhklij", output=[9, 7, 8]),
            LeetcodeTestCase(input="eccbbbbdec", output=[10]),
            LeetcodeTestCase(input="a", output=[1]),
        ]
        sln = Solution_763()
        for tc in testcases:
            output = sln.partitionLabels(tc.input)
            self.assertEqual(tc.output, output)

    def test_case_877(self):
        testcases: list[LeetcodeTestCase] = [
            LeetcodeTestCase(input={"k": 1, "n": 2}, output=2),
            LeetcodeTestCase(input={"k": 2, "n": 4}, output=3),
            LeetcodeTestCase(input={"k": 2, "n": 6}, output=3),
            LeetcodeTestCase(input={"k": 3, "n": 2}, output=2),
            LeetcodeTestCase(input={"k": 3, "n": 3}, output=2),
            LeetcodeTestCase(input={"k": 3, "n": 14}, output=4),
        ]
        sln = Solution_877()
        for tc in testcases:
            output = sln.superEggDrop(tc.input["k"], tc.input["n"])
            self.assertEqual(tc.output, output)

    def test_case_908(self):
        testcases: list[LeetcodeTestCase] = [
            LeetcodeTestCase(input={"nums": [1], "k": 0}, output=0),
            LeetcodeTestCase(input={"nums": [0, 10], "k": 2}, output=6),
            LeetcodeTestCase(input={"nums": [1, 3, 6], "k": 3}, output=0),
        ]
        sln = Solution_908()
        for tc in testcases:
            output = sln.smallestRangeI(tc.input["nums"], tc.input["k"])
            self.assertEqual(tc.output, output)

    def test_case_910(self):
        testcases: list[LeetcodeTestCase] = [
            LeetcodeTestCase(input={"nums": [1], "k": 0}, output=0),
            LeetcodeTestCase(input={"nums": [0, 10], "k": 2}, output=6),
            LeetcodeTestCase(input={"nums": [1, 3, 6], "k": 3}, output=3),
            LeetcodeTestCase(input={"nums": [7, 8, 8], "k": 5}, output=1),
            LeetcodeTestCase(input={"nums": [3, 4, 7, 0], "k": 5}, output=7),
        ]
        sln = Solution_910()
        for tc in testcases:
            output = sln.smallestRangeII(tc.input["nums"], tc.input["k"])
            self.assertEqual(tc.output, output)

    def test_case_918(self):
        testcases: list[LeetcodeTestCase] = [
            LeetcodeTestCase(input=[1, -2, 3, -2], output=3),
            LeetcodeTestCase(input=[5, -3, 5], output=10),
            LeetcodeTestCase(input=[4, -2, -3, 1], output=5),
            LeetcodeTestCase(input=[3, -2, 2, -3], output=3),
        ]
        sln = Solution_918()
        for tc in testcases:
            output = sln.maxSubarraySumCircular(tc.input)
            self.assertEqual(tc.output, output)

    def test_case_994(self):
        testcases: list[LeetcodeTestCase] = [
            LeetcodeTestCase(
                input={"grid": [[2, 1, 1], [1, 1, 0], [0, 1, 1]]}, output=4
            ),
            LeetcodeTestCase(input={"grid": [[0, 2]]}, output=0),
            LeetcodeTestCase(input={"grid": [[1]]}, output=-1),
            LeetcodeTestCase(
                input={"grid": [[2, 1, 1], [0, 1, 1], [1, 0, 1]]}, output=-1
            ),
        ]
        sln = Solution_994()
        for tc in testcases:
            output = sln.orangesRotting(tc.input["grid"])
            self.assertEqual(tc.output, output)

    def test_case_1143(self):
        testcases: list[LeetcodeTestCase] = [
            LeetcodeTestCase(input={"text1": "abcde", "text2": "ace"}, output=3),
            LeetcodeTestCase(input={"text1": "abc", "text2": "abc"}, output=3),
            LeetcodeTestCase(input={"text1": "abc", "text2": "def"}, output=0),
        ]
        sln = Solution_1143()
        for tc in testcases:
            output = sln.longestCommonSubsequence(
                text1=tc.input["text1"], text2=tc.input["text2"]
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

    def test_case_1394(self):
        testcases: list[LeetcodeTestCase] = [
            LeetcodeTestCase(input=[2, 2, 3, 4], output=2),
            LeetcodeTestCase(input=[1, 2, 2, 3, 3, 3], output=3),
            LeetcodeTestCase(input=[2, 2, 2, 3, 3], output=-1),
            LeetcodeTestCase(input=[5], output=-1),
            LeetcodeTestCase(input=[7, 7, 7, 7, 7, 7, 7], output=7),
        ]
        sln = Solution_1394()
        for tc in testcases:
            output = sln.findLucky(tc.input)
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

    def test_case_2040(self):
        testcases: list[LeetcodeTestCase] = [
            LeetcodeTestCase(
                input={"nums1": [2, 5], "nums2": [3, 4], "k": 2}, output=8
            ),
            LeetcodeTestCase(
                input={"nums1": [-4, -2, 0, 3], "nums2": [2, 4], "k": 6}, output=0
            ),
            LeetcodeTestCase(
                input={"nums1": [-2, -1, 0, 1, 2], "nums2": [-3, -1, 2, 4, 5], "k": 3},
                output=-6,
            ),
        ]
        sln = Solution_2040()
        for tc in testcases:
            output = sln.kthSmallestProduct(
                tc.input["nums1"],
                tc.input["nums2"],
                tc.input["k"],
            )
            self.assertEqual(tc.output, output)

    def test_case_2099(self):
        testcases: list[LeetcodeTestCase] = [
            LeetcodeTestCase(input={"nums": [2, 1, 3, 3], "k": 2}, output=[3, 3]),
            LeetcodeTestCase(input={"nums": [-1, -2, 3, 4], "k": 3}, output=[-1, 3, 4]),
            LeetcodeTestCase(input={"nums": [3, 4, 3, 3], "k": 2}, output=[3, 4]),
        ]
        sln = Solution_2099()
        for tc in testcases:
            output = sln.maxSubsequence(
                tc.input["nums"],
                tc.input["k"],
            )
            self.assertAlmostEqual(tc.output, output)

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

    def test_case_2200(self):
        testcases: list[LeetcodeTestCase] = [
            LeetcodeTestCase(
                input={"nums": [3, 4, 9, 1, 3, 9, 5], "key": 9, "k": 1},
                output=[1, 2, 3, 4, 5, 6],
            ),
            LeetcodeTestCase(
                input={"nums": [2, 2, 2, 2, 2], "key": 2, "k": 2},
                output=[0, 1, 2, 3, 4],
            ),
        ]
        sln = Solution_2200()
        for tc in testcases:
            output = sln.findKDistantIndices(
                tc.input["nums"], tc.input["key"], tc.input["k"]
            )
            self.assertEqual(str(tc.output), str(output))

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

    def test_case_2410(self):
        testcases: list[LeetcodeTestCase] = [
            LeetcodeTestCase(
                input={"players": [4, 7, 9], "trainers": [8, 2, 5, 8]}, output=2
            ),
            LeetcodeTestCase(input={"players": [1, 1, 1], "trainers": [10]}, output=1),
            LeetcodeTestCase(
                input={"players": [1, 2, 3], "trainers": [1, 2, 3]}, output=3
            ),
        ]
        sln = Solution_2410()
        for tc in testcases:
            output = sln.matchPlayersAndTrainers(
                tc.input["players"], tc.input["trainers"]
            )
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

    def test_case_3085(self):
        testcases: list[LeetcodeTestCase] = [
            LeetcodeTestCase(input={"word": "aabcaba", "k": 0}, output=3),
            LeetcodeTestCase(input={"word": "dabdcbdcdcd", "k": 2}, output=2),
            LeetcodeTestCase(input={"word": "aaabaaa", "k": 2}, output=1),
        ]
        sln = Solution_3085()
        for tc in testcases:
            output = sln.minimumDeletions(tc.input["word"], tc.input["k"])
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

    def test_case_3169(self):
        testcases: list[LeetcodeTestCase] = [
            LeetcodeTestCase(
                input={"days": 10, "meetings": [[5, 7], [1, 3], [9, 10]]}, output=2
            ),
            LeetcodeTestCase(input={"days": 5, "meetings": [[2, 4], [1, 3]]}, output=1),
            LeetcodeTestCase(input={"days": 6, "meetings": [[1, 6]]}, output=0),
        ]
        sln = Solution_3169()
        for tc in testcases:
            output = sln.countDays(tc.input["days"], tc.input["meetings"])
            self.assertEqual(tc.output, output)

    def test_case_3184(self):
        testcases: list[LeetcodeTestCase] = [
            LeetcodeTestCase(input=[12, 12, 30, 24, 24], output=2),
            LeetcodeTestCase(input=[72, 48, 24, 3], output=3),
            LeetcodeTestCase(input=[21, 19, 3], output=1),
        ]
        sln = Solution_3184()
        for tc in testcases:
            output = sln.countCompleteDayPairs(tc.input)
            self.assertEqual(tc.output, output)

    def test_case_3191(self):
        testcases: list[LeetcodeTestCase] = [
            LeetcodeTestCase(input=[0, 1, 1, 1, 0, 0], output=3),
            LeetcodeTestCase(input=[0, 1, 1, 1], output=-1),
        ]
        sln = Solution_3191()
        for tc in testcases:
            output = sln.minOperations(tc.input)
            self.assertEqual(tc.output, output)

    def test_case_3192(self):
        testcases: list[LeetcodeTestCase] = [
            LeetcodeTestCase(input=[0, 1, 1, 0, 1], output=4),
            LeetcodeTestCase(input=[1, 0, 0, 0], output=1),
        ]
        sln = Solution_3192()
        for tc in testcases:
            output = sln.minOperations(tc.input)
            self.assertEqual(tc.output, output)

    def test_case_3194(self):
        testcases = [
            LeetcodeTestCase(input=[7, 8, 3, 4, 15, 13, 4, 1], output=5.5),
            LeetcodeTestCase(input=[1, 2, 3, 7, 8, 9], output=5.0),
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
            output = sln.maxHeightOfTriangle(tc.input["red"], tc.input["blue"])
            self.assertEqual(tc.output, output)

    def test_case_3304(self):
        testcases: list[LeetcodeTestCase] = [
            LeetcodeTestCase(input=5, output="b"),
            LeetcodeTestCase(input=10, output="c"),
        ]
        sln = Solution_3304()
        for tc in testcases:
            output = sln.kthCharacter(tc.input)
            self.assertEqual(tc.output, output)

    def test_case_3307(self):
        testcases: list[LeetcodeTestCase] = [
            LeetcodeTestCase(input={"k": 5, "operations": [0, 0, 0]}, output="a"),
            LeetcodeTestCase(input={"k": 10, "operations": [0, 1, 0, 1]}, output="b"),
            LeetcodeTestCase(
                input={
                    "k": 33031255,
                    "operations": [
                        0,
                        1,
                        0,
                        0,
                        1,
                        1,
                        1,
                        0,
                        1,
                        0,
                        1,
                        1,
                        1,
                        0,
                        0,
                        1,
                        0,
                        0,
                        1,
                        1,
                        1,
                        1,
                        0,
                        1,
                        1,
                    ],
                },
                output="j",
            ),
            LeetcodeTestCase(
                input={
                    "k": 13610138,
                    "operations": [
                        0,
                        1,
                        0,
                        0,
                        1,
                        1,
                        0,
                        0,
                        0,
                        0,
                        0,
                        0,
                        0,
                        0,
                        0,
                        0,
                        1,
                        1,
                        0,
                        0,
                        0,
                        0,
                        1,
                        0,
                        1,
                    ],
                },
                output="e",
            ),
            LeetcodeTestCase(
                input={
                    "k": 4685106,
                    "operations": [
                        0,
                        1,
                        1,
                        0,
                        1,
                        0,
                        0,
                        1,
                        0,
                        0,
                        0,
                        1,
                        1,
                        0,
                        1,
                        0,
                        0,
                        1,
                        1,
                        0,
                        0,
                        0,
                        0,
                        1,
                        0,
                    ],
                },
                output="g",
            ),
        ]
        sln = Solution_3307()
        for tc in testcases:
            output = sln.kthCharacter(tc.input["k"], tc.input["operations"])
            self.assertEqual(tc.output, output)

    def test_case_3440(self):
        testcases: list[LeetcodeTestCase] = [
            LeetcodeTestCase(
                input={
                    "eventTime": 5,
                    "startTime": [1, 3],
                    "endTime": [2, 5],
                },
                output=2,
            ),
            LeetcodeTestCase(
                input={
                    "eventTime": 10,
                    "startTime": [0, 7, 9],
                    "endTime": [1, 8, 10],
                },
                output=7,
            ),
            LeetcodeTestCase(
                input={
                    "eventTime": 10,
                    "startTime": [0, 3, 7, 9],
                    "endTime": [1, 4, 8, 10],
                },
                output=6,
            ),
            LeetcodeTestCase(
                input={
                    "eventTime": 5,
                    "startTime": [0, 1, 2, 3, 4],
                    "endTime": [1, 2, 3, 4, 5],
                },
                output=0,
            ),
            LeetcodeTestCase(
                input={
                    "eventTime": 41,
                    "startTime": [17, 24],
                    "endTime": [19, 25],
                },
                output=24,
            ),
        ]
        sln = Solution_3440()
        for tc in testcases:
            output = sln.maxFreeTime(
                tc.input["eventTime"],
                tc.input["startTime"],
                tc.input["endTime"],
            )
            self.assertEqual(tc.output, output)


    def test_case_hj44(self):
        testcases: list[LeetcodeTestCase] = [
            LeetcodeTestCase(
                input=[
                    [0, 9, 2, 4, 8, 1, 7, 6, 3],
                    [4, 1, 3, 7, 6, 2, 9, 8, 5],
                    [8, 6, 7, 3, 5, 9, 4, 1, 2],
                    [6, 2, 4, 1, 9, 5, 3, 7, 8],
                    [7, 5, 9, 8, 4, 3, 1, 2, 6],
                    [1, 3, 8, 6, 2, 7, 5, 9, 4],
                    [2, 7, 1, 5, 3, 8, 6, 4, 9],
                    [3, 8, 6, 9, 1, 4, 2, 5, 7],
                    [0, 4, 5, 2, 7, 6, 8, 3, 1],
                ],
                output=[
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
            ),
            LeetcodeTestCase(
                input=[
                    [7,3,0,0,0,8,0,0,0],
                    [2,0,0,0,0,0,6,0,0],
                    [0,0,1,0,0,0,4,5,0],
                    [0,0,0,0,0,5,9,6,0],
                    [9,0,0,8,1,0,0,4,0],
                    [0,0,0,0,0,2,7,8,0],
                    [0,0,6,0,0,0,5,2,0],
                    [1,0,0,0,0,0,8,0,0],
                    [8,9,0,0,0,6,0,0,0]
                ],
                output=[
                    [7,3,5,4,6,8,1,9,2],
                    [2,4,9,1,5,7,6,3,8],
                    [6,8,1,2,3,9,4,5,7],
                    [3,2,8,7,4,5,9,6,1],
                    [9,6,7,8,1,3,2,4,5],
                    [5,1,4,6,9,2,7,8,3],
                    [4,7,6,3,8,1,5,2,9],
                    [1,5,3,9,2,4,8,7,6],
                    [8,9,2,5,7,6,3,1,4]
                ],
            ),
        ]
        sln = Solution_hj44()
        for tc in testcases:
            output=sln.resolve_sudoku(tc.input)
            self.assertAlmostEqual(output, tc.output)
            # for i in range(9):
            #     self.assertAlmostEqual(output[i], tc.output[i])


    def test_case_hj75(self):
        testcases: list[LeetcodeTestCase] = [
            LeetcodeTestCase(input={"s": "awaabb", "t": "aawbb"}, output=2),
            LeetcodeTestCase(input={"s": "asdfas", "t": "werasdfaswer"}, output=6),
            LeetcodeTestCase(input={"s": "asdfghjk", "t": "zxcvbnm"}, output=0),
        ]
        sln = Solution_hj75()
        for tc in testcases:
            output = sln.max_common_substr(tc.input["s"], tc.input["t"])
            self.assertEqual(tc.output, output)

    def test_case_hj86(self):
        testcases: list[LeetcodeTestCase] = [
            LeetcodeTestCase(input=200, output=2),
            LeetcodeTestCase(input=1023, output=10),
            LeetcodeTestCase(input=77, output=2),
        ]
        sln = Solution_hj86()
        for tc in testcases:
            output = sln.max_bits(tc.input)
            self.assertEqual(tc.output, output)


if __name__ == "__main__":
    unittest.main()
