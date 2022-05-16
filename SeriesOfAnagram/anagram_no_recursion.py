"""
File Name : anagram_no_recursion.py
Name : David Wei
Date : May 12th 2022
--------------------------------------
This file is derived from anagram.py
The fastest algorithm of anagram is created another small dictionary depending upon input string from created
English dictionary.
For example: If the goal is looking for the "contains" string anagrams. The faster algorithm is to create a small relevant
dictionary. These words in small dictionary only contains 8 alphabets and with the same alphabets of the string
"contains" -c,o,n,t,a,i,s -. There are only very few words in small dictionary. So, the code will reduce great time to
search the matched word.
If all the words in small dictionary are very few and similar to the input string very much. Why don't we directly
match the anagrams in dictionary and without using recursion function. This is what this code does and expect to reduce
algorithm time in advance.
Conclusion: This code is still kind of slower than creating relevant small dictionary. May be it need too much time to
execute the statement of string.count().
May 16th 2022 update: Amend two positions in find_anagram(s):
                      1. Take s_dic.items() out from 'for ch, time_ in s_dic.items():' loop to reduce repeat split
                         process in every loop. This will make this code close to the fastest code.
                      2. Reverse the value of s_dic.item(). This means to check the most frequently repeating alphabet
                         first. This will exclude the un-matched word earlier. Then this code faster than the fastest
                         code.
"""

import time

# Constants
FILE = 'dictionary.txt'
EXIT = '-1'

# Global variable
dic_dic = {}


def main():
    read_dic()                  # create dictionary
    while True:
        s = input_s()               # To process input the correct string to be found
        if s == EXIT:
            break
        total_time = 0
        for i in range(1000):
            start = time.time()
            lst = find_anagram(s)       # To find out anagram by matched up dictionary
            print(f'{len(lst)} anagrams: {lst}')
            print('-------------------------------------')
            end = time.time()
            print(f'The speed of your anagram algorithm: {end - start} seconds')
            total_time += (end - start)
        print(f'The average time to proceed 1,000 times :  {total_time / 1_000} seconds')


def read_dic():
    """
    The structure of dic_dic is {key = len(word), int : value = {word}, set}
    :return: None
    """
    start = time.time()
    with open(FILE, "r")as f:
        for line in f:
            word = line.strip()
            if len(word) not in dic_dic:
                dic_dic[len(word)] = {word}
            else:
                dic_dic[len(word)].add(word)
    end = time.time()
    print(f'The time to create dictionary: {end - start} seconds')


def input_s():
    """
    input is case and space insensitive. Re-input again while input illegal.
    :return: s, string - lowercase or '-1'
    """
    while True:
        s = input('Find anagrams for: ')
        if s == EXIT:
            return s
        s = s.lower()
        s = s.strip()
        if s.isalpha():
            return s
        else:
            print('Illegal input again: ')


def find_anagram(s):
    """
    Use dictionary to find anagrams of string directly.
    To create s_dic first. the key is every alphabet in string, value is the number of alphabet in string. then use this
    s_dic to match up every anagram appeared in dictionary dic_dic.
    :param s: string
    :return: lst, list with result anagrams.
    """
    s_dic = {}                  # The features of string store in s_dic
    lst = []                    # To store the result anagrams

    # to create s_dic, {key= every alphabet of string, value = times to be appeared in string}
    for ch in s:
        if ch not in s_dic:
            s_dic[ch] = 1
        else:
            s_dic[ch] += 1
    print('Search...')

    # To judge if s matches every word in the value of key = len(s)
    s_lst = s_dic.items()
    s_lst = sorted(s_lst, key=lambda t: t[1], reverse=True)
    for word in dic_dic[len(s)]:
        finish = True                           # To judge if finish next for loop
        for ch, time_ in s_lst:
            # Every alphabet must have the same appeared times if anagram is.
            if word.count(ch) != time_:
                finish = False                  # not finish means not match
                break
        if finish:
            print(f'Found:     {word}\nSearch...')
            lst.append(word)
    return lst


if __name__ == '__main__':
    main()
