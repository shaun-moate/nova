#!/usr/bin/env python3

import bin.config as cfg

def uncons(xs):
    return (xs[0], xs[1:])

def iota(reset=False):
    if reset == True:
        cfg.iota_counter = 0
    result = cfg.iota_counter
    cfg.iota_counter += 1
    return result
