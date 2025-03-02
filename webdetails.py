import csv
import re
from urllib.parse import urlparse
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Initialize Selenium WebDriver
driver = webdriver.Chrome()  # Ensure you have ChromeDriver installed

def validate_url(url):
    """Ensure the URL has a valid scheme."""
    if not urlparse(url).scheme:
        return "http://" + url
    return url

def extract_contact_details(url):
    try:
        driver.get(url)
        wait = WebDriverWait(driver, 10)

        # Extract page source and parse with BeautifulSoup
        page_source = driver.page_source
        soup = BeautifulSoup(page_source, "html.parser")

        # Extract phone numbers from href with tel:
        phone_numbers = set()
        for tag in soup.find_all("a", href=True):
            if tag["href"].startswith("tel:"):
                phone_numbers.add(tag["href"].replace("tel:", "").strip())

        # Extract email IDs from href with mailto:
        email_ids = set()
        for tag in soup.find_all("a", href=True):
            if tag["href"].startswith("mailto:"):
                email_ids.add(tag["href"].replace("mailto:", "").strip())

        # Handle clickable elements with "Call" or "Email" text
        clickable_elements = soup.find_all("a", text=re.compile(r"call|email", re.IGNORECASE))
        for element in clickable_elements:
            try:
                # Use Selenium to click on the element
                clickable = wait.until(EC.element_to_be_clickable((By.XPATH, f"//*[text()='{element.text.strip()}']")))
                ActionChains(driver).move_to_element(clickable).click().perform()

                # Re-fetch the page source after interaction
                updated_page_source = driver.page_source
                updated_soup = BeautifulSoup(updated_page_source, "html.parser")

                # Look for new phone or email info in href attributes
                for tag in updated_soup.find_all("a", href=True):
                    if tag["href"].startswith("tel:"):
                        phone_numbers.add(tag["href"].replace("tel:", "").strip())
                    elif tag["href"].startswith("mailto:"):
                        email_ids.add(tag["href"].replace("mailto:", "").strip())
            except Exception as e:
                print(f"Error interacting with clickable element: {e}")

        # Additional email extraction using regex
        additional_emails = re.findall(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}", soup.text)
        email_ids.update(additional_emails)

        return {"emails": ", ".join(email_ids), "phones": ", ".join(phone_numbers)}

    except Exception as e:
        print(f"Error processing {url}: {e}")
        return {"emails": "", "phones": ""}

# Input and output file paths
input_file = "Company1.csv"
output_file = "ContactDetails4.csv"

try:
    # Read input CSV
    with open(input_file, mode='r', encoding='utf-8') as infile:
        reader = csv.DictReader(infile)
        rows = [row for row in reader if row["Company Website"].strip()]  # Skip empty URLs

    # Prepare and write to output CSV
    with open(output_file, mode='w', encoding='utf-8', newline='') as outfile:
        fieldnames = ["Company Name", "Website", "Email IDs", "Contact Numbers"]
        writer = csv.DictWriter(outfile, fieldnames=fieldnames)
        writer.writeheader()

        for row in rows:
            company_name = row["Company Name"]
            raw_website = row["Company Website"].strip()

            if not raw_website:
                continue

            # Validate and normalize the URL
            website = validate_url(raw_website)

            # Extract contact details
            contact_details = extract_contact_details(website)

            # Write row to the output CSV
            writer.writerow({
                "Company Name": company_name,
                "Website": website,
                "Email IDs": contact_details["emails"],
                "Contact Numbers": contact_details["phones"]
            })
            print(contact_details)

except FileNotFoundError as e:
    print(f"File not found: {e}")
except KeyError as e:
    print(f"Missing expected column in input file: {e}")
except Exception as e:
    print(f"Unexpected error: {e}")
finally:
    driver.quit()
