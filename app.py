import streamlit as st
import ollama
from pypdf import PdfReader

def extract_text_from_pdf(file):
    reader = PdfReader(file)
    return " ".join([page.extract_text() for page in reader.pages])

st.set_page_config(page_title="AuthAI Assistant", page_icon="🏥")
st.title("🏥 Medical Prior-Auth Assistant")
st.markdown("### local AI-Powered Eligibility Verification")

# Sidebar for Instructions
with st.sidebar:
    st.header("How to use")
    st.write("1. Upload clinical notes (PDF).\n2. Paste insurance rules.\n3. Click 'Check Eligibility'.")
    st.info("Note: This runs locally via Ollama for HIPAA-compliant data handling.")

# UI Layout
col1, col2 = st.columns(2)

with col1:
    uploaded_file = st.file_uploader("Upload Patient Records (PDF)", type="pdf")

with col2:
    criteria = st.text_area("Insurance Criteria", placeholder="e.g., Patient must fail 6 weeks of conservative therapy...")

if st.button("🔍 Analyze Eligibility"):
    if uploaded_file and criteria:
        with st.spinner("Mistral-7B is analyzing documentation..."):
            patient_text = extract_text_from_pdf(uploaded_file)
            
            prompt = f"""
            Task: Medical Prior Authorization Audit
            Insurance Rule: {criteria}
            Clinical Data: {patient_text}
            
            Instructions:
            - Determine if the criteria is MET, NOT MET, or PARTIAL.
            - Quote specific lines from the clinical record as evidence.
            - List missing documentation required for approval.
            """
            
            try:
                response = ollama.generate(model='mistral', prompt=prompt)
                st.success("Analysis Complete")
                st.markdown("### **AI Findings**")
                st.write(response['response'])
            except Exception as e:
                st.error(f"Error connecting to Ollama: {e}")
    else:
        st.warning("Please provide both patient records and insurance criteria.")
