import streamlit as st
import google.generativeai as genai
from qiskit import QuantumCircuit
import cirq
import matplotlib.pyplot as plt
from io import BytesIO

# Configure Gemini API
genai.configure(api_key='AIzaSyBaQNejtu3-_46HWqcb93v3qwMr0ufVgDs')
model = genai.GenerativeModel('gemini-2.0-flash')


class QuantumAICoder:
    def __init__(self, model=model):
        self.model = model

    def generate_quantum_code(self, prompt):
        """Generates quantum computing code for Qiskit or Cirq based on a given prompt."""
        response = self.model.generate_content(prompt)
        return response.text if response else "Error: No response generated."

    def self_improve(self, previous_code, feedback):
        """Improves quantum code based on feedback using AI."""
        prompt = f"Improve the following quantum code based on the feedback: {feedback}\n\n{previous_code}"
        return self.generate_quantum_code(prompt)

    def retrieve_knowledge(self, query):
        """Retrieves relevant quantum computing information (Placeholder for RAG system)."""
        return f"[RAG] Retrieving relevant knowledge for: {query}"

    def generate_circuit_diagram(self, prompt):
        """Generates a quantum circuit diagram dynamically based on user input."""
        try:
            # Use AI to generate quantum circuit code
            code = self.generate_quantum_code(f"Generate Qiskit quantum circuit for: {prompt}")

            # Execute generated code safely
            local_vars = {}
            exec(code, {}, local_vars)

            # Check if a circuit was created
            if "circuit" in local_vars and isinstance(local_vars["circuit"], QuantumCircuit):
                fig, ax = plt.subplots()
                local_vars["circuit"].draw(output='mpl', ax=ax)
                return fig
            else:
                return None
        except Exception as e:
            return None


# Streamlit UI
st.title("Q_orld AI Coder AI (Qiskit & Cirq)")

# Maintain state
if 'generated_code' not in st.session_state:
    st.session_state.generated_code = ""
if 'generated_circuit' not in st.session_state:
    st.session_state.generated_circuit = None

user_input = st.text_area("Enter your quantum computing problem:", "")
ai_coder = QuantumAICoder()

if st.button("Generate Quantum Code"):
    if user_input:
        if "retrieve knowledge" in user_input.lower():
            st.session_state.generated_code = ai_coder.retrieve_knowledge(user_input)
        else:
            st.session_state.generated_code = ai_coder.generate_quantum_code(user_input)
    else:
        st.warning("Please enter a prompt!")

st.markdown("**Generated Response:**")
st.code(st.session_state.generated_code, language="python")























