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

def output_results(results):
    if not results:
        exit("Couldn't find any results!")

    import os
    for row in results:
        for key in row.keys():
            print '{} {}'.format(key, row[key])
        print os.linesep
    
    if parser.parse_args().output:
        #out_f = open(parser.parse_args().output, 'w')
        out_f = parser.parse_args().output

        # Write out header
        header = results[0].keys()
        #out_f.write(header)

        # Write out dictionary
        import csv
        print header
        data = csv.DictWriter(out_f, header,delimiter=',') 
        data.writeheader()
        for r in results:
            data.writerow(r)

        out_f.close()



parser = argparse.ArgumentParser()
parser.add_argument('--csv', help='Provide a CSV to scan links from with the format: link, link to look for')
parser.add_argument('--prcsv', help='Provide a CSV to scan links from with the pagerank included in sho\'s format')
parser.add_argument('--output', type=argparse.FileType('w'), help='Path to output CSV')

links = Links()
if parser.parse_args().csv:
    print "Parsing CSV..."
    results = links.status_table_from_csv(parser.parse_args().csv)
    output_results(results) 

if  parser.parse_args().prcsv:
    print "Parsing Pagerank CSV..."
    results = links.status_table_from_pagerank_csv(parser.parse_args().prcsv)
    output_results(results)

