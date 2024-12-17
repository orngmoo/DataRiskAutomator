import requests
from bs4 import BeautifulSoup
import json
import csv

#1. Read the Employee Data (Python Data Scraping)
def scrape_employee_data(url):
    #sends HTTP GET request to the specified URL and stores repsonse in response variable
    response = requests.get(url)
    #if HTTP response status code=200 (successful request)
    if response.status_code == 200:
        # create soup object from the HTML content;
        #html.parser argument specifies the HTML parser to use
        soup = BeautifulSoup(response.text, 'html.parser')
        #create empty list to store extracted employee information
        employee_data = []
        #Iterates over all <div> elements with the class 'card employee' in the HTML content
        for card in soup.find_all('div', class_='card employee'):
            #Extract info from each employee's card and store in dictionary called info
            info = {
                'first_name': card.find('span', class_='emp_first_name').text,
                'last_name': card.find('span', class_='emp_last_name').text,
                'email': card.find('span', class_='emp_email').text,
                'ssn': card.find('span', class_='secret').text 
            }
            #append info dictionary to the employee_data list (which represents 1 employee's data)
            employee_data.append(info)
        return employee_data
    else:
        #In case HTTP request not successful, print an error message and return and empty list
        print(f"Failed to fetch data. Status code: {response.status_code}")
        return []

#2. Evaluate the Exposure
def evaluate_exposure(ssn):
    #API URL for checking the exposure using the "Have I Been Pwned" service
    api_url = f'https://us-central1-cit-37400-elliott-dev.cloudfunctions.net/have-i-been-pwned?username=omoo&ssn={ssn}'
    return json.loads(requests.get(api_url).text)['exposure']

#3. Write a CSV File
#Parameter 1: filename (name of CSV file to be created)
#Parameter 2: data (data to be written to the CSV file)
def write_to_csv(filename, data):
    #Open the filename in write mode
    #Newline='' handle newlines in a universal way across different platforms
    with open(filename, 'w', newline='') as csvfile:
        #Define list of column_headings that will be used as headers in the CSV file
        column_headings = ['first_name', 'last_name', 'email', 'ssn', 'risk_level']
        #Create a DictWriter object to write dictionaries to the CSV file. 
        writer = csv.DictWriter(csvfile, fieldnames=column_headings)
        #writes header row to the CSV filea
        writer.writeheader()
        #Loop thtough each row in data list
        for row in data:
            #Writes each dictionary row as a row in the CSV file. 
            writer.writerow(row)

#4. Compose an Email
def compose_email(employee):
    #If risk level is 'high'
    if employee['risk_level'] == 'high':
        #Construct filename for email text file based on the employee's first and last names
        email_filename = f"{employee['first_name']}_{employee['last_name']}.txt"
        #Open email text file, for writing
        with open(email_filename, 'w') as email_file:
            #Write email content
            email_file.write(f"Dear {employee['first_name']} {employee['last_name']},\n\n")
            email_file.write("Your personal data was accidentally exposed on the Strawbridge Industries website and is at risk of being compromised. The company regrets this error and would like to offer a credit monitoring service at no cost to you. Please contact HR to establish this service.\n\n")
            email_file.write("Thank you,\nDick Strawbridge, CEO\n")

#Main
def main():
    #Step 1: Read the Employee Data using Python Data Scraping
    employee_data_url = 'https://cit30900.github.io/strawbridge/'
    employee_data = scrape_employee_data(employee_data_url)

    #Step 2: Evaluate the exposure for each employee
    #Iterate through each employee in employee_data list
    for employee in employee_data:
        #For each employee, call:evaluate_exposure function using employee's SSN 
        #Assign the returned 'exposure' value to the 'risk_level' key in CSV File
        employee['risk_level'] = evaluate_exposure(employee['ssn'])

    #Step 3: Write employee data to CSV
    #Set variable csv_filename to the name of the CSV file ('employee_risk.csv')
    csv_filename = 'employee_risk.csv'
    #Call write_to_csv function, pass the CSV filename and employee_data list as arguments
    write_to_csv(csv_filename, employee_data)

    # Step 4: Compose emails for high-risk employees
    #Iterate though each employee with high risk level and compose email
    for employee in employee_data:
        if employee['risk_level'] == 'high':
            compose_email(employee)

    #5. Write the Results to the Screen
    #Count number of employees with a 'low', 'medium', and 'high' risk level in the employee_data list
    low = sum(1 for employee in employee_data if employee['risk_level'] == 'low')
    medium = sum(1 for employee in employee_data if employee['risk_level'] == 'medium')
    high = sum(1 for employee in employee_data if employee['risk_level'] == 'high')

    print(f"{low} low risk exposures detected")
    print(f"{medium} medium risk exposures detected")
    print(f"{high} high risk exposures detected")

if __name__ == "__main__":
    main()
