import requests
import csv

BASE_URL = "https://repo.packagist.org/p2/"
def get_package_links(infile, outfile, nolinkout):
    no_links = []
    with open(infile, newline='') as names, open (outfile, "w", newline = '') as out:
        writer = csv.writer(out)
        count = 0
        for name in names:
            #reformat name
            trailing = (name.split(",")[2]).strip()
            r = requests.get(BASE_URL + trailing + ".json")

            if r.status_code != 200 or not r.json():
                print("no json for " + trailing)
                no_links.append(trailing)
                continue
            elif not r.json()["packages"] or not r.json()["packages"][trailing]:
                print("no package field of " + trailing)
                no_links.append(trailing)
                continue
            elif not r.json()["packages"][trailing][0]["source"]:
                print("failed for " + trailing)
                no_links.append(trailing)
                continue
            elif not r.json()["packages"][trailing][0]["source"]["url"]:
                print("failed for " + trailing)
                no_links.append(trailing)
                continue
            count += 1

            link = r.json()["packages"][trailing][0]["source"]["url"]
            writer.writerow([trailing, link])
            print(count)

    with open(nolinkout, "w", newline = "") as noLink:
        writer = csv.writer(noLink)

        for name in no_links:
            writer.writerow([name])
    print("success")
