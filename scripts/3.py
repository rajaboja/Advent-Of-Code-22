# https://adventofcode.com/2022/day/3
from utils import get_data
from string import ascii_letters
url = "https://adventofcode.com/2022/day/3/input"



def find_score(strings):
    if isinstance(strings,str):
        idx = len(strings)//2
        strings = [strings[:idx],strings[idx:]]
    common_char,*_ = set.intersection(*[set(i) for i in strings])
    return ascii_letters.index(common_char)+1


if __name__=='__main__':
    fp = get_data(url)
    with open(fp) as f:
        data = f.read()
    data = [i.strip() for i in data.split('\n') if i]
    ans_1 = sum(find_score(i) for i in data)
    print(ans_1)
    ans_2 =sum(find_score(data[i:i+3]) for i in range(0,len(data),3))
    print(ans_2)
