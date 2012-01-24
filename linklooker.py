from linklooker.linklooker import Links, Link
import argparse

#links = Links(
#            [
#            "http://google.com",
#            "http://yahoo.com",
#            "http://totally-made-up-domain-name.com",
#            ]
#        ) 
#
#links_table = links.status_table()
#for link in links_table.keys():
#    status = 'Success' if links_table[link] == True else 'Failure'
#    print '{:<40} {}'.format(link + ':', status);

parser = argparse.ArgumentParser()
parser.add_argument('--csv', help='Provide a CSV to scan links from with the format: link, link to look for')

csv_name = parser.parse_args().csv

links = Links()
results = links.status_table_from_csv(csv_name)

import os
for row in results:
    for key in row.keys():
        print '{} {}'.format(key, row[key])
    print os.linesep


