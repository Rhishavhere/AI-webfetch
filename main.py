import streamlit as st
from scrape import scrape_website, extract_content, clean_content, split_dom
from parse import parse_with_ollama
st.write("AI WebFetch")
# st.subheader("Searching for information ?")
st.title("WebSearch with AI-WebFetch")
url = st.text_input("Enter a Website URL : ")

if st.button("Fetch Site"):
  st.write("Fetching the website details")
  
  result = scrape_website(url)
  body_content = extract_content(result)
  cleaned_content = clean_content(body_content)

  st.session_state.dom_content = cleaned_content

  with st.expander("View Page Content"):
    st.text_area("Page Content", cleaned_content, height=300)

if "dom_content" in st.session_state:
  parse_description = st.text_area("Describe what you want to know ?")

  if st.button("Go"):
    if parse_description:
      st.write("Getting you the info...")

      dom_chunks = split_dom(st.session_state.dom_content)
      result = parse_with_ollama(dom_chunks, parse_description)
      st.write(result)