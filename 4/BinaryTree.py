#!/usr/bin/env python
# coding: utf-8

# In[ ]:

from random import randint

class Node:
    def __init__(self, data=None):
        self.data = data
        self.left = None
        self.right = None
        self.parent = None
        
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
            return None
        h = len(arr)
        l = 0
        mid = (h+l)//2
        root = Node(arr[mid])
        root.left = self.createTree(arr[l:mid])
        if root.left:
            root.left.parent = root
        root.right = self.createTree(arr[mid+1:h])
        if root.right:
            root.right.parent = root
        return root

    def createRandomTree(self, size, min_value, max_value):
        arr = [randint(min_value,max_value) for i in range(size)]
        return self.createTree(arr)
    
    def createRandomBalancedTree(self, size, min_value, max_value):
        class SizeTooBigException(Exception):
            
            def __init__(self):
                self.message = 'Size is bigger than range'
                super().__init__(self.message)
        if max_value-min_value+1 < size:
            raise SizeTooBigException
        s = set()
        arr = []
        for i in range(size):
            n = randint(min_value,max_value)
            while n in s:
                n = randint(min_value,max_value)
            s.add(n)
            arr.append(n)
        arr.sort()
#         arr = sorted([randint(min_value,max_value) for i in range(size)])
        return self.createTree(arr)

# Taken from https://stackoverflow.com/a/54074933/6792562
    def display(self):
        lines, *_ = self._display_aux()
        for line in lines:
            print(line)

    def _display_aux(self):
        """Returns list of strings, width, height, and horizontal coordinate of the root."""
        # No child.
        if self.right is None and self.left is None:
            line = '%s' % self.data
            width = len(line)
            height = 1
            middle = width // 2
            return [line], width, height, middle

        # Only left child.
        if self.right is None:
            lines, n, p, x = self.left._display_aux()
            s = '%s' % self.data
            u = len(s)
            first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s
            second_line = x * ' ' + '/' + (n - x - 1 + u) * ' '
            shifted_lines = [line + u * ' ' for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, n + u // 2

        # Only right child.
        if self.left is None:
            lines, n, p, x = self.right._display_aux()
            s = '%s' % self.data
            u = len(s)
            first_line = s + x * '_' + (n - x) * ' '
            second_line = (u + x) * ' ' + '\\' + (n - x - 1) * ' '
            shifted_lines = [u * ' ' + line for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, u // 2

        # Two children.
        left, n, p, x = self.left._display_aux()
        right, m, q, y = self.right._display_aux()
        s = '%s' % self.data
        u = len(s)
        first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s + y * '_' + (m - y) * ' '
        second_line = x * ' ' + '/' + (n - x - 1 + u + y) * ' ' + '\\' + (m - y - 1) * ' '
        if p < q:
            left += [n * ' '] * (q - p)
        elif q < p:
            right += [m * ' '] * (p - q)
        zipped_lines = zip(left, right)
        lines = [first_line, second_line] + [a + u * ' ' + b for a, b in zipped_lines]
        return lines, n + m + u, max(p, q) + 2, n + u // 2
