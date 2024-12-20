import streamlit as st
from scrape import scrape_website, extract_content, clean_content, split_dom
from parse import parse_with_ollama

# Configure page settings
st.set_page_config(
    page_title="AI WebFetch",
    page_icon="🔍",
    layout="wide"
)

# Add custom CSS
st.markdown("""
    <style>
    .main {
        padding: 2rem;
    }
    .stTitle {
        color: #2E4374;
        margin-bottom: 2rem;
    }
    .stButton>button {
        background-color: #2E4374;
        color: white;
        border-radius: 5px;
        padding: 0.5rem 2rem;
    }
    .stTextInput>div>div>input {
        border-radius: 5px;
    }
    </style>
    """, unsafe_allow_html=True)

# Header section with columns
col1, col2 = st.columns([3,1])
with col1:
    st.title("🔍 AI WebFetch")
    st.markdown("*Your AI-powered web content analyzer*")

# Main content
st.markdown("---")
url = st.text_input("🌐 Enter a Website URL", placeholder="https://example.com")

if st.button("🚀 Fetch Site", use_container_width=True):
    with st.spinner("Fetching website content..."):
        result = scrape_website(url)
        body_content = extract_content(result)
        cleaned_content = clean_content(body_content)
        st.session_state.dom_content = cleaned_content

    with st.expander("📄 View Page Content"):
        st.text_area("Raw Content", cleaned_content, height=300)

if "dom_content" in st.session_state:
    st.markdown("---")
    st.subheader("🤖 Ask AI about the content")
    parse_description = st.text_area(
        "What would you like to know?",
        placeholder="Ask any question about the webpage content...",
        height=100
    )

    if st.button("🔍 Analyze", use_container_width=True):
        if parse_description:
            with st.spinner("Analyzing content..."):
                dom_chunks = split_dom(st.session_state.dom_content)
                result = parse_with_ollama(dom_chunks, parse_description)
                
                st.success("Analysis complete!")
                st.markdown("### 📝 Results")
                st.markdown(result)