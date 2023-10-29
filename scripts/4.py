# https://adventofcode.com/2022/day/4

from utils import get_data


def is_subset_range(r1,r2):
    smaller,larger = sorted([r1,r2],key=len) 
    return set(smaller).issubset(larger)

def string_to_ranges(string):
    r1,r2 = [i.split('-') for i in string.strip().split(',')]
    r1 = range(eval(r1[0]),eval(r1[1])+1)
    r2 = range(eval(r2[0]),eval(r2[1])+1)
    return r1,r2

def intersect(r1,r2):
    return not (set(r1).isdisjoint(r2))

if __name__=='__main__':
    fp = get_data('https://adventofcode.com/2022/day/4/input')
    with open(fp) as f:
        data = f.readlines()
    data = [string_to_ranges(i) for i in data]
    ans_p1 = sum(is_subset_range(*i) for i in data)
    print(ans_p1)
    ans_p2 = sum(intersect(*i) for i in data)
    print(ans_p2)