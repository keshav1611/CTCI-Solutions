#!/usr/bin/env python
# coding: utf-8

# In[ ]:

from random import randint

class Node:
    def __init__(self, data=None):
        self.data = data
        self.left = None
        self.right = None
        
    def __str__(self):
        return '('+str(self.left)+':L ' + "V:" + str(self.data) + " R:" + str(self.right)+')'
    
    def PrintTree(self):
        print(self.data)
        
        if self.left:
            print(str(self.data)+" Left: ",end='')
            self.left.PrintTree()
        
        if self.right:
            print(str(self.data)+" Right: ",end='')
            self.right.PrintTree()
            
    def insert(self, data):
# Compare the new value with the parent node
        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data
            
    def createTree(self, arr):
        if not arr:
            return ''
        h = len(arr)
        l = 0
        mid = (h+l)//2
        root = Node(arr[mid])
        root.left = self.createTree(arr[l:mid])
        root.right = self.createTree(arr[mid+1:h])
        return root

    def createRandomTree(self, size, min_value, max_value):
        arr = [randint(min_value,max_value) for i in range(size)]
        return self.createTree(arr)

