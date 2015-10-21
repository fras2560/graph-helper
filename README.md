# graph-helper
A python package with algorithms to help with graph theory coloring and more.

Algorithms
-----------
color: colors a graph
	```sh
	from algorithms import color
	color(G)
	```

contains: checks if a graph contains an induced subgraph
	```sh
	from algorithms import contains
	contains(G)
	```
critical: checks if the graph is critical
	```sh
	from algorithms import critical
	critical(G)
	```
	
clique_cutset: check if a graph has a clique cutset
	```sh
	from algorithms import clique_cutset
	clique_cutset(G)
	```

strong_stable_set: check if a graph has a strong stable set
	```sh
	from algorithms import strong_stable_set
	strong_stable_set(G)
	```

Install Dependencies
-----------
```sh
	pip install networkx
```


Dependencies
-----------
* [Networkx] - NetworkX is a Python language software package for the creation, manipulation, and study of the structure, dynamics, and functions of complex networks.


Contact
-----------
Feel free to contact me for ideas and help at [fras2560@mylaurier.ca]

License
----

Apache

[Networkx]:http://networkx.github.io/documentation/networkx-1.9/
[fras2560@mylaurier.ca]:mailto:fras2560@mylaurier.ca
