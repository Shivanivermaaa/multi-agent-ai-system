from agents.classifier_agent import ClassifierAgent
from agents.json_agent import JSONAgent
from agents.email_agent import EmailAgent
from shared_memory.memory import SharedMemory
from utils.file_loader import load_file_content

import os

print("Starting Multi-Agent AI System...")

# === Initialize shared memory ===
memory = SharedMemory()

# === Initialize agents ===
classifier = ClassifierAgent(memory)
json_agent = JSONAgent(memory)
email_agent = EmailAgent(memory)

# === File path (use raw string or forward slashes) ===
file_path = r"sample_inputs/sample_email.txt"  # or use forward slashes: "sample_inputs/sample_email.txt"
print(f"Processing file: {r'C:\Users\rv176\OneDrive\Pictures\SHIVANI\multi-agent-ai-system\sample_inputs\sample_email.txt'}")

# === Load content ===
content = load_file_content(r'C:\Users\rv176\OneDrive\Pictures\SHIVANI\multi-agent-ai-system\sample_inputs\sample_email.txt')

# === Classify and route ===
result = classifier.classify_and_route(content)

# === Display results ===
print("\n--- Final Output from Agent ---")
print(result)

# === Display memory ===
print("\nMemory contents:")
for item in memory.data:
    print(item)
