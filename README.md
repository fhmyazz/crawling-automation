# Crawling and automation
Searching in google with a keyword using Selenium (Python)

Details:
- File "g_search-selenium.py" is a basic selenium. Only Searching file based on keyword in list.
- File "g_search-selenium_bs4.py" is an updated version. Added bs4 to crawl some link on the first page.
- File "g_search-selenium_bs4_mysql.py" is an updated version. Fetching data from DB (MySQL) - search the data on google - crawl some link on the first page - insert to DB (MySQL)
- File "crawl_selenium.sql" is a query I used to create the table which is used on "g_search-selenium_bs4_mysql.py".:
  - Table "list_kw" is filled by the keyword that'll used to search on google.
  - Table "item_list" is filled by all the links from crawling result.
