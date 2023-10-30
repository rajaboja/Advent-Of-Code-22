from utils import get_data
import pandas as pd
from io import StringIO
import re
import copy

url = 'https://adventofcode.com/2022/day/5/input'
r = re.compile("move (\d+) from (\d+) to (\d+)")

def find_top_crate(records,moves,reverse=True):
    for move in moves:
        n, fro, to = move
        crates = records[fro][-int(n):]
        if reverse:
            crates.reverse()
        records[to].extend(crates)
        records[fro] = records[fro][:-int(n)]
    records = sorted(records.items())
    return ''.join([v[-1] for _,v in records])

def stack_to_records(stack):
    records = (pd.read_fwf(
                StringIO(stack.replace('[',' ')
                .replace(']',' ')[::-1])).fillna('')
                .to_dict(orient='list'))
    records = {k:[i for i in v if i] for k,v in records.items()}
    return records



if __name__=='__main__':
    fp = get_data('https://adventofcode.com/2022/day/5/input')
    with open(fp) as f:
        data = f.read()

    stack, moves = data.split('\n\n')
    
    moves = [r.findall(i)[0] for i in moves.splitlines() if i]
    original_records = stack_to_records(stack)

    ans_1 = find_top_crate(copy.deepcopy(original_records),moves)
    print(ans_1)

    ans_2 = find_top_crate(original_records,moves,reverse=False)
    print(ans_2)