from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import csv

def scrape_jobs():
    # Disabling the Automation Indicator WebDriver Flags
    options = webdriver.ChromeOptions()  # creating chromeoptions instance
    options.add_argument("--disable-blink-features=AutomationControlled")  # adding arg
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option("useAutomationExtension", False)
    options.add_argument("--headless")  # run headless

    # Initialize the driver (adjust if you're using Firefox or another browser)
    driver = webdriver.Chrome(options=options)

    try:
        # Open the career site
        url = "https://trafigura.wd3.myworkdayjobs.com/TrafiguraCareerSite"
        driver.get(url)

        # Wait for the page to load job titles and job locations
        wait = WebDriverWait(driver, 15)
        all_jobs = []

        # Loop over the 7 pages.
        for page in range(1, 8):
            print(f"Scraping page {page}...")

            # Wait until the job title and job location elements are present
            wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, '[data-automation-id="jobTitle"]')))
            wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, '.css-129m7dg')))

            # Additional pause to allow dynamic content to fully load.
            time.sleep(3)

            # Find all job title and job location elements.
            job_title_elements = driver.find_elements(By.CSS_SELECTOR, '[data-automation-id="jobTitle"]')
            job_location_elements = driver.find_elements(By.CSS_SELECTOR, 'div.css-248241 > div > div > dl > dd.css-129m7dg')

            # Combine the job title and location data.
            # (Assuming that both lists are in sync, we iterate over the minimum count.)
            count = min(len(job_title_elements), len(job_location_elements))
            for i in range(count):
                job_title = job_title_elements[i].text.strip()
                job_location = job_location_elements[i].text.strip()
                if job_title:
                    all_jobs.append({
                        "job title": job_title,
                        "job location": job_location
                    })

            print(f"Found {count} job postings on page {page}.")

            # If this is the last page, break out of the loop.
            if page == 7:
                break

            # Locate the next button and click it.
            next_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.wd-icon-chevron-right-small')))
            next_button.click()

            # Wait a short moment for the new results to load.
            time.sleep(3)

        return all_jobs

    finally:
        driver.quit()


def write_to_csv(jobs, filename="jobs.csv"):
    # Write the list of dictionaries to a CSV file.
    with open(filename, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=["job title", "job location"])
        writer.writeheader()
        for job in jobs:
            writer.writerow(job)
    print(f"Data written to {filename}")


if __name__ == "__main__":
    job_data = scrape_jobs()
    print("\nAll job postings scraped:")
    for job in job_data:
        print(job)
    write_to_csv(job_data)
