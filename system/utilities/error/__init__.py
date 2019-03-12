class NoServiceError(Exception):
	def __init__(self):
		# use this error to notify that no known map service running for the given url
		self.message = 'Error there are no known map service running for the given url'
		super(self.__class__, self).__init__(self.message)

	def __str__(self):
		return self.message

class UnreachableError(Exception):
	def __init__(self):
		# use this error to notify that client cannot reach the given url
		self.message = 'Error cannot reach the given url'
		super(self.__class__, self).__init__(self.message)

	def __str__(self):
		return self.message