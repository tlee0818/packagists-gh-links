import getNames as gn
import getLinks as gl

PACKAGE_NAME_FILE = "csv/packageNames.csv"
LINK_FILE = "csv/links.csv"
NO_LINK_FILE = "csv/no-links.csv"

gn.get_package_names(PACKAGE_NAME_FILE)
gl.get_package_links(PACKAGE_NAME_FILE, LINK_FILE, NO_LINK_FILE)


