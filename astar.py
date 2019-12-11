#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from typing import List


class PriorityQueue(object):
    def __init__(self):
        self.queue = []

    def str(self):
        return ' '.join([str(i) for i in self.queue])

    # for checking if the queue is empty
    def isEmpty(self):
        return len(self.queue) == []

    # for inserting an element in the queue
    def insert(self, data):
        self.queue.append(data)

    # for popping an element based on Priority
    def delete(self):
        try:
            max = 0
            for i in range(len(self.queue)):
                if self.queue[i].heuristic < self.queue[max].heuristic:
                    max = i
            item = self.queue[max]
            del self.queue[max]
            return item
        except IndexError:
            print()
            exit()


class Node:
    def __init__(self, x, y, value, nodeParent):
        self.x = x
        self.y = y
        self.cost = 0
        self.heuristic = 0
        self.value = value
        self.nodeParent = nodeParent

    def showYou(self):
        current = self.nodeParent
        p = "-> {},{} \n".format(self.y, self.x)
        while(current != None):
            p += "-> {},{}\n".format(current.y, current.x)
            current = current.nodeParent
        return p

    def getValue(self):
        return self.value


def findNeighbours(node: Node, graph: List[List[Node]]):
    row = node.y
    column = node.x
    neighbours = []

    # len(graph) -1 = only avaible if graph is a square

    if(row + 1 >= 0 and row + 1 <= (len(graph)-1)):
        if(graph[row+1][column].value != 0):
            neighbours.append(graph[row+1][column])

    if(column + 1 >= 0 and column + 1 <= (len(graph)-1)):
        if(graph[row][column + 1].value != 0):
            neighbours.append(graph[row][column + 1])

    if(row - 1 >= 0 and row - 1 <= (len(graph)-1)):
        if(graph[row - 1][column].value != 0):
            neighbours.append(graph[row - 1][column])

    if(column - 1 >= 0 and column - 1 <= (len(graph)-1)):
        if(graph[row][column - 1].value != 0):
            neighbours.append(graph[row][column - 1])

    return neighbours


def ifExist(graph, node):
    for v in graph:
        if(v == node):
            return v.cost
    return 999


def shortestPath(graph: List[List[Node]], depart: Node, arriver: Node):
    closeList = []
    openList = PriorityQueue()

    openList.insert(depart)

    while not openList.isEmpty():
        current = openList.delete()
        if(current.x == arriver.x and current.y == arriver.y):
            return current

        neighbours = findNeighbours(current, graph)
        for v in neighbours:
            if(v in closeList or ifExist(openList.queue, v) < v.cost):
                continue
            else:
                v.cost = current.cost + current.value
                v.heuristic = v.cost + \
                    (abs(v.x - arriver.x) + abs(v.y - arriver.y))
                v.nodeParent = current
                openList.insert(v)
        closeList.append(current)

# 0 wall, the algo pref go the < value


if __name__ == "__main__":

    array = [[1, 0, 1, 1, 1],
             [1, 1, 1, 5, 1],
             [1, 0, 0, 1, 1],
             [1, 0, 1, 3, 2],
             [1, 0, 1, 1, 1]]

    for y in range(0, 5):
        for x in range(0, 5):
            array[y][x] = Node(x, y, array[y][x], None)

    print(shortestPath(array, array[4][4], array[4][0]).showYou())

# array = [y][x] then [row][col]
