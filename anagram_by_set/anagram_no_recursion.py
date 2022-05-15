"""
File Name : anagram_no_recursion.py
Name : David Wei
--------------------------------------
This file is derived from anagram.py
The fastest algorithm of anagram is created another small dictionary depending upon input string from created
English dictionary.
For example: The goal is looking for the "contains" string anagrams. The faster algorithm is created a small relative
dictionary. These words only contains 8 alphabets and the same alphabets of the string "contains" -c,o,n,t,a,i,s -
in small dictionary. There are only a few words in small dictionary. So, the code will reduce great time to search
the matched word. The words in small dictionary are few and much similar to the input string. Why don't we directly
match the anagrams in dictionary if it's not necessary to use recursion function. This is what this code does.

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
    for word in dic_dic[len(s)]:
        finish = True                           # To judge if finish next for loop
        for ch, time_ in s_dic.items():
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
