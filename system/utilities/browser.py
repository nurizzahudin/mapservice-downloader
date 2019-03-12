import requests

class Browser:
	def __init__(self, useragent=None):
		self.useragent = useragent or 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:54.0) Gecko/20100101 Firefox/54.0'

	def ping(self, url):
		status = requests.head(url).status_code
		if status in [200, 401]:
			return True
		else:
			return False

	def visit(self, url, data=None, method='get', content='application/json', accept='application/json'):
		method = method.lower()
		headers = {'Content-type': content, 'Accept': accept, 'User-Agent': self.useragent}
		visit_options = {
			'headers': headers,
			'url': url
		}
		if method == 'post':
			visit_options['data'] = data
		else:
			visit_options['params'] = data
		visit_method = getattr(requests, method)
		return visit_method(**visit_options)