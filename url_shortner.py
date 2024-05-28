import pyshorteners
website_url = input("PLEASE ENTER THE WEBSITE URL HERE : ")
s = pyshorteners.Shortener()
short_url = s.tinyurl.short(website_url)
print(short_url)
