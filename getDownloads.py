import requests
import csv

BASE_URL = "https://packagist.org/packages/{vendor}/{framework}/stats/all.json?average=monthly"
def get_download_count(infile, outfile):

    with open(infile, newline='') as names, open (outfile, "w", newline = '') as out:
        writer = csv.writer(out)
        for name in names:
            #reformat name
            this_vendor = (name.split(",")[0]).strip()
            this_framework = (name.split(",")[1]).strip()
            trailing = (name.split(",")[2]).strip()

            r = requests.get(BASE_URL.format(vendor = this_vendor, framework = this_framework))

            if r.status_code != 200 or not r.json():
                print("no json for " + trailing)
                continue
            elif not r.json()["labels"] or not r.json()["values"]:
                print("failed for " + trailing)
                continue
            elif not r.json()["values"][trailing]:
                print("failed for " + trailing)
                continue
            elif len(r.json()["labels"]) != len(r.json()["values"][trailing]):
                print("not same length for " + trailing)
                continue

            print(trailing)
            for date, count in zip(r.json()["labels"], r.json()["values"][trailing]):
                writer.writerow([trailing, str(date), str(count)])


    print("success")
