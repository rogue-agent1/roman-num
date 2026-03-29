#!/usr/bin/env python3
"""Roman Numerals - Convert between Arabic and Roman numeral systems."""
import sys, re

ROMAN = [(1000,"M"),(900,"CM"),(500,"D"),(400,"CD"),(100,"C"),(90,"XC"),
         (50,"L"),(40,"XL"),(10,"X"),(9,"IX"),(5,"V"),(4,"IV"),(1,"I")]

def to_roman(n):
    if n <= 0 or n >= 4000: return "N/A"
    result = ""
    for val, sym in ROMAN:
        while n >= val: result += sym; n -= val
    return result

def from_roman(s):
    vals = {"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
    result = 0; s = s.upper()
    for i, c in enumerate(s):
        if i + 1 < len(s) and vals.get(c, 0) < vals.get(s[i+1], 0):
            result -= vals[c]
        else:
            result += vals.get(c, 0)
    return result

def is_valid_roman(s):
    return bool(re.match(r"^M{0,3}(CM|CD|D?C{0,3})(XC|XL|L?X{0,3})(IX|IV|V?I{0,3})$", s.upper()))

def main():
    if len(sys.argv) > 1:
        arg = sys.argv[1]
        if arg.isdigit():
            n = int(arg)
            print(f"{n} = {to_roman(n)}")
        else:
            print(f"{arg} = {from_roman(arg)} {'(valid)' if is_valid_roman(arg) else '(invalid format)'}")
    else:
        print("=== Roman Numerals ===\n")
        for n in [1, 4, 9, 14, 42, 99, 399, 1776, 2024, 3999]:
            r = to_roman(n)
            back = from_roman(r)
            print(f"  {n:5d} = {r:15s} -> {back}")

if __name__ == "__main__":
    main()
