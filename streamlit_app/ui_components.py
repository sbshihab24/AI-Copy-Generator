import streamlit as st

def render_header():
    """Renders the top navigation styling"""
    st.markdown("### AI Tools")
    st.markdown("Generate compelling ad copy and optimize your campaigns with AI")
    st.markdown("---")
    
    # Simplified header showing only the active tool
    # Using st.info gives it the blue, active tab appearance
    st.info("✨ **AI Copy Generator**", icon="✨")

    st.markdown("###") # Add some spacing

def render_output_card(text):
    """Renders a single generated copy variation as a clean white card"""
    # Using container(border=True) creates a clean, white, outlined card
    with st.container(border=True):
        # We use st.markdown to respect the \n\n line breaks for paragraphs
        st.markdown(text)