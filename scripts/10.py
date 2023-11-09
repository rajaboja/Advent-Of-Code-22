from utils import get_data

url = "https://adventofcode.com/2022/day/10/input"


    


if __name__=="__main__":
    fp = get_data(url)
    with open(fp) as f:
        data = f.readlines()

    cycles=0
    score=0
    X=[1]
    cycle_pos = []

    for i,j in enumerate(data):
        x=sum(X[:i+1])
        if not 'noop' in j:
            n = j.split(' ')[-1]
            for _ in range(2):
                cycles+=1
                cycle_pos.append((cycles-1,x))
                if (cycles-20)%40==0:
                    score+=cycles*x
            X.append(int(n))
        else:
            X.append(0)
            cycles+=1
            cycle_pos.append((cycles-1,x))
            if (cycles-20)%40==0:
                score+=cycles*x

    print(score)
    screen_string = ['#' if i%40 in [j,j-1,j+1] else '.' for i,j in cycle_pos]
    screen_string = [''.join(screen_string[i:i+40]) for i in range(0,len(screen_string),40)]
    print('\n'.join(screen_string))





