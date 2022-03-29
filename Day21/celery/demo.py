import requests

res = requests.get("http://api.coincap.io/v2/assets/gala")
if res.status_code == 200:
    print(request.form['data'])