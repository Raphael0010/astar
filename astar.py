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
    def __init__(self, x, y, cost, heuristic, nodeParent):
        self.x = x
        self.y = y
        self.cost = cost
        self.heuristic = heuristic
        self.nodeParent = nodeParent

    def showYou(self):
        current = self.nodeParent
        p = "-> {},{} \n".format(self.x, self.y)
        while(current != None):
            p += "-> {},{}\n".format(current.x, current.y)
            current = current.nodeParent
        return p


def reduce(function, iterable, initializer=None):
    it = iter(iterable)
    if initializer is None:
        try:
            initializer = next(it)
        except StopIteration:
            raise TypeError('reduce() of empty sequence with no initial value')
    accum_value = initializer
    for x in it:
        accum_value = function(accum_value, x)
    return accum_value


def access(obj, indexes):
    try:
        return reduce(list.__getitem__, indexes, obj)
    except Exception:
        return None


def findNeighbours(node: Node, graph: List[List[Node]]):
    row = node.y
    column = node.x
    neighbours = []

    if(access(graph, (row+1, column)) != None):
        neighbours.append(graph[row+1][column])

    if(access(graph, (row, column+1)) != None):
        neighbours.append(graph[row][column + 1])

    if(access(graph, (row - 1, column)) != None):
        neighbours.append(graph[row - 1][column])

    if(access(graph, (row, column - 1)) != None):
        neighbours.append(graph[row][column - 1])

    return neighbours


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
            result = (elem if elem.x == v.x and elem.y == v.y else None
                      for elem in openList.queue)
            if(v in closeList or any(elem != None and elem.cost < v.cost for elem in result)):
                continue
            else:
                v.cost = current.cost + 1
                v.heuristic = v.cost + \
                    (abs(v.x - arriver.x) + abs(v.y - arriver.y))
                v.nodeParent = current
                openList.insert(v)
        closeList.append(current)


if __name__ == "__main__":
    array = [[0, 0, 0, 0],
             [0, 0, 0, 0],
             [0, 0, 0, 0],
             [0, 0, 0, 0]]

    for y in range(0, 4):
        for x in range(0, 4):
            array[y][x] = Node(x, y, array[y][x], 0, None)

    print(shortestPath(array, array[0][1], array[3][3]).showYou())
