import os
from utils import get_data

url = "https://adventofcode.com/2022/day/7/input"
allowed = 7*10**7
least = 3*10**7



def dir_size(path,dir_contents,dirs_and_children):
    size=0
    for i in dir_contents:
        if isinstance(i,int):
            size+=i
        else:
            k = os.path.join(path,i)
            v = dirs_and_children[k]
            size+=dir_size(k,v,dirs_and_children)
    return size







if __name__== "__main__":
    fp = get_data(url)
    with open(fp) as f:
        data = f.read()

    outputs = data.split("$ ")
    cmds = [i.strip('$ \n') for i in data.split("$ ") if i ]

    dirs = []
    dirs_and_children = {}
    for n,i in enumerate(cmds):
        if i.startswith('cd'):
            _,dir_name = i.split(' ')
            if dir_name=='..':
                dirs = dirs[:-1]
            else:
                dirs.append(dir_name)
        else:
            contents = i.splitlines()[1:]
            contents = [i.split(' ') for i in contents if i]
            sub_dirs = [j for i,j in contents if i=='dir']
            fs = sum(int(i) for i,_ in contents if i!='dir')

            key = os.path.join(*dirs)
            dirs_and_children[key] = sub_dirs+[fs]


    
    dir_sizes = {k:dir_size(k,v,dirs_and_children) for k,v in dirs_and_children.items()}
    ans_1 = sum(i for i in dir_sizes.values() if i<=10**5)
    print(ans_1)

   
    total = max(dir_sizes.values())
    ans_2 = min(filter(lambda x:allowed-(total-x)>=least,dir_sizes.values()))
    print(ans_2)