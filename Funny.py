import webbrowser
import urllib.request

webUrl = urllib.request.urlopen("https://www.worldwildlife.org/species/directory?direction=desc&sort=extinction_status")
print(str(webUrl.getCode))
# link = "https://teamtrees.org/"


