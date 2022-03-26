import requests
import csv

def get_package_names(outfile):
    r = requests.get("https://packagist.org/packages/list.json")

    if r.status_code != 200:
        print('exiting')
        return
    
    json = r.json()["packageNames"]
    
    with open(outfile, 'w', newline='') as out:
        writer = csv.writer(out)
        
        for name in json:
            writer.writerow(name.split("/"))

    print("success")
