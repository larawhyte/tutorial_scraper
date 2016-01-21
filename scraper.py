# This is a template for a Python scraper on morph.io (https://morph.io)
# including some code snippets below that you should find helpful

import scraperwiki
import lxml.html


# # Read in a page
html = scraperwiki.scrape("http://uk.soccerway.com/teams/netherlands/fortuna-sittard/")
print html
# # Find something on the page using css selectors
#now I want to drill into the variable called html to get the fragments that I want using the lxml library function 'fromstring' results
#go into 'root'
root = lxml.html.fromstring(html)
#'using a selector, I am looking for the following anything in a <td> tag within the lxml object  - this will be a list -change td to a 
#different selector to grab different information
tds=root.cssselect('td')
print tds 
# # Write out to the sqlite database using scraperwiki library
# scraperwiki.sqlite.save(unique_keys=['name'], data={"name": "susan", "occupation": "software developer"})
#
# # An arbitrary query against the database
# scraperwiki.sql.select("* from data where 'name'='peter'")

# You don't have to do things with the ScraperWiki and lxml libraries.
# You can use whatever libraries you want: https://morph.io/documentation/python
# All that matters is that your final data is written to an SQLite database
# called "data.sqlite" in the current working directory which has at least a table
# called "data".
