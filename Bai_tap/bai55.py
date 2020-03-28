# raise RuntimeError('something wrong')
class RuntimeError(Exception):
	def __init__(self, mismatch):
		Exception.__init__(self, mismatch)
		try:
			print ("And now, the Vocational Guidance Counsellor Sketch.")
			RuntimeError("Does not have proper hat")
		except RuntimeError as problem:
			print ("Vocation problem: {0}".format(problem))