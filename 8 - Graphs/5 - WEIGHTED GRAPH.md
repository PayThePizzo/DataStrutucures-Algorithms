# Weighted Graphs
Weighted graphs are graphs <mark>G(V,E, w) where w is a weight function</mark> that
can be associated with vertices, edges or both.

For this reason we can derive three types of weighted graphs
* Graphs weighted on vertices
* Graphs weighted on edges
* Graphs weighted on vertices and edges

However, the **weight changes its meaning based on the problem we face**.

---

## Vertex-Weighted
Graphs for which each **vertex has an associated weight**, given by the weight function
`w : V -> R` which returns a real number

![ex vertex weighted directed graph](https://github.com/PayThePizzo/DataStrutucures-Algorithms/blob/main/Resources/exWDGV.png?raw=TRUE)

It is best to use an adjacency list and save the weight info for each vertex, inside the main 
vector and the linked list for each different vertex

## Edge-Weighted
Graphs for which each **edge has an associated weight**, given by the weight function
`w : E -> R` which returns a real number

![ex edge weighted directed graph](https://github.com/PayThePizzo/DataStrutucures-Algorithms/blob/main/Resources/exWDGE.png?raw=TRUE)

It is best use an adjacency matrix and 

## Weighted on vertices and edges

---

## Implementations 

Using an adjacency list:
* VW: It is best to save the weight info for each vertex, inside the **main
vector**.
* EW: It is best to save the weight info for each edge, as an additional field inside each
element of the linked list

Using an adjacency matrix:
* VW: Using the main diagonal for the weights associated with the vertices and 
leaving the rest with 0s or `inf()`
* EW: Instead of having 1s, we would put the weight of the edge in the right 
position and instead of having 0s, we would use something like `inf()`



