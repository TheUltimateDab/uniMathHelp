#!/usr/bin/env python3

# how to handle html forms in python: https://www.youtube.com/watch?v=hV1NWnbC-D8

print("Content-type: text/html\n\n")

import cgi

form = cgi.FieldStorage()

RREF = form.getvalue("get RREF")

transpose = form.getvalue("get transpose of matrix")

rank = form.getvalue("get rank of matrix")

print(RREF + transpose + rank)