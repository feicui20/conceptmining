#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May  6 10:48:21 2019

@author: oliver_sun
"""

import os, sys
import jieba, codecs, math
import jieba.posseg as pseg

nouns = {}          # 三农有关专业名词字典
relationships = {}  # 关系字典
lineNames = []      # 每段内专业名词之间的关系

# count nouns
jieba.load_userdict("dict.txt")     # 加载字典
with codecs.open("2018-news.txt", "r", "utf8") as f:
    for line in f.readlines():
        poss = pseg.cut(line)       # 分词并返回该词词性
        lineNames.append([])        # 为新读入的一段添加名词列表
        for w in poss:
            if w.flag != "nr" or len(w.word) < 2:
                continue
            lineNames[-1].append(w.word)    # 为当前段的环境增加一个名词
            if nouns.get(w.word) is None:
                nouns[w.word] = 0
                relationships[w.word] = {}
            nouns[w.word] += 1      # 该名词出现次数加 1
            
# explore relationships
for line in lineNames:
    for nouns1 in line:
        for nouns2 in line:
            if nouns1 == nouns2:
                continue
            if relationships[nouns1].get(nouns2) is None:
                relationships[nouns1][nouns2] = 1
            else:
                relationships[nouns1][nouns2] = relationships[nouns1][nouns2] + 1
                
# output
with codecs.open("sannong_node.csv", "w", "gbk") as f:
    f.write("Id Label Weight\r\n")
    for noun, times in nouns.items():
        f.write(noun + " " + noun + " " + str(times) + "\r\n")

with codecs.open("sannong_edge.csv", "w", "gbk") as f:
    f.write("Source Target Weight\r\n")
    for noun, edges in relationships.items():
        for v, w in edges.items():
            if w > 3:
                f.write(noun + " " + v + " " + str(w) + "\r\n")