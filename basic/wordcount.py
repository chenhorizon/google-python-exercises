#!/usr/bin/python3
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

"""Wordcount exercise
Google's Python class

The main() below is already defined and complete. It calls print_words()
and print_top() functions which you write.

1. For the --count flag, implement a print_words(filename) function that counts
how often each word appears in the text and prints:
word1 count1
word2 count2
...

Print the above list in order sorted by word (python will sort punctuation to
come before letters -- that's fine). Store all the words as lowercase,
so 'The' and 'the' count as the same word.

2. For the --topcount flag, implement a print_top(filename) which is similar
to print_words() but which prints just the top 20 most common words sorted
so the most common word is first, then the next most common, and so on.

Use str.split() (no arguments) to split on all whitespace.

Workflow: don't build the whole program at once. Get it to an intermediate
milestone and print your data structure and sys.exit(0).
When that's working, try for the next milestone.

Optional: define a helper function to avoid code duplication inside
print_words() and print_top().

"""

import sys

# +++your code here+++
# Define print_words(filename) and print_top(filename) functions.
# You could write a helper utility function that reads a file
# and builds and returns a word/count dict for it.
# Then print_words() and print_top() can just call the utility function.

def print_words(f_path: str) -> dict:
    ret = {}

    f_content = read_file(f_path)
    if f_content == None:
        return ret

    word_list = f_content.split()
    for x in word_list:
        x = x.lower()
        if x in ret:
            ret[x] += 1
        else:
            ret[x] = 1

    # for x in sorted(ret):
    for x in sorted(ret.keys()):
        print(f"{x} {ret[x]}")

    return ret

def print_top(f_path: str) -> dict:
    ret = {}
    num_to_print = 20

    f_content = read_file(f_path)
    if f_content == None:
        return ret

    word_list = f_content.split()
    for x in word_list:
        x = x.lower()
        if x in ret:
            ret[x] += 1
        else:
            ret[x] = 1

    for word, word_cnt in sorted(ret.items(), key=lambda item:item[1], reverse=True)[0:num_to_print]:
        print(f"{word} {word_cnt}")

    return ret

def read_file(f_path: str) -> str:
    try:
        with open(f_path, 'r', encoding='utf-8') as f:
            return f.read()
    except FileNotFoundError:
        print(f"Error: the file '{f_path}' was not found.")
        return None
    except Exception as e:
        print(f"Error: an unexpected error occurred, {e}")
        return None

###

# This basic command line argument parsing code is provided and
# calls the print_words() and print_top() functions which you must define.
def main():
  if len(sys.argv) != 3:
    print('usage: ./wordcount.py {--count | --topcount} file')
    sys.exit(1)

  option = sys.argv[1]
  filename = sys.argv[2]
  if option == '--count':
    print_words(filename)
  elif option == '--topcount':
    print_top(filename)
  else:
    print('unknown option: ' + option)
    sys.exit(1)

if __name__ == '__main__':
  main()
