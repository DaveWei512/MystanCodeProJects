"""
File: recursion.py
Name: David Wei
Date: 5/16/2022
This code is to test the difference of two recursion function to find out anagrams.
One is using 'for i in range(len(s)):'. Another one is using 'for ch in s:'
Conclusion:
1. There's no difference and get the right answer directly if all the characters are different in string.
2. If there's the same character in the string: 'for i in range()' is same and no influence. But 'for ch in s' will be
    multiply algorithm time than real_answer.( It means will spend multiply times to process.)
"""


def main():
    for s in ['a', 'ab', 'abc', 'abcd', 'abcde', 'abcdef', 'abcdefg', 'abcdefgh', 'aabcdefg', 'aabbcdef', 'aaabcdef']:
        recursion(s)


def recursion(s):

    # To calculate the real number of anagrams should be len(s)!
    real_ans = 1
    for i in range(1, len(s)+1):    # Be aware that i is beginning from 0
        real_ans *= i

    # To use 'for i in range()' to calculate
    lst = helper1(s, '', [], len(s))
    print(f'"{s}" for helper1(for i) to find out the number of anagrams: {len(lst)}')

    # To use 'for ch in string' to calculate
    lst = helper(s, '', [], len(s))
    print(f'"{s}" for helper(for ch) to find out the number of anagrams: {len(lst)}')

    print(f'The real answer should be : {real_ans}')
    print('-' * 80)


def helper1(s, ans, lst, x):
    if len(ans) == x:
        lst.append(ans)
    else:
        for i in range(len(s)):
            ans += s[i]
            s = s[:i]+s[i+1:]
            helper1(s, ans, lst, x)
            s = s[:i] + ans[-1] + s[i:]
            ans = ans[:-1]
    return lst


def helper(s, ans, lst, x):
    if len(ans) == x:
        lst.append(ans)
    else:
        for ch in s:
            if s.count(ch) == ans.count(ch):
                pass
            else:
                ans += ch
                helper(s, ans, lst, x)
                ans = ans[:-1]
    return lst


if __name__ == '__main__':
    main()
