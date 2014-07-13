
<span class="ModuleDoc YAMLDoc" markdown="1">

# *module* yamldoc

v0.1.0


*Copyright 2014 Sebastiaan Mathôt* (<http://www.cogsci.nl/smathot>)

__About yamldoc:__

With `yamldoc` you can take Python docstrings to the next level.

-       A systematic YAML-based docstring notation.
-       Generates markdown-formatted documentation for modules, classes, and
        functions.
-       Automatically validate input and output of functions and methods.

__Index:__


- [*module* yamldoc](#module-yamldoc)
	- [*class* yamldoc.BaseDoc](#class-yamldoc.basedoc)
	- [*function* yamldoc.DocFactory(obj, types=[u'function', u'class', u'module'])](#function-yamldoc.docfactoryobj-typesufunction-uclass-umodule)
	- [*function* yamldoc.validate(func)](#function-yamldoc.validatefunc)




__Example:__

~~~
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

~~~



<span class="ClassDoc YAMLDoc" markdown="1">

## *class* yamldoc.BaseDoc

The base class from which the other doc classes are derived. You don't create a `BaseDoc` object directly, but use the `DocFactory()` function to create an object-specific doc object for you.



<span class="FunctionDoc YAMLDoc" markdown="1">

### *function* yamldoc.BaseDoc.\_\_init\_\_(obj, level=1, enc=u'utf-8', namePrefix=u'')

Constructor.

__Arguments:__

- obj -- The object to document.

__Keywords:__

- enc -- The string encoding.
	- Default: u'utf-8'
	- Type: str, unicode
- namePrefix -- A prefix to be pre-pended to the object's name.
	- Default: u''
	- Type: str, unicode
- level -- Describes the header level to be used, so that you can generate formatted documentation.
	- Default: 1
	- Type: int




</span>

<span class="FunctionDoc YAMLDoc" markdown="1">

### *function* yamldoc.BaseDoc.\_\_str\_\_()

Returns a string representation of the object's documentation.

__Returns:__

A string representation of the object's documentation.

- Type: str




</span>

<span class="FunctionDoc YAMLDoc" markdown="1">

### *function* yamldoc.BaseDoc.\_\_unicode\_\_()

Returns a unicode string representation of the object's documentation.

__Returns:__

A unicode string representation of the object's documentation.

- Type: unicode




</span>

<span class="FunctionDoc YAMLDoc" markdown="1">

### *function* yamldoc.BaseDoc._dict()

Generates a dict representation of the object's documentation.

__Returns:__

A dict representation of the object's documentation.

- Type: dict




</span>

<span class="FunctionDoc YAMLDoc" markdown="1">

### *function* yamldoc.BaseDoc.name()

Returns the object's name with prefix.

__Returns:__

The object's name with prefix.

- Type: unicode




</span>


</span>

<span class="FunctionDoc YAMLDoc" markdown="1">

## *function* yamldoc.DocFactory(obj, types=[u'function', u'class', u'module'])

Creates a type-specific doc object.

__Example:__

~~~
import yamldoc

# Create a type-specific docstring processor for `myFunction`.
df = yamldoc.DocFactory(myFunction)
# Get a markdown-style formatted docstring and print it.
md = unicode(df)
print md
~~~

__Arguments:__

- obj -- The object to document.

__Keywords:__

- types -- A list of types that should be documented.
	- Default: [u'function', u'class', u'module']
	- Type: list

__Argument list:__

- *args: No description.

__Keyword dict:__

- **kwargs: No description.

__Returns:__

A doc object.





</span>

<span class="FunctionDoc YAMLDoc" markdown="1">

## *function* yamldoc.validate(func)

A decorator to validate arguments and return values for a function or method. This decorator allows you to fully specify and check the input and output of a function or method through a properly formatted docstring.

__Example:__

~~~
import yamldoc

@yamldoc.validate
def test(a):

        """
        desc:
                Example function.

        arguments:
                a:
                        desc:   An argument that should be integer.
                        type:   int

        returns:
                desc:           The function should return a boolean.
                type:           bool
        """

        return True
~~~

__Arguments:__

- func -- The function to validate.
	- Type: function, method




</span>


</span>

