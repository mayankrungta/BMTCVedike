Chosen conventions for this project from - PEP 8 -- Style Guide for Python Code https://www.python.org/dev/peps/pep-0008/

A Foolish Consistency is the Hobgoblin of Little Minds

Some other good reasons to ignore a particular guideline:

    When applying the guideline would make the code less readable, even for someone who is used to reading code that follows this PEP.
    To be consistent with surrounding code that also breaks it (maybe for historic reasons) -- although this is also an opportunity to clean up someone else's mess (in true XP style).
    Because the code in question predates the introduction of the guideline and there is no other reason to be modifying that code.
    When the code needs to remain compatible with older versions of Python that don't support the feature recommended by the style guide.

NOTE: In particular: do not break backwards compatibility just to comply with this PEP!



# More indentation included to distinguish this from the rest.
def long_function_name(
        var_one, var_two, var_three,
        var_four):
    print(var_one)

# Add some extra indentation on the conditional continuation line.
if (this_is_one_thing
        and that_is_another_thing):
    do_something()


my_list = [
    1, 2, 3,
    4, 5, 6,
]
result = some_function_that_takes_arguments(
    'a', 'b', 'c',
    'd', 'e', 'f',
)

The Python standard library is conservative and requires limiting lines to 79 characters (and docstrings/comments to 72).

with open('/path/to/some/file/you/want/to/read') as file_1, \
     open('/path/to/some/file/being/written', 'w') as file_2:
    file_2.write(file_1.read())

Following the tradition from mathematics usually results in more readable code:

# Yes: easy to match operators with operands
income = (gross_wages
          + taxable_interest
          + (dividends - qualified_dividends)
          - ira_deduction
          - student_loan_interest)

Blank Lines

Surround top-level function and class definitions with two blank lines.

Method definitions inside a class are surrounded by a single blank line.

Extra blank lines may be used (sparingly) to separate groups of related functions. Blank lines may be omitted between a bunch of related one-liners (e.g. a set of dummy implementations).

Use blank lines in functions, sparingly, to indicate logical sections.


Source File Encoding

Code in the core Python distribution should always use UTF-8

For Python 3.0 and beyond, the following policy is prescribed for the standard library (see PEP 3131): All identifiers in the Python standard library MUST use ASCII-only identifiers, and SHOULD use English words wherever feasible (in many cases, abbreviations and technical terms are used which aren't English). In addition, string literals and comments must also be in ASCII. The only exceptions are (a) test cases testing the non-ASCII features, and (b) names of authors. Authors whose names are not based on the Latin alphabet (latin-1, ISO/IEC 8859-1 character set) MUST provide a transliteration of their names in this character set.

Imports

    Imports should usually be on separate lines:

    Yes: import os
         import sys

    No:  import sys, os

    It's okay to say this though:

    from subprocess import Popen, PIPE

Imports should be grouped in the following order:

    Standard library imports.
    Related third party imports.
    Local application/library specific imports.

You should put a blank line between each group of imports.

Wildcard imports (from <module> import *) should be avoided, as they make it unclear which names are present in the namespace, confusing both readers and many automated tools. There is one defensible use case for a wildcard import, which is to republish an internal interface as part of a public API (for example, overwriting a pure Python implementation of an interface with the definitions from an optional accelerator module and exactly which definitions will be overwritten isn't known in advance).


String Quotes

In Python, single-quoted strings and double-quoted strings are the same. This PEP does not make a recommendation for this. Pick a rule and stick to it. When a string contains single or double quote characters, however, use the other one to avoid backslashes in the string. It improves readability.

For triple-quoted strings, always use double quote characters to be consistent with the docstring convention in PEP 257.

ASIDE: In this project single quotes are encouraged for Python and JavaScript while double quotes for HTML and (S)CSS Styling. When mixing languages give importance to style recommendations for that language.

White Spaces

Yes: spam(ham[1], {eggs: 2})
No:  spam( ham[ 1 ], { eggs: 2 } )

Yes: foo = (0,)
No:  bar = (0, )

Yes: if x == 4: print x, y; x, y = y, x
No:  if x == 4 : print x , y ; x , y = y , x

Yes:

ham[1:9], ham[1:9:3], ham[:9:3], ham[1::3], ham[1:9:]
ham[lower:upper], ham[lower:upper:], ham[lower::step]
ham[lower+offset : upper+offset]
ham[: upper_fn(x) : step_fn(x)], ham[:: step_fn(x)]
ham[lower + offset : upper + offset]

No:

ham[lower + offset:upper + offset]
ham[1: 9], ham[1 :9], ham[1:9 :3]
ham[lower : : upper]
ham[ : upper]

Yes: spam(1)
No:  spam (1)

Yes: dct['key'] = lst[index]
No:  dct ['key'] = lst [index]

Yes:

x = 1
y = 2
long_variable = 3

No:

x             = 1
y             = 2
long_variable = 3


Yes:

i = i + 1
submitted += 1
x = x*2 - 1
hypot2 = x*x + y*y
c = (a+b) * (a-b)

No:

i=i+1
submitted +=1
x = x * 2 - 1
hypot2 = x * x + y * y
c = (a + b) * (a - b)


NOTE: Don't use spaces around the = sign when used to indicate a keyword argument or a default parameter value.

Yes:

def complex(real, imag=0.0):
    return magic(r=real, i=imag)

No:

def complex(real, imag = 0.0):
    return magic(r = real, i = imag)


When combining an argument annotation with a default value, use spaces around the = sign (but only for those arguments that have both an annotation and a default).

Yes:

def munge(sep: AnyStr = None): ...
def munge(input: AnyStr, sep: AnyStr = None, limit=1000): ...

No:

def munge(input: AnyStr=None): ...
def munge(input: AnyStr, limit = 1000): ...


Compound statements (multiple statements on the same line) are generally discouraged.

Rather not:

if foo == 'blah': do_blah_thing()
do_one(); do_two(); do_three()


While sometimes it's okay to put an if/for/while with a small body on the same line, never do this for multi-clause statements. Also avoid folding such long lines!

Rather not:

if foo == 'blah': do_blah_thing()
for x in lst: total += x
while t < 10: t = delay()

Definitely not:

if foo == 'blah': do_blah_thing()
else: do_non_blah_thing()

try: something()
finally: cleanup()

do_one(); do_two(); do_three(long, argument,
                             list, like, this)

if foo == 'blah': one(); two(); three()


Trailing Commas

For clarity, it is recommended to surround the latter in (technically redundant) parentheses.

Yes:

FILES = ('setup.cfg',)

OK, but confusing:

FILES = 'setup.cfg',

Yes:

FILES = [
    'setup.cfg',
    'tox.ini',
    ]
initialize(FILES,
           error=True,
           )

No:

FILES = ['setup.cfg', 'tox.ini',]
initialize(FILES, error=True,)


Comments

Comments that contradict the code are worse than no comments. Always make a priority of keeping the comments up-to-date when the code changes!

Comments should be complete sentences. The first word should be capitalized, unless it is an identifier that begins with a lower case letter (never alter the case of identifiers!).

Block comments generally consist of one or more paragraphs built out of complete sentences, with each sentence ending in a period.

You should use two spaces after a sentence-ending period in multi- sentence comments, except after the final sentence.

When writing English, follow Strunk and White.

Python coders from non-English speaking countries: please write your comments in English, unless you are 120% sure that the code will never be read by people who don't speak your language.



Block Comments

Block comments generally apply to some (or all) code that follows them, and are indented to the same level as that code. Each line of a block comment starts with a # and a single space (unless it is indented text inside the comment).

Paragraphs inside a block comment are separated by a line containing a single #.



Inline Comments

Use inline comments sparingly.

An inline comment is a comment on the same line as a statement. Inline comments should be separated by at least two spaces from the statement. They should start with a # and a single space.

Inline comments are unnecessary and in fact distracting if they state the obvious. Don't do this:

x = x + 1                 # Increment x

But sometimes, this is useful:

x = x + 1                 # Compensate for border




Documentation Strings

Conventions for writing good documentation strings (a.k.a. "docstrings") are immortalized in PEP 257.

    Write docstrings for all public modules, functions, classes, and methods. Docstrings are not necessary for non-public methods, but you should have a comment that describes what the method does. This comment should appear after the def line.

    PEP 257 describes good docstring conventions. Note that most importantly, the """ that ends a multiline docstring should be on a line by itself:

    """Return a foobang

    Optional plotz says to frobnicate the bizbaz first.
    """

    For one liner docstrings, please keep the closing """ on the same line.



The following naming styles are commonly distinguished:

    b (single lowercase letter)

    B (single uppercase letter)

    lowercase

    lower_case_with_underscores

    UPPERCASE

    UPPER_CASE_WITH_UNDERSCORES

    CapitalizedWords (or CapWords, or CamelCase -- so named because of the bumpy look of its letters [4]). This is also sometimes known as StudlyCaps.

    Note: When using acronyms in CapWords, capitalize all the letters of the acronym. Thus HTTPServerError is better than HttpServerError.

    mixedCase (differs from CapitalizedWords by initial lowercase character!)

    Capitalized_Words_With_Underscores (ugly!)
In addition, the following special forms using leading or trailing underscores are recognized (these can generally be combined with any case convention):

    _single_leading_underscore: weak "internal use" indicator. E.g. from M import * does not import objects whose name starts with an underscore.

    single_trailing_underscore_: used by convention to avoid conflicts with Python keyword, e.g.

    Tkinter.Toplevel(master, class_='ClassName')

    __double_leading_underscore: when naming a class attribute, invokes name mangling (inside class FooBar, __boo becomes _FooBar__boo; see below).

    __double_leading_and_trailing_underscore__: "magic" objects or attributes that live in user-controlled namespaces. E.g. __init__, __import__ or __file__. Never invent such names; only use them as documented.

NOTE: Names to Avoid - Never use the characters 'l' (lowercase letter el), 'O' (uppercase letter oh), or 'I' (uppercase letter eye) as single character variable names.

Package and Module Names

Modules should have short, all-lowercase names. Underscores can be used in the module name if it improves readability. Python packages should also have short, all-lowercase names, although the use of underscores is discouraged.


Class Names

Class names should normally use the CapWords convention.

The naming convention for functions may be used instead in cases where the interface is documented and used primarily as a callable.

Note that there is a separate convention for builtin names: most builtin names are single words (or two words run together), with the CapWords convention used only for exception names and builtin constants.



Exception Names

Because exceptions should be classes, the class naming convention applies here. However, you should use the suffix "Error" on your exception names (if the exception actually is an error).



Global Variable Names

(Let's hope that these variables are meant for use inside one module only.) The conventions are about the same as those for functions.

Modules that are designed for use via from M import * should use the __all__ mechanism to prevent exporting globals, or use the older convention of prefixing such globals with an underscore (which you might want to do to indicate these globals are "module non-public").



Function and Variable Names

Function names should be lowercase, with words separated by underscores as necessary to improve readability.

Variable names follow the same convention as function names.

NOTE: mixedCase is allowed only in contexts where that's already the prevailing style (e.g. threading.py), to retain backwards compatibility.



Function and Method Arguments

Always use self for the first argument to instance methods.

Always use cls for the first argument to class methods.

If a function argument's name clashes with a reserved keyword, it is generally better to append a single trailing underscore rather than use an abbreviation or spelling corruption. Thus class_ is better than clss. (Perhaps better is to avoid such clashes by using a synonym.)


Method Names and Instance Variables

Use the function naming rules: lowercase with words separated by underscores as necessary to improve readability.

Use one leading underscore only for non-public methods and instance variables.

To avoid name clashes with subclasses, use two leading underscores to invoke Python's name mangling rules.

Python mangles these names with the class name: if class Foo has an attribute named __a, it cannot be accessed by Foo.__a. (An insistent user could still gain access by calling Foo._Foo__a.) Generally, double leading underscores should be used only to avoid name conflicts with attributes in classes designed to be subclassed.


Constants

Constants are usually defined on a module level and written in all capital letters with underscores separating words. Examples include MAX_OVERFLOW and TOTAL.


Yes:

if foo is not None:

No:

if not foo is None:


Always use a def statement instead of an assignment statement that binds a lambda expression directly to an identifier.

Yes:

def f(x): return 2*x

No:

f = lambda x: 2*x

The first form means that the name of the resulting function object is specifically 'f' instead of the generic '<lambda>'. This is more useful for tracebacks and string representations in general. The use of the assignment statement eliminates the sole benefit a lambda expression can offer over an explicit def statement (i.e. that it can be embedded inside a larger expression)


When catching exceptions, mention specific exceptions whenever possible instead of using a bare except: clause:

try:
    import platform_specific_module
except ImportError:
    platform_specific_module = None

A bare except: clause will catch SystemExit and KeyboardInterrupt exceptions, making it harder to interrupt a program with Control-C, and can disguise other problems. If you want to catch all exceptions that signal program errors, use except Exception: (bare except is equivalent to except BaseException:).

A good rule of thumb is to limit use of bare 'except' clauses to two cases:

    If the exception handler will be printing out or logging the traceback; at least the user will be aware that an error has occurred.
    If the code needs to do some cleanup work, but then lets the exception propagate upwards with raise. try...finally can be a better way to handle this case.


When binding caught exceptions to a name, prefer the explicit name binding syntax added in Python 2.6:

try:
    process_data()
except Exception as exc:
    raise DataProcessingFailedError(str(exc))

This is the only syntax supported in Python 3, and avoids the ambiguity problems associated with the older comma-based syntax.

ASIDE: Please ensure the below is the rule of any exception handling if a specific error is not handled.
try:
    process_data()
except Exception as e:
    logger.error('Exception: [{exception}]'.format(excpetion=str(exc))) # Use critical, warning, etc. as is appropriate
	.
	.
	.

NOTE: The above is used instead of bare except (which is equivalent to except BaseException:) ALWAYS!


Additionally, for all try/except clauses, limit the try clause to the absolute minimum amount of code necessary. Again, this avoids masking bugs.

Yes:

try:
    value = collection[key]
except KeyError:
    return key_not_found(key)
else:
    return handle_value(value)

No:

try:
    # Too broad!
    return handle_value(collection[key])
except KeyError:
    # Will also catch KeyError raised by handle_value()
    return key_not_found(key)

ASIDE:  ^^^--- Been hit several times by this :)

When a resource is local to a particular section of code, use a with statement to ensure it is cleaned up promptly and reliably after use. A try/finally statement is also acceptable.

ASIDE: ^^^--- Almost always use with, copy the content into local variables and release the resource if not needed. Especially, when dealing with files. Limit operations with 'with'


Be consistent in return statements. Either all return statements in a function should return an expression, or none of them should. If any return statement returns an expression, any return statements where no value is returned should explicitly state this as return None, and an explicit return statement should be present at the end of the function (if reachable).

Yes:

def foo(x):
    if x >= 0:
        return math.sqrt(x)
    else:
        return None

def bar(x):
    if x < 0:
        return None
    return math.sqrt(x)

No:

def foo(x):
    if x >= 0:
        return math.sqrt(x)

def bar(x):
    if x < 0:
        return
    return math.sqrt(x)

ASIDE: Always use return in this project. If nothing to be returned, return None


Use ''.startswith() and ''.endswith() instead of string slicing to check for prefixes or suffixes.

startswith() and endswith() are cleaner and less error prone:

Yes: if foo.startswith('bar'):
No:  if foo[:3] == 'bar':


Object type comparisons should always use isinstance() instead of comparing types directly.

Yes: if isinstance(obj, int):

No:  if type(obj) is type(1):


For sequences, (strings, lists, tuples), use the fact that empty sequences are false.

Yes: if not seq:
     if seq:

No:  if len(seq):
     if not len(seq):


Don't compare boolean values to True or False using ==.

Yes:   if greeting:
No:    if greeting == True:
Worse: if greeting is True:


ASIDE: In this project the following are the conventions ALWAYS:

if not url:
	url = 'default-url'

if downloaded:
	parse()

def my_view(request):
    my_objects = list(MyModel.objects.filter(published=True))
    if not my_objects:





