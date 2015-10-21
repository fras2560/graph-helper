"""
-------------------------------------------------------
This program analyzes (C4,C5,4K1)-free graphs.

We are primarily interested in which graphs from this class
contains a strong stable set which meets all the maximal 
cliques of the graph in question. If no such strong stable
set exists, we wonder if the chromatic number is equal
to the ceiling of n/3.
-------------------------------------------------------
Author:  Tom LaMantia, Dallas Fraser
Email:   lama3790@mylaurier.ca, fras2560@mylaurier.ca
Version: 2015-10-21
-------------------------------------------------------
"""
from networkx import find_cliques, maximal_independent_set, graph_clique_number
from networkx.exception import NetworkXUnfeasible
from networkx import complement
"""
-------------------------------------------------------
This function finds the largest clique in a NetworkX graph.

Preconditions: G, a NetworkX graph.

Postconditions: This function returns a list of lists, where each list entry
contains a list of vertices which comprise the largest clique(s)
in G.
-------------------------------------------------------
"""
def findLargestCliques(G):
    maximalCliques = list(find_cliques(G))
    largestSoFar = len(maximalCliques[0])
    for thisClique in maximalCliques:
        if len(thisClique) > largestSoFar:
            largestSoFar = len(thisClique)
            
    result = list()
    for thisClique in maximalCliques:
        if len(thisClique) == largestSoFar:
            result.append(thisClique)
    return result

"""
-------------------------------------------------------
This function takes a NetworkX graph G and returns a strong
stable set belonging to G, if such a stable set exists, and
returns None otherwise.
-------------------------------------------------------
"""
def FindStrongStableSet(G):
    result = None
    maximalCliques = findLargestCliques(G)
    V = G.nodes()
    for thisVertex in V:
        #Find maximum stable sets which contain each vertex of G
        try:
            verticesToInclude = list()
            verticesToInclude.append(thisVertex)
            thisMaximalStableSet = maximal_independent_set(G, verticesToInclude)
        except NetworkXUnfeasible:
            thisMaximalStableSet = []
        #Now determine if thisMaximumStableSet is strong, that is, meets every maximal clique
        foundStrongStableSet = True
        for thisMaximalClique in maximalCliques:
            if set(thisMaximalStableSet).isdisjoint(set(thisMaximalClique)):
                foundStrongStableSet = False
                break
        if foundStrongStableSet == True:
            result = thisMaximalStableSet
            break
    return result

def strong_stable_set(G):
    clique = graph_clique_number(G)
    result = None
    for stable in stable_set(G):
        g = G.copy()
        for node in stable:
            g.remove_node(node)
        if clique != graph_clique_number(g):
            result = G.subgraph(stable)
            break;
    return result

def stable_set(G):
    co_g = complement(G)
    for clique in find_cliques(co_g):
        yield clique

import unittest
from helper import make_clique, make_diamond, make_cycle
import networkx as nx
class Test(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testStableSet(self):
        expect = [[0], [1], [2, 3]]
        for i in stable_set(make_diamond()):
            self.assertEqual(i in expect, True)

    def testStrongStableSet(self):
        g = nx.Graph()
        g.add_node(0)
        # check a triangle
        result = strong_stable_set(make_clique(3))
        self.assertEqual(result.nodes(), g.nodes())
        # check a diamond
        result = strong_stable_set(make_diamond())
        self.assertEqual(result.nodes(), g.nodes())
        # C5
        result = strong_stable_set(make_cycle(5))
        self.assertEqual(result, None)

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()