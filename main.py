import streamlit as st
from scrape import scrape_website, extract_content, clean_content, split_dom

st.title("AI WebFetch")
url = st.text_input("Enter a Website URL : ")

if st.button("Scrape Site"):
  st.write("Scraping the website")
  
  result = scrape_website(url)
  body_content = extract_content(result)
  cleaned_content = clean_content(body_content)

  st.session_state.dom_content = cleaned_content

  with st.expander("View DOM Content"):
    st.text_area("DOM Content", cleaned_content, height=300)

if "dom_content" in st.session_state:
  parse_description = st.text_area("Describe what you want to parse ?")

  if st.button("Parse Content"):
    if parse_description:
      st.write("Parsing the content")

      dom_chunks = split_dom(st.session_state.dom_content)