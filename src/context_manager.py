from collections import deque

class ContextManager:
    def __init__(self, max_size=1000):
        self.context = deque(maxlen=max_size)
    
    def update_context(self, new_call):
        self.context.append(new_call)
    
    def get_context(self):
        return ' '.join(self.context)
        