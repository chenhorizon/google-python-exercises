#!/usr/bin/python3
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import sys
import re
import os
import shutil
import subprocess

"""Copy Special exercise
"""

# +++your code here+++
# Write functions and modify main() to call them

def get_special_paths(dir) -> []:
    if not os.path.exists(dir):
        print(f"Error: dir {dir} does not exist.")
        return []

    f_list = os.listdir(dir)

    return [ os.path.abspath(f) for f in f_list if re.search(r'__\w+__', f) ]

def copy_to(paths: str, dir: str) -> int:
    if not os.path.exists(dir):
        print(f"Error: dir {dir} does not exist.")
        return 1

    for p in paths:
        if not os.path.exists(p):
            print(f"Notice: path {p} does not exists.")
            continue

        shutil.copy(p, dir)

    return 1

def zip_to(paths: str, zippath: str) -> int:

    if not zippath.endswith(".zip"):
        print(f"Error: zippath {zippath} must end with '.zip'.")
        return 1

    zip_cmd = "zip -j " + zippath + " " + " ".join(paths)
    print(f"zip cmd: {zip_cmd}")
    errno, errmsg = subprocess.getstatusoutput(zip_cmd)
    if errno:
        print(errmsg)
        return errno

    return errno


def main():
  # This basic command line argument parsing code is provided.
  # Add code to call your functions below.

  # Make a list of command line arguments, omitting the [0] element
  # which is the script itself.
  args = sys.argv[1:]
  if not args:
    print('usage: [--todir dir][--tozip zipfile] dir [dir ...]')
    sys.exit(1)

  # todir and tozip are either set from command line
  # or left as the empty string.
  # The args array is left just containing the dirs.
  todir = ''
  if args[0] == '--todir':
    todir = args[1]
    del args[0:2]

  tozip = ''
  if args[0] == '--tozip':
    tozip = args[1]
    del args[0:2]

  if not args: # A zero length array evaluates to "False".
    print('error: must specify one or more dirs')
    sys.exit(1)

  # +++your code here+++
  # Call your functions

  special_paths = []
  for path in args:
      special_paths.extend(get_special_paths(path))

  if todir:
      # copy_to(paths, dir)
      copy_to(special_paths, todir)
  elif tozip:
      # zip_to(paths, zippath)
      zip_to(special_paths, tozip)
  else:
      print(f"Notice: no --todir and --tozip options, just list all special paths:")
      for p in special_paths:
          print(p)

if __name__ == '__main__':
  main()
