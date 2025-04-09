"""
A module for implementing queue by using stacks.
"""
class MyQueue:
    """
    A class for implementing queue by stacks.
    """
    def __init__(self):
        """
        Initializing variables.
        """
        self.stack_push = []
        self.stack_pop = []

    def push(self, x: int) -> None:
        """
        A push method.
        """
        self.stack_push.append(x)

    def pop(self) -> int:
        """
        A pop method.
        """
        if not self.stack_pop:
            while self.stack_push:
                self.stack_pop.append(self.stack_push.pop())
        return self.stack_pop.pop()

    def peek(self) -> int:
        """
        A peek method.
        """
        if not self.stack_pop:
            while self.stack_push:
                self.stack_pop.append(self.stack_push.pop())
        return self.stack_pop[-1]

    def empty(self) -> bool:
        """
        A method for checking if queue is empty.
        """
        return len(self.stack_push) == 0 and len(self.stack_pop) == 0

# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
