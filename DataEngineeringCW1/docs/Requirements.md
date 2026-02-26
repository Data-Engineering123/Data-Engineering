# TechReads Data Engineering Project - Requirements

## Python Libraries Required

To run all scripts in this project, install the following Python libraries:

### Core Libraries
```bash
pip install requests beautifulsoup4 pandas pymongo mysql-connector-python
```

### Library Descriptions

| Library | Purpose | Used In |
|---------|---------|---------|
| `requests` | HTTP library for making web requests (scraping) | `src/scrape_techreads.py` |
| `beautifulsoup4` | HTML parsing library for extracting data from web pages | `src/scrape_techreads.py` |
| `pandas` | Data manipulation and CSV/JSON handling | All data processing scripts |
| `pymongo` | MongoDB driver for Python | `src/mongodb_pipeline.py` |
| `mysql-connector-python` | MySQL database connector for Python | `src/import_csv_to_mysql.py` |

## Additional Requirements

### MySQL Database
- Install MySQL Server (or use XAMPP/WAMP for easy setup)
- Start MySQL service
- Default port: 3306

### MongoDB Database
- Install MongoDB Community Edition
- Start MongoDB service (mongod)
- Default port: 27017

### Apache NiFi
- Download from: https://nifi.apache.org/download.html
- Extract to: `nifi/nifi-2.7.2-bin/`
- Start with: `nifi-2.7.2-bin/nifi-2.7.2/bin/nifi.bat start`

## Quick Install Command

Open Command Prompt and run:
```cmd
pip install requests beautifulsoup4 pandas pymongo mysql-connector-python
```

## Verify Installation

After installing, verify with:
```cmd
python -c "import requests; import bs4; import pandas; import pymongo; import mysql.connector; print('All libraries installed successfully!')"