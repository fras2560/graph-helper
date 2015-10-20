"""
-------------------------------------------------------
algorithms
a package to hold common algorithms used to find
interesting facts about a graph and its coloring
-------------------------------------------------------
Author:  Dallas Fraser
ID:      110242560
Email:   fras2560@mylaurier.ca
Version: 2014-09-17
-------------------------------------------------------
"""
from color import coloring
from dense_color import dense_color_wrapper
from induced_subgraph import induced_subgraph
def color(G, logger=None, dense=False):
    '''
    a function to color the G with least amount of colors
    IT MAY TAKE AWHILE
    Parameters:
        G: the graph to color (networkx)
        logger: an optional logger argument
        dense: True if the graph is dense (boolean)
    Retuns:
        result: a list of colors where each color is a list of nodes
            E.G [[0],[1],[2]] for K3
    '''
    if not dense:
        result = coloring(G, logger=logger)
    else:
        result = dense_color_wrapper(G, logger=logger)
    return result

def critical(G, logger=None, dense=False):
    '''
    a method that finds if the graph is is_critical
    Parameters:
        G: the graph to check (networkx)
        logger: an optional logger
        dense: True if the graph is quite dense (boolean)
    Returns:
        K: how many colors the graphs need to be colored (int),
            None if the graph is not critical
    '''
    if dense:
        coloring = color
    else:
        coloring = dense_color_wrapper
    is_critical = True
    nodes = G.nodes()
    index = 0
    chromatic = len(coloring(G))
    while is_critical and index < len(nodes):
        g = G.copy()
        g.remove_node(nodes[index])
        check = len(coloring(g))
        if check != (chromatic -1):
            if logger is not None:
                logger.info(index)
                logger.info("G is not critical")
            is_critical = False
        index += 1
    K = None
    if is_critical:
        K = chromatic
    return K

def contains(G, H):
    '''
    checks if G contains an induced subgraph of H
    Parameters:
        G: the graph to check (networkx)
        H: the graph to check for (networkx)
    Returns:
        a list of vertices that form the induced subgraph (list)
        None if no induced subgraph exists
    '''
    return induced_subgraph(G, H)

