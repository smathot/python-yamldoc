import yamldoc

class ExampleClass(object):

	"""
	desc:
		This is a description for `ExampleClass`. The docstring is a YAML
		dictionary, where `desc` contains the main description.
	"""

	@yamldoc.validate
	def ExampleFunction(self, a, b=1, *arglist, **kwdict):

		"""
		desc:
			This function accepts only `str` and `unicode` values for `a` and
			only `int` values for `b`. In addition, it accepts an argument list
			and a keyword dictionary.

		example: |
			ExampleFunction('test value')
			ExampleFunction('test value', b=0)

		arguments:
			a:
				desc:	An argument.
				type:	[str, unicode]

		keywords:
			b:
				desc:	A keyword.
				type:	int

		argument-list:
			varargs:	An argument list.

		keyword-dict:
			keywords:	A keyword dictionary.

		returns:
			desc:	Some return value.
			type:	int
		"""

		return 1

# Generate and print nicely formatted documentation for ExampleClass
df = yamldoc.DocFactory(ExampleClass)
print df
# Create an instance of ExampleClass
ec = ExampleClass()
# This works, because argument `a` should be string and keyword `b` should int.
ec.ExampleFunction('test', b=10)
# This will give an error, because the argument types do not match the docstring
# specification.
ec.ExampleFunction(10, b='test')
