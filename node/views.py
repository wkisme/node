from django.shortcuts import render
from  testmodel.models import Node
from ClusterShell.NodeSet import NodeSet

def runoob(request):
    context = {}
    context['hello'] = 'Hello World'
    return render(request, 'runoob.html', context)

def nodes(request):

    # nodes = Node.objects.all()[:10]
    # nodes = Node.objects.filter(name__contains='cn0')
    # nodes = Node.objects.filter(name__gt='cn0').order_by('name')
    nodes = Node.objects.order_by('cab')
    nodes = Node.objects.filter(cab__in=[0,4], homo_linpack=0)

    aggre_nodes = []
    context_list = []
    for node in nodes:
        aggre_nodes.append(node.name)

        context = {}
        context['name'] = node.name
        context['memtest'] = node.memtest
        context['homo_linpack'] = node.homo_linpack
        context['heter_linpack'] = node.heter_linpack
        context['heter_dgemm'] = node.heter_dgemm
        context['heter_stream'] = node.heter_stream
        context['change_time'] = node.change_time
        context['cab'] = node.cab
        context_list.append(context)
    print(context_list)
    aggre_nodes = ','.join(aggre_nodes)
    aggre_nodes = NodeSet(aggre_nodes)  # NodeSet input type need to be string
    print("\033[0;34m------------------------\033[0m")
    print("\033[0;34m{}  {} ({})\033[0m".format('aggre_nodes:', aggre_nodes, len(aggre_nodes)))
    print("\033[0;34m------------------------\033[0m")

    return render(request, 'nodes.html', {'context_list': context_list})


def AddNodes(request):
    nodes = 'cn[5000-5100]'
    nodes = NodeSet(nodes)

    for node in nodes:
        a = Node(name=node, memtest='1', homo_linpack='0', heter_linpack='0', heter_dgemm='0', heter_stream='0')
        print(node.split('cn'))
        a.cab = str(int((int(node.split('cn')[-1]) / 1024)))  # compute cab num through node's name
        a.save()

    nodes = Node.objects.order_by('-change_time')[:10] # get the last ten elements to confirm add successfully.



    context_list = []
    for node in nodes:
        context = {}
        context['name'] = node.name
        context['memtest'] = node.memtest
        context['homo_linpack'] = node.homo_linpack
        context['heter_linpack'] = node.heter_linpack
        context['heter_dgemm'] = node.heter_dgemm
        context['heter_stream'] = node.heter_stream
        context['change_time'] = node.change_time
        context['cab'] = node.cab
        context_list.append(context)
    print(context_list)
    return render(request, 'AddNodes.html', {'context_list': context_list})



