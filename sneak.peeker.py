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
    parser_commit.set_defaults(func=commit)
    
    # Main
    args = parser.parse_args()
    args.func(args)

# Creates .snk dir in current directory
def init(args):
    print "INIT"
    if os.path.isdir(prog_dir):
        print "Existing %s directory in %s" % (prog, prog_dir)
        exit(1)
    os.makedirs(prog_dir) 
    print "Initialized empty %s directory in %s" % (prog, prog_dir)

# Parses 
def add(args):
    print "ADD"

def commit(args):
    print "COMMIT"

if __name__ == "__main__":
    main()
