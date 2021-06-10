
from ClusterShell.NodeSet import NodeSet

if __name__ == '__main__':
    a = ['cn1', 'cn2']
    a = ','.join(a)
    print(a)
    a = NodeSet(a)
    print(a)
    for i in a:
        print(i)