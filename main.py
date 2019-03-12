from system.utilities.browser import Browser

if __name__ == '__main__':
	test_url = {
		'https://httpstat.us/200': True,
		'https://httpstat.us/401': True,
		'https://httpstat.us/300': False,
		'https://httpstat.us/400': False,
		'https://httpstat.us/404': False
	}
	browser = Browser()
	for url in test_url.keys():
		res = test_url[url]
		result = browser.ping(url)
		print(result)