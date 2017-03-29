#!/usr/bin/env python

class Node: 
    def __init__(self, time=None, dist=None, next=None, prev=None): 
        self.time = time 
        self.dist = dist
        self.next = next
        self.prev = prev
    def __str__(self): 
        return str(self.car)


class LinkedList: 
    def __init__(self, window, head=None, tail=None): 
        self.head = head 
        self.tail = tail
        self.time_window = window
        self.length = 0

    def add(self, time, dist):
        if self.head == None:
            newNode = Node(time, dist, None, None)
            self.head = newNode
            self.tail = newNode
        else:
            newNode = Node(time, dist, self.head, None)
            self.head.prev = newNode
            self.head = newNode

        self.length += 1

        self.check_time_window(self.time_window)


    def remove_tail(self):
        if self.tail.prev == None:
            self.head = None
            self.tail = None
            self.length -= 1
            return

        self.tail.prev.next = None
        self.tail = self.tail.prev
        self.length -= 1


    def check_time_window(self, window):
        if self.head == None:
            return

        if (self.head.time - self.tail.time) > window:
            self.remove_tail()
            self.check_time_window(window)

    def get_points(self):
        if self.length < 10:
            return [[0, 0], [10, 10]]

        points = [self.head.dist, self.tail.dist]
        return points


    def __str__(self): 
        return str(self.car)



    




