#!/usr/bin/env python3

import sys

if __name__ == "__main__":
    print(f'got {len(sys.argv)} arguments:')

    i = 0
    for arg in sys.argv:
        print(f'    {i}: {arg}')
        i += 1
