import sys

if __name__ == "__main__":
    print(f'got {len(sys.argv)} arguments:')
    for arg in sys.argv:
        print(arg)
