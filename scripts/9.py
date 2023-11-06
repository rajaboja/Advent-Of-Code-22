from utils import get_data


url = "https://adventofcode.com/2022/day/9/input"
sign = {'R':1,'U':1,'D':-1,'L':-1}



def n_new_coordinates(start_coords,move):
    direction,n = move.strip().split(' ')
    coord = direction not in 'RL'
    value = sign[direction]
    tails = []

    for _ in range(int(n)):
        head=start_coords[0]
        head[coord]+= value
        start_coords[0] = head

        for i in range(1,len(start_coords)):
            tail = start_coords[i]
            x,y = [(a-b) for a,b in zip(head,tail)]
            if max(map(abs,[x,y]))>1:
                tail[0]+=x//(abs(x) or 1)
                tail[1]+=y//(abs(y) or 1)

                start_coords[i]=tail
            head = tail
        tails.append(tuple(start_coords[-1]))
    return start_coords,tails

    
def unique_points(data,n):
    all_tails = []
    start_coords = [[0,0] for _ in range(n)]

    for i in data:
        start_coords, tails = n_new_coordinates(start_coords,i)
        all_tails.extend(tails)
            
    return len(set(all_tails))


if __name__=='__main__':
    fp = get_data(url)
    with open(fp) as f:
        data = f.readlines()

    print(unique_points(data,2))
    print(unique_points(data,10))

            
    

