from django.shortcuts import render
from  testmodel.models import Node

def runoob(request):
    context = {}
    context['hello'] = 'Hello World'
    return render(request, 'runoob.html', context)

def nodes(request):
    if 1:
        node = Node(name='cn1', homo_linpack='1', heter_linpack='1', heter_dgemm='1', heter_stream='1')
        node.save()


    nodes = Node.objects.all()[:10]
    context_list = []
    for node in nodes:
        context = {}
        context['name'] = node.name
        context['homo_linpack'] = node.homo_linpack
        context['heter_linpack'] = node.heter_linpack
        context['heter_dgemm'] = node.heter_dgemm
        context['heter_stream'] = node.heter_stream
        context_list.append(context)
    print(context_list)
    return render(request, 'nodes.html', {'context_list': context_list})


