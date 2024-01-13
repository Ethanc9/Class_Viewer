from bs4 import BeautifulSoup
import requests

page = requests.get("https://catalog-archives.apps.buffalo.edu/2223/courses/computer_science__engineering.html")
scraper = BeautifulSoup(page.text, "html.parser")

# Find Classes
class_contents = scraper.find_all("div", class_="accordion-content")

# Iterate through each class and extract class name and prerequisites
for class_content in class_contents:
    # Extract class name
    class_name_elem = class_content.find_previous("a", class_="accordion-title")
    class_name = class_name_elem.text.strip() if class_name_elem else "Class name not found"
    
    # Extract prerequisite information
    prerequisite_elem = class_content.find("strong", text="Requisites:")
    
    if prerequisite_elem:
        prerequisite_links = prerequisite_elem.find_next_siblings("a")
        prerequisites = [link.text.strip() for link in prerequisite_links]
        
        if prerequisites:
            print(f"Class: {class_name}\nPrerequisites: {', '.join(prerequisites)}\n")
        else:
            print(f"Class: {class_name}\nNo prerequisites mentioned\n")
    else:
        print(f"Class: {class_name}\nNo prerequisites mentioned\n")
