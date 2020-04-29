import pandas as pd
import matplotlib.pyplot as plt
from networkx.drawing.nx_agraph import graphviz_layout, write_dot
import os
import numpy as np
import networkx as nx
import gzip
import wget
import pygraphviz

url = 'https://snap.stanford.edu/data/facebook_combined.txt.gz'
dest_path = './facebook_combined.txt'

# https://stackoverflow.com/questions/52332897/how-to-extract-a-gz-file-in-python/52333182#52333182
def ex1(url, dest_path, block_size):
    filename = url[url.rfind('/') + 1:]
    if not os.path.exists('./' + filename):
        wget.download(url=url, out=filename)
    with gzip.open(filename, 'rb') as s_file, \
            open(dest_path, 'wb') as d_file:
        while True:
            block = s_file.read(block_size)
            if not block:
                break
            else:
                d_file.write(block)
        d_file.write(block)

#ex1(url, dest_path, block_size=65536)


def ex2():
    graph = nx.read_edgelist(dest_path)
    print(nx.info(graph))
    # Type: Graph
    # Number of nodes: 4039
    # Number of edges: 88234
    # Average degree:  43.6910
    nx.draw(graph, pos=graphviz_layout(graph),
            node_size=30, width=.05, cmap=plt.cm.Blues,
            with_labels=True, font_size=4, node_color=range(len(graph)))
    plt.show()

#ex2()


# https://stackoverflow.com/questions/48382575
def ex3():
    graph = nx.read_edgelist(dest_path)
    top10 = sorted(graph.degree, key=lambda x: x[1], reverse=True)[:10]
    print(top10)
    #(node, connections)
    #[('107', 1045), ('1684', 792), ('1912', 755), ('3437', 547), ('0', 347), ('2543', 294), ('2347', 291), ('1888', 254), ('1800', 245), ('1663', 235)]
ex3()