DISCLAIMER
==========

_This document is written by applying the concept of 'wishful thinking'. In
other words, it describes the desired functionality which is **NOT** implemented
yet._

_If you find it confusing, take a look at this short and very nicely written
introduction to_ [Readme Driven Development][1] _by_ Tom Preston-Werner, _its
author and evangelist._

_As soon as the contents of this README reflects the actual functionality that
is available to the end user, this disclaimer will disappear._

  [1]: http://tom.preston-werner.com/2010/08/23/readme-driven-development.html

numspell
========

A Python module for spelling numbers.

From the user's point of view, **numspell** is a Python module with a single
public class — the `Speller`. A convenience command-line tool called
**spellnum** is distributed alongside the module. It is but a simple shell
script which executes the command

```shell
$ python -m numspell
```


## Command-Line Interface ##

Let the utility itself describe how it is supposed to be used.

```shell
$ spellnum -h
usage: spellnum [-hd] [--lang=LANG] [--check=<spelling>] <number>

Spell a number in one of the available languages
or check a user's spelling for correctness.


Positional arguments:

  number
      An integer to spell. It has to be a simple number without spaces or
      punctuation marks to separate thousands.

Optional arguments:

  -h, --help
      Show this help message and exit.

  -d, --debug
      Print all of the steps taken to produce the spelling for a given number.
      Useful for debugging purposes and to get to know the algorithm behind
      the process.

  -l LANG, --lang=LANG
      Language code in ISO 639-1 format. Default: en.

      Specify the language to spell with or to use when checking the user-
      provided spelling (see the --check option below).

      Currently supported languages:
        de (German)
        en (English)
        es (Spanish)
        fr (French)
        it (Italian)
        ja (Japanese)
        ru (Russian)
        uk (Ukrainian)

  -c <spelling>, --check=<spelling>
      Provide your own spelling for numspell to check and correct.

      If the spelling is correct, exit with 0 status code. If the spelling is
      wrong, output the correct spelling to stdout and exit with a non-zero
      status code.
```


## Module API ##

The API of the **numspell** module is very straightforward. It can be
explained in two words: `spell` and `check`.

```python
import numspell

# The language code is passed to the Speller class constructor.
gentleman = numspell.Speller('en')

# Pass an integer to the 'spell' method
# and it will return a string with its spelling.
assert(gentleman.spell(1300) == 'one thousand three hundred')
assert(gentleman.spell(10700010) == 'ten million seven hundred thousand ten')

# Here we use the 'es' language code to spell some numbers in Spanish.
torero = numspell.Speller('es')
assert(torero.spell(1989) == 'mil novecientos ochenta y nueve')

# numspell can also check and correct your spelling.
#
# The 'check' method returns a string with correct spelling if the spelling
# provided by the user is wrong.
#
# It returns None otherwise.
assert(torero.check(10007, 'diez mil siete') is None)
assert(torero.check(1, 'dos') == 'uno')
```

This example is taken from the _example.py_ script in the root directory of the
project. You can actually run it yourself to make sure that all of the
assertions hold true.

If you're looking for a more detailed description of the **numspell** module
API, take a look at its help:

    $ python
    >>> import numspell
    >>> help(numspell)

If, however, you would like to dive deeper and find out how you can add a new
spelling language, port the spelling algorithm to another programming language
or contribute to the project in some other way, take a look at developer
documentation in the _doc_ directory.


## How To Contribute ##

The project will have a roadmap at some point in the future.

The _doc_ directory contains developer documentation which describes the design
and implementation of the modules that **numspell** is comprised of. Here's a
brief overview of the documentation files:

* _DeveloperIntro.md_ describes the goals, design decisions and high-level
  architecture of the project.

* _SpellingAlgorithm.md_ outlines the steps of the spelling algorithm and
  explains how each step is implemented.

* _RuleSyntax.md_ represents a reference of the syntax for defining rules by
  which a number is decomposed into logical elements.

* _TemplateSyntax.md_ is a reference of the template string syntax used by the
  **listparse** submodule. It allows to transform the logical elements of a
  number to adjust for possible exceptions and irregularities of a particular
  human language.


## License ##

**numspell** is Copyright (c) 2012 Alexei Sholik. It is distributed under the
terms of the MIT license. See the LICENSE file for the full license text.
