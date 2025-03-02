# Scraping_companies_contacts

## Description
This repository contains scripts for extracting company information and contact details from the web. The project includes:
- **script.py**: Pulls out a list of companies along with their websites and stores them in `companies.csv`.
- **web_details.py**: Scrapes contact details, including email addresses, and saves them in `ContactDetails.csv`.
- **MergeExcel.py**: Merges two Excel files with the same columns while removing duplicates.

## Features
- Scrapes company names and website URLs.
- Extracts contact details such as email addresses.
- Merges Excel files while ensuring no duplicate entries remain.
- Automates data collection for lead generation or research purposes.

## Installation

### Prerequisites
Ensure you have:
- Python 3.x installed.
- Required dependencies listed in `requirements.txt`.

### Steps to Install
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/Scraping_companies_contacts.git
   cd Scraping_companies_contacts
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage
1. **Extract Company List**  
   Run `script.py` to scrape company names and websites:
   ```bash
   python script.py
   ```
   Output: `companies.csv` (Company Name, Website)

2. **Scrape Contact Details**  
   Run `web_details.py` to fetch company contact details:
   ```bash
   python web_details.py
   ```
   Output: `ContactDetails.csv` (Company Name, Website, Email, Contact Info)

3. **Merge Excel Files**  
   Run `MergeExcel.py` to merge two Excel files while removing duplicates:
   ```bash
   python MergeExcel.py file1.xlsx file2.xlsx output.xlsx
   ```

## Configuration
- Modify `script.py` and `web_details.py` to change scraping logic or add more fields.
- Ensure proper handling of website structures that require authentication or CAPTCHAs.

## Contributing
1. Fork the repository.
2. Create a feature branch (`git checkout -b feature-branch`).
3. Commit your changes (`git commit -m 'Add new feature'`).
4. Push to the branch (`git push origin feature-branch`).
5. Submit a Pull Request.

## License
This project is licensed under the MIT License.

## Contact
For any issues or feature requests, please open an issue on the repository.


