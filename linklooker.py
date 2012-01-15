from Linklooker.Linklooker import Links, Link

links = Links(["http://google.com"]) 

for link in links.status_table():
    print link
