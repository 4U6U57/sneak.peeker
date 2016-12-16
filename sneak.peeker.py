#!/usr/bin/env python

import sys
import argparse
import os

# Global variables
prog = os.path.basename(__file__)
prog_dir = ".snk"
test_prefix = "test__"

def main():

    # Top level parser
    parser = argparse.ArgumentParser()
    parser.add_argument("-d", "--directory", metavar="DIR", help="directory to save program files", default=prog_dir)
    parser.add_argument("-v", "--verbose", action="store_true", help="show additional output")
    subparsers = parser.add_subparsers(title='subcommands', description='valid subcommands')

    # Parser for init
    parser_init = subparsers.add_parser("init", help="initializes the current directory")
    parser_init.set_defaults(func=init)

    # Parser for add
    parser_add = subparsers.add_parser("add", help="adds test files and processes them")
    parser_add.add_argument("tests", metavar="FILE", help="test file to add and process", nargs='+')
    parser_add.set_defaults(func=add)

    # Parser for commit
    parser_commit = subparsers.add_parser("commit", help="adds sneak peek file and processes it")
    parser_commit.add_argument("sneak_peek", metavar="FILE", help="sneak peek file to compare to tests")
    parser_commit.set_defaults(func=commit)

    # Main
    args = parser.parse_args()
    if args.verbose: print "%s ran with verbose output" % prog
    args.directory = os.path.abspath(args.directory)
    if args.verbose: print "%s directory: %s" % (prog, args.directory)
    args.func(args)

# Creates .snk dir in current directory
def init(args):
    if os.path.isdir(args.directory):
        print "Existing %s directory: %s" % (prog, args.directory)
    else:
        os.makedirs(args.directory)
        print "Initialized empty %s directory: %s" % (prog, args.directory)

# Parses
def add(args):
    if not os.path.isdir(args.directory):
        print "fatal: not a %s directory: %s" % (prog, args.directory)
    else:
        for test in args.tests:
            # TODO: Handle UNIX file expressions, wildcards, etc
            # For now handling each test as explicit filename
            test_file = os.path.abspath(test)
            test_name = os.path.basename(test_file)
            test_dir = args.directory + "/" + test_prefix + test_name
            if not os.path.isfile(test_file):
                print "warning: test %s cannot be found, ignoring: %s" % (test_name, test_file)
            elif os.path.isdir(test_dir):
                print "warning: test %s already exists, ignoring: %s" % (test_name, test_dir)
            else:
                print "%s is a valid file: %s" % (test, test_file)
                os.makedirs(test_dir)
                if args.verbose: print "Created test directory: %s" % test_dir

def commit(args):
    if not os.path.isdir(args.directory):
        print "fatal: not a %s directory: %s" % (prog, args.directory)
    else:
        print args.sneak_peek
        # TODO: Create subfolder in .snk folder for this sneak peek
        # Then process each question file using the sneak peek

if __name__ == "__main__":
    main()
