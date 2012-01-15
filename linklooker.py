from linklooker.linklooker import Links, Link

links = Links(
            [
            "http://google.com",
            "http://yahoo.com",
            "http://totally-made-up-domain-name.com",
            ]
        ) 

links_table = links.status_table()
for link in links_table.keys():
    status = 'Success' if links_table[link] == True else 'Failure'
    print format(link).rjust(2) + ':', format(status).rjust(3)
