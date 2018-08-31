import requests
#Open image with binary
files = {"file":open("lena.jpg","rb")}

#Send Http request with web server
r = requests.post(" http://127.0.0.1:5000/upload", files = files)

print(r.status_code, r.reason)
print(r.text[:300] + '...')


