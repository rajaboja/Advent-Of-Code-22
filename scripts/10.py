from utils import get_data

url = "https://adventofcode.com/2022/day/10/input"



def get_score_and_pos(data):
    cycles,score=0,0
    X=1
    pos = []
    
    for i in data:
        for _ in range(len(i)):
            cycles+=1
            pos.append(X)
            if (cycles-20)%40==0:
                score+=cycles*X
        if len(i)>1:
            X+=int(i[-1])        

    return score, pos
    


if __name__=="__main__":
    fp = get_data(url)
    with open(fp) as f:
        data = f.readlines()
    data = [i.strip().split(' ') for i in data]

    score,pos = get_score_and_pos(data)
    print(score)

    screen_string = [('#' if i%40 in range(j-1,j+2) else '.') for i,j in enumerate(pos)]
    screen_string = [''.join(screen_string[i:i+40]) for i in range(0,len(screen_string),40)]
    print('\n'.join(screen_string))





