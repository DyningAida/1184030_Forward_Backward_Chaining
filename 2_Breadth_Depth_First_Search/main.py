# -*- coding: utf-8 -*-
"""
Created on Sun Mar 21 14:52:16 2021

@author: DyningAida
"""

#contoh skema grafik
graph = {
    'A':set(['B','C']),
    'B':set(['A','D','E']),
    'C':set(['A','F']),
    'D':set(['B']),
    'E':set(['B']),
    'F':set(['C'])
}

#funstion bfs
def bfs(visited, graph, node, destination):
    queue = []
    visited.append(node)
    queue.append(node)

    while queue:
        jalur = queue.pop(0)
        print(jalur, end=" ")

        if jalur == destination:
            break

        for branch in graph[jalur]:
            if branch not in visited:
                visited.append(branch)
                queue.append(branch)
visited = []

#function dfs
def dfs(graph, start, destination):
    stack = [[start]]
    visited = set()
    
    while stack:
        #menghitung panjang tumpukan
        jalur = stack.pop(-1)
        
        state = jalur[-1]
        #cek apakah state = destination
        if state == destination:
            return jalur
        elif state not in visited:
            for branch in graph.get(state, []):
                #memasukkan semua yang ada di variabel jalur ke jalur_baru
                jalur_baru = list(jalur)
                jalur_baru.append(branch)
                stack.append(jalur_baru)
            #memberikan tag pada state yang sudah dikunjungi sebagai visited
            visited.add(state)
            
        isi = len(stack)
        if isi == 0:
            print("Tidak ditemukan")
dfs(graph, 'A','F')

#menjalankan dfs
print("DFS nya yaitu")
print(dfs(graph, 'A','F'))
#menjalankan bfs
print("BFS nya yaitu")
bfs(visited, graph, 'A', 'F')


