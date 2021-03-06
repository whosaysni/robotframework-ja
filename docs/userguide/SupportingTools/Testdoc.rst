.. _testdoc:

.. _Test data documentation tool (Testdoc):

Test data documentation tool (Testdoc)
======================================

.. contents::
   :depth: 1
   :local:

Testdoc is Robot Framework's built-in tool for generating high level
documentation based on test cases. The created documentation is in HTML
format and it includes name, documentation and other metadata of each
test suite and test case, as well as the top-level keywords and their
arguments.

.. _General usage:

General usage
-------------

.. _Synopsis:

Synopsis
~~~~~~~~

::

    python -m robot.testdoc [options] data_sources output_file

.. _Options:

Options
~~~~~~~

 -T, --title <title>           Set the title of the generated documentation.
                               Underscores in the title are converted to spaces.
                               The default title is the name of the top level suite.
 -N, --name <name>             Override the name of the top level test suite.
 -D, --doc <doc>               Override the documentation of the top level test suite.
 -M, --metadata <name:value>   Set/override free metadata of the top level test suite.
 -G, --settag <tag>            Set given tag(s) to all test cases.
 -t, --test <name>             Include tests by name.
 -s, --suite <name>            Include suites by name.
 -i, --include <tag>           Include tests by tags.
 -e, --exclude <tag>           Exclude tests by tags.
 -h, --help                    Print this help in the console.

All options except :option:`--title` have exactly the same semantics as same
options have when `executing test cases`__.

__ `Configuring execution`_

.. _Generating documentation:

Generating documentation
------------------------

Data can be given as a single file, directory, or as multiple files and
directories. In all these cases, the last argument must be the file where
to write the output.

Testdoc works with all interpreters supported by Robot Framework (Python,
Jython and IronPython). It can be executed as an installed module like
`python -m robot.testdoc` or as a script like `python path/robot/testdoc.py`.

Examples::

  python -m robot.testdoc my_test.html testdoc.html
  jython -m robot.testdoc --name smoke_tests --include smoke path/to/my_tests smoke.html
  ipy path/to/robot/testdoc.py first_suite.txt second_suite.txt output.html
