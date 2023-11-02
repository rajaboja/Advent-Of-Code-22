# https://adventofcode.com/2022/day/8

from functools import reduce
from utils import get_data
from typing import List
from operator import mul

url = "https://adventofcode.com/2022/day/8/input"


def is_visible(length:int,surroundings:List[List[str]]):
    return not all(any(j>=length for j in i) for i in surroundings)


def scenic_score(length,surroundings):
    scores=[]
    for side in surroundings:
        distance=0
        for tree in side:
            distance+=1
            if tree>=length:
                break
        scores.append(distance)
    return reduce(mul,scores)

        
def forest_stats(data):
    visible = 0
    n_rows,n_columns = len(data),len(data[0])
    scores = []
    for i in range(n_rows):
        for j in range(n_columns):
            if (i in [0,n_rows-1]) or (j in ([0,n_columns-1])):
                visible+=1
                continue

            len_tree = data[i][j]
            surroundings=[]
            surroundings.append(data[i][:j][::-1])
            surroundings.append(data[i][j+1:])
            surroundings.append([data[k][j] for k in range(0,i)][::-1])
            surroundings.append([data[k][j] for k in range(i+1,n_rows)])

            visible+=is_visible(len_tree,surroundings)
            scores.append(scenic_score(len_tree,surroundings))

    return visible, max(scores)

if __name__=="__main__":
    fp = get_data(url)
    with open(fp) as f:
        data = f.read()

    data = [list(i.strip('\n')) for i in data.splitlines() if i]

    visible, max_score = forest_stats(data)
    

    print(visible)
    print(max_score)