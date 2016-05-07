.. _test suite:
.. _test suites:
.. _Creating test suites:

テストスイートの作成
======================

Robot Framework のテストケースは、テストケースファイルの中に書かれます。
複数のテストケースファイルを一つのディレクトリ中に置いて、一つの階層化されたテストスイートとして構造化できます。

.. contents::
   :depth: 2
   :local:

.. _test case file:
.. _Test case files:

テストケースファイル
------------------------

Robot Framework のテストケースは、テストケースファイルにテストケーステーブルを :ref:`定義する <Test case syntax>` ことで作成します。
個々のテストケースファイルは、中に入っているテストケースからなる一つのテストスイートを自動的に形成します。
一つのファイル中に書けるテストケースの数に制限はありませんが、 :ref:`データ駆動テスト <data-driven approach>` のように、テストケースあたり一つのキーワードを使っているのでないかぎり、一つのファイルに書くのはたかだか 10個程度のテストケースとするよう勧めます。

ファイル単位のテストスイートは、設定テーブルに以下のような設定ができます:
`Documentation`:setting:
   :ref:`テストスイートのドキュメント <test suite documentation>` の指定に使います。
`Metadata`:setting:
   :ref:`テストスイートのメタデータ <free test suite metadata>` を名前-値のペアで指定します。
`Suite Setup`:setting:, `Suite Teardown`:setting:
   :ref:`テストスイートのセットアップとティアダウン <suite setup and teardown>` を指定します。

.. note:: 設定の名前には、 :setting:`Documentation:` 末尾にオプションのコロンをつけてもかまいません。
   この書き方だと、プレーンテキスト形式でテストを書くときに、多少読みやすさが増します。

.. _test suite directory:
.. _Test suite directories:

テストスイートディレクトリ
----------------------------

テストケースファイルはディレクトリに分けて管理でき、個々のディレクトリがより高水準のテストケースを形成します。
ディレクトリでできたテストスイートそのものにはテストケースがありませんが、テストケースの入った他のテストスイートを中に格納できます。
テストスイートのディレクトリを他のディレクトリの中に入れていくことで、より高水準のテストスイートを形成できます。
テストスイートの構造には制約がないので、好きなようにテストケースを組織化して構成できます。

テストディレクトリ単位でテストを実行すると、そのディレクトリ下のファイルを、以下のような手順で階層的に実行していきます:

- ファイル名がドット (:file:`.`) やアンダースコア (:file:`_`) で始まるものは無視します。
- :file:`CVS` (大小文字は区別) という名前のディレクトリは無視します。
- テストファイルとしてサポートしている :ref:`ファイル拡張子タイプ <supported file formats>` (:file:`.html`, :file:`.xhtml`, :file:`.htm`, :file:`.tsv`, :file:`.txt`, :file:`.rst`, :file:`.rest`) 以外のファイルは無視します (拡張子は大小文字を区別しません)。
- 上記以外のファイルやディレクトリを処理対象にします。

処理対象となったファイルやディレクトリにテストケースが全く定義されていなかったとしても、単に無視して (メッセージを syslog_ に書いて) 処理を継続します。

.. _Warning on invalid files:

無効なファイルに対する警告
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

通常は、テストケースとして正しく認識できるテーブルが入っていないファイルは無視し、 syslog_ にメッセージを出力します。
コマンドラインオプション :option:`--warnonskippedfiles` を指定すると、 :ref:`テスト実行エラー <Errors and warnings during execution>` にメッセージを出力するようになります。

.. _initialization file:
.. _test suite initialization file:
.. _test suite initialization files:
.. _Initialization files:

Initialization files
~~~~~~~~~~~~~~~~~~~~

A test suite created from a directory can have similar settings as a suite
created from a test case file. Because a directory alone cannot have that
kind of information, it must be placed into a special test suite initialization
file. An initialization file name must always be of the format
:file:`__init__.ext`, where the extension must be one of the `supported
file formats`_ (for example, :file:`__init__.robot` or :file:`__init__.html`).
The name format is borrowed from Python, where files named in this manner
denote that a directory is a module.

Initialization files have the same structure and syntax as test case files,
except that they cannot have test case tables and not all settings are
supported. Variables and keywords created or imported in initialization files
*are not* available in the lower level test suites. If you need to share
variables or keywords, you can put them into `resource files`_ that can be
imported both by initialization and test case files.

The main usage for initialization files is specifying test suite related
settings similarly as in `test case files`_, but setting some `test case
related settings`__ is also possible. How to use different settings in the
initialization files is explained below.

`Documentation`:setting:, `Metadata`:setting:, `Suite Setup`:setting:, `Suite Teardown`:setting:
   These test suite specific settings work the same way as in test case files.
`Force Tags`:setting:
   Specified tags are unconditionally set to all test cases in all test case files
   this directory contains directly or recursively.
`Test Setup`:setting:, `Test Teardown`:setting:, `Test Timeout`:setting:
   Set the default value for test setup/teardown or test timeout to all test
   cases this directory contains. Can be overridden on lower level.
   Support for defining test timeout in initialization files was added in
   Robot Framework 2.7.
`Default Tags`:setting:, `Test Template`:setting:
   Not supported in initialization files.

.. sourcecode:: robotframework

   *** Settings ***
   Documentation    Example suite
   Suite Setup      Do Something    ${MESSAGE}
   Force Tags       example
   Library          SomeLibrary

   *** Variables ***
   ${MESSAGE}       Hello, world!

   *** Keywords ***
   Do Something
       [Arguments]    ${args}
       Some Keyword    ${arg}
       Another Keyword

__ `Test case related settings in the Setting table`_

.. _test suite name:
.. _test suite documentation:
.. _Test suite name and documentation:

Test suite name and documentation
---------------------------------

The test suite name is constructed from the file or directory name. The name
is created so that the extension is ignored, possible underscores are
replaced with spaces, and names fully in lower case are title cased. For
example, :file:`some_tests.html` becomes :name:`Some Tests` and
:file:`My_test_directory` becomes :name:`My test directory`.

The file or directory name can contain a prefix to control the `execution
order`_ of the suites. The prefix is separated from the base name by two
underscores and, when constructing the actual test suite name, both
the prefix and underscores are removed. For example files
:file:`01__some_tests.txt` and :file:`02__more_tests.txt` create test
suites :name:`Some Tests` and :name:`More Tests`, respectively, and
the former is executed before the latter.

The documentation for a test suite is set using the :setting:`Documentation`
setting in the Setting table. It can be used in test case files
or, with higher-level suites, in test suite initialization files. Test
suite documentation has exactly the same characteristics regarding to where
it is shown and how it can be created as `test case
documentation`_.

.. sourcecode:: robotframework

   *** Settings ***
   Documentation    An example test suite documentation with *some* _formatting_.
   ...              See test documentation for more documentation examples.

Both the name and documentation of the top-level test suite can be
overridden in test execution. This can be done with the command line
options :option:`--name` and :option:`--doc`, respectively, as
explained in section `Setting metadata`_.

Free test suite metadata
------------------------

Test suites can also have other metadata than the documentation. This metadata
is defined in the Setting table using the :setting:`Metadata` setting. Metadata
set in this manner is shown in test reports and logs.

The name and value for the metadata are located in the columns following
:setting:`Metadata`. The value is handled similarly as documentation, which means
that it can be split `into several cells`__ (joined together with spaces)
or `into several rows`__ (joined together with newlines),
simple `HTML formatting`_ works and even variables_ can be used.

__ `Dividing test data to several rows`_
__ `Newlines in test data`_

.. sourcecode:: robotframework

   *** Settings ***
   Metadata    Version        2.0
   Metadata    More Info      For more information about *Robot Framework* see http://robotframework.org
   Metadata    Executed At    ${HOST}

For top-level test suites, it is possible to set metadata also with the
:option:`--metadata` command line option. This is discussed in more
detail in section `Setting metadata`_.

.. _suite setup:
.. _suite teardown:
.. _Suite setup and teardown:

Suite setup and teardown
------------------------

Not only `test cases`__ but also test suites can have a setup and
a teardown. A suite setup is executed before running any of the suite's
test cases or child test suites, and a test teardown is executed after
them. All test suites can have a setup and a teardown; with suites created
from a directory they must be specified in a `test suite
initialization file`_.

__ `Test setup and teardown`_

Similarly as with test cases, a suite setup and teardown are keywords
that may take arguments. They are defined in the Setting table with
:setting:`Suite Setup` and :setting:`Suite Teardown` settings,
respectively. Keyword names and possible arguments are located in
the columns after the setting name.

If a suite setup fails, all test cases in it and its child test suites
are immediately assigned a fail status and they are not actually
executed. This makes suite setups ideal for checking preconditions
that must be met before running test cases is possible.

A suite teardown is normally used for cleaning up after all the test
cases have been executed. It is executed even if the setup of the same
suite fails. If the suite teardown fails, all test cases in the
suite are marked failed, regardless of their original execution status.
Note that all the keywords in suite teardowns are executed even if one
of them fails.

The name of the keyword to be executed as a setup or a teardown can be
a variable. This facilitates having different setups or teardowns
in different environments by giving the keyword name as a variable
from the command line.
