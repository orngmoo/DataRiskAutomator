# Automation of Data Scraping

## Description  
This project was developed as the final assignment for my "Programming for Networking and Cybersecurity" class. 
It automates critical processes such as data scraping, risk evaluation, notification, and reporting to help a company manage potential data exposure incidents effectively. The script performs the following key tasks:

### 1. Scrape Employee Data (Web Scraping)  
The `scrape_employee_data` function:  
- Sends an HTTP GET request to a specified URL: [https://cit30900.github.io/strawbridge/](https://cit30900.github.io/strawbridge/).  
- Parses the HTML content using BeautifulSoup.  
- Extracts employee data, including first name, last name, email, and SSN, from specific HTML elements (`<div>` with the class `card employee` and nested `<span>` elements).  
- Stores each employee's details as a dictionary in a list and returns the list.  

### 2. Evaluate the Exposure (Data Validation via API)  
The `evaluate_exposure` function:  
- Uses an external API ([Have I Been Pwned](https://us-central1-cit-37400-elliott-dev.cloudfunctions.net/have-i-been-pwned)) to check if an employee's SSN has been compromised.  
- Sends a GET request to the API with the SSN as a parameter.  
- Parses the JSON response and retrieves the exposure level (`low`, `medium`, or `high`).  

### 3. Write Employee Data to a CSV File  
The `write_to_csv` function:  
- Writes the employee data (including risk levels) to a CSV file named `employee_risk.csv`.  
- Uses `csv.DictWriter` to create a structured CSV file with the following columns:  
  - `first_name`  
  - `last_name`  
  - `email`  
  - `ssn`  
  - `risk_level`  

### 4. Compose Emails for High-Risk Employees  
The `compose_email` function:  
- Creates personalized email files for employees classified as high risk.  
- Writes a warning message to a text file named after the employee's first and last names.  

### 5. Summarize and Display Results  
The `main` function coordinates the entire workflow:  
1. **Scrape Employee Data**: Retrieves data from the specified URL.  
2. **Evaluate Risk**: Determines the risk level for each employee based on their SSN using the `evaluate_exposure` function.  
3. **Save to CSV**: Saves the employee data (with risk levels) to the `employee_risk.csv` file.  
4. **Send Emails**: Composes warning emails for employees at high risk.  
5. **Print Summary**: Counts and prints the number of employees in each risk category (`low`, `medium`, `high`) to the console.  

---

## Outputs  
- **CSV File**: `employee_risk.csv` containing employee data and risk levels.  
- **Email Files**: Individual text files for employees at high risk.  
- **Console Summary**: Displays a count of employees in each risk category.  

---

## Key Dependencies  
This script requires the following Python libraries:  
- **`requests`**: Handles HTTP requests.  
- **`BeautifulSoup`**: Parses and extracts data from HTML.  
- **`json`**: Handles JSON data from the API.  
- **`csv`**: Writes structured data to CSV files.  

---

## Language  
- **Python**  

---

## Environment Used  
- **MacOS**  


<!--
Comments
--!>
