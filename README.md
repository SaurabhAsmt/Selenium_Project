# Trafigura Job Scraper

This project uses Selenium to scrape job postings from the [Trafigura Careers site](https://trafigura.wd3.myworkdayjobs.com/TrafiguraCareerSite). The script extracts both the **job title** and **job location** for each posting and writes the data to a CSV file.

## Features

- Scrapes job titles and job locations from 7 pages of the careers site.
- Handles dynamic content loading using Selenium's explicit waits and time delays.
- Outputs the scraped data as a CSV file (`jobs.csv`).

## Prerequisites

- [Python 3.x](https://www.python.org/downloads/)
- [Selenium](https://pypi.org/project/selenium/)
- [Chrome WebDriver](https://chromedriver.chromium.org/) (or an appropriate driver for your browser) installed and added to your system PATH.

## Installation

1. **Clone the repository** (if applicable) or download the script file.

2. **Install Selenium** using pip:

   ```bash
   pip install selenium
