# Ecommerce-parse
Scrapy spider parsing website and checking whether it is an ecommerce website or not.

The file websites.txt contains a list of 500 websites that will be checked by the spider.
The result is saved into a txt file named result.txt.
It has this form:
```
Website                                             Ecommerce
http://radiounumanele.com                           false
http://www.watchesbestdeals.com/                    false
http://brujas.nyc                                   false
http://microwinner.cn                               false
https://schullin.at/                                true
```
## Approach
This algorithm make a request for every website and check for existant ecommerce vocabulary in the Html response.
In our case we used the word "Cart".

## Setting up the envirenement
Python is required (2.7)
### Installing Scrapy
```
pip install Scrapy
```
### Running the spiders
You can run a spider using the scrapy crawl command, such as:
```
$ scrapy crawl ecommerce
```
