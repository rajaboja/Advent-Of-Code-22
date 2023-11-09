from utils import get_data

url = "https://adventofcode.com/2022/day/10/input"



def get_score_and_pos(data):
    cycles,score,pos=(0,)*3
    X=[1]
    cycle_pos = []
    
    for i,j in enumerate(data):
        pos+=sum(X[i:i+1])
        if not 'noop' in j:
            n = j.split(' ')[-1]
            for _ in range(2):
                cycles+=1
                cycle_pos.append((cycles-1,pos))
                if (cycles-20)%40==0:
                    score+=cycles*pos
            X.append(int(n))
        else:
            X.append(0)
            cycles+=1
            cycle_pos.append((cycles-1,pos))
            if (cycles-20)%40==0:
                score+=cycles*pos
    return score, cycle_pos
    


if __name__=="__main__":
    fp = get_data(url)
    with open(fp) as f:
        data = f.readlines()

    score,cycle_pos = get_score_and_pos(data)
    print(score)

    screen_string = [('#' if i%40 in range(j-1,j+2) else '.') for i,j in cycle_pos]
    screen_string = [''.join(screen_string[i:i+40]) for i in range(0,len(screen_string),40)]
    print('\n'.join(screen_string))





