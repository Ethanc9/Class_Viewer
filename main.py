from bs4 import BeautifulSoup
import requests

page = requests.get("https://catalog-archives.apps.buffalo.edu/2223/courses/computer_science__engineering.html")
scraper = BeautifulSoup(page.text, "html.parser")

# Find all elements with class "accordion-content"
class_contents = scraper.find_all("div", class_="accordion-content")

# Iterate through each class content and extract class name and prerequisite
for class_content in class_contents:
    # Extract class name
    class_name_elem = class_content.find_previous("a", class_="accordion-title")
    class_name = class_name_elem.text.strip() if class_name_elem else "Class name not found"
    
    # Extract prerequisite information
    prerequisite_elem = class_content.find("strong", text="Requisites:")
    if prerequisite_elem:
        prerequisite_text = prerequisite_elem.find_next("a")
        prerequisite = prerequisite_text.text.strip() if prerequisite_text else "No prerequisite mentioned"
    else:
        prerequisite = "No prerequisite mentioned"
    
    print(f"Class: {class_name}\nPrerequisite: {prerequisite}\n")

