import selenium.webdriver as webdriver
from selenium.webdriver.edge.service import Service
from bs4 import BeautifulSoup
import time

def scrape_website(website):
  print("Launching edge browser...")

  edge_driver_path = "./msedgedriver.exe"
  options = webdriver.EdgeOptions()
  driver = webdriver.Edge(service=Service(edge_driver_path), options=options)

  driver.get(website)
  print("Page Loaded...")
  html = driver.page_source

  return html
  

def extract_content(html_content):
  soup = BeautifulSoup(html_content, "html.parser")
  body_content = soup.body
  if body_content:
    return str(body_content)
  return ""

def clean_content(body_content):
  soup = BeautifulSoup(body_content, "html.parser")

  for tags in soup(["script", "style"]):
    tags.extract()

  cleaned_content = soup.get_text(separator="\n")
  cleaned_content = "\n".join(
    line.strip() for line in cleaned_content.splitlines() if line.strip()
  )

  return cleaned_content

def split_dom(dom_content, max_length = 6000):
  return [
    dom_content[i:i+max_length] for i in range(0,len(dom_content),max_length)
  ]

