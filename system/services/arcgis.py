from system.utilities.error import *

class Arcgis:
	def __init__(self, url):
		try:
			self.browser = Browser()
			self.root = self._get_root(url)
		except Exception as e:
			print(Exception)
			return False

	def _make_url(self, url):
		pattern = '/arcgis/service'
		if pattern in url:
			return url.split(pattern, 1)[0]
		else:
			return f'{url}{pattern}'

	def _get_root(self, url):
		url = self._make_url(url)
		if self.browser.ping(url):
			return url
		else:
			raise UnreachableError

	def _get_content(self, url):
		result = self.browser.visit(url)
		print(result)

	def _get_type(self):
		pass