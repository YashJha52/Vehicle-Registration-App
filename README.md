# Vehicle Registration Analyzer

A Streamlit-based application that validates and analyzes Indian vehicle registration numbers using Python Regular Expressions (Regex). The project demonstrates real-world applications of regex concepts such as validation, searching, extraction, and text cleaning.

## Features

- Validate Indian vehicle registration numbers
- Upload vehicle records from a `.txt` file
- Extract valid registration numbers using Regex
- Detect duplicate vehicle numbers
- Display state-wise vehicle count
- Search vehicles by state code
- Extract registration details (State, RTO Code, Series, Number)
- Export cleaned records as a CSV file

## Technologies Used

- Python
- Streamlit
- Pandas
- Regular Expressions (`re`)

## Project Structure

```
Vehicle-Registration-Analyzer/
│── app.py
│── vehicle_records.txt
│── requirements.txt
│── run.sh
└── README.md
```

## Installation

Clone the repository.

```bash
git clone https://github.com/yourusername/Vehicle-Registration-Analyzer.git
cd Vehicle-Registration-Analyzer
```

Install the required packages.

```bash
pip install -r requirements.txt
```

Run the application.

```bash
streamlit run app.py
```

Or use the shell script.

```bash
chmod +x run.sh
./run.sh
```

## Sample Vehicle Numbers

```
MH12AB1234
DL01CD5678
KA05XY9876
TN09PQ9999
UP16GH4567
```

## Regex Pattern Used

```regex
\b[A-Z]{2}[0-9]{1,2}[A-Z]{1,3}[0-9]{4}\b
```

### Pattern Explanation

| Pattern | Description |
|---------|-------------|
| `[A-Z]{2}` | State Code |
| `[0-9]{1,2}` | RTO Code |
| `[A-Z]{1,3}` | Registration Series |
| `[0-9]{4}` | Vehicle Number |

## Screenshots

Add screenshots of the application here.

```
images/home.png
images/results.png
```

## Learning Outcomes

This project demonstrates the use of:

- File handling in Python
- Regular Expressions
- Pattern matching
- Data extraction
- Text cleaning
- Duplicate detection
- Streamlit web application development

## Future Enhancements

- Support for CSV uploads
- Interactive charts with Plotly
- Vehicle registration history
- State-wise analytics dashboard
- Advanced search and filtering

## License

This project is created for educational purposes.
