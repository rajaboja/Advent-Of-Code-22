from utils import get_data
import re
from itertools import compress
from operator import not_,mul
from functools import reduce

input_url = "https://adventofcode.com/2022/day/11/input"
r = re.compile("^[\w ]+:\n\s{2}[\w ]+:([\d, ]+)\n\s{2}\w+:(.+)\n\s{2}\w+:[a-z ]+(\d+)\n\s{4}[\w ]+:[a-z ]+(\d+)\n\s{4}[\w ]+:[a-z ]+(\d+)",re.MULTILINE)


def clean_up_data(data):
    matches = r.findall(data)
    cleaned = []
    for  i in matches:
        wlevel,expr,cond,pos,neg = i
        wlevel = list(map(int,wlevel.split(', ')))
        cond,pos,neg = map(int,(cond,pos,neg))
        cleaned.append((wlevel,expr.strip(),cond,pos,neg))    
    return cleaned

def condition(values,expr,denom):
    expr = expr.split(" = ")[-1]
    values = [eval(expr)//3 for old in values]
    cond = [i%denom==0 for i in values]
    return list(compress(values,cond)), list(compress(values,map(not_,cond)))

def iteration(data):
    n_items = []
    for i in range(len(data)):
        n_items.append(len(data[i][0]))
        pos,neg = condition(*data[i][:3])
        data[data[i][-2]][0].extend(pos)
        data[data[i][-1]][0].extend(neg)
        data[i][0].clear()
    return data,n_items

if __name__=="__main__":
    fp = get_data(input_url)
    with open(fp) as f:
        data = f.read()
    clean_data = clean_up_data(data)
    total_items = [0]*len(data)
    for _ in range(20):
        clean_data ,n_items= iteration(clean_data)
        total_items = [sum(i) for i in zip(total_items,n_items)]
    answer_1 = reduce(mul,sorted(total_items)[-2:])
    print(answer_1)

