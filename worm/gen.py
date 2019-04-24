# encoding=utf-8
import sys
sys.path.insert(0, 'C:\\snap\\snap-4.1.0-4.1-Win-x64-py2.7')
import snap


def alter(file, old_str, new_str):
    file_data = ""
    with open(file, "r") as f:
        for line in f:
            if old_str in line:
                line = line.replace(old_str, new_str)
            file_data += line
    with open(file, "w") as f:
        f.write(file_data)


for year in ['2008', '2018']:
    graph_list = []
    dict_of_word = {}
    with open('graph{}.txt'.format(year), 'r') as f:
        for line in f.readlines():
            if line.split():
                graph_list.append(line.split())
    Graph = snap.PUNGraph.New()
    for w1, w2 in graph_list:
        if w1 not in dict_of_word.keys():
            dict_of_word[w1] = len(dict_of_word)
        if w2 not in dict_of_word.keys():
            dict_of_word[w2] = len(dict_of_word)

    for w1, w2 in graph_list:
        v1 = dict_of_word[w1]
        v2 = dict_of_word[w2]
        if not Graph.IsNode(v1):
            Graph.AddNode(v1)
        if not Graph.IsNode(v2):
            Graph.AddNode(v2)
        if not Graph.IsEdge(v1, v2) and v1 != v2:
            Graph.AddEdge(v1, v2)
    # labels = snap.TIntStrH()
    #
    # for NI in Graph.Nodes():
    #     labels[NI.GetId()] = str(dict_of_word.keys()[NI.GetId()])

    # snap.SaveGViz(Graph, 'graph{}.dot'.format(year), "", labels)
    snap.SaveGViz(Graph, 'graph{}.dot'.format(year), "")

    # alter('graph{}.dot'.format(year),
    #       'shape=ellipse, width=0.3, height=0.3',
    #       'shape=ellipse, width=0.3, height=0.3, fontname="SimSun" size=\"20,20\"')

