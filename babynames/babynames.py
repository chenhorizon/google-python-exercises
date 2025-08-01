#!/usr/bin/python3
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import sys
import re

"""Baby Names exercise

Define the extract_names() function below and change main()
to call it.

For writing regex, it's nice to include a copy of the target
text for inspiration.

Here's what the html looks like in the baby.html files:
...
<h3 align="center">Popularity in 1990</h3>
....
<tr align="right"><td>1</td><td>Michael</td><td>Jessica</td>
<tr align="right"><td>2</td><td>Christopher</td><td>Ashley</td>
<tr align="right"><td>3</td><td>Matthew</td><td>Brittany</td>
...

Suggested milestones for incremental development:
 -Extract the year and print it
 -Extract the names and rank numbers and just print them
 -Get the names data into a dict and print it
 -Build the [year, 'name rank', ... ] list and print it
 -Fix main() to use the extract_names list
"""

def extract_names(filename) -> list:
  """
  Given a file name for baby.html, returns a list starting with the year string
  followed by the name-rank strings in alphabetical order.
  ['2006', 'Aaliyah 91', Aaron 57', 'Abagail 895', ' ...]
  """
  # +++your code here+++
  f_content = read_file(filename)
  if f_content == None:
      return []

  year_match = re.search(r'Popularity in (\d*)', f_content)
  if not year_match:
      print(f"Notice: no information of year in the file, {filename}")
      return []
  year = year_match.group(1)

  rank_names_match = re.findall(r'<td>(\d+)</td><td>(\w+)</td><td>(\w+)</td>', f_content)
  if not rank_names_match:
      print(f"Notice: no rank and name was found in the file, {filename}")
      return []
  y_list = []
  for rank_names in rank_names_match:
      y_list.append(f"{rank_names[1]} {rank_names[0]}")
      y_list.append(f"{rank_names[2]} {rank_names[0]}")
  y_list.sort()

  return [year] + y_list

def read_file(f_path: str) -> str:
    try:
        with open(f_path, 'r', encoding='utf-8') as f:
            return f.read()
    except FileNotFoundError:
        print(f"Error: file {f_path} was not found.")
        return None
    except Exception:
        print(f"Error: an unexpected error occurred, {e}")
        return None


def main():
  # This command-line parsing code is provided.
  # Make a list of command line arguments, omitting the [0] element
  # which is the script itself.
  args = sys.argv[1:]

  if not args:
    print('usage: [--summaryfile] file [file ...]')
    sys.exit(1)

  # Notice the summary flag and remove it from args if it is present.
  summary = False
  if args[0] == '--summaryfile':
    summary = True
    del args[0]

  # +++your code here+++
  # For each filename, get the names, then either print the text output
  # or write it to a summary file
  for f in args:
      y_list = extract_names(f)
      for y in y_list:
          print(y)

if __name__ == '__main__':
  main()
