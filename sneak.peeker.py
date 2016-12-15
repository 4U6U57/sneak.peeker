#!/usr/bin/env python

import sys
import argparse
import os

# Global variables
prog = os.path.basename(__file__)
prog_dir = os.path.abspath(".snk")

def main():

    # Top level parser
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers(title='subcommands', description='valid subcommands')

    # Parser for init
    parser_init = subparsers.add_parser("init", help="Initializes the current directory")
    parser_init.set_defaults(func=init)
    
    # Parser for add
    parser_add = subparsers.add_parser("add", help="Adds test files and processes them")
    parser_add.add_argument("tests", metavar="FILE", help="Test file to add and process", nargs='+')
    parser_add.set_defaults(func=add)

    # Parser for commit
    parser_commit = subparsers.add_parser("commit", help="Adds sneak peek file and processes it")
    parser_commit.add_argument("sneak_peek", metavar="FILE", help="Sneak peek file to compare to tests")
    parser_commit.set_defaults(func=commit)
    
    # Main
    args = parser.parse_args()
    args.func(args)

# Creates .snk dir in current directory
def init(args):
    if os.path.isdir(prog_dir):
        print "Existing %s directory in %s" % (prog, prog_dir)
    else:
        os.makedirs(prog_dir) 
        print "Initialized empty %s directory in %s" % (prog, prog_dir)

# Parses 
def add(args):
    if not os.path.isdir(prog_dir):
        print "fatal: not a %s directory: %s" % (prog, prog_dir)
    else:
        for test in args.tests:
            # TODO: Process test file, separating by question and saving
            # files to .snk directory
            print test

def commit(args):
    if not os.path.isdir(prog_dir):
        print "fatal: not a %s directory: %s" % (prog, prog_dir)
    else:
        print args.sneak_peek
        # TODO: Create subfolder in .snk folder for this sneak peek
        # Then process each question file using the sneak peek

if __name__ == "__main__":
    main()
