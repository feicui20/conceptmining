# encoding=utf-8

import sys
import numpy
import matplotlib.pyplot as plt

sys.path.insert(0, 'C:\\snap\\snap-4.1.0-4.1-Win-x64-py2.7')
import snap
reload(sys)
sys.setdefaultencoding('utf-8')


def cos(a, b):
    a = numpy.array(a)
    b = numpy.array(b)
    if sum(a) == 0 or sum(b) == 0:
        return 0
    else:
        return (sum(a * b))/((sum(a*a)**0.5)*(sum(b*b)**0.5))


def nbrgen(Graph, nodeid):
    node = Graph.GetNI(nodeid)
    degree = node.GetDeg()
    NIdV = snap.TIntV()
    for i in range(degree):
        NIdV.Add(node.GetNbrNId(i))
    NIdV.Add(nodeid)
    return NIdV


def subgraphgen(Graph, NIdV):
    SubGraph = snap.GetSubGraph(Graph, NIdV)
    return SubGraph


def nbrofnbr(Graph, NIdV):
    NNIdV = snap.TIntV()
    for nodeid in NIdV:
        node = Graph.GetNI(nodeid)
        degree = node.GetDeg()
        for i in range(degree):
            if not node.GetNbrNId(i) in NNIdV:
               NNIdV.Add(node.GetNbrNId(i))
    return NNIdV


def vec(Graph, nodeid):
    node = Graph.GetNI(nodeid)
    degree = node.GetDeg()
    NIdV = nbrgen(Graph, nodeid)
    SubGraph = subgraphgen(Graph, NIdV)
    vbr = SubGraph.GetEdges()
    NNIdV = nbrofnbr(Graph, NIdV)
    SubSubGraph = subgraphgen(Graph, NNIdV)
    vminus = SubSubGraph.GetEdges()-SubGraph.GetEdges()
    return numpy.array([degree, vbr, vminus])


year_list = ["{}".format(i) for i in range(2001, 2011)]
for year in year_list:

    Graph = snap.LoadEdgeList(snap.PUNGraph, "graph\\graph{}".format(year), 0, 1)
    word_dict = dict()
    with open("dict\\dict{}".format(year), 'r') as f:
        for line in f.readlines():
            word_dict[line.split()[0]] = int(line.split()[1])
    dict_word = dict([val, key] for key,val in word_dict.items())
    # if '贫困' not in word_dict.keys():
    #     print(year+" no")
    #     continue
    a = vec(Graph, word_dict['改革'])

    a_list = []
    l = []
    m = []
    for v in Graph.Nodes():
        b = vec(Graph, v.GetId())
        cosin = cos(a, b)
        l.append([v.GetId(), cosin])
        b = numpy.ndarray.tolist(b)
        a_list.append(b)
        m.append(v.GetDeg())

    print(m)
    # l.sort(key=lambda x:x[1], reverse=True)
    # ll = [item[1] for item in l]
    # plt.hist(ll, bins=20)
    # plt.show()
    # print(l[:10])
    # with open("text.txt", 'a') as f:
    #     f.write(year+" "+" ".join([dict_word[l[i][0]] for i in range(10)])+'\n')
    # print(l.sort(axis=1, reverse=True))
