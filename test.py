#!/usr/bin/env python3
#
# This VERY COOL program is Copyright (c) 2023 Michael Greenberg.

import sys

if __name__ == "__main__":
    print(f'got {len(sys.argv)} arguments:')

    i = 0
    for arg in sys.argv:
        print(f'\t{i}: {arg}')
        
        i += 1
