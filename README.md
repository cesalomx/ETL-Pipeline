
<!---
cesalomx/cesalomx is a ✨ special ✨ repository because its `README.md` (this file) appears on your GitHub profile.
You can click the Preview link to take a look at your changes.
--->

# ETL Vivanuncios.com.mx Pipeline

The main purpose of this project is to develop a sqlite database storing data extracted from vivanuncios.com.mx, specificaly Querétaro. The first step is to extract specific data by doing some web-scraping using selenium & scrapy and then, as a second step, append it to a sqlite database by running a pipeline.

## Installation

In order to run this spider, it is mandatory to have the following libraries installed:

```bash
pip install scrapy
pip install scrapy_selenium
```

## Files

* homes.py: _Main python file which contains the code to fetch the data from vivanuncios.com.mx_
* pipeline.py: _A simple function to execute the ETL process in homes.py_
* settings.py: _This file contains only settings considered important or commonly used._

## To run the spider:
```
scrapy crawl homes
```
