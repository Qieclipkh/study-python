from urllib import  request
response = request.urlopen("https://www.python.org/")
print(response.read())
request.urlretrieve("https://www.python.org/",r'F:\ff.html')
