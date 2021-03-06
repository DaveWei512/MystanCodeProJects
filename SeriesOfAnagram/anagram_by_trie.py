"""
File: anagram_by_trie.py
Name: David Wei
----------------------------------
This program recursively finds all the anagram(s)
for the word input by user and terminates when the
input string matches the EXIT constant defined
at line 23

If you correctly implement this program, you should see the
number of anagrams for each word listed below:
    * arm -> 3 anagrams
    * contains -> 5 anagrams
    * stop -> 6 anagrams
    * tesla -> 10 anagrams
    * spear -> 12 anagrams

This code is one of the series to find anagrams codes. And Using TrieNode
Conclusion: This code is the slowest in the series.
"""

import time  # This file allows you to calculate the speed of your algorithm

# Constants
FILE = 'dictionary.txt'  # This is the filename of an English dictionary
EXIT = '-1'  # Controls when to stop the loop

# Global variable
# In order to print the time of creating the dictionary at the end in main function. It will be clearer to compare the
# different algorithm speed.
dic_time = 0


# class TrieNode in order to create dictionary.
class TrieNode:
    def __init__(self):
        self.children = {}
        self.end = False


# Global variable. This is the root of Trie of english dictionary. Starting point to search any word.
root = TrieNode()


def main():
    """
    This code is case insensitive, remove the careless blanket input automatically and excluding the illegal input. So
    this code won't run error because of wrong input.
    This code use TrieNode to create English dictionary. Speeding algorithm is expected!
    """

    # Create a words' dictionary in order to be searched.
    read_dictionary()

    # Print the welcome title and exit condition
    print(f'Welcome to stanCode "Anagram Generator" (or -1 to quit)')

    # You can look for another word until you want to exit.
    while True:

        # input string to be processed(reordered and searched).
        s = input('Find anagrams for: ')

        # string case insensitive
        s = s.lower()

        # clear the space of input string
        s = s.strip(' ')

        # Set exit condition
        if s == EXIT:
            break

        # Exclude the illegal input string - if input string is not all alphabets.
        elif not s.isalpha():
            print('Illegal, Input again.')

        else:

            # begin to calculate the algorithm time
            start = time.time()
            print(f'Search...')

            # Reorder the string and find the anagrams by return a list.
            lst = find_anagrams(s)

            # Create a lst to store been searched real english anagrams - appeared in english dictionary.
            ans_lst = []

            # If there's no word found in lst from function find_anagram().
            if len(lst) == 0:
                print(f'0  anagrams :[]')

            else:
                for ele in lst:
                    cur = root
                    switch = True
                    for ch in ele:
                        if ch in cur.children:
                            cur = cur.children[ch]
                        else:
                            switch = False
                            break
                    if cur.end and switch:
                        print(f'Found:      {ele}')
                        print(f'Search...')
                        ans_lst.append(ele)
                print(f'{len(ans_lst)} anagrams: {ans_lst}')

            # End to calculate the algorithm time.
            end = time.time()
            alg_time = end - start
            print('----------------------------------')
            print(f'Time to create dictionary: {dic_time} seconds')
            print(f'The speed of your anagram algorithm: {alg_time} seconds.')
            print(f'The total algorithm time: {dic_time + alg_time} seconds')


def read_dictionary():
    """
    This function is to create english dictionary by using TrieNode(class showed at the beginning of this code).
    The root of Trie is a global variable in order to be used for searching in the other function.
    :return: None
    """
    # The time to create dictionary.
    global dic_time

    # To calculate the time to create dictionary. Start here.
    start = time.time()

    # Open the english dictionary text(one line one word) and re-store in a dictionary named dic_dic.
    with open(FILE, 'r')as f:
        for line in f:
            word = line.rstrip('\n')
            cur = root
            for ch in word:
                if ch not in cur.children:
                    cur.children[ch] = TrieNode()
                    cur = cur.children[ch]
                else:
                    cur = cur.children[ch]
            cur.end = True

        # To calculate the time to create dictionary. End here.
        end = time.time()
        dic_time = end - start
        print(f'{dic_time} second to create dictionary')


def find_anagrams(s):
    """
    Recursion is necessary. Passed argument is insufficient. Transfer to another helper function.
    :param s:
    :return:
    """

    return find_anagrams_helper(s, '', [], [])


def find_anagrams_helper(s, result, lst, pass_):
    """
    This function is to calculate the input string into the candidates of anagram. Using recursion to reorder alphabets.
    Create and transfer to has_prefix() function to reduce words those are impossible to be anagrams.
    :param s: string - To calculate this word's anagrams.
    :param result: string - candidates of possible anagram or un-finished result in procedure.
    :param lst: list - the list contains all possible anagrams.
    :param pass_: list - the list store impossible leading characters(pre-fix) from dictionary to reduce recursive time.
    :return: lst : list
    """

    # To set base case:
    if len(result) == len(s):

        # Maybe the same word(result) appeared twice or much more after recursive algorithm.
        # Excluding the appeared word by using if statement.
        if result not in lst:
            lst.append(result)

    else:
        for ch in s:
            # Excluding the same character that repeating time in result is as same as the original string 's'. It means
            # that you can't add again. Or the the pre-fix of anagram is not existed in dictionary, so you shouldn't
            # continue to process.
            if result.count(ch) == s.count(ch) or result in pass_:
                pass

            else:
                # choose
                result += ch

                # Excluding pre-fix is not in dictionary
                if not has_prefix(result) and result not in pass_:
                    pass_.append(result)

                # explore
                find_anagrams_helper(s, result, lst, pass_)
                # un-choose
                result = result[:len(result) - 1]

    return lst


def has_prefix(sub_s):
    """
    This function to calculate whether sub_s is the leading alphabets in dictionary.
    :param sub_s: string
    :return: Boolean
    """
    cur = root
    for ch in sub_s:
        if ch in cur.children:
            cur = cur.children[ch]
        else:
            return False
    return True


if __name__ == '__main__':
    main()
