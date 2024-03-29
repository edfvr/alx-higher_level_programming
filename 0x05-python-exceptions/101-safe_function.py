#!/usr/bin/python3
import sys

def safe_function(fct, *args):
    try:
        result = fct(*args)
        return result
    except Exception as e:
        print("Excpetion:", str(e), file=sys.stderr)
        return None
