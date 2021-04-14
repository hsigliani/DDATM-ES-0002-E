import sys


def complete_array(arr):
    _max = 0
    for x in arr:
        if type(x) == int and x >= 0:
            _max = max(_max, x)
        else:
            raise Exception('Array should be of positive integer numbers')

    return [i for i in range(1, _max + 1)]


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print('usage: python main.py <integer array> # without spaces between eg. [1,12,4]')
    else:
        arr = sys.argv[1][1:len(sys.argv[1])-1].split(',')
        print(complete_array([int(i) for i in arr]))
