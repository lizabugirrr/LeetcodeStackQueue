"""
A module for implementing maximum frequency stack.
"""
from collections import deque

class FreqStack:
    """
    A class for implementing maximum frequency stack.
    """
    def __init__(self):
        """
        Initializing variables.
        """
        self.stack = deque()
        self.freq_map = {}
        self.freq_stacks = {}
        self.max_freq = 0

    def push(self, val: int) -> None:
        """
        A push method.
        """
        if val in self.freq_map:
            self.freq_map[val] += 1
        else:
            self.freq_map[val] = 1
        freq = self.freq_map[val]
        if freq > self.max_freq:
            self.max_freq = freq
        if freq not in self.freq_stacks:
            self.freq_stacks[freq] = deque()
        self.freq_stacks[freq].append(val)
        self.stack.append(val)

    def pop(self) -> int:
        """
        A pop method.
        """
        max_freq_stack = self.freq_stacks[self.max_freq]
        val = max_freq_stack.pop()
        self.freq_map[val] -= 1
        if not max_freq_stack and self.max_freq > 0:
            self.max_freq -= 1
        return val

# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()
