# Data Risk Automator

## Description  
This project was developed as the final assignment for my "Programming for Networking and Cybersecurity" class. 
It automates critical processes such as data scraping, risk evaluation, notification, and reporting to help a company manage potential data exposure incidents effectively. The script performs the following key tasks:

### 1. Scrape Employee Data (Web Scraping)  
- Sends an HTTP GET request to: [https://cit30900.github.io/strawbridge/](https://cit30900.github.io/strawbridge/).  
- Parses the HTML content using BeautifulSoup.  
- Extracts employee data (first name, last name, email, and SSN) and stores it as dictionaries in a list.  

### 2. Evaluate the Exposure (Data Validation via API)  
- Uses an external API ([Have I Been Pwned](https://us-central1-cit-37400-elliott-dev.cloudfunctions.net/have-i-been-pwned)) to check if an employee's SSN has been compromised.  

### 3. Write Employee Data to a CSV File  
- Writes employee data and risk levels to `employee_risk.csv`.  

### 4. Compose Emails for High-Risk Employees  
- Creates personalized email files for high-risk employees.

### 5. Summarize and Display Results  
- Outputs risk category counts (`low`, `medium`, `high`) to the console.  

---

## Outputs  
- **CSV File**: `employee_risk.csv` containing employee data and risk levels.  
- **Email Files**: Individual text files for high-risk employees.  
- **Console Summary**: Displays a count of employees in each risk category.  

---

## Key Dependencies  
This script requires the following Python libraries:  
- **`requests`**  
- **`BeautifulSoup`**  
- **`json`**  
- **`csv`**  

---

## How to Run  
1. Clone the repository:  
   ```bash
   git clone https://github.com/yourusername/data-risk-automator.git


<!--
Comments
--!>
