class EmailAgent:
    def __init__(self, memory):
        self.memory = memory

    def process(self, content):
        result = {
            "status": "processed",
            "type": "Email",
            "summary": content[:50]  # show preview
        }
        self.memory.store(source='EmailAgent', data=result)
        return result
