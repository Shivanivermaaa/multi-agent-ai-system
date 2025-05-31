import json

class JSONAgent:
    def __init__(self, memory):
        self.memory = memory

    def process(self, content):
        try:
            data = json.loads(content)
        except json.JSONDecodeError:
            return {"error": "Invalid JSON"}

        result = {
            "status": "processed",
            "type": "JSON",
            "keys": list(data.keys())
        }

        self.memory.store(source='JSONAgent', data=result)
        return result
