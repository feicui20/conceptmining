# encoding=utf-8
import sys
sys.path.insert(0, 'C:\\snap\\snap-4.1.0-4.1-Win-x64-py2.7')
import snap
import json
reload(sys)
sys.setdefaultencoding('utf-8')
from graphviz import Digraph


def alter(file, old_str, new_str):
    file_data = ""
    with open(file, "r") as f:
        for line in f:
            if old_str in line:
                line = line.replace(old_str, new_str)
            file_data += line
    with open(file, "w") as f:
        f.write(file_data)


def alter2(file, index, color):
    file_data = ""
    with open(file, "r") as f:
        for line in f:
            if line.split()[0] == str(index):
                # line = line.replace(']', ', fillcolor="{}", style=filled]'.format(color))
                line += '{} [fillcolor="{}", style=filled]\n'.format(index, color)
            file_data += line
    with open(file, "w") as f:
        f.write(file_data)


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




year_list = ["{}".format(i) for i in range(2001, 2011)]


for year in year_list:
    graph_list = []
    dict_of_word = {}
    with open('graph{}.txt'.format(year), 'r') as f:
        for line in f.readlines():
            if line.split():
                graph_list.append(line.split())
    Graph = snap.TUNGraph.New()
    for w1, w2 in graph_list:
        if w1 not in dict_of_word.keys():
            dict_of_word[w1] = len(dict_of_word)
        if w2 not in dict_of_word.keys():
            dict_of_word[w2] = len(dict_of_word)
    word_of_dict = dict([val, key] for key,val in dict_of_word.items())
    for w1, w2 in graph_list:
        v1 = dict_of_word[w1]
        v2 = dict_of_word[w2]
        if not Graph.IsNode(v1):
            Graph.AddNode(v1)
        if not Graph.IsNode(v2):
            Graph.AddNode(v2)
        if not Graph.IsEdge(v1, v2) and v1 != v2:
            Graph.AddEdge(v1, v2)
    snap.SaveEdgeList(Graph, 'graph{}'.format(year))
    with open('dict{}'.format(year), 'w') as f:
        for w1, w2 in dict_of_word.items():
            f.write(w1+' '+str(w2)+'\n')
    # v = dict_of_word['改革']
    #
    # nodefirst = v
    # node = Graph.GetNI(nodefirst)
    #
    # degree = node.GetDeg()
    # Nlist = snap.TIntV()
    # NIdV = snap.TIntV()
    #
    # for i in range(degree):
    #     if node.GetNbrNId(i) != nodefirst:
    #         NIdV.Add(node.GetNbrNId(i))
    #         Nlist.Add(node.GetNbrNId(i))
    #
    # NNIdV = snap.TIntV()
    # for nodeid in NIdV:
    #     node = Graph.GetNI(nodeid)
    #     degree = node.GetDeg()
    #     for i in range(degree):
    #         if not node.GetNbrNId(i) in NIdV and not node.GetNbrNId(i) in NNIdV and node.GetNbrNId(i) != nodefirst:
    #             NNIdV.Add(node.GetNbrNId(i))
    #             Nlist.Add(node.GetNbrNId(i))
    # Nlist.Add(nodefirst)
    # SubGraph = snap.GetSubGraph(Graph, Nlist)
    #
    # labels = snap.TIntStrH()
    #
    # for NI in SubGraph.Nodes():
    #     labels[NI.GetId()] = word_of_dict[NI.GetId()]
    #
    # snap.SaveGViz(SubGraph, 'subgraph{}.dot'.format(year), "", labels)
    # alter("subgraph{}.dot".format(year),
    #       'shape=ellipse, width=0.3, height=0.3',
    #       'shape=ellipse, width=0.3, height=0.3, fontname="SimSun" size=\"10,10\"')
    # for i in NIdV:
    #     alter2("subgraph{}.dot".format(year), i, "#65934A")
    # for i in NNIdV:
    #     alter2("subgraph{}.dot".format(year), i, "#A0BF7C")
    #
    # alter2("subgraph{}.dot".format(year), v, "#407434")

