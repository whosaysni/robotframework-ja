.. _test data:
.. _general parsing rules:
.. _Test data syntax:

テストデータの書き方
======================

この節では、 Robot Framework のテストデータの書き方を大まかに解説します。
実際のテストケースやテストスイートなどの作成方法は、後の節で述べます。

.. contents::
   :depth: 2
   :local:

ファイルとディレクトリ
------------------------

テストケースを階層的にアレンジする方法は、以下の通りです:

- テストケースは :ref:`テストケースファイル <test case files>` の中に書きます。
- テストケースファイル一つが、自動的にファイル中の全てのテストケースからなる :ref:`テストスイート <test suite>` になります。
- テストケースファイルの入ったディレクトリは、より高水準のテストスイートとなります。
  この :ref:`テストスイートディレクトリ <test suite directory>` の中には、ディレクトリ内のテストファイルによるテストスイートが、サブテストスイートとして入っています
- テストスイートディレクトリの中に、別のテストスイートディレクトリを配置できます。
  その場合、階層構造は必要に応じて深くなっていきます。
- テストスイートディレクトリに、特殊な :ref:`初期化ファイル <initialization file>` を置くことがあります。

上のルールの他に、テストに関係する以下のファイルがあります:

- :ref:`ライブラリファイル <Test libraries>` には、他のテストを定義するための低水準のキーワードが入っています。
- :ref:`リソースファイル <Resource files>` には、 :ref:`変数 <variables>` と、高水準の  `ユーザ定義のキーワード <user keywords>` が入っています。
- :ref:`変数ファイル <Variable files>` は、リソースファイルよりも柔軟なやりかたで変数を生成する方法を提供します。


.. _Supported file formats:

サポートするファイル形式
--------------------------

Robot Framework のテストデータは、 HTML, タブ区切りの値(TSV)、プレーンテキスト、 reStruncturedText (reST) フォーマットのいずれかを使ったテーブル形式です。
それぞれのフォーマットの詳細と長所や短所については、以降の節で個々に説明していきます。
どのフォーマットを使うべきかは状況次第ですが、特に事情がないのなら、プレーンテキストを推奨します。

Robot Framework は、ファイルの拡張子に基づいて、テストデータのパーザを切り替えます。拡張子の大小文字は区別しません。
認識する拡張子は、 :file:`.html`, :file:`.htm`, :file:`.xhtml` が HTML,  :file:`.tsv` が TSV, :file:`.txt` と :file:`.robot` がプレーンテキスト、 :file:`.rst` と :file:`.rest` が reStructuredText です。

テストの書き方を学びやすくするため、 HTML と TSV 形式には特別なテストデータ形式があります。
.. Different `test data templates`_ are available for HTML and TSV
.. formats to make it easier to get started writing tests.

.. note:: 拡張子 :file:`.robot` のプレーンテキストファイルへの対応は Robot Framework 2.7.6 以降でサポートしています。


.. _HTML format:

HTML 形式
~~~~~~~~~~~

HTML ファイルを使うと、テーブルのフォーマットができ、その前後に自由にテキストを書けます。
テストケースファイルに追加の情報を記載できるので、様式に沿ったテスト仕様書にできます。
HTML フォーマットの大きな問題は、普通のテキストエディタで編集するのが楽ではないことです。
もう一つの問題は、 HTML にすると、差分の中にテストデータに加えて HTML の構文が交じるので、バージョン管理システムでの管理がしづらいことです。

HTML ファイルでは、テストデータは個別のテーブルで定義します (下の例を参照)。
Robot Framework は :ref:`テストデータテーブル <test data tables>` を、テーブルの最初のセルのテキストで判別します。
テーブルの外にある情報は、全て無視されます。

.. table:: HTML 形式の書き方
   :class: example

   ============  ================  =======  =======
      Setting          Value        Value    Value
   ============  ================  =======  =======
   Library       OperatingSystem
   \
   ============  ================  =======  =======

.. table::
   :class: example

   ============  ================  =======  =======
     Variable        Value          Value    Value
   ============  ================  =======  =======
   ${MESSAGE}    Hello, world!
   \
   ============  ================  =======  =======

.. table::
   :class: example

   ============  ===================  ============  =============
    Test Case           Action          Argument      Argument
   ============  ===================  ============  =============
   My Test       [Documentation]      Example test
   \             Log                  ${MESSAGE}
   \             My Keyword           /tmp
   \
   Another Test  Should Be Equal      ${MESSAGE}    Hello, world!
   ============  ===================  ============  =============

.. table::
   :class: example

   ============  ======================  ============  ==========
     Keyword            Action             Argument     Argument
   ============  ======================  ============  ==========
   My Keyword    [Arguments]             ${path}
   \             Directory Should Exist  ${path}
   ============  ======================  ============  ==========


テストデータの編集
'''''''''''''''''''''

HTML ファイルのテストデータはどんなエディタでも編集できますが、テーブルを表の形で見られるグラフィカルなエディタがお勧めです。
RIDE_ は HTML を読み書きできますが、残念ながら、 HTML によるフォーマットが失われ、テストケーステーブルの外にある情報が欠落することがあります。

.. _Encoding and entity references:

エンコーディングとエンティティ参照
''''''''''''''''''''''''''''''''''''

Robot Framework は HTML エンティティ参照 (`&auml;` など) をサポートしています。
さらに、どんなエンコーディングも、データファイル中で指定している限り使えます。
通常の HTML ファイルには、以下のような META エレメントが必要です::

  <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">

XHTML ファイルの場合は、以下のように XML のプリアンブルが必要です::

  <?xml version="1.0" encoding="Big5"?>

エンコーディングを指定しない場合、 Robot Framework はデフォルト値として ISO-8859-1 (latin-1) を使います。 


.. _TSV format:

TSV 形式
~~~~~~~~~~

TSV ファイルは表計算プログラムで編集でき、構文が簡単なためプログラムで簡単に生成できます。
普通のテキストエディタでも編集しやすく、バージョン管理システムでの管理も楽です。
とはいえ、同じ理由で選ぶのであれば、 :ref:`プレーンテキスト形式 <plain text format>` の方がもっと向いています。

TSV 形式は、ほぼ HTML と同じ用途のテストデータに使えます。
TSV ファイルの中では、全テストデータが一つの大きなテーブルの中に入っています。
各々の  :ref:`テストデータテーブル <test data tables>`  は、「一つ以上のアスタリスク (`*`)、テーブル名、アスタリスク」が書かれている場所から始まります。ただし、テーブル名の後のアスタリスクは省略できます。
最初に認識されたテーブルよりも前にかかれている内容は、 HTML データのテーブルの外のデータと同様、無視されます。

.. table:: TSV 形式の書き方
   :class: tsv-example

   ============  =======================  =============  =============
   \*Setting*    \*Value*                 \*Value*       \*Value*
   Library       OperatingSystem
   \
   \
   \*Variable*   \*Value*                 \*Value*       \*Value*
   ${MESSAGE}    Hello, world!
   \
   \
   \*Test Case*  \*Action*                \*Argument*    \*Argument*
   My Test       [Documentation]          Example test
   \             Log                      ${MESSAGE}
   \             My Keyword               /tmp
   \
   Another Test  Should Be Equal          ${MESSAGE}     Hello, world!
   \
   \
   \*Keyword*    \*Action*                \*Argument*    \*Argument*
   My Keyword    [Arguments]              ${path}
   \             Directory Should Exist   ${path}
   ============  =======================  =============  =============

テストデータの編集
'''''''''''''''''''''

TSV ファイルの作成や編集は、Microsoft Excel をはじめほとんどの表計算ソフトでできます。
ファイルを保存するときに、タブ区切り形式のフォーマットにして、ファイルの拡張子を :file:`.tsv` にセットしてください。
編集するときは、オートコレクトをオフにして、ファイル中の全ての値をプレーンテキストで保存する設定にしてください。

TSV ファイルは、テキストエディタでも比較的容易に編集できます。
特に、エディタがタブとスペースを視覚的に区別できると便利です。
RIDE_ は TSV 形式をサポートしています。

Robot Framework は、 TSV データを解析するときに、全ファイルコンテンツを行に分割して、さらに各行をタブ文字で分割します。
表計算ソフトによっては、(`"my value"` のように) セルの値をクオートで囲うことがあり、 Robot Framework はクオートを除去します。
データ中のクオートが2重でエスケープされている場合 (例: `"my ""quoted"" value"`) もありますが、これも正しく扱います。
表計算ソフトで TSV データを作成する場合はこうした挙動を気にする必要はありませんが、プログラムでデータを生成するときには、表計算と同じクオートの取扱いが必要なので注意してください。

エンコーディング
'''''''''''''''''''

TSV ファイルは、常に UTF-8 エンコーディングとみなします。
ASCII は UTF-8 のサブセットなので、 ASCII エンコーディングもサポートしています。

.. _Plain text format:

プレーンテキスト形式
~~~~~~~~~~~~~~~~~~~~~

プレーンテキスト形式は、編集がとても簡単で、どんなテキストエディタでも編集でき、バージョン管理システムでも容易に扱えます。
こうした諸々の長所から、 Robot Framework で最もよく使われているデータ形式です。

プレーンテキスト形式は、技術的にはどちらかといえば :ref:`TSV形式 <tsv format>` に近いですが、セルの区切り方が違います。
TSV 形式がタブを使うのに対して、プレーンテキスト形式は 2 個以上のスペースか、パイプ文字の両側にスペースを入れたもの ( :codesc:`\ |\ ` ) で区切ります。

:ref:`テストデータテーブル <test data tables>` は、TSVと同様、「一つ以上のアスタリスク (`*`)、テーブル名、アスタリスク」が書かれている場所から始まります。余分なアスタリスクとスペースがヘッダにあっても無視されるので、 `*** Settings ***` と `*Settings` は同じです。
また、 TSV と同様、最初に認識したテーブルよりも前の内容は無視されます。

プレーンテキスト形式では、タブは自動的に 2 スペースに変換されます。そのため、 TSV と同様、タブを区切り文字として使えます。
ただし、TSV 形式ではタブは常に区切り文字ですが、プレーンテキスト形式では、複数のタブ文字が連続すると合わせて一つの区切りとみなします。

.. _Space separated format:

スペース区切り方式
''''''''''''''''''''''

スペース区切り方式では、区切りに使うスペースの数は 2文字以上なら何個つづけてもかまいません。
そのため、データを見栄え良く並べられます。
これはテキストエディタで TSV 形式を編集するより好都合です。
というのも、TSV は列の並びを完全にはコントロールできないからです。

.. sourcecode:: robotframework

   *** Settings ***
   Library       OperatingSystem

   *** Variables ***
   ${MESSAGE}    Hello, world!

   *** Test Cases ***
   My Test
       [Documentation]    Example test
       Log    ${MESSAGE}
       My Keyword    /tmp

   Another Test
       Should Be Equal    ${MESSAGE}    Hello, world!

   *** Keywords ***
   My Keyword
       [Arguments]    ${path}
       Directory Should Exist    ${path}

スペースを区切り文字として使っているので、空のセルは `${EMPTY}` という特殊な変数か、バックスラッシュ一文字で :ref:`エスケープ <Escaping>` せねばなりません。
また、 :ref:`空白文字の扱い <handling whitespace>` が他のテストデータと違っていて、テストデータの前後にスペースがある場合や、データの中に2つ以上続くスペースがある場合は常にエスケープせねばなりません。

.. tip:: キーワードと引数の間は、4文字以上スペースを入れるよう勧めます。

.. _pipe separated format:

スペース・パイプ区切り方式
'''''''''''''''''''''''''''''''

スペース区切り方式の最大の問題は、キーワードと引数の区切りが見づらいことです。
特に、引数がたくさんあるキーワードや、引数にスペースが入る場合には厄介です。
そんな時は、パイプとスペースを使った区切りの方が、セルの境界がはっきり判ります。

.. sourcecode:: robotframework

   | *Setting*  |     *Value*     |
   | Library    | OperatingSystem |

   | *Variable* |     *Value*     |
   | ${MESSAGE} | Hello, world!   |

   | *Test Case*  | *Action*        | *Argument*   |
   | My Test      | [Documentation] | Example test |
   |              | Log             | ${MESSAGE}   |
   |              | My Keyword      | /tmp         |
   | Another Test | Should Be Equal | ${MESSAGE}   | Hello, world!

   | *Keyword*  |
   | My Keyword | [Arguments] | ${path}
   |            | Directory Should Exist | ${path}

プレーンテキスト形式のテストデータには、スペース区切り方式とスペース・パイプ区切り方式を混在させられます。
ただし、一つの行の中ではどちらかに揃えねばなりません。
パイプ・スペース方式の行はパイプで開始せねばなりませんが、行末のパイプは省略可能です。
行の先頭を除き、パイプ文字の両側には必ず一つ以上スペースがなければなりません。
ただし、データの並びをはっきりさせるために、パイプの位置を他の行と揃える必要はありません。

パイプ・スペース方式では、(:ref:`末尾の空白セル <trailing empty cells>` を除き、) 空のセルをエスケープする必要はありません。
唯一、エスケープを考慮しなければならないのは、パイプの両側にスペースがあるような文字列を書きたい時で、その場合はバックスラッシュでエスケープしてください:

.. sourcecode:: robotframework

   | *** Test Cases *** |                 |                 |                      |
   | Escaping Pipe      | ${file count} = | Execute Command | ls -1 *.txt \| wc -l |
   |                    | Should Be Equal | ${file count}   | 42                   |


.. Editing and encoding:

編集とエンコーディング
''''''''''''''''''''''''

プレーンテキスト形式が HTML や TSV に対して最も優れているのは、普通のテキストエディタでの編集がとても簡単なことです。
ほとんどのエディタや IDE (Eclipse, Emacs, Vim, TextMate など) には、 Robot Framework のテストデータを編集するための構文ハイライト用プラグインがあり、キーワード保管などの機能も備えています。
RIDE_ もプレーンテキスト形式をサポートしています。

TSV 形式のテストデータと同様、プレーンテキスト形式のファイルも UTF-8 エンコーディング想定です。
従って、 ASCII エンコーディングのファイルもサポートしています。

Recognized extensions
'''''''''''''''''''''

Robot Framework 2.7.6 から、プレーンテキスト形式のテストデータファイルの拡張子として、従来の :file:`.txt` に加えて :file:`.robot` のサポートを追加しました。
新しい拡張子を使えば、他のプレーンテキストファイルとテストデータを区別しやすくなります。

reStructuredText format
~~~~~~~~~~~~~~~~~~~~~~~

reStructuredText_ (reST) is an easy-to-read plain text markup syntax that
is commonly used for documentation of Python projects (including
Python itself, as well as this User Guide). reST documents are most
often compiled to HTML, but also other output formats are supported.

Using reST with Robot Framework allows you to mix richly formatted documents
and test data in a concise text format that is easy to work with
using simple text editors, diff tools, and source control systems.
In practice it combines many of the benefits of plain text and HTML formats.

When using reST files with Robot Framework, there are two ways to define the
test data. Either you can use `code blocks`__ and define test cases in them
using the `plain text format`_ or alternatively you can use tables__ exactly
like you would with the `HTML format`_.

.. note:: Using reST files with Robot Framework requires the Python docutils_
          module to be installed.

__ `Using code blocks`_
__ `Using tables`_

Using code blocks
'''''''''''''''''

reStructuredText documents can contain code examples in so called code blocks.
When these documents are compiled into HTML or other formats, the code blocks
are syntax highlighted using Pygments_. In standard reST code blocks are
started using the `code` directive, but Sphinx_ uses `code-block`
or `sourcecode` instead. The name of the programming language in
the code block is given as an argument to the directive. For example, following
code blocks contain Python and Robot Framework examples, respectively:

.. sourcecode:: rest

    .. code:: python

       def example_keyword():
           print 'Hello, world!'

    .. code:: robotframework

       *** Test Cases ***
       Example Test
           Example Keyword

When Robot Framework parses reStructuredText files, it first searches for
possible `code`, `code-block` or `sourcecode` blocks
containing Robot Framework test data. If such code blocks are found, data
they contain is written into an in-memory file and executed. All data outside
the code blocks is ignored.

The test data in the code blocks must be defined using the `plain text format`_.
As the example below illustrates, both space and pipe separated variants are
supported:

.. sourcecode:: rest

    Example
    -------

    This text is outside code blocks and thus ignored.

    .. code:: robotframework

       *** Settings ***
       Library       OperatingSystem

       *** Variables ***
       ${MESSAGE}    Hello, world!

       *** Test Cases ***
       My Test
           [Documentation]    Example test
           Log    ${MESSAGE}
           My Keyword    /tmp

       Another Test
           Should Be Equal    ${MESSAGE}    Hello, world!

    Also this text is outside code blocks and ignored. Above block used
    the space separated plain text format and the block below uses the pipe
    separated variant.

    .. code:: robotframework

       | *** Keyword ***  |                        |         |
       | My Keyword       | [Arguments]            | ${path} |
       |                  | Directory Should Exist | ${path} |

.. note:: Escaping_ using the backslash character works normally in this format.
          No double escaping is needed like when using reST tables.

.. note:: Support for test data in code blocks is a new feature in
          Robot Framework 2.8.2.

Using tables
''''''''''''

If a reStructuredText document contains no code blocks with Robot Framework
data, it is expected to contain the data in tables similarly as in
the `HTML format`_. In this case Robot Framework compiles the document to
HTML in memory and parses it exactly like it would parse a normal HTML file.

Robot Framework identifies `test data tables`_ based on the text in the first
cell and all content outside of the recognized table types is ignored.
An example of each of the four test data tables is shown below
using both simple table and grid table syntax:

.. sourcecode:: rest

    Example
    -------

    This text is outside tables and thus ignored.

    ============  ================  =======  =======
      Setting          Value         Value    Value
    ============  ================  =======  =======
    Library       OperatingSystem
    ============  ================  =======  =======


    ============  ================  =======  =======
      Variable         Value         Value    Value
    ============  ================  =======  =======
    ${MESSAGE}    Hello, world!
    ============  ================  =======  =======


    =============  ==================  ============  =============
      Test Case          Action          Argument      Argument
    =============  ==================  ============  =============
    My Test        [Documentation]     Example test
    \              Log                 ${MESSAGE}
    \              My Keyword          /tmp
    \
    Another Test   Should Be Equal     ${MESSAGE}    Hello, world!
    =============  ==================  ============  =============

    Also this text is outside tables and ignored. Above tables are created
    using the simple table syntax and the table below uses the grid table
    approach.

    +-------------+------------------------+------------+------------+
    |   Keyword   |         Action         |  Argument  |  Argument  |
    +-------------+------------------------+------------+------------+
    | My Keyword  | [Arguments]            | ${path}    |            |
    +-------------+------------------------+------------+------------+
    |             | Directory Should Exist | ${path}    |            |
    +-------------+------------------------+------------+------------+

.. note:: Empty cells in the first column of simple tables need to be escaped.
          The above example uses :codesc:`\\` but `..` could also be used.

.. note:: Because the backslash character is an escape character in reST,
          specifying a backslash so that Robot Framework will see it requires
          escaping it with an other backslash like `\\`. For example,
          a new line character must be written like `\\n`. Because
          the backslash is used for escaping_ also in Robot Framework data,
          specifying a literal backslash when using reST tables requires double
          escaping like `c:\\\\temp`.

Generating HTML files based on reST files every time tests are run obviously
adds some overhead. If this is a problem, it can be a good idea to convert
reST files to HTML using external tools separately, and let Robot Framework
use the generated files only.

Editing and encoding
''''''''''''''''''''

Test data in reStructuredText files can be edited with any text editor, and
many editors also provide automatic syntax highlighting for it. reST format
is not supported by RIDE_, though.

Robot Framework requires reST files containing non-ASCII characters to be
saved using UTF-8 encoding.

Syntax errors in reST source files
''''''''''''''''''''''''''''''''''

If a reStructuredText document is not syntactically correct (a malformed table
for example), parsing it will fail and no test cases can be found from that
file. When executing a single reST file, Robot Framework will show the error
on the console. When executing a directory, such parsing errors will
generally be ignored.

Starting from Robot Framework 2.9.2, errors below level `SEVERE` are ignored
when running tests to avoid noise about non-standard directives and other such
markup. This may hide also real errors, but they can be seen when processing
files normally.

Test data tables
----------------

Test data is structured in four types of tables listed below. These
test data tables are identified by the first cell of the table. Recognized
table names are `Settings`, `Variables`, `Test Cases`, and `Keywords`. Matching
is case-insensitive and also singular variants like `Setting` and `Test Case`
are accepted.

.. table:: Different test data tables
   :class: tabular

   +--------------+--------------------------------------------+
   |    Table     |                 Used for                   |
   +==============+============================================+
   | Settings     | | 1) Importing `test libraries`_,          |
   |              |   `resource files`_ and `variable files`_. |
   |              | | 2) Defining metadata for `test suites`_  |
   |              |   and `test cases`_.                       |
   +--------------+--------------------------------------------+
   | Variables    | Defining variables_ that can be used       |
   |              | elsewhere in the test data.                |
   +--------------+--------------------------------------------+
   | Test Cases   | `Creating test cases`_ from available      |
   |              | keywords.                                  |
   +--------------+--------------------------------------------+
   | Keywords     | `Creating user keywords`_ from existing    |
   |              | lower-level keywords                       |
   +--------------+--------------------------------------------+

Rules for parsing the data
--------------------------

.. _comment:

Ignored data
~~~~~~~~~~~~

When Robot Framework parses the test data, it ignores:

- All tables that do not start with a `recognized table name`__ in the first cell.
- Everything else on the first row of a table apart from the first cell.
- All data before the first table. If the data format allows data between
  tables, also that is ignored.
- All empty rows, which means these kinds of rows can be used to make
  the tables more readable.
- All empty cells at the end of rows, unless they are escaped__.
- All single backslashes (:codesc:`\\`) when not used for escaping_.
- All characters following the hash character (`#`), when it is the first
  character of a cell. This means that hash marks can be used to enter
  comments in the test data.
- All formatting in the HTML/reST test data.

When Robot Framework ignores some data, this data is not available in
any resulting reports and, additionally, most tools used with Robot
Framework also ignore them. To add information that is visible in
Robot Framework outputs, place it to the documentation or other metadata of
test cases or suites, or log it with the BuiltIn_ keywords :name:`Log` or
:name:`Comment`.

__ `Test data tables`_
__ `Prevent ignoring empty cells`_

Handling whitespace
~~~~~~~~~~~~~~~~~~~

Robot Framework handles whitespace the same way as they are handled in HTML
source code:

- Newlines, carriage returns, and tabs are converted to spaces.
- Leading and trailing whitespace in all cells is ignored.
- Multiple consecutive spaces are collapsed into a single space.

In addition to that, non-breaking spaces are replaced with normal spaces.
This is done to avoid hard-to-debug errors
when a non-breaking space is accidentally used instead of a normal space.

If leading, trailing, or consecutive spaces are needed, they `must be
escaped`__. Newlines, carriage returns, tabs, and non-breaking spaces can be
created using `escape sequences`_ `\n`, `\r`, `\t`, and `\xA0` respectively.

__ `Prevent ignoring spaces`_

Escaping
~~~~~~~~

The escape character in Robot Framework test data is the backslash
(:codesc:`\\`) and additionally `built-in variables`_ `${EMPTY}` and `${SPACE}`
can often be used for escaping. Different escaping mechanisms are
discussed in the sections below.

Escaping special characters
'''''''''''''''''''''''''''

The backslash character can be used to escape special characters
so that their literal values are used.

.. table:: Escaping special characters
   :class: tabular

   ===========  ================================================================  ==============================
    Character                              Meaning                                           Examples
   ===========  ================================================================  ==============================
   `\$`         Dollar sign, never starts a `scalar variable`_.                   `\${notvar}`
   `\@`         At sign, never starts a `list variable`_.                         `\@{notvar}`
   `\%`         Percent sign, never starts an `environment variable`_.            `\%{notvar}`
   `\#`         Hash sign, never starts a comment_.                               `\# not comment`
   `\=`         Equal sign, never part of `named argument syntax`_.               `not\=named`
   `\|`         Pipe character, not a separator in the `pipe separated format`_.  `| Run | ps \| grep xxx |`
   `\\`         Backslash character, never escapes anything.                      `c:\\temp, \\${var}`
   ===========  ================================================================  ==============================

.. _escape sequence:
.. _escape sequences:

Forming escape sequences
''''''''''''''''''''''''

The backslash character also allows creating special escape sequences that are
recognized as characters that would otherwise be hard or impossible to create
in the test data.

.. table:: Escape sequences
   :class: tabular

   =============  ====================================  ============================
      Sequence                  Meaning                           Examples
   =============  ====================================  ============================
   `\n`           Newline character.                    `first line\n2nd line`
   `\r`           Carriage return character             `text\rmore text`
   `\t`           Tab character.                        `text\tmore text`
   `\xhh`         Character with hex value `hh`.        `null byte: \x00, ä: \xE4`
   `\uhhhh`       Character with hex value `hhhh`.      `snowman: \u2603`
   `\Uhhhhhhhh`   Character with hex value `hhhhhhhh`.  `love hotel: \U0001f3e9`
   =============  ====================================  ============================

.. note:: All strings created in the test data, including characters like
          `\x02`, are Unicode and must be explicitly converted to
          byte strings if needed. This can be done, for example, using
          :name:`Convert To Bytes` or :name:`Encode String To Bytes` keywords
          in BuiltIn_ and String_ libraries, respectively, or with
          something like `str(value)` or `value.encode('UTF-8')`
          in Python code.

.. note:: If invalid hexadecimal values are used with `\x`, `\u`
          or `\U` escapes, the end result is the original value without
          the backslash character. For example, `\xAX` (not hex) and
          `\U00110000` (too large value) result with `xAX`
          and `U00110000`, respectively. This behavior may change in
          the future, though.

.. note:: `Built-in variable`_ `${\n}` can be used if operating system
          dependent line terminator is needed (`\r\n` on Windows and
          `\n` elsewhere).

.. note:: Possible un-escaped whitespace character after the `\n` is
          ignored. This means that `two lines\nhere` and
          `two lines\n here` are equivalent. The motivation for this
          is to allow wrapping long lines containing newlines when using
          the HTML format, but the same logic is used also with other formats.
          An exception to this rule is that the whitespace character is not
          ignored inside the `extended variable syntax`_.

.. note:: `\x`, `\u` and `\U` escape sequences are new in Robot Framework 2.8.2.

Prevent ignoring empty cells
''''''''''''''''''''''''''''

If empty values are needed as arguments for keywords or otherwise, they often
need to be escaped to prevent them from being ignored__. Empty trailing cells
must be escaped regardless of the test data format, and when using the
`space separated format`_ all empty values must be escaped.

Empty cells can be escaped either with the backslash character or with
`built-in variable`_ `${EMPTY}`. The latter is typically recommended
as it is easier to understand. An exception to this recommendation is escaping
the indented cells in `for loops`_ with a backslash when using the
`space separated format`_. All these cases are illustrated in the following
examples first in HTML and then in the space separated plain text format:

.. table::
   :class: example

   ==================  ============  ==========  ==========  ================================
        Test Case         Action      Argument    Argument                Argument
   ==================  ============  ==========  ==========  ================================
   Using backslash     Do Something  first arg   \\
   Using ${EMPTY}      Do Something  first arg   ${EMPTY}
   Non-trailing empty  Do Something              second arg  # No escaping needed in HTML
   For loop            :FOR          ${var}      IN          @{VALUES}
   \                                 Log         ${var}      # No escaping needed here either
   ==================  ============  ==========  ==========  ================================

.. sourcecode:: robotframework

   *** Test Cases ***
   Using backslash
       Do Something    first arg    \
   Using ${EMPTY}
       Do Something    first arg    ${EMPTY}
   Non-trailing empty
       Do Something    ${EMPTY}     second arg    # Escaping needed in space separated format
   For loop
       :FOR    ${var}    IN    @{VALUES}
       \    Log    ${var}                         # Escaping needed here too

__ `Ignored data`_

Prevent ignoring spaces
'''''''''''''''''''''''

Because leading, trailing, and consecutive spaces in cells are ignored__, they
need to be escaped if they are needed as arguments to keywords or otherwise.
Similarly as when preventing ignoring empty cells, it is possible to do that
either using the backslash character or using `built-in variable`_
`${SPACE}`.

.. table:: Escaping spaces examples
   :class: tabular

   ==================================  ==================================  ==================================
        Escaping with backslash             Escaping with `${SPACE}`                      Notes
   ==================================  ==================================  ==================================
   :codesc:`\\ leading space`          `${SPACE}leading space`
   :codesc:`trailing space \\`         `trailing space${SPACE}`            Backslash must be after the space.
   :codesc:`\\ \\`                     `${SPACE}`                          Backslash needed on both sides.
   :codesc:`consecutive \\ \\ spaces`  `consecutive${SPACE * 3}spaces`     Using `extended variable syntax`_.
   ==================================  ==================================  ==================================

As the above examples show, using the `${SPACE}` variable often makes the
test data easier to understand. It is especially handy in combination with
the `extended variable syntax`_ when more than one space is needed.

__ `Handling whitespace`_

.. _split into several rows:
.. _Dividing test data to several rows:

Dividing test data to several rows
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

If there is more data than readily fits a row, it possible to use ellipsis
(`...`) to continue the previous line. In test case and keyword tables,
the ellipsis must be preceded by at least one empty cell.  In settings and
variable tables, it can be placed directly under the setting or variable name.
In all tables, all empty cells before the ellipsis are ignored.

Additionally, values of settings that take only one value (mainly
documentations) can be split to several columns. These values will be
then catenated together with spaces when the test data is
parsed. Starting from Robot Framework 2.7, documentation and test
suite metadata split into multiple rows will be `catenated together
with newlines`__.

All the syntax discussed above is illustrated in the following examples.
In the first three tables test data has not been split, and
the following three illustrate how fewer columns are needed after
splitting the data to several rows.

__ `Newlines in test data`_

.. table:: Test data that has not been split
   :class: example

   ============  =======  =======  =======  =======  =======  =======
     Setting      Value    Value    Value    Value    Value    Value
   ============  =======  =======  =======  =======  =======  =======
   Default Tags  tag-1    tag-2    tag-3    tag-4    tag-5    tag-6
   ============  =======  =======  =======  =======  =======  =======

.. table::
   :class: example

   ==========  =======  =======  =======  =======  =======  =======
    Variable    Value    Value    Value    Value    Value    Value
   ==========  =======  =======  =======  =======  =======  =======
   @{LIST}     this     list     has      quite    many     items
   ==========  =======  =======  =======  =======  =======  =======

.. table::
   :class: example

   +-----------+-----------------+---------------+------+-------+------+------+-----+-----+
   | Test Case |     Action      |   Argument    | Arg  |  Arg  | Arg  | Arg  | Arg | Arg |
   +===========+=================+===============+======+=======+======+======+=====+=====+
   | Example   | [Documentation] | Documentation |      |       |      |      |     |     |
   |           |                 | for this test |      |       |      |      |     |     |
   |           |                 | case.\\n This |      |       |      |      |     |     |
   |           |                 | can get quite |      |       |      |      |     |     |
   |           |                 | long...       |      |       |      |      |     |     |
   +-----------+-----------------+---------------+------+-------+------+------+-----+-----+
   |           | [Tags]          | t-1           | t-2  | t-3   | t-4  | t-5  |     |     |
   +-----------+-----------------+---------------+------+-------+------+------+-----+-----+
   |           | Do X            | one           | two  | three | four | five | six |     |
   +-----------+-----------------+---------------+------+-------+------+------+-----+-----+
   |           | ${var} =        | Get X         | 1    | 2     | 3    | 4    | 5   | 6   |
   +-----------+-----------------+---------------+------+-------+------+------+-----+-----+

.. table:: Test data split to several rows
   :class: example

   ============  =======  =======  =======
     Setting      Value    Value    Value
   ============  =======  =======  =======
   Default Tags  tag-1    tag-2    tag-3
   ...           tag-4    tag-5    tag-6
   ============  =======  =======  =======

.. table::
   :class: example

   ==========  =======  =======  =======
    Variable    Value    Value    Value
   ==========  =======  =======  =======
   @{LIST}     this     list     has
   ...         quite    many     items
   ==========  =======  =======  =======

.. table::
   :class: example

   ===========  ================  ==============  ==========  ==========
    Test Case       Action           Argument      Argument    Argument
   ===========  ================  ==============  ==========  ==========
   Example      [Documentation]   Documentation   for this    test case.
   \            ...               This can get    quite       long...
   \            [Tags]            t-1             t-2         t-3
   \            ...               t-4             t-5
   \            Do X              one             two         three
   \            ...               four            five        six
   \            ${var} =          Get X           1           2
   \                              ...             3           4
   \                              ...             5           6
   ===========  ================  ==============  ==========  ==========
