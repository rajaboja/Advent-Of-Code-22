# https://adventofcode.com/2022/day/2

from utils import get_data


data_url = "https://adventofcode.com/2022/day/2/input"
scores_dict = dict(X=1,Y=2,Z=3)
aliases = dict(X='A',Y='B',Z='C')
rules = ['a>c','c>b','b>a']


def get_score(them,me):
    score = scores_dict[me]
    me = aliases[me]
    result = 0
    if them==me:
        result=3
    if f"{me}>{them}".lower() in rules:
        result=6
    return score+result




if __name__=="__main__":
    fp = get_data(data_url)

    with open(fp) as f:
        data = f.read()
    data_arr = [i.strip().split(' ') for i in data.split('\n') if i]
    answer_1 = sum(get_score(arr[0],arr[1]) for arr in data_arr)
    print(answer_1)

