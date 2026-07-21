# Excel Data Cleaner - București

Automated Python tool for cleaning and standardizing real estate property data from București listings.

## Purpose
Processes raw real estate data from multiple sources, standardizes formats, validates values, and generates clean Excel reports.

## Features
- Automatic data type detection (price, date, area sqm)
- Address normalization and geocoding
- Duplicate detection and merging
- Missing value imputation where applicable
- Data standardization (currency conversion, unit normalization)
- Pandas-based processing for 12,000+ records
- Generates pivot tables and profitability analysis per neighborhood

## Usage
```bash
python3 cleaner.py --input raw_listings.xlsx --output cleaned_listings.xlsx
```

## Data Structure
Input requires:
- Property ID
- Address
- Price (RON)
- Area (sqm)
- Rooms
- Floor
- Building Year
- Status (Available/Sold/Rented)

Output includes:
- All input fields (cleaned)
- Standardized price/sqm ratio
- Neighborhood cluster
- Quality score (1-5)
- Processing notes

## Technologies
- Python 3.8+
- Pandas, Openpyxl, NumPy

## Author
Vitalie Turcanu
