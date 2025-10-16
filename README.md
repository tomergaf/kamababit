# KamaBabit

## An easy splitter app 

This is a Python-based application that helps calculate and assign payments for debts among a group of people. It uses JSON files to store the initial data and outputs the calculated results in JSON format.

Installation
To run this application, you'll need to have Python 3 installed on your machine. You can install the required dependencies by running the following command:

```bash

pip install -r requirements.txt
```
Usage
To use this application, you'll need to provide a JSON file containing the initial data. This file should have the following structure:


```json

[
  {
    "name": "John",
    "gave": [
      {"name": "drinks", "amount": 800}
    ]
  },
  {
    "name": "Shawn",
    "gave": [
      {"name": "food", "amount": 120}
    ]
  },
  {
    "name": "Nivo",
    "gave": [
      {"name": "food", "amount": 250}
    ]
  },
  {
    "name": "Ari",
    "gave": [
      {"name": "food", "amount": 250},
      {"name": "basar", "amount": 2200}
    ]
  },
  {
    "name": "Avivo",
    "exceptions": ["basar"]
  },
  { "name": "Saar" },
  { "name": "Tomer" }
]
```
To run the application, use the following command:

```bash
python main.py
```
The application will read the JSON file, calculate the debts, and output the results in JSON format. The output will be stored in the output/processed_participants.json file.

You can also provide a JSON file directly to the application using the following command:
```
bash
python scripts/run-kama.sh path/to/file.json
This will send the JSON file to the application's API endpoint at http://localhost:8080/kama, and the results will be printed to the console.
```
API
The application provides an API endpoint at http://localhost:8080/kama that you can use to send JSON files directly to the application. The API endpoint expects a JSON payload with the following structure:
```
json
CopyInsert
{
  "data": [
    {
      "name": "John",
      "gave": [
        {"name": "drinks", "amount": 800}
      ]
    },
    ...
  ]
}
```
The application will return a JSON response with the calculated results.

