import streamlit as st
from utils.file_loader import load_file_content
from shared_memory.memory import SharedMemory
from agents.classifier_agent import ClassifierAgent
from agents.json_agent import JSONAgent
from agents.email_agent import EmailAgent

st.title("🧠 Multi-Agent AI System")

uploaded_file = st.file_uploader("Upload a .txt or .json file", type=["txt", "json"])
if uploaded_file:
    content = uploaded_file.read().decode("utf-8")
    st.text_area("📄 File Content", content, height=200)

    # Setup memory and agents
    memory = SharedMemory()
    classifier = ClassifierAgent(memory)
    JSONAgent(memory)
    EmailAgent(memory)

    if st.button("Run Classification"):
        result = classifier.classify_and_route(content)
        st.subheader("🧾 Final Output")
        st.json(result)

        st.subheader("🧠 Memory Log")
        for item in memory.data:
            st.json(item)
