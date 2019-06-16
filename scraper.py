import scraperwiki
html = scraperwiki.scrape('https://inmo.ie/6022')
print "Click on the ...more link to see the whole page"
# print html

import lxml.html
root = lxml.html.fromstring(html) # turn our HTML into an lxml object
tds = root.cssselect('td') # get all the <td> tags
print tds
for td in tds:
    print lxml.html.tostring(td) # the full HTML tag
    print td.text                # just the text inside the HTML tag

for td in tds:
    record = { "td" : td.text } # column name and value
    try:
        scraperwiki.sqlite.save(["td"], record) # save the records one by one
    except:
        record = { "td" : "NO ENTRY" } # column name and value
        scraperwiki.sqlite.save(["td"], record) # save the records one by one
        
        
