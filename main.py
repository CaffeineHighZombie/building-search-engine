
page =('<div id="top_bin"><div id="top_content" class="width960">'
'<div class="udacity float-left"><a href="http://udacity.com">')
start_link = page.find('<a href="')
start_link = start_link + len('<a href="')
end_link = page.find('">', start_link)
url = page[start_link:end_link]

print url
