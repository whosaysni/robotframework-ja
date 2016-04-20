.. _test case:
.. _test cases:
.. _Creating test cases:

テストケースの作成
===================

この節では、テストケースの作り方を説明します。
テストケースを :ref:`テストケースファイル <test case files>` と
:ref:`テストケースディレクトリ<test suite directories>` を使った
:ref:`テストスイート <test suite>` の作り方は、この節の次の節で説明します。

.. contents::
   :depth: 2
   :local:

.. Test case syntax:

テストケースの構文
----------------------

.. Basic syntax:

基本の構文
~~~~~~~~~~~~

テストケースは、キーワードを組み合わせたテーブル（表）として作成します。
ここでいう「テーブル」とは、「テキストをスペースやタブ、パイプ (``|``) で区切ったもの」です。
区切られた各文字列を「カラム」と呼び、行の頭から区切りごとに 1 カラム目、2カラム目、...と数えていきます。
::

      テストケース1
          キーワード1   引数1   引数2   ...
          キーワード2   引数1   ...
          ...

      テストケース2
          ...


「キーワード」は、テスト中のひとつひとつの操作の命令で、 :ref:`テストライブラリ <test libraries>` や :ref:`リソースファイル <resource files>` からインポートしたり、テストケースファイル中の :ref:`キーワードテーブル<keyword table>` で作成したりできます。

テストケースの最初のカラムには、テストケースの名前を入れます。
あるテストケース名の入った行から、次のテストケース名が始まるまで、もしくはテストケーステーブルの末尾に到達するまでが、ひとつのテストケースとみなされます。

テストケースを書く場所には、先頭に ``*** test cases ***`` というヘッダを書きます。
テーブルのヘッダから最初のテストケースまでの間にテストケース以外の内容を記述すると、エラーになります。

.. note::
   スペースやタブで区切る書き方のテストケースの場合、テーブルの「最初のカラム」は行頭、「2番めのカラム」は、行頭から 2 文字以上のスペース、またはタブを入れた後の文字列になります。そのため、テストケース名以外の行は、字下げしているように見えます::

      Test Case Name
          Keyword   Arg1   Arg2...

   このテストを表にすると、以下のようになります::

      +----------------+---------+------+----------+
      | Test Case Name |         |      |          |
      +----------------+---------+------+----------+
      |                | Keyword | Arg1 | Arg2 ... |
      +----------------+---------+------+----------+

テストケースの2行目は、たいていはキーワード名ではじまっています。
例外は、2行目で :ref:`キーワードの戻り値を変数に代入<User keyword return values>` しているときで、この場合、二つめのカラムに変数名、その後にキーワードがあります。
どちらの場合も、キーワード名の後には、キーワードの引数などを表すカラムが入ることがあります。

.. _example-tests:
.. sourcecode:: robotframework

   *** Test Cases ***
   Valid Login
       Open Login Page
       Input Username    demo
       Input Password    mode
       Submit Credentials
       Welcome Page Should Be Open

   Setting Variables
       Do Something    first argument    second argument
       ${value} =    Get Some Value
       Should Be Equal    ${value}    Expected value

.. Settings in the Test Case table:

テストケースに書ける設定
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

テストケースには、ケースごとの設定（テスト設定）を持たせられます。
テスト設定の名前を2カラム目に、設定の値をその後のカラムに指定します。
テスト設定名は、キーワードと区別するために角括弧 (``[ ]``) で囲います。
使える設定名を以下に示します。これらは、このセクションの後でも説明します。

:setting:`[Documentation]`
    テストケースの :ref:`ドキュメント <test case documentation>` を書くときに使います。

:setting:`[Tags]`
    テストケースを :ref:`タグ付け <tagging test cases>` するときに使います。

:setting:`[Setup]`, :setting:`[Teardown]`
    テストケースごとに :ref:`セットアップやティアダウン <test setup and teardown>` を指定するときに使います。

:setting:`[Template]`
   テストの :ref:`テンプレートキーワード <template keyword>` の設定に使います。
   この設定を使うと、テストケースの中には、テンプレートに対して適用する引数のデータしか入れられません。

:setting:`[Timeout]`
   :ref:`テストケースのタイムアウトの設定 <test case timeout>` に使います。
   :ref:`タイムアウト <timeouts>` についての説明も参照してください。

テスト設定を使ったテストケースの例を示します:

.. sourcecode:: robotframework

   *** Test Cases ***
   Test With Settings
       [Documentation]    Another dummy test
       [Tags]    dummy    owner-johndoe
       Log    Hello, world!


.. _Test case related settings in the Setting table:

Setting に書けるテストケース関連の設定
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Setting セクションに、以下のようなテストケース関連の設定が書かれていることがあります。
この設定は、主に、先に挙げたテストケースごとの設定で変更できる値のデフォルト値です。

:setting:`Default Tags`, :setting:`Force Tags`
   :ref:`タグ <tags>` のデフォルトの値や、全てのテストに強制的に付与されるタグです。

:setting:`Test Setup`, :setting:`Test Teardown`
   テストの :ref:`セットアップやティアダウン<test setup and teardown>` のデフォルト値です。

:setting:`Test Template`
   :ref:`テンプレートキーワード <template keyword>` のデフォルト値です。

`Test Timeout`:setting:
   :ref:`テストケースの タイムアウト<test case timeout>` のデフォルト値です。
   :ref:`タイムアウト <timeouts>` についての説明も参照してください。


.. _Using arguments:

引数の使い方
---------------

これまでの例でも、キーワードが様々な引数を取るさまを示してきました。
この節では、この重要な機能について詳しく説明します。
引数を持つような :ref:`ユーザ定義のキーワード <user keyword arguments>` や :ref:`ライブラリのキーワード <Keyword arguments>` の書き方は、別の節で説明します。

キーワードは、引数をとらない場合も、複数取る場合もあります。
引数によっては、デフォルト値が存在する場合もあります。
キーワードがどのような引数を取るかは実装によって決まり、あるキーワードがどんな引数を取るかを知りたければ、キーワードのドキュメントを調べるのがベストです。
この節の例で使われているキーワードのドキュメントは :ref:`Libdoc` ツールで生成できるはずですが、
``javadoc`` のような汎用のドキュメントツールでも、同じ情報が得られます。

.. _Mandatory arguments:

必須の引数
~~~~~~~~~~~~~~~~~~~

ほとんどのキーワードには、常に指定しなければならない引数があります。
こうした引数は、キーワードのドキュメント中では、カンマ区切りの引数名、例えば
`first, second, third` のように表されています。
引数名自体にはあまり意味はなく、大事なのはドキュメントに指定されたのと同じ数の引数を指定しなければならないということです。
引数が少なすぎても、多すぎてもエラーになります。

以下のテストでは、 :ref:`OperatingSystem` ライブラリの :name:`Create Directory` と :name:`Copy File` というキーワードを使っています。
引数は `path` と `source, destination` で、前者のキーワードは引数を一つ、後者は二つ取ります。
最後のキーワードは組み込み :ref:`BuiltIn` ライブラリの :name:`No Operation` で、引数を取りません。

.. sourcecode:: robotframework

   *** Test Cases ***
   Example
       Create Directory    ${TEMPDIR}/stuff
       Copy File    ${CURDIR}/file.txt    ${TEMPDIR}/stuff
       No Operation

Default values
~~~~~~~~~~~~~~

Arguments often have default values which can either be given or
not. In the documentation the default value is typically separated
from the argument name with an equal sign like `name=default
value`, but with keywords implemented using Java there may be
`multiple implementations`__ of the same keyword with different
arguments instead. It is possible that all the arguments have default
values, but there cannot be any positional arguments after arguments
with default values.

__ `Default values with Java`_

Using default values is illustrated by the example below that uses
:name:`Create File` keyword which has arguments `path, content=,
encoding=UTF-8`. Trying to use it without any arguments or more than
three arguments would not work.

.. sourcecode:: robotframework

   *** Test Cases ***
   Example
       Create File    ${TEMPDIR}/empty.txt
       Create File    ${TEMPDIR}/utf-8.txt         Hyvä esimerkki
       Create File    ${TEMPDIR}/iso-8859-1.txt    Hyvä esimerkki    ISO-8859-1

.. _varargs:

Variable number of arguments
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

It is also possible that a keyword accepts any number of arguments.
These so called *varargs* can be combined with mandatory arguments
and arguments with default values, but they are always given after
them. In the documentation they have an asterisk before the argument
name like `*varargs`.

For example, :name:`Remove Files` and :name:`Join Paths` keywords from
the OperatingSystem_ library have arguments `*paths` and `base, *parts`,
respectively. The former can be used with any number of arguments, but
the latter requires at least one argument.

.. sourcecode:: robotframework

   *** Test Cases ***
   Example
       Remove Files    ${TEMPDIR}/f1.txt    ${TEMPDIR}/f2.txt    ${TEMPDIR}/f3.txt
       @{paths} =    Join Paths    ${TEMPDIR}    f1.txt    f2.txt    f3.txt    f4.txt

.. _Named argument syntax:

Named arguments
~~~~~~~~~~~~~~~

The named argument syntax makes using arguments with `default values`_ more
flexible, and allows explicitly labeling what a certain argument value means.
Technically named arguments work exactly like `keyword arguments`__ in Python.

__ http://docs.python.org/2/tutorial/controlflow.html#keyword-arguments

Basic syntax
''''''''''''

It is possible to name an argument given to a keyword by prefixing the value
with the name of the argument like `arg=value`. This is especially
useful when multiple arguments have default values, as it is
possible to name only some the arguments and let others use their defaults.
For example, if a keyword accepts arguments `arg1=a, arg2=b, arg3=c`,
and it is called with one argument `arg3=override`, arguments
`arg1` and `arg2` get their default values, but `arg3`
gets value `override`. If this sounds complicated, the `named arguments
example`_ below hopefully makes it more clear.

The named argument syntax is both case and space sensitive. The former
means that if you have an argument `arg`, you must use it like
`arg=value`, and neither `Arg=value` nor `ARG=value`
works.  The latter means that spaces are not allowed before the `=`
sign, and possible spaces after it are considered part of the given value.

When the named argument syntax is used with `user keywords`_, the argument
names must be given without the `${}` decoration. For example, user
keyword with arguments `${arg1}=first, ${arg2}=second` must be used
like `arg2=override`.

Using normal positional arguments after named arguments like, for example,
`| Keyword | arg=value | positional |`, does not work.
Starting from Robot Framework 2.8 this causes an explicit error.
The relative order of the named arguments does not matter.

.. note:: Prior to Robot Framework 2.8 it was not possible to name arguments
          that did not have a default value.

Named arguments with variables
''''''''''''''''''''''''''''''

It is possible to use `variables`_ in both named argument names and values.
If the value is a single `scalar variable`_, it is passed to the keyword as-is.
This allows using any objects, not only strings, as values also when using
the named argument syntax. For example, calling a keyword like `arg=${object}`
will pass the variable `${object}` to the keyword without converting it to
a string.

If variables are used in named argument names, variables are resolved before
matching them against argument names. This is a new feature in Robot Framework
2.8.6.

The named argument syntax requires the equal sign to be written literally
in the keyword call. This means that variable alone can never trigger the
named argument syntax, not even if it has a value like `foo=bar`. This is
important to remember especially when wrapping keywords into other keywords.
If, for example, a keyword takes a `variable number of arguments`_ like
`@{args}` and passes all of them to another keyword using the same `@{args}`
syntax, possible `named=arg` syntax used in the calling side is not recognized.
This is illustrated by the example below.

.. sourcecode:: robotframework

   *** Test Cases ***
   Example
       Run Program    shell=True    # This will not come as a named argument to Run Process

   *** Keywords ***
   Run Program
       [Arguments]    @{args}
       Run Process    program.py    @{args}    # Named arguments are not recognized from inside @{args}

If keyword needs to accept and pass forward any named arguments, it must be
changed to accept `free keyword arguments`_. See `kwargs examples`_ for
a wrapper keyword version that can pass both positional and named arguments
forward.

Escaping named arguments syntax
'''''''''''''''''''''''''''''''

The named argument syntax is used only when the part of the argument
before the equal sign matches one of the keyword's arguments. It is possible
that there is a positional argument with a literal value like `foo=quux`,
and also an unrelated argument with name `foo`. In this case the argument
`foo` either incorrectly gets the value `quux` or, more likely,
there is a syntax error.

In these rare cases where there are accidental matches, it is possible to
use the backslash character to escape__ the syntax like `foo\=quux`.
Now the argument will get a literal value `foo=quux`. Note that escaping
is not needed if there are no arguments with name `foo`, but because it
makes the situation more explicit, it may nevertheless be a good idea.

__ Escaping_

Where named arguments are supported
'''''''''''''''''''''''''''''''''''

As already explained, the named argument syntax works with keywords. In
addition to that, it also works when `importing libraries`_.

Naming arguments is supported by `user keywords`_ and by most `test libraries`_.
The only exception are Java based libraries that use the `static library API`_.
Library documentation generated with Libdoc_ has a note does the library
support named arguments or not.

.. note:: Prior to Robot Framework 2.8 named argument syntax did not work
          with test libraries using the `dynamic library API`_.

Named arguments example
'''''''''''''''''''''''

The following example demonstrates using the named arguments syntax with
library keywords, user keywords, and when importing the Telnet_ test library.

.. sourcecode:: robotframework

   *** Settings ***
   Library    Telnet    prompt=$    default_log_level=DEBUG

   *** Test Cases ***
   Example
       Open connection    10.0.0.42    port=${PORT}    alias=example
       List files    options=-lh
       List files    path=/tmp    options=-l

   *** Keywords ***
   List files
       [Arguments]    ${path}=.    ${options}=
       Execute command    ls ${options} ${path}

Free keyword arguments
~~~~~~~~~~~~~~~~~~~~~~

Robot Framework 2.8 added support for `Python style free keyword arguments`__
(`**kwargs`). What this means is that keywords can receive all arguments that
use the `name=value` syntax and do not match any other arguments as kwargs.

Free keyword arguments support variables similarly as `named arguments
<Named arguments with variables_>`__. In practice that means that variables
can be used both in names and values, but the escape sign must always be
visible literally. For example, both `foo=${bar}` and `${foo}=${bar}` are
valid, as long as the variables that are used exist. An extra limitation is
that free keyword argument names must always be strings. Support for variables
in names is a new feature in Robot Framework 2.8.6, prior to that possible
variables were left un-resolved.

Initially free keyword arguments only worked with Python based libraries, but
Robot Framework 2.8.2 extended the support to the `dynamic library API`_
and Robot Framework 2.8.3 extended it further to Java based libraries and to
the `remote library interface`_. Finally, user keywords got `kwargs support
<Kwargs with user keywords_>`__ in Robot Framework 2.9. In other words,
all keywords can nowadays support kwargs.

__ http://docs.python.org/2/tutorial/controlflow.html#keyword-arguments

Kwargs examples
'''''''''''''''

As the first example of using kwargs, let's take a look at
:name:`Run Process` keyword in the Process_ library. It has a signature
`command, *arguments, **configuration`, which means that it takes the command
to execute (`command`), its arguments as `variable number of arguments`_
(`*arguments`) and finally optional configuration parameters as free keyword
arguments (`**configuration`). The example below also shows that variables
work with free keyword arguments exactly like when `using the named argument
syntax`__.

.. sourcecode:: robotframework

   *** Test Cases ***
   Using Kwargs
       Run Process    program.py    arg1    arg2    cwd=/home/user
       Run Process    program.py    argument    shell=True    env=${ENVIRON}

See `Free keyword arguments (**kwargs)`_ section under `Creating test
libraries`_ for more information about using the kwargs syntax in
your custom test libraries.

As the second example, let's create a wrapper `user keyword`_ for running the
`program.py` in the above example. The wrapper keyword :name:`Run Program`
accepts any number of arguments and kwargs, and passes them forward for
:name:`Run Process` along with the name of the command to execute.

.. sourcecode:: robotframework

   *** Test Cases ***
   Using Kwargs
       Run Program    arg1    arg2    cwd=/home/user
       Run Program    argument    shell=True    env=${ENVIRON}

   *** Keywords ***
   Run Program
       [Arguments]    @{arguments}    &{configuration}
       Run Process    program.py    @{arguments}    &{configuration}

__ `Named arguments with variables`_

Arguments embedded to keyword names
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

A totally different approach to specify arguments is embedding them
into keyword names. This syntax is supported by both `test library keywords`__
and `user keywords`__.

__ `Embedding arguments into keyword names`_
__ `Embedding arguments into keyword name`_

Failures
--------

When test case fails
~~~~~~~~~~~~~~~~~~~~

A test case fails if any of the keyword it uses fails. Normally this means that
execution of that test case is stopped, possible `test teardown`_ is executed,
and then execution continues from the next test case. It is also possible to
use special `continuable failures`__ if stopping test execution is not desired.

Error messages
~~~~~~~~~~~~~~

The error message assigned to a failed test case is got directly from the
failed keyword. Often the error message is created by the keyword itself, but
some keywords allow configuring them.

In some circumstances, for example when continuable failures are used,
a test case can fail multiple times. In that case the final error message
is got by combining the individual errors. Very long error messages are
automatically cut from the middle to keep reports_ easier to read. Full
error messages are always visible in log_ file as a message of the failed
keyword.

By default error messages are normal text, but
starting from Robot Framework 2.8 they can `contain HTML formatting`__. This
is enabled by starting the error message with marker string `*HTML*`.
This marker will be removed from the final error message shown in reports
and logs. Using HTML in a custom message is shown in the second example below.

.. sourcecode:: robotframework

   *** Test Cases ***
   Normal Error
       Fail    This is a rather boring example...

   HTML Error
       ${number} =    Get Number
       Should Be Equal    ${number}    42    *HTML* Number is not my <b>MAGIC</b> number.

__ `Continue on failure`_
__ `HTML in error messages`_

.. _test case name:
.. _test case documentation:
.. _Test case name and documentation:

Test case name and documentation
--------------------------------

The test case name comes directly from the Test Case table: it is
exactly what is entered into the test case column. Test cases in one
test suite should have unique names.  Pertaining to this, you can also
use the `automatic variable`_ `${TEST_NAME}` within the test
itself to refer to the test name. It is available whenever a test is
being executed, including all user keywords, as well as the test setup
and the test teardown.

The :setting:`[Documentation]` setting allows you to set a free
documentation for a test case. That text is shown in the command line
output, as well as the resulting test logs and test reports.
It is possible to use simple `HTML formatting`_ in documentation and
variables_ can be used to make the documentation dynamic.

If documentation is split into multiple columns, cells in one row are
concatenated together with spaces. This is mainly be useful when using
the `HTML format`_ and columns are narrow. If documentation is `split
into multiple rows`__, the created documentation lines themselves are
`concatenated using newlines`__. Newlines are not added if a line
already ends with a newline or an `escaping backslash`__.

__ `Dividing test data to several rows`_
__ `Newlines in test data`_
__ `Escaping`_

.. sourcecode:: robotframework

   *** Test Cases ***
   Simple
       [Documentation]    Simple documentation
       No Operation

   Formatting
       [Documentation]    *This is bold*, _this is italic_  and here is a link: http://robotframework.org
       No Operation

   Variables
       [Documentation]    Executed at ${HOST} by ${USER}
       No Operation

   Splitting
       [Documentation]    This documentation    is split    into multiple columns
       No Operation

   Many lines
       [Documentation]    Here we have
       ...                an automatic newline
       No Operation

It is important that test cases have clear and descriptive names, and
in that case they normally do not need any documentation. If the logic
of the test case needs documenting, it is often a sign that keywords
in the test case need better names and they are to be enhanced,
instead of adding extra documentation. Finally, metadata, such as the
environment and user information in the last example above, is often
better specified using tags_.

.. _tag:
.. _tags:
.. _test case tags:
.. _Tagging test cases:

Tagging test cases
------------------

Using tags in Robot Framework is a simple, yet powerful mechanism for
classifying test cases. Tags are free text and they can be used at
least for the following purposes:

- Tags are shown in test reports_, logs_ and, of course, in the test
  data, so they provide metadata to test cases.
- Statistics__ about test cases (total, passed, failed  are
  automatically collected based on tags).
- With tags, you can `include or exclude`__ test cases to be executed.
- With tags, you can specify which test cases are considered `critical`_.

__ `Configuring statistics`_
__ `By tag names`_

In this section it is only explained how to set tags for test
cases, and different ways to do it are listed below. These
approaches can naturally be used together.

`Force Tags`:setting: in the Setting table
   All test cases in a test case file with this setting always get
   specified tags. If it is used in the `test suite initialization file`,
   all test cases in sub test suites get these tags.

`Default Tags`:setting: in the Setting table
   Test cases that do not have a :setting:`[Tags]` setting of their own
   get these tags. Default tags are not supported in test suite initialization
   files.

`[Tags]`:setting: in the Test Case table
   A test case always gets these tags. Additionally, it does not get the
   possible tags specified with :setting:`Default Tags`, so it is possible
   to override the :setting:`Default Tags` by using empty value. It is
   also possible to use value `NONE` to override default tags.

`--settag`:option: command line option
   All executed test cases get tags set with this option in addition
   to tags they got elsewhere.

`Set Tags`:name:, `Remove Tags`:name:, `Fail`:name: and `Pass Execution`:name: keywords
   These BuiltIn_ keywords can be used to manipulate tags dynamically
   during the test execution.

Tags are free text, but they are normalized so that they are converted
to lowercase and all spaces are removed. If a test case gets the same tag
several times, other occurrences than the first one are removed. Tags
can be created using variables, assuming that those variables exist.

.. sourcecode:: robotframework

   *** Settings ***
   Force Tags      req-42
   Default Tags    owner-john    smoke

   *** Variables ***
   ${HOST}         10.0.1.42

   *** Test Cases ***
   No own tags
       [Documentation]    This test has tags owner-john, smoke and req-42.
       No Operation

   With own tags
       [Documentation]    This test has tags not_ready, owner-mrx and req-42.
       [Tags]    owner-mrx    not_ready
       No Operation

   Own tags with variables
       [Documentation]    This test has tags host-10.0.1.42 and req-42.
       [Tags]    host-${HOST}
       No Operation

   Empty own tags
       [Documentation]    This test has only tag req-42.
       [Tags]
       No Operation

   Set Tags and Remove Tags Keywords
       [Documentation]    This test has tags mytag and owner-john.
       Set Tags    mytag
       Remove Tags    smoke    req-*

Reserved tags
~~~~~~~~~~~~~

Users are generally free to use whatever tags that work in their context.
There are, however, certain tags that have a predefined meaning for Robot
Framework itself, and using them for other purposes can have unexpected
results. All special tags Robot Framework has and will have in the future
have a `robot-` prefix. To avoid problems, users should thus not use any
tag with a `robot-` prefix unless actually activating the special functionality.

At the time of writing, the only special tag is `robot-exit` that is
automatically added to tests when `stopping test execution gracefully`_.
More usages are likely to be added in the future, though.

.. _test setup:
.. _test teardown:
.. _Test setup and teardown:

Test setup and teardown
-----------------------

Robot Framework has similar test setup and teardown functionality as many
other test automation frameworks. In short, a test setup is something
that is executed before a test case, and a test teardown is executed
after a test case. In Robot Framework setups and teardowns are just
normal keywords with possible arguments.

Setup and teardown are always a single keyword. If they need to take care
of multiple separate tasks, it is possible to create higher-level `user
keywords`_ for that purpose. An alternative solution is executing multiple
keywords using the BuiltIn_ keyword :name:`Run Keywords`.

The test teardown is special in two ways. First of all, it is executed also
when a test case fails, so it can be used for clean-up activities that must be
done regardless of the test case status. In addition, all the keywords in the
teardown are also executed even if one of them fails. This `continue on failure`_
functionality can be used also with normal keywords, but inside teardowns it is
on by default.

The easiest way to specify a setup or a teardown for test cases in a
test case file is using the :setting:`Test Setup` and :setting:`Test
Teardown` settings in the Setting table. Individual test cases can
also have their own setup or teardown. They are defined with the
:setting:`[Setup]` or :setting:`[Teardown]` settings in the test case
table and they override possible :setting:`Test Setup` and
:setting:`Test Teardown` settings. Having no keyword after a
:setting:`[Setup]` or :setting:`[Teardown]` setting means having no
setup or teardown. It is also possible to use value `NONE` to indicate that
a test has no setup/teardown.

.. sourcecode:: robotframework

   *** Settings ***
   Test Setup       Open Application    App A
   Test Teardown    Close Application

   *** Test Cases ***
   Default values
       [Documentation]    Setup and teardown from setting table
       Do Something

   Overridden setup
       [Documentation]    Own setup, teardown from setting table
       [Setup]    Open Application    App B
       Do Something

   No teardown
       [Documentation]    Default setup, no teardown at all
       Do Something
       [Teardown]

   No teardown 2
       [Documentation]    Setup and teardown can be disabled also with special value NONE
       Do Something
       [Teardown]    NONE

   Using variables
       [Documentation]    Setup and teardown specified using variables
       [Setup]    ${SETUP}
       Do Something
       [Teardown]    ${TEARDOWN}

The name of the keyword to be executed as a setup or a teardown can be a
variable. This facilitates having different setups or teardowns in
different environments by giving the keyword name as a variable from
the command line.

.. note:: `Test suites can have a setup and teardown of their
           own`__. A suite setup is executed before any test cases or sub test
           suites in that test suite, and similarly a suite teardown is
           executed after them.

__  `Suite setup and teardown`_

.. _test temlate:
.. _template keyword:
.. _Test templates:

Test templates
--------------

Test templates convert normal `keyword-driven`_ test cases into
`data-driven`_ tests. Whereas the body of a keyword-driven test case
is constructed from keywords and their possible arguments, test cases with
template contain only the arguments for the template keyword.
Instead of repeating the same keyword multiple times per test and/or with all
tests in a file, it is possible to use it only per test or just once per file.

Template keywords can accept both normal positional and named arguments, as
well as arguments embedded to the keyword name. Unlike with other settings,
it is not possible to define a template using a variable.

Basic usage
~~~~~~~~~~~

How a keyword accepting normal positional arguments can be used as a template
is illustrated by the following example test cases. These two tests are
functionally fully identical.

.. sourcecode:: robotframework

   *** Test Cases **
   Normal test case
       Example keyword    first argument    second argument

   Templated test case
       [Template]    Example keyword
       first argument    second argument

As the example illustrates, it is possible to specify the
template for an individual test case using the :setting:`[Template]`
setting. An alternative approach is using the :setting:`Test Template`
setting in the Setting table, in which case the template is applied
for all test cases in that test case file. The :setting:`[Template]`
setting overrides the possible template set in the Setting table, and
an empty value for :setting:`[Template]` means that the test has no
template even when :setting:`Test Template` is used. It is also possible
to use value `NONE` to indicate that a test has no template.

If a templated test case has multiple data rows in its body, the template
is applied for all the rows one by one. This
means that the same keyword is executed multiple times, once with data
on each row. Templated tests are also special so that all the rounds
are executed even if one or more of them fails. It is possible to use this
kind of `continue on failure`_ mode with normal tests too, but with
the templated tests the mode is on automatically.

.. sourcecode:: robotframework

   *** Settings ***
   Test Template    Example keyword

   *** Test Cases ***
   Templated test case
       first round 1     first round 2
       second round 1    second round 2
       third round 1     third round 2

Using arguments with `default values`_ or `varargs`_, as well as using
`named arguments`_ and `free keyword arguments`_, work with templates
exactly like they work otherwise. Using variables_ in arguments is also
supported normally.

Templates with embedded arguments
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Starting from Robot Framework 2.8.2, templates support a variation of
the `embedded argument syntax`_. With templates this syntax works so
that if the template keyword has variables in its name, they are considered
placeholders for arguments and replaced with the actual arguments
used with the template. The resulting keyword is then used without positional
arguments. This is best illustrated with an example:

.. sourcecode:: robotframework

   *** Test Cases ***
   Normal test case with embedded arguments
       The result of 1 + 1 should be 2
       The result of 1 + 2 should be 3

   Template with embedded arguments
       [Template]    The result of ${calculation} should be ${expected}
       1 + 1    2
       1 + 2    3

   *** Keywords ***
   The result of ${calculation} should be ${expected}
       ${result} =    Calculate    ${calculation}
       Should Be Equal    ${result}     ${expected}

When embedded arguments are used with templates, the number of arguments in
the template keyword name must match the number of arguments it is used with.
The argument names do not need to match the arguments of the original keyword,
though, and it is also possible to use different arguments altogether:

.. sourcecode:: robotframework

   *** Test Cases ***
   Different argument names
       [Template]    The result of ${foo} should be ${bar}
       1 + 1    2
       1 + 2    3

   Only some arguments
       [Template]    The result of ${calculation} should be 3
       1 + 2
       4 - 1

   New arguments
       [Template]    The ${meaning} of ${life} should be 42
       result    21 * 2

The main benefit of using embedded arguments with templates is that
argument names are specified explicitly. When using normal arguments,
the same effect can be achieved by naming the columns that contain
arguments. This is illustrated by the `data-driven style`_ example in
the next section.

Templates with for loops
~~~~~~~~~~~~~~~~~~~~~~~~

If templates are used with `for loops`_, the template is applied for
all the steps inside the loop. The continue on failure mode is in use
also in this case, which means that all the steps are executed with
all the looped elements even if there are failures.

.. sourcecode:: robotframework

   *** Test Cases ***
   Template and for
       [Template]    Example keyword
       :FOR    ${item}    IN    @{ITEMS}
       \    ${item}    2nd arg
       :FOR    ${index}    IN RANGE    42
       \    1st arg    ${index}

Different test case styles
--------------------------

There are several different ways in which test cases may be written. Test
cases that describe some kind of *workflow* may be written either in
keyword-driven or behavior-driven style. Data-driven style can be used to test
the same workflow with varying input data.

.. _keyword-driven:
.. _Keyword-driven style:

Keyword-driven style
~~~~~~~~~~~~~~~~~~~~

Workflow tests, such as the :name:`Valid Login` test described
earlier_, are constructed from several keywords and their possible
arguments. Their normal structure is that first the system is taken
into the initial state (:name:`Open Login Page` in the :name:`Valid
Login` example), then something is done to the system (:name:`Input
Name`, :name:`Input Password`, :name:`Submit Credentials`), and
finally it is verified that the system behaved as expected
(:name:`Welcome Page Should Be Open`).

.. _earlier: example-tests_

.. _data-driven:
.. _Data-driven style:

Data-driven style
~~~~~~~~~~~~~~~~~

Another style to write test cases is the *data-driven* approach where
test cases use only one higher-level keyword, normally created as a
`user keyword`_, that hides the actual test workflow. These tests are
very useful when there is a need to test the same scenario with
different input and/or output data. It would be possible to repeat the
same keyword with every test, but the `test template`_ functionality
allows specifying the keyword to use only once.

.. sourcecode:: robotframework

   *** Settings ***
   Test Template    Login with invalid credentials should fail

   *** Test Cases ***                USERNAME         PASSWORD
   Invalid User Name                 invalid          ${VALID PASSWORD}
   Invalid Password                  ${VALID USER}    invalid
   Invalid User Name and Password    invalid          invalid
   Empty User Name                   ${EMPTY}         ${VALID PASSWORD}
   Empty Password                    ${VALID USER}    ${EMPTY}
   Empty User Name and Password      ${EMPTY}         ${EMPTY}

.. tip:: Naming columns like in the example above makes tests easier to
         understand. This is possible because on the header row other
         cells except the first one `are ignored`__.

The above example has six separate tests, one for each invalid
user/password combination, and the example below illustrates how to
have only one test with all the combinations. When using `test
templates`_, all the rounds in a test are executed even if there are
failures, so there is no real functional difference between these two
styles. In the above example separate combinations are named so it is
easier to see what they test, but having potentially large number of
these tests may mess-up statistics. Which style to use depends on the
context and personal preferences.

.. sourcecode:: robotframework

   *** Test Cases ***
   Invalid Password
       [Template]    Login with invalid credentials should fail
       invalid          ${VALID PASSWORD}
       ${VALID USER}    invalid
       invalid          whatever
       ${EMPTY}         ${VALID PASSWORD}
       ${VALID USER}    ${EMPTY}
       ${EMPTY}         ${EMPTY}

__ `Ignored data`_

Behavior-driven style
~~~~~~~~~~~~~~~~~~~~~

It is also possible to write test cases as requirements that also non-technical
project stakeholders must understand. These *executable requirements* are a
corner stone of a process commonly called `Acceptance Test Driven Development`__
(ATDD) or `Specification by Example`__.

One way to write these requirements/tests is *Given-When-Then* style
popularized by `Behavior Driven Development`__ (BDD). When writing test cases in
this style, the initial state is usually expressed with a keyword starting with
word :name:`Given`, the actions are described with keyword starting with
:name:`When` and the expectations with a keyword starting with :name:`Then`.
Keyword starting with :name:`And` or :name:`But` may be used if a step has more
than one action.

.. sourcecode:: robotframework

   *** Test Cases ***
   Valid Login
       Given login page is open
       When valid username and password are inserted
       and credentials are submitted
       Then welcome page should be open

__ http://testobsessed.com/2008/12/08/acceptance-test-driven-development-atdd-an-overview
__ http://en.wikipedia.org/wiki/Specification_by_example
__ http://en.wikipedia.org/wiki/Behavior_Driven_Development

Ignoring :name:`Given/When/Then/And/But` prefixes
'''''''''''''''''''''''''''''''''''''''''''''''''

Prefixes :name:`Given`, :name:`When`, :name:`Then`, :name:`And` and :name:`But`
are dropped when matching keywords are searched, if no match with the full name
is found. This works for both user keywords and library keywords. For example,
:name:`Given login page is open` in the above example can be implemented as
user keyword either with or without the word :name:`Given`. Ignoring prefixes
also allows using the same keyword with different prefixes. For example
:name:`Welcome page should be open` could also used as :name:`And welcome page
should be open`.

.. note:: Ignoring :name:`But` prefix is new in Robot Framework 2.8.7.

Embedding data to keywords
''''''''''''''''''''''''''

When writing concrete examples it is useful to be able pass actual data to
keyword implementations. User keywords support this by allowing `embedding
arguments into keyword name`_.
