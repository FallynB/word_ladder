#!/bin/python3
import copy
from collections import deque


def word_ladder(start_word, end_word, dictionary_file='words5.dict'):
    '''
    Returns a list satisfying the following properties:

    1. the first element is `start_word`
    2. the last element is `end_word`
    3. elements at index i and i+1 are `_adjacent`
    4. all elements are entries in the `dictionary_file` file

    For example, running the command
    ```
    word_ladder('stone','money')
    ```
    may give the output
    ```
    ['stone', 'shone', 'phone', 'phony', 'peony',
    'penny', 'benny', 'bonny', 'boney', 'money']
    ```
    but the possible outputs are not unique,
    so you may also get the output
    ```
    ['stone', 'shone', 'shote', 'shots', 'soots',
    non
    'hoots', 'hooty', 'hooey', 'honey', 'money']
    ```
    (We cannot use doctests here because the outputs are not unique.)

    Whenever it is impossible to generate a word ladder between the two words,
    the function returns `None`.
    '''
    x = True
    stack = []
    stack.append(start_word)

    dequei = deque()
    dequei.append(stack)
    if start_word == end_word:
        return stack
    with open(dictionary_file, 'r') as f:
        dictionary_file = [word.strip() for word in f]

    while len(dequei) != 0:
        current = dequei.popleft()
        copy_dictionary = copy.copy(dictionary_file)
        for word in copy_dictionary:
            if _adjacent(word, current[-1]) is x:
                if word == end_word:
                    current.append(word)
                    return current
                else:
                    sc = copy.copy(current)
                    sc.append(word)
                    dequei.append(sc)
                    dictionary_file.remove(word)


def verify_word_ladder(ladder):
    '''
    Returns True if each entry of the input list is adjacent to its neighbors;
    otherwise returns False.

    >>> verify_word_ladder(['stone', 'shone', 'phone', 'phony'])
    True
    >>> verify_word_ladder(['stone', 'shone', 'phony'])
    False
    '''

    count = 0
    x = True

    if ladder == []:
        return False

    for i in range(len(ladder) - 1):
        word1 = ladder[i]
        word2 = ladder[i + 1]

        if _adjacent(word1, word2) is x:
            count += 1

    if count == len(ladder) - 1:
        return True
    else:
        return False


def _adjacent(word1, word2):
    '''
    Returns True if the input words differ by only a single character;
    returns False otherwise.

    >>> _adjacent('phone','phony')
    True
    >>> _adjacent('stone','money')
    False
    '''

    count = 0
    if len(word1) == len(word2):
        for i in range(len(word1)):
            if word1[i] != word2[i]:
                count += 1
        if count > 1:
            return False
        else:
            return True
    else:
        return False
