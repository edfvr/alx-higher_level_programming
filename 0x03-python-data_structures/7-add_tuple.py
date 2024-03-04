#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    a_tuple = tuple_a[:2] + (0,)*(2-len(tuple_a[:2]))
    b_tuple = tuple_b[:2] + (0,)*(2-len(tuple_b[:2]))
    return(a_tuple[0] + b_tuple[0], a_tuple[1] + b_tuple[1])
