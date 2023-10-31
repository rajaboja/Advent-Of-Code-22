from utils import get_data

url = "https://adventofcode.com/2022/day/6/input"

def n_unique(data,n=4):
    for i in range(len(data)):
        string = data[i:i+n]
        if len(string)==len(set(string)):
            ans_1 = i+n
            break
    return ans_1



if __name__=='__main__':
    fp = get_data(url)
    with open(fp) as f:
        data = f.read()
    
    print(n_unique(data))
    print(n_unique(data,n=14))
