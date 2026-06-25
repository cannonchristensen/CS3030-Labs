import requests

url_list = ["https://github.com", "https://www.apple.com", "https://musicians.int"]

for url in url_list:
	try:
		if requests.get(url).status_code == 200:
			print(f"{url}: SITE UP")
		else:
			print(f"{url}: SITE DOWN")
	except requests.exceptions.RequestException:	
		print(f"{url}: SITE DOWN")