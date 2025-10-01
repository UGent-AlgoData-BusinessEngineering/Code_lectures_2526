import urllib.request
input = urllib.request.urlopen('http://www.google.com')
print(input.read())