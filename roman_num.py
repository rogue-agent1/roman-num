#!/usr/bin/env python3
"""Roman numeral encoder/decoder."""
import sys

ROMAN = [(1000,"M"),(900,"CM"),(500,"D"),(400,"CD"),(100,"C"),(90,"XC"),
         (50,"L"),(40,"XL"),(10,"X"),(9,"IX"),(5,"V"),(4,"IV"),(1,"I")]

def to_roman(n):
    if n <= 0 or n >= 4000: raise ValueError("1-3999 only")
    result = []
    for val, sym in ROMAN:
        while n >= val:
            result.append(sym)
            n -= val
    return "".join(result)

def from_roman(s):
    vals = {"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
    result = 0
    for i in range(len(s)):
        if i+1 < len(s) and vals[s[i]] < vals[s[i+1]]:
            result -= vals[s[i]]
        else:
            result += vals[s[i]]
    return result

def is_valid(s):
    try:
        n = from_roman(s)
        return to_roman(n) == s
    except (KeyError, ValueError):
        return False

def test():
    assert to_roman(1994) == "MCMXCIV"
    assert to_roman(3999) == "MMMCMXCIX"
    assert to_roman(1) == "I"
    assert from_roman("MCMXCIV") == 1994
    assert from_roman("XIV") == 14
    assert is_valid("XIV")
    assert not is_valid("IIII")
    for n in [1, 42, 100, 999, 2024, 3999]:
        assert from_roman(to_roman(n)) == n
    print("  roman_num: ALL TESTS PASSED")

if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "test": test()
    else:
        n = int(sys.argv[2]) if len(sys.argv) > 2 else 2026
        print(f"{n} = {to_roman(n)}")
