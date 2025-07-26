import re, sys

QUANTS = set('*+?')
Q_START = QUANTS.union({'{'})

def has_multiple_repeat(pat: str) -> bool:
    escaped = False
    prev = ''
    for ch in pat:
        if escaped:
            escaped = False
        elif ch == '\\':
            escaped = True
        else:
            if prev in Q_START and (ch in QUANTS or ch == '{'):
                return True
        prev = ch
    return False

def main():
    data = sys.stdin.read().splitlines()
    if not data:
        return
    t = int(data[0])
    for pat in data[1:1 + t]:
        if has_multiple_repeat(pat):
            print("False")
        else:
            try:
                re.compile(pat)
                print("True")
            except re.error:
                print("False")

if __name__ == "__main__":
    main()




'''
Sample Input
2
.*\+
.*+

Sample Output
True
False'''