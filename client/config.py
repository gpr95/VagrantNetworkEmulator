clickDepth = 5 # how deep to browse from the rootURL
minWait = 5 # minimum amount of time allowed between HTTP requests
maxWait = 10 # maximum amount of time to wait between HTTP requests
debug = True # set to True to enable useful console output

# use this single item list to test how a site responds to this crawler
# be sure to comment out the list below it.
#rootURLs = ["https://digg.com/"] 

rootURLs = [
	"http://zone0.net:8000/"
	]


# items can be a URL "https://t.co" or simple string to check for "amazon"
blacklist = [
	]  

# must use a valid user agent or sites will hate you
userAgent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) ' \
	'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'
    