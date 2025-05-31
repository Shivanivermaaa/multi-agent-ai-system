from utils.intent_detector import detect_format_and_intent

class ClassifierAgent:
    def __init__(self, memory):
        self.memory = memory

    def classify_and_route(self, content):
        fmt, intent = detect_format_and_intent(content)
        self.memory.store(format=fmt, intent=intent, source='ClassifierAgent')

        if fmt == 'JSON':
            from agents.json_agent import JSONAgent
            agent = JSONAgent(self.memory)
        elif fmt == 'Email':
            from agents.email_agent import EmailAgent
            agent = EmailAgent(self.memory)
        else:
            return {'error': 'Unsupported format'}

        return agent.process(content)
