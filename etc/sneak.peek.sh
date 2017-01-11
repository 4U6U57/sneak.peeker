#!/bin/sh
# $Id: sneak.peek.sh,v 1.3 2016-10-31 12:43:09-07 - - $
cat $0
cat $* | tr A-Z a-z | tr -c '[:alnum:]' '\n' | sort | uniq | fmt
