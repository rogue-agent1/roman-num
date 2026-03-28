#!/usr/bin/env python3
"""roman_num - Convert between Roman numerals and integers."""
import sys

VALS = [(1000,'M'),(900,'CM'),(500,'D'),(400,'CD'),(100,'C'),(90,'XC'),
        (50,'L'),(40,'XL'),(10,'X'),(9,'IX'),(5,'V'),(4,'IV'),(1,'I')]
ROM = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}

def to_roman(n):
    r = ''
    for val, sym in VALS:
        while n >= val: r += sym; n -= val
    return r

def from_roman(s):
    total = 0
    for i, c in enumerate(s.upper()):
        val = ROM.get(c, 0)
        if i+1 < len(s) and val < ROM.get(s[i+1].upper(), 0): total -= val
        else: total += val
    return total

def main():
    args = sys.argv[1:]
    if not args or '-h' in args:
        print("Usage: roman_num.py 42 | roman_num.py XLII"); return
    for a in args:
        if a.isdigit():
            n = int(a); print(f"  {n} = {to_roman(n)}")
        elif all(c.upper() in ROM for c in a):
            print(f"  {a.upper()} = {from_roman(a)}")
        else:
            print(f"  {a}: invalid")

if __name__ == '__main__': main()
