# Food Supplier Web Scraper 🍎

A Python web scraping tool to collect food industry suppliers data for building a B2B directory.

## Features

- ✅ Scrape supplier information from multiple sources
- ✅ Extract company names, contact details, locations, products
- ✅ Save data to CSV/JSON formats
- ✅ Filter by region and product category
- ✅ Easy to use command-line interface

## What This Scrapes

- Food suppliers and distributors
- Company contact information
- Product categories
- Location/region data
- Website URLs
- Phone numbers and emails (where available)

## Installation

### Prerequisites
- Python 3.8+
- pip (Python package manager)

### Setup

1. Clone the repository:
```bash
git clone https://github.com/05t03b/food-supplier-scraper.git
cd food-supplier-scraper
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage

### Basic Scraping
```bash
python scraper.py --query "food suppliers" --region "USA" --limit 50
```

### Save to CSV
```bash
python scraper.py --query "food suppliers" --output suppliers.csv --format csv
```

### Save to JSON
```bash
python scraper.py --query "food exporters" --output suppliers.json --format json
```

## Options

- `--query`: Search term (e.g., "food suppliers", "spice exporters")
- `--region`: Filter by region/country
- `--limit`: Number of results to scrape (default: 100)
- `--output`: Output file name
- `--format`: Output format (csv or json, default: csv)

## Examples

### Scrape Indian Food Suppliers
```bash
python scraper.py --query "food suppliers India" --region "India" --limit 100 --output indian_suppliers.csv
```

### Scrape Organic Food Exporters
```bash
python scraper.py --query "organic food exporters" --limit 50 --format json
```

### Scrape Seafood Distributors
```bash
python scraper.py --query "seafood distributors" --region "Southeast Asia" --limit 200
```

## Output Format

### CSV Format
```
company_name,website,location,category,email,phone
ABC Food Exports,www.abc.com,Mumbai India,Spices,info@abc.com,+91-123456789
XYZ Supplies,www.xyz.com,Bangkok Thailand,Seafood,contact@xyz.com,+66-987654321
```

### JSON Format
```json
[
  {
    "company_name": "ABC Food Exports",
    "website": "www.abc.com",
    "location": "Mumbai, India",
    "category": "Spices",
    "email": "info@abc.com",
    "phone": "+91-123456789"
  }
]
```

## Data Sources

The scraper collects data from:
- Google Search results
- Business directories
- Trade portals
- LinkedIn company pages (public data)
- Industry websites

## Legal & Ethics

⚠️ **Important**: 
- Always respect website `robots.txt` files
- Don't overload servers with requests
- Use data responsibly and legally
- Check terms of service of websites before scraping
- Add delays between requests to avoid being blocked

## Troubleshooting

### "Connection Error"
- Check your internet connection
- Some websites may block scrapers
- Try with a different search query

### "No Results Found"
- Try broader search terms
- Check region spelling
- Increase the `--limit` value

### "Rate Limit Exceeded"
- Wait a few minutes before scraping again
- Reduce the `--limit` value
- Add longer delays in configuration

## Next Steps

1. Run the scraper to collect data
2. Import data into Google Sheets or Notion
3. Clean and validate the data
4. Upload to your B2B dictionary

## Contributing

Got ideas to improve the scraper? Feel free to fork and submit pull requests!

## License

MIT License - Free to use and modify

## Support

For issues or questions, open a GitHub issue in this repository.

---

**Happy Scraping! 🚀**