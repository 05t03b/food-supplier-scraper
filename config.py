"""
Configuration file for Food Supplier Scraper
"""

# Scraper settings
DELAY_BETWEEN_REQUESTS = 2.0  # seconds
REQUEST_TIMEOUT = 10  # seconds
MAX_RETRIES = 3
RETRY_DELAY = 5  # seconds

# Output settings
DEFAULT_OUTPUT_FORMAT = 'csv'  # csv or json
OUTPUT_DIRECTORY = './output'

# Scraping sources
ENABLE_GOOGLE_BUSINESS = True
ENABLE_INDUSTRY_DIRECTORIES = True
ENABLE_LINKEDIN = False  # Manual only due to ToS

# Search categories for food industry
FOOD_CATEGORIES = [
    'Food Exporter',
    'Food Importer',
    'Food Distributor',
    'Seafood Supplier',
    'Dairy Supplier',
    'Grain Supplier',
    'Spice Exporter',
    'Organic Food Producer',
    'Food Manufacturer',
    'Beverage Supplier'
]

# Common regions
REGIONS = {
    'ASIA': ['India', 'Thailand', 'Vietnam', 'Indonesia', 'China'],
    'EUROPE': ['Germany', 'Netherlands', 'France', 'Poland', 'Italy'],
    'AMERICAS': ['USA', 'Canada', 'Brazil', 'Mexico', 'Argentina'],
    'AFRICA': ['South Africa', 'Kenya', 'Ethiopia', 'Nigeria', 'Morocco']
}

# Legal/ethical settings
RESPECT_ROBOTS_TXT = True
ADD_DELAYS = True
USER_AGENT = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
