"""
File: anagram_set.py
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
2022/5/7 p.s.:
This code is amended from anagram. I try to use set to instead of list. This maybe can speed up the algorithm.
Set in python only store one element only one time. So it's not necessary to use if to exclude the repeating words.
"""

import time  # This file allows you to calculate the speed of your algorithm

# Constants
FILE = 'dictionary.txt'  # This is the filename of an English dictionary
EXIT = '-1'  # Controls when to stop the loop

# Global variable
dic_dic = {}

# In order to print the time of creating the dictionary at the end in main function. It will be clearer to compare the
# different algorithm speed.
dic_time = 0


def main():
    """
    This code is case insensitive, remove the careless blanket input automatically and excluding the illegal input. So
    this code won't run error because of wrong input.
    In order to speed the algorithm. I change 2 original setting:
    1. Change the global list variable dic_lst=[] to global dictionary variable dic_dic{}.
    2. Because the key of dictionary is the length of input string, has_prefix function need the key to compare. I add
        another argument - length of word.
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
        s = s.strip()

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

            # Reorder the string and find the anagrams by return a set.
            set_, x = find_anagrams(s)
            print(f'{len(set_)} anagrams: {set_}')

            # End to calculate the algorithm time.
            end = time.time()
            alg_time = end - start
            print('----------------------------------')
            print(f'Time to create dictionary: {dic_time} seconds')
            print(f'The speed of your anagram algorithm: {alg_time} seconds.')
            print(f'The total algorithm time: {dic_time + alg_time} seconds')


def read_dictionary():
    """
    This function is to convert a one word one line english dictionary to a python dictionary dic_dic.
    Analyze the english dic.text: If the number of words more than 1,000, The length of words will be between 4 to 14.
    The maximum is 26,448 words for 8 characters' word. So the dic_dic construction is described as below:
    1. If word contains below 4 characters or more than 14 characters : key = length of word, value = words by set
    2. The others : key = length of word, value is another python dictionary: key = the first 2 english alphabet,
       value = words by set.
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

            # Number of characters < 3: key = len(word), value = word
            if len(word) < 4 or len(word) > 14:
                if len(word) in dic_dic:
                    dic_dic[len(word)].add(word)
                else:
                    dic_dic[len(word)] = {word}

            # The others {key=len(word): value = {first 2 character : [words]} }
            else:
                if len(word) in dic_dic:
                    if word[:2] in dic_dic[len(word)]:
                        dic_dic[len(word)][word[:2]].add(word)
                    else:
                        dic_dic[len(word)][word[:2]] = {word}
                else:
                    dic_dic[len(word)] = {word[:2]: {word}}

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

    return find_anagrams_helper(s, len(s), '', set())


def find_anagrams_helper(s, len_s, result, set_):
    """
    This function is to calculate the input string into the candidates of anagram. Using recursion to reorder alphabets.
    Create and transfer to has_prefix() function to reduce words those are impossible to be anagrams.
    :param s: string - To calculate this word's anagrams.
    :param len_s: int - the length of s
    :param result: string - candidates of possible anagram or un-finished result in procedure.
    :param set_: set - the set contains all possible anagrams.
    :return: set_ : set, len(s) : int
    """

    # To set base case:
    if len(result) == len_s:

        # Maybe the same word(result) appeared twice or much more after recursive algorithm.
        # Excluding the appeared word by using if statement.
        set_.add(result)

    else:
        for i in range(len(s)):
            # choose:
            result += s[i]
            s = s[:i] + s[i+1:]

            # explore:
            if len(result) == 1:
                find_anagrams_helper(s, len_s, result, set_)
            elif has_prefix(result, len_s):
                find_anagrams_helper(s, len_s, result, set_)
            # un-choose:
            s = s[:i] + result[-1] + s[i:]
            result = result[:-1]
    return set_, len_s


def has_prefix(sub_s, length):
    """
    This function to calculate whether sub_s is the leading alphabets in dictionary.
    :param length: int - the input word's length, it is the key of dic_dic.
    :param sub_s: string
    :return: Boolean
    """
    # If word contains below 4 characters or more than 14 characters : key = length of word, value = word.
    if length < 4 or length > 14:
        for ele in dic_dic[length]:
            if ele.startswith(sub_s):
                return True
        return False

    # key = length of word, value is another python dictionary: key = the first 2 english alphabet, value = word
    else:
        if len(sub_s) == 2:
            return True if sub_s in dic_dic[length] else False
        else:
            for ele in dic_dic[length][sub_s[:2]]:
                if ele.startswith(sub_s):
                    return True
            return False


if __name__ == '__main__':
    main()
