
page =('<div id="top_bin"><div id="top_content" class="width960">'
'<div class="udacity float-left"><a href="http://udacity.com">')


def get_next_target(page):
    start_link = page.find('<a href="')

    if start_link == -1:
        return None, 0
    else:
        start_quote = page.find('"', start_link)
        end_quote = page.find('"', start_quote+1)
        url = page[start_quote+1:end_quote]
        return url, end_quote


def print_all_links(page):
    url, end_pos = get_next_target(page)
    if url:
        print url
        print_all_links(page[end_pos:])


def get_page(url):
    try:
        import urllib
        return urllib.urlopen(url).read()
    except:
        return ''
        

source_url = "http://google.com"
page = get_page(source_url)
print_all_links(page)
