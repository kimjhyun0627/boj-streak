# https://www.acmicpc.net/problem/3154

from sys import stdin
from itertools import product

input = lambda: stdin.readline().rstrip()


def calculate_effort(d1_char, d2_char, d3_char, d4_char):
    coords1 = key_coords[d1_char]
    coords2 = key_coords[d2_char]
    coords3 = key_coords[d3_char]
    coords4 = key_coords[d4_char]

    e1 = abs(coords1[0] - coords2[0]) + abs(coords1[1] - coords2[1])
    e2 = abs(coords2[0] - coords3[0]) + abs(coords2[1] - coords3[1])
    e3 = abs(coords3[0] - coords4[0]) + abs(coords3[1] - coords4[1])
    return e1 + e2 + e3


target_time_str = input()
target_hh_str, target_mm_str = target_time_str.split(":")
target_hh = int(target_hh_str)
target_mm = int(target_mm_str)

key_coords = {
    "1": (0, 0),
    "2": (0, 1),
    "3": (0, 2),
    "4": (1, 0),
    "5": (1, 1),
    "6": (1, 2),
    "7": (2, 0),
    "8": (2, 1),
    "9": (2, 2),
    "0": (3, 1),
}


min_effort = float("inf")
best_input_time_str = ""

digits = [str(ii) for ii in range(10)]

for d1_char, d2_char, d3_char, d4_char in product(digits, repeat=4):
    input_hh = int(d1_char) * 10 + int(d2_char)
    input_mm = int(d3_char) * 10 + int(d4_char)

    displayed_hh = input_hh % 24
    displayed_mm = input_mm % 60

    if displayed_hh == target_hh and displayed_mm == target_mm:
        current_effort = calculate_effort(d1_char, d2_char, d3_char, d4_char)

        current_input_time_str = f"{d1_char}{d2_char}:{d3_char}{d4_char}"

        if current_effort < min_effort:
            min_effort = current_effort
            best_input_time_str = current_input_time_str
        elif current_effort == min_effort:
            if (
                best_input_time_str == ""
                or current_input_time_str < best_input_time_str
            ):
                best_input_time_str = current_input_time_str

print(best_input_time_str)
