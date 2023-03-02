# web-crawler-scrapy
- Terminal Commands for Scrapy
    1. Install package
        
        ```bash
        pip install scrapy
        ```
        
    2. Setup a scrapy project
        
        ```bash
        cd {where you want to create the project folder}
        scrapy startproject {your pj name}
        ```
        
    3. Change dir to the project folder
        
        ```bash
        cd {your pj name}
        ```
        
    4. Create a spider
        
        ```bash
        scrapy genspider {spider name} {the domain you want to scrape the data from}
        
        # e.g
        # scrapy genspider getquotes quotes.toscrape.com
        ```
        
    5. Edit spider in jupyter notebook / spider /
        
        check [getbooks.py](http://getbooks.py) file for details
        
    6. Run the spider
        
        ```bash
        scrapy crawl {spider name}
        scrapy crawl {spider name} -a address="40-18 48th st" -a borough="4" -o output.csv
        ```
        
    
## getbooks.py
This is a Python script that uses the Scrapy library to scrape book information from the website books.toscrape.com. The script defines a spider called getbooks that navigates to each book page on the website and extracts the title, price, rating, and availability of the book. 
The spider can save this information to a CSV file named on your own. The script uses CSS selectors to extract data from the website's HTML pages and demonstrates how to use Scrapy's functionality to navigate a website and extract data from it.
