
# finding url within a piece of html text
def get_next_target(page):
    start_link = page.find('<a href="')

    if start_link == -1:
        return None, 0
    else:
        start_quote = page.find('"', start_link)
        end_quote = page.find('"', start_quote+1)
        url = page[start_quote+1:end_quote]
        return url, end_quote


# recursively finding all the url within the html source page
def print_all_links(page):
    url, end_pos = get_next_target(page)
    if url:
        print url
        print_all_links(page[end_pos:])


# getting the source page for the given url argument
def get_page(url):
    try:
        import urllib
        return urllib.urlopen(url).read()
    except:
        return ''
        

source_url = "http://xkcd.com"  # hard coded url, would need it to be runtime input
page = get_page(source_url)
print_all_links(page)
