#!/usr/bin/env python

import sys
import argparse

def main():

    # Top level parser
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers(title='subcommands',
            description='valid subcommands')

    # Parser for init
    parser_init = subparsers.add_parser("init", help="Initializes the current directory")
    parser_init.add_argument("FILE", help="Test files to add and process")
    parser_init.set_defaults(func=init)
    
    # Parser for add
    parser_add = subparsers.add_parser("add", help="Adds test files and processes them")
    parser_add.set_defaults(func=add)

    # Parser for commit
    parser_commit = subparsers.add_parser("commit", help="Adds sneak peek file and processes it")
    parser_commit.set_defaults(func=commit)
    
    # Main
    args = parser.parse_args()
    args.func(args)

def init(args):
    print "INIT"

def add(args):
    print "ADD"

def commit(args):
    print "COMMIT"

if __name__ == "__main__":
    main()
