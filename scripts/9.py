from utils import get_data

url = "https://adventofcode.com/2022/day/9/input"
sign = {'R':1,'U':1,'D':-1,'L':-1}

def new_coordinates(tail,head,move):
    direction,n = move.strip().split(' ')
    value = sign[direction]
    coord = direction not in 'RL'
    tails = []
    for _ in range(int(n)):
        head[coord]+= value
        if max(abs(a-b) for a,b in zip(tail,head))>1:
            if all([head[0]!=tail[0],head[1]!=tail[1]]):
                tail[coord]+=value
                tail[not coord]=head[not coord]
            else:
                tail[coord]+=value
            tails.append(tuple(tail))
    return tail,head,tails


    


if __name__=='__main__':
    fp = get_data(url)
    with open(fp) as f:
        data = f.readlines()
    head=[0,0]
    tail=[0,0]
    all_tails = []
    
    for i in data:
        tail, head, tails = new_coordinates(tail,head,i)
        all_tails.extend(tails)
            
    answer_1 = len(set(all_tails))+1
    print(answer_1)
            
    

