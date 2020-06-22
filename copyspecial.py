#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Copyspecial Assignment"""

# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# give credits
__author__ = "???"

import re
import os
import sys
import shutil
import subprocess
import argparse


def get_special_paths(dir):
    """Given a dirname, returns a list of all its special files."""
    # your code here

    files_list = []
    files = os.listdir(dir)
    for file in files:
        match = re.search(r'__(\w+)__', file)
        if match:
            files_list.append(os.path.abspath(os.path.join(dir, file)))
    return files_list



def copy_to(paths, dir):
    # your code here

    if not os.path.exists(paths):
        os.makedirs(paths)
    else:
        print("This path exists")

    
    for file in dir:
        shutil.copy(file, paths)

    


def zip_to(paths, zippath):
    # your code here

    paths = list(paths)
    command = "zip -j {} {}".format(zippath, ' '.join(paths))
    print("Command I am going to do: ")
    print(command)
    os.system(command)



def main(args):
    """Main driver code for copyspecial."""
    # This snippet will help you get started with the argparse module.
    parser = argparse.ArgumentParser()
    parser.add_argument('--todir', help='dest dir for special files')
    parser.add_argument('--tozip', help='dest zipfile for special files')
    # TODO: add one more argument definition to parse the 'from_dir' argument
    parser.add_argument('fromdir', help='src dir for local files')
    ns = parser.parse_args(args)
    all_paths = get_special_paths(ns.fromdir)

    # TODO: you must write your own code to get the command line args.
    # Read the docs and examples for the argparse module about how to do this.

    # Parsing command line arguments is a must-have skill.
    # This is input data validation. If something is wrong (or missing) with
    # any required args, the general rule is to print a usage message and
    # exit(1).

    # Your code here: Invoke (call) your functions

    if ns.todir:
        copy_to(ns.todir, all_paths)
    if ns.tozip:
        zip_to(all_paths, ns.tozip)
    if not ns.todir and not ns.tozip:
        print('\n'.join(all_paths))


if __name__ == "__main__":
    main(sys.argv[1:])
