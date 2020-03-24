class Person():
	name = "Person"
	def __init__(self, name = None):
		self.name = name

jeffray = Person("Huy")
print("%s is name %s" % (Person.name, jeffray.name))
		