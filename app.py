import streamlit as st
import os
import sys

# Add the directory containing imports to the system path
sys.path.append(os.path.abspath(os.path.dirname(__file__)))

from backend.ai_copy_generator import generate_ad_copy
from streamlit_app.ui_components import render_header, render_output_card

# 1. Page Configuration
st.set_page_config(page_title="AdPortal - AI Copy Generator", layout="wide")

# 2. Updated CSS for Centering and Banner Styling
css_path = os.path.join(".streamlit", "style.css")
if os.path.exists(css_path):
    with open(css_path) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
else:
    st.markdown("""
        <style>
        .stButton>button { width: 100%; border-radius: 8px; }
        /* Center Alignment Styles */
        .centered-text {
            text-align: center;
        }
        /* Blue Banner Styling */
        .banner-container {
            background-color: #e8f0fe;
            color: #1a73e8;
            padding: 18px;
            border-radius: 10px;
            display: flex;
            justify-content: center;
            align-items: center;
            font-weight: 600;
            margin-bottom: 30px;
            border: 1px solid #d1e3ff;
        }
        </style>
    """, unsafe_allow_html=True)

# 3. CENTERED HEADER SECTION
# This replaces the default render_header() to force the alignment you want
st.markdown("""
    <div class="centered-text">
        <h1 style="margin-bottom: 0;">AI Tools</h1>
        <p style="color: #666; font-size: 1.5rem;">Generate compelling ad copy and optimize your campaigns with AI</p>
    </div>
    <hr>
    <div class="banner-container">
        <span style="font-size: 20px; font-weight: bold;">✨ ✨ AI Copy Generator</span>
    </div>
""", unsafe_allow_html=True)

# 4. Initialize Session State for Results
if "generated_copy" not in st.session_state:
    st.session_state.generated_copy = []
if "last_inputs" not in st.session_state:
    st.session_state.last_inputs = {}

# 5. Main Layout (Keeping your previous 2-column style)
left_col, right_col = st.columns([1, 1], gap="large")

# --- LEFT COLUMN: INPUT FORM ---
with left_col:
    with st.container(border=True):
        st.subheader("Generate Ad Copy")
        
        product = st.text_input("Product/Service", placeholder="e.g., SaaS platform, fitness app")
        audience = st.text_input("Target Audience", placeholder="e.g., small business owners")
        benefits = st.text_input("Key Benefits", placeholder="List main benefits...")
        tone = st.selectbox("Tone", ["Professional", "Friendly", "Persuasive", "Bold", "Minimal"])
        
        copy_type = st.radio(
            "Copy Type", 
            ["Headlines", "Primary Text", "Descriptions", "CTAs"], 
            horizontal=True
        )

        st.markdown("###") 
        
        if st.button("✨ Generate Copy", type="primary", use_container_width=True):
            if not product or not audience or not benefits:
                st.warning("Please fill in all fields.")
            else:
                with st.spinner("Generating..."):
                    try:
                        variations = generate_ad_copy(product, audience, benefits, tone, copy_type)
                        st.session_state.generated_copy = variations
                        st.session_state.last_inputs = {
                            "product": product, "audience": audience, 
                            "benefits": benefits, "tone": tone, "copy_type": copy_type
                        }
                    except Exception as e:
                        st.error(f"Error calling AI service: {e}")

# --- RIGHT COLUMN: OUTPUT DISPLAY ---
with right_col:
    with st.container(border=True):
        r_col1, r_col2 = st.columns([3, 1])
        with r_col1:
            st.subheader("Generated Copy")
        with r_col2:
            if st.button("🔄 Regenerate"):
                if st.session_state.last_inputs:
                    inputs = st.session_state.last_inputs
                    with st.spinner("Regenerating..."):
                        variations = generate_ad_copy(
                            inputs["product"], inputs["audience"], 
                            inputs["benefits"], inputs["tone"], 
                            inputs["copy_type"]
                        )
                        st.session_state.generated_copy = variations
                        st.rerun()
                else:
                    st.info("No previous inputs found.")

        st.markdown("---")

        if st.session_state.generated_copy:
            for item in st.session_state.generated_copy:
                st.markdown("**Variation**")
                render_output_card(item)
        else:
            st.markdown("<div style='text-align: center; padding: 40px;'>", unsafe_allow_html=True)
            st.image("https://cdn-icons-png.flaticon.com/512/7486/7486747.png", width=100)
            st.info("Fill in the form and click 'Generate Copy' to see AI-suggestions.")
            st.markdown("</div>", unsafe_allow_html=True)