"""
A module for implementing stack using queues.
"""
class MyStack:
    """
    A class for implementing stack using queues.
    """
    def __init__(self):
        """
        Initializing variables.
        """
        self.queue = []

    def push(self, x: int) -> None:
        """
        Push method.
        """
        self.queue.append(x)
        size = len(self.queue)
        for _ in range(size - 1):
            self.queue.append(self.queue.pop(0))

    def pop(self) -> int:
        """
        Pop method.
        """
        return self.queue.pop(0)

    def top(self) -> int:
        """
        Top method.
        """
        return self.queue[0]

    def empty(self) -> bool:
        """
        Checking if stack is empty.
        """
        return len(self.queue) == 0

# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
