import getNames as gn
import getLinks as gl
import getDownloads as gd

PACKAGE_NAME_FILE = "csv/packageNames.csv"
LINK_FILE = "csv/links.csv"
NO_LINK_FILE = "csv/no-links.csv"
DOWNLOAD_FILE = "csv/monthly-download-counts.csv"

#gn.get_package_names(PACKAGE_NAME_FILE)
#gl.get_package_links(PACKAGE_NAME_FILE, LINK2, NO_LINK_FILE)

#gl.get_packages_no_link(LINK_FILE, PACKAGE_NAME_FILE, NO_LINK_FILE)

gd.get_download_count(PACKAGE_NAME_FILE, DOWNLOAD_FILE)
