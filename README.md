This repository contains:

* the code to scrape products and their current stock levels from vinbudin.is,
  the website of Iceland's state alcohol monopoly [ÁTVR] [1]; and
* data files containing these products and their current stock levels.

The code is in the form of a [Scrapy] [2]-based scraper written using
[Python 2.7] [3].

To load the data into two tables named `vinbudin_products` and `vinbudin_stock`
in a [PostgreSQL] [4] database named `data`, run this command in the top-level
directory of this repo:

     psql -d data -1 -f import.sql


[1]: http://www.vinbudin.is/english/Heim/um_%C3%81TVR/history-of-%C3%A1tvr/history-of-atvr.aspx
[2]: http://scrapy.org/
[3]: https://www.python.org/
[4]: http://www.postgresql.org/
