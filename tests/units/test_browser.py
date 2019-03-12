import unittest
import re
from system.utilities.browser import Browser

class TestBrowser(unittest.TestCase):
	def test_useragent(self):
		useragent = [
			None,
			'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36 Edge/12.246',
			'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/601.3.9 (KHTML, like Gecko) Version/9.0.2 Safari/601.3.9',
			'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:15.0) Gecko/20100101 Firefox/15.0.1'
		]
		for ua in useragent:
			browser = Browser(useragent=ua)
			result = browser.visit('https://www.whatsmyua.info/')
			result_ua = re.search(r'(<script>var WMUArawUa = ")(.*)(";<\/script>)', result.text).group(2)
			if ua:
				self.assertEqual(result_ua, ua)
			else:
				self.assertEqual(result_ua, 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:54.0) Gecko/20100101 Firefox/54.0')

	def test_ping(self):
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
			self.assertEqual(result, res)

if __name__ == '__main__':
	unittest.main()