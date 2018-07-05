import requests
#Open image with binary
files = {"file":open("lena.jpg","rb")}

#Send Http request with web server
r = requests.post("http://18.216.246.52/upload", files = files) 
    
print(r.status_code, r.reason)
print(r.text[:300] + '...')


