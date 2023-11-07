from utils import get_data

url = "https://adventofcode.com/2022/day/10/input"



if __name__=="__main__":
    fp = get_data(url)
    with open(fp) as f:
        data = f.readlines()

    cycles=0
    score=0
    X=[]

    for i,j in enumerate(data):
        x=sum(X[:i])+1
        if not 'noop' in j:
            n = j.split(' ')[-1]
            for _ in range(2):
                cycles+=1
                if (cycles-20)%40==0:
                    score+=cycles*x
            X.append(int(n))
        else:
            X.append(0)
            cycles+=1
            if (cycles-20)%40==0:
                score+=cycles*x

    print(score)







