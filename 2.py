# https://adventofcode.com/2022/day/2

from utils import get_data


data_url = "https://adventofcode.com/2022/day/2/input"

scores_dict = dict(A=1,B=2,C=3)
aliases = dict(X='A',Y='B',Z='C')
rules = ['A>C','C>B','B>A']
outcome_scores = dict(X=0,Y=3,Z=6)

def get_score(them,me):
    me = aliases[me]
    score = scores_dict[me]
    result = 0
    if them==me:
        result=3
    if f"{me}>{them}" in rules:
        result=6
    return score+result

def get_score_2(them,outcome):
    score = outcome_scores[outcome]
    if outcome=='Y':
        me = them
    elif outcome=='Z':
        string = '>'+them
        me = [i.strip(string) for i in rules if i.endswith(string) ][0]
    else:
        string = them+'>'
        me = [i.strip(string) for i in rules if i.startswith(string)][0]
    score += scores_dict[me]
    return score

if __name__=="__main__":
    fp = get_data(data_url)

    with open(fp) as f:
        data = f.read()
    data_arr = [i.strip().split(' ') for i in data.split('\n') if i]
    answer_1 = sum(get_score(*arr) for arr in data_arr)
    print(answer_1)

    answer_2 = sum(get_score_2(*arr) for arr in data_arr)
    print(answer_2)


