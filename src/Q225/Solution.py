"""
Implement a last-in-first-out (LIFO) stack using only two queues.
The implemented stack should support all the functions of a normal stack (push, top, pop, and empty).
Implement the MyStack class:
    void push(int x) Pushes element x to the top of the stack.
    int pop() Removes the element on the top of the stack and returns it.
    int top() Returns the element on the top of the stack.
    boolean empty() Returns true if the stack is empty, false otherwise.
Notes:
You must use only standard operations of a queue, which means that only push to back, peek/pop from front, size and is
empty operations are valid.
Depending on your language, the queue may not be supported natively. You may simulate a queue using a list or deque
(double-ended queue) as long as you use only a queue's standard operations.
"""

class MyStack:

    def __init__(self):
        self.queue1 = []
        self.queue2 = []

    def push(self, x: int) -> None:
        if len(self.queue1) == 0:
            self.queue1.append(x)
            for i in range(len(self.queue2)):
                self.queue1.append(self.queue2.pop(0))
        else:
            self.queue2.append(x)
            for i in range(len(self.queue1)):
                self.queue2.append(self.queue1.pop(0))

    def pop(self) -> int:
        if len(self.queue1) == 0:
            return self.queue2.pop(0)
        else:
            return self.queue1.pop(0)

    def top(self) -> int:
        if len(self.queue1) == 0:
            return self.queue2[0]
        else:
            return self.queue1[0]

    def empty(self) -> bool:
        return not self.queue1 and not self.queue2


if __name__ == '__main__':
    s = MyStack()
    s.push(1)
    s.push(2)
    s.push(3)
    s.push(4)
    s.push(2)
    print(s.top())
    print(s.pop())
    print(s.top())