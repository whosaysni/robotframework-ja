.. _Variables:

変数
=========

.. contents::
   :depth: 2
   :local:

.. Introduction

はじめに
------------

変数は Robot Framework の重要な機能の一つで、多くの場所で使われています。
最もよく見かけるのは、テストケースやキーワードテーブル中のキーワードの引数でしょう。
その他には、設定テーブルで変数が使えます。
通常、キーワード自体は変数として指定 *できません* が、 BuiltIn ライブラリのキーワード、 :name:`Run Keyword` を使えば、同じような効果が得られます。

Robot Framework has its own variables that can be used as scalars__, lists__
or `dictionaries`__ using syntax `${SCALAR}`, `@{LIST}` and `&{DICT}`,
respectively. In addition to this, `environment variables`_ can be used
directly with syntax `%{ENV_VAR}`.

Robot Framework は独自の変数の仕組みを備えていて、 :ref:`スカラ型変数 <scalar variables>`, :ref:`リスト型変数 <list variables>`, :ref:`辞書型変数 <Dictionary variables>` といった変数を、それぞれ `${SCALAR}`, `@{LIST}`, `&{DICT}` といった記法で扱えます。
そのほか、:ref:`環境変数 <environment variable>` を `%{ENV_VAR}` で表すこともできます。

変数は、例えば以下のようなケースで有用です:

- テストデータ中でよく変わる文字列を扱うとき。変数を使えば、一箇所で変更を行なうだけで済みます。

- システムや OS に依存しないテストデータを作成したいとき。
  ハードコードする代わりに変数を使います (例えば、 `${RESOURCES}` を `c:\resources` の代わりに、 `${HOST}` を `10.0.0.1:8080` の代わりに)。
  変数は、テストを開始するときに :ref:`コマンドラインでセット <setting variables in command line>` できるので、システム固有の変数を簡単に変更できます (`--variable HOST:10.0.0.2:1234 --variable RESOURCES:/opt/resources` といったように)。
  変数を使えば、テストの同じテストを様々な文字列でテストできるので、ローカライズのテストを楽にします。

- 文字列以外のオブジェクトを引数に渡す必要がある場合は、変数以外の手段がありません。

- 変数を使えば、たとえ別々のライブラリ上のキーワードであっても、キーワード間で情報を受け渡しできます。あるキーワードからの戻り値を変数に入れ、別のキーワードの引数にすればよいのです。

- テストデータ中の値が長大だったり、複雑すぎるとき。
  例えば、 `http://long.domain.name:8080/path/to/service?foo=1&bar=2&zap=42` よりも `${URL}` の方が短く書けます。

テストデータ中で、存在しない変数を使おうとすると、その変数を参照したキーワードは失敗します。
変数を使える場所で、変数のような書き方をした文字列をリテラルとして扱いたければ、 `\${NAME}` のように :ref:`バックスラッシュでエスケープ <escaping>` する必要があります。


.. Variable types

変数タイプ
-----------

この節では、様々なタイプの変数について説明します。
変数の作り方は、その後の節で解説します。

Robot Framework の変数は、キーワードと同じように、大小文字を区別せず、スペースやアンダースコアが入っていても無視します。
ただし、グローバルな変数を定義するときは大文字 (`${PATH}` や `${TWO WORDS}`) を、特定のテストケースやユーザキーワードの中でのみ使う変数は小文字 (`${my var}` や
`${myVar}`) を使うよう勧めます。
加えるならば、もっと重要なのは、大小文字の使い分けには一貫性をもたせることです。

変数名は、変数の型識別文字 (`$`, `@`, `&`, `%`)、波括弧 (`{`, `}`) 、そして、波括弧中に書いた変数名からなります。
似たような変数の記法を持つ言語は他にもありますが、それらとは違い、波括弧は常に必須です。
変数名は、波括弧の間に書きさえすれば、基本的に何にでもできます。ただし、aからzまでのアルファベット、数字、アンダースコアと数字だけにするよう勧めます。
このルールは :ref:`拡張変数記法 <extended variable syntax>` で変数を使うときの変数名の必須のルールでもあります。

.. _scalar variable:

スカラ変数
~~~~~~~~~~~~

テストデータ中でスカラ変数を使うと、変数は、その変数に結びついた値に置き換えられます。
スカラ変数は、単純な文字列を扱うときによく使われますが、実際にはリストをはじめ任意のオブジェクトを入れておけます。
スカラ変数の記法、 `${NAME}` は、シェルスクリプトや Perl などでも使われていて、大抵のユーザに馴染みのある形式でしょう。

以下の例では、スカラ変数の使い方を示しています。
変数 `${GREET}` と `${NAME}` が定義済みで、それぞれの値が `Hello` と `world` だとしましょう。
以下の二つのテストケースは同じ結果になります。

.. sourcecode:: robotframework

   *** Test Cases ***
   Constants
       Log    Hello
       Log    Hello, world!!

   Variables
       Log    ${GREET}
       Log    ${GREET}, ${NAME}!!


テストデータのあるセルにスカラ変数だけが入っていると、スカラ変数は、変数ｎ値そのものに置き換わります。その場合、値は任意のオブジェクトです。
一方、あるセルに、スカラ変数以外に何か (文字列の定数や他の変数) が入っていると、その値は、まず Unicode 文字列に変換され、セルの他の要素と結合されます。
オブジェクトから Unicode 文字列への変換は、 `__uinicode__` メソッド (Python の場合。 `__unicode__` がなければ `__str__` にフォールバックする) か、 `toString` (Javaの場合) を呼び出して行います。

.. note:: キーワードに引数を渡す際、 `argname=${var}` のような :ref:`名前付き引数<named arguments>` にした場合も、変数の値は Unicode 文字列に変換されず、そのまま渡されます。

以下の例は、セルに変数だけを入れた場合と、それ以外のコンテンツも入っている場合の違いを示しています。
まず、変数 `${STR}` は `Hello, world!` にセットされていて、 `${OBJ}` は以下のような Java オブジェクトだとしましょう:

.. sourcecode:: java

 public class MyObj {

     public String toString() {
         return "Hi, tellus!";
     }
 }

それぞれの変数がセットされている状態で、以下のテストデータがあるとします:

.. sourcecode:: robotframework

   *** Test Cases ***
   Objects
       KW 1    ${STR}
       KW 2    ${OBJ}
       KW 3    I said "${STR}"
       KW 4    You said "${OBJ}"

このテストデータを実行すると、各キーワードは、それぞれ以下のように引数を受け取ります:

- :name:`KW 1` 文字列 `Hello, world!` 
- :name:`KW 2`  `${OBJ}` に設定したオブジェクト
- :name:`KW 3` 文字列 `I said "Hello, world!"`
- :name:`KW 4` 文字列 `You said "Hi, tellus!"`

.. Note:: 言うまでもなく、Unicode に変換できない変数を Unicode に変換しようとすると失敗します。
          例えば、バイト列をキーワードの引数として渡したいときに、 `${byte1}${byte2}` のような書き方をすると、この落とし穴に落ちてしまいます。
          回避するには、必要な値全体の入った変数を作っておき、一つのセルで渡します。 (e.g. `${bytes}`) そうすれば、値がそのままキーワード側に渡るからです。

.. _list variable:

リスト型変数
~~~~~~~~~~~~~~

変数を `${EXAMPLE}` のようにスカラーとして参照した場合、その変数はあるがままの値を表します。
一方、値がリストやリストライクなオブジェクトの場合には、 `@{EXAMPLE}` のように書くことで、変数をリスト変数として使えます。
キーワードの引数にリスト変数を指定すると、リストの各要素をそれぞれ個別の変数として渡せます。
例えば、変数 `@{USER}` が `['robot', 'secret']` という値のとき、以下の二つのテストケースは同じです:

.. sourcecode:: robotframework

   *** Test Cases ***
   Constants
       Login    robot    secret

   List Variable
       Login    @{USER}

Robot Framework は、どの変数も、内部的には同じ仕組みで保存しており、一つの変数をスカラ型、リスト型、辞書型で扱えるようにしています。
変数をリストとして扱いたいときは、その値は Python のリストか、リストライクなオブジェクトでなければなりません。
Robot Framework では、文字列をリストとしては扱えませんが、タプルや辞書であればリストとして扱えます。

Robot Framework 2.9 までは、スカラ変数とリスト変数は別々に保存されていましたが、リスト変数をスカラとして使ったり、スカラ変数をリストとして扱ったりできました。
そのため、同じ名前のスカラ変数とリスト変数に別々の値が入ってしまうことがあり、よく混乱を招いていました。

.. Using list variables with other data

リスト変数を他のデータと組み合わせる
''''''''''''''''''''''''''''''''''''''

リスト変数は他の引数と合わせて使えます。リスト同士でも組み合わせられます。

.. sourcecode:: robotframework

   *** Test Cases ***
   Example
       Keyword    @{LIST}    more    args
       Keyword    ${SCALAR}    @{LIST}    constant
       Keyword    @{LIST}    @{ANOTHER}    @{ONE MORE}


リスト変数を、他のデータ（文字列定数や、他の変数）と一緒のセルに入れた場合、そのセルは最終的には各変数の値を文字列にした結果が入ります。
結果は、変数をスカラとして他のデータと一緒のセルにいれたときと同じになります。

.. Accessing individual list items

リストの個別の要素にアクセスする
''''''''''''''''''''''''''''''''''

リスト変数中の特定の要素にアクセスしたいときには、 `@{NAME}[index]` のように書きます。 `index` は、アクセスしたい要素のインデクスです。
インデクスは 0 から数えます。負の数を指定すると、末尾からの順になり、インデクスがリストの要素数より大きい時にはエラーになります。
インデクス部分の内容は値は自動的に整数変換されます。そのため、インデクスには変数も使えます。
インデクスを指定してリストの要素にアクセスした場合、その変数はスカラ変数のように扱えます。

.. sourcecode:: robotframework

   *** Test Cases ***
   List Variable Item
       Login    @{USER}[0]    @{USER}[1]
       Title Should Be    Welcome @{USER}[0]!

   Negative Index
       Log    @{LIST}[-1]

   Index As Variable
       Log    @{LIST}[${INDEX}]

.. Using list variables with settings

リスト変数を設定テーブルで使う
''''''''''''''''''''''''''''''''

設定テーブルの :ref:`設定 <All available settings in test data>` の中には、リスト変数を渡せるものもあります。
ライブラリや変数ファイルのインポート設定の場合、引数にはリスト変数を使えますが、ファイル名には使えません。
同様に、セットアップやティアダウン設定でも、引数にはリスト変数を使えますが、ファイル名には使えません。
タグ関連の設定では、リスト変数を自由に使えます。
リスト変数が指定できない場所では、必ずスカラ変数を使えるようになっています。

.. sourcecode:: robotframework

   *** Settings ***
   Library         ExampleLibrary      @{LIB ARGS}    # OK
   Library         ${LIBRARY}          @{LIB ARGS}    # OK
   Library         @{NAME AND ARGS}                   # うまくいかない
   Suite Setup     Some Keyword        @{KW ARGS}     # OK
   Suite Setup     ${KEYWORD}          @{KW ARGS}     # OKThis works
   Suite Setup     @{KEYWORD}                         # うまくいかない
   Default Tags    @{TAGS}                            # OK


.. _dictionary variable:

辞書変数
~~~~~~~~~~

As discussed above, a variable containing a list can be used as a `list
variable`_ to pass list items to a keyword as individual arguments.
Similarly a variable containing a Python dictionary or a dictionary-like
object can be used as a dictionary variable like `&{EXAMPLE}`. In practice
this means that individual items of the dictionary are passed as
`named arguments`_ to the keyword. Assuming that a variable `&{USER}` has
value `{'name': 'robot', 'password': 'secret'}`, the following two test cases
are equivalent.

.. sourcecode:: robotframework

   *** Test Cases ***
   Constants
       Login    name=robot    password=secret

   Dict Variable
       Login    &{USER}

Dictionary variables are new in Robot Framework 2.9.

Using dictionary variables with other data
''''''''''''''''''''''''''''''''''''''''''

It is possible to use dictionary variables with other arguments, including
other dictionary variables. Because `named argument syntax`_ requires positional
arguments to be before named argument, dictionaries can only be followed by
named arguments or other dictionaries.

.. sourcecode:: robotframework

   *** Test Cases ***
   Example
       Keyword    &{DICT}    named=arg
       Keyword    positional    @{LIST}    &{DICT}
       Keyword    &{DICT}    &{ANOTHER}    &{ONE MORE}

If a dictionary variable is used in a cell with other data (constant strings or
other variables), the final value will contain a string representation of the
variable value. The end result is thus exactly the same as when using the
variable as a scalar with other data in the same cell.

Accessing individual dictionary items
'''''''''''''''''''''''''''''''''''''

It is possible to access a certain value of a dictionary variable
with the syntax `&{NAME}[key]`, where `key` is the name of the
selected value. Keys are considered to be strings, but non-strings
keys can be used as variables. Dictionary values accessed in this
manner can be used similarly as scalar variables.

If a key is a string, it is possible to access its value also using
attribute access syntax `${NAME.key}`. See `Creating dictionary variables`_
for more details about this syntax.

.. sourcecode:: robotframework

   *** Test Cases ***
   Dict Variable Item
       Login    &{USER}[name]    &{USER}[password]
       Title Should Be    Welcome &{USER}[name]!

   Key As Variable
       Log Many    &{DICT}[${KEY}]    &{DICT}[${42}]

   Attribute Access
       Login    ${USER.name}    ${USER.password}
       Title Should Be    Welcome ${USER.name}!

Using dictionary variables with settings
''''''''''''''''''''''''''''''''''''''''

Dictionary variables cannot generally be used with settings. The only exception
are imports, setups and teardowns where dictionaries can be used as arguments.

.. sourcecode:: robotframework

   *** Settings ***
   Library        ExampleLibrary    &{LIB ARGS}
   Suite Setup    Some Keyword      &{KW ARGS}     named=arg

.. _environment variable:

Environment variables
~~~~~~~~~~~~~~~~~~~~~

Robot Framework allows using environment variables in the test
data using the syntax `%{ENV_VAR_NAME}`. They are limited to string
values.

Environment variables set in the operating system before the test execution are
available during it, and it is possible to create new ones with the keyword
:name:`Set Environment Variable` or delete existing ones with the
keyword :name:`Delete Environment Variable`, both available in the
OperatingSystem_ library. Because environment variables are global,
environment variables set in one test case can be used in other test
cases executed after it. However, changes to environment variables are
not effective after the test execution.

.. sourcecode:: robotframework

   *** Test Cases ***
   Env Variables
       Log    Current user: %{USER}
       Run    %{JAVA_HOME}${/}javac

Java system properties
~~~~~~~~~~~~~~~~~~~~~~

When running tests with Jython, it is possible to access `Java system properties`__
using same syntax as `environment variables`_. If an environment variable and a
system property with same name exist, the environment variable will be used.

.. sourcecode:: robotframework

   *** Test Cases ***
   System Properties
       Log    %{user.name} running tests on %{os.name}

__ http://docs.oracle.com/javase/tutorial/essential/environment/sysprop.html

Creating variables
------------------

Variables can spring into existence from different sources.

Variable table
~~~~~~~~~~~~~~

The most common source for variables are Variable tables in `test case
files`_ and `resource files`_. Variable tables are convenient, because they
allow creating variables in the same place as the rest of the test
data, and the needed syntax is very simple. Their main disadvantages are
that values are always strings and they cannot be created dynamically.
If either of these is a problem, `variable files`_ can be used instead.

Creating scalar variables
'''''''''''''''''''''''''

The simplest possible variable assignment is setting a string into a
scalar variable. This is done by giving the variable name (including
`${}`) in the first column of the Variable table and the value in
the second one. If the second column is empty, an empty string is set
as a value. Also an already defined variable can be used in the value.

.. sourcecode:: robotframework

   *** Variables ***
   ${NAME}         Robot Framework
   ${VERSION}      2.0
   ${ROBOT}        ${NAME} ${VERSION}

It is also possible, but not obligatory,
to use the equals sign `=` after the variable name to make assigning
variables slightly more explicit.

.. sourcecode:: robotframework

   *** Variables ***
   ${NAME} =       Robot Framework
   ${VERSION} =    2.0

If a scalar variable has a long value, it can be split to multiple columns and
rows__. By default cells are catenated together using a space, but this
can be changed by having `SEPARATOR=<sep>` in the first cell.

.. sourcecode:: robotframework

   *** Variables ***
   ${EXAMPLE}      This value is joined    together with a space
   ${MULTILINE}    SEPARATOR=\n    First line
   ...             Second line     Third line

Joining long values like above is a new feature in Robot Framework 2.9.
Creating a scalar variable with multiple values was a syntax error in
Robot Framework 2.8 and with earlier versions it created a variable with
a list value.

__ `Dividing test data to several rows`_

Creating list variables
'''''''''''''''''''''''

Creating list variables is as easy as creating scalar variables. Again, the
variable name is in the first column of the Variable table and
values in the subsequent columns. A list variable can have any number
of values, starting from zero, and if many values are needed, they
can be `split into several rows`__.

__ `Dividing test data to several rows`_

.. sourcecode:: robotframework

   *** Variables ***
   @{NAMES}        Matti       Teppo
   @{NAMES2}       @{NAMES}    Seppo
   @{NOTHING}
   @{MANY}         one         two      three      four
   ...             five        six      seven

Creating dictionary variables
'''''''''''''''''''''''''''''

Dictionary variables can be created in the variable table similarly as
list variables. The difference is that items need to be created using
`name=value` syntax or existing dictionary variables. If there are multiple
items with same name, the last value has precedence. If a name contains
a literal equal sign, it can be escaped__ with a backslash like `\=`.

.. sourcecode:: robotframework

   *** Variables ***
   &{USER 1}       name=Matti    address=xxx         phone=123
   &{USER 2}       name=Teppo    address=yyy         phone=456
   &{MANY}         first=1       second=${2}         ${3}=third
   &{EVEN MORE}    &{MANY}       first=override      empty=
   ...             =empty        key\=here=value

Dictionary variables have two extra properties
compared to normal Python dictionaries. First of all, values of these
dictionaries can be accessed like attributes, which means that it is possible
to use `extended variable syntax`_ like `${VAR.key}`. This only works if the
key is a valid attribute name and does not match any normal attribute
Python dictionaries have. For example, individual value `&{USER}[name]` can
also be accessed like `${USER.name}` (notice that `$` is needed in this
context), but using `${MANY.3}` is not possible.

Another special property of dictionary variables is
that they are ordered. This means that if these dictionaries are iterated,
their items always come in the order they are defined. This can be useful
if dictionaries are used as `list variables`_ with `for loops`_ or otherwise.
When a dictionary is used as a list variable, the actual value contains
dictionary keys. For example, `@{MANY}` variable would have value `['first',
'second', 3]`.

__ Escaping_

Variable file
~~~~~~~~~~~~~

Variable files are the most powerful mechanism for creating different
kind of variables. It is possible to assign variables to any object
using them, and they also enable creating variables dynamically. The
variable file syntax and taking variable files into use is explained
in section `Resource and variable files`_.

Setting variables in command line
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Variables can be set from the command line either individually with
the :option:`--variable (-v)` option or using a variable file with the
:option:`--variablefile (-V)` option. Variables set from the command line
are globally available for all executed test data files, and they also
override possible variables with the same names in the Variable table and in
variable files imported in the test data.

The syntax for setting individual variables is :option:`--variable
name:value`, where `name` is the name of the variable without
`${}` and `value` is its value. Several variables can be
set by using this option several times. Only scalar variables can be
set using this syntax and they can only get string values. Many
special characters are difficult to represent in the
command line, but they can be escaped__ with the :option:`--escape`
option.

__ `Escaping complicated characters`_

.. sourcecode:: bash

   --variable EXAMPLE:value
   --variable HOST:localhost:7272 --variable USER:robot
   --variable ESCAPED:Qquotes_and_spacesQ --escape quot:Q --escape space:_

In the examples above, variables are set so that

- `${EXAMPLE}` gets the value `value`
- `${HOST}` and `${USER}` get the values
  `localhost:7272` and `robot`
- `${ESCAPED}` gets the value `"quotes and spaces"`

The basic syntax for taking `variable files`_ into use from the command line
is :option:`--variablefile path/to/variables.py`, and `Taking variable files into
use`_ section has more details. What variables actually are created depends on
what variables there are in the referenced variable file.

If both variable files and individual variables are given from the command line,
the latter have `higher priority`__.

__ `Variable priorities and scopes`_

Return values from keywords
~~~~~~~~~~~~~~~~~~~~~~~~~~~

Return values from keywords can also be set into variables. This
allows communication between different keywords even in different test
libraries.

Variables set in this manner are otherwise similar to any other
variables, but they are available only in the `local scope`_
where they are created. Thus it is not possible, for example, to set
a variable like this in one test case and use it in another. This is
because, in general, automated test cases should not depend on each
other, and accidentally setting a variable that is used elsewhere
could cause hard-to-debug errors. If there is a genuine need for
setting a variable in one test case and using it in another, it is
possible to use BuiltIn_ keywords as explained in the next section.

Assigning scalar variables
''''''''''''''''''''''''''

Any value returned by a keyword can be assigned to a `scalar variable`_.
As illustrated by the example below, the required syntax is very simple:

.. sourcecode:: robotframework

   *** Test Cases ***
   Returning
       ${x} =    Get X    an argument
       Log    We got ${x}!

In the above example the value returned by the :name:`Get X` keyword
is first set into the variable `${x}` and then used by the :name:`Log`
keyword. Having the equals sign `=` after the variable name is
not obligatory, but it makes the assignment more explicit. Creating
local variables like this works both in test case and user keyword level.

Notice that although a value is assigned to a scalar variable, it can
be used as a `list variable`_ if it has a list-like value and as a `dictionary
variable`_ if it has a dictionary-like value.

.. sourcecode:: robotframework

   *** Test Cases ***
   Example
       ${list} =    Create List    first    second    third
       Length Should Be    ${list}    3
       Log Many    @{list}

Assigning list variables
''''''''''''''''''''''''

If a keyword returns a list or any list-like object, it is possible to
assign it to a `list variable`_:

.. sourcecode:: robotframework

   *** Test Cases ***
   Example
       @{list} =    Create List    first    second    third
       Length Should Be    ${list}    3
       Log Many    @{list}

Because all Robot Framework variables are stored in the same namespace, there is
not much difference between assigning a value to a scalar variable or a list
variable. This can be seen by comparing the last two examples above. The main
differences are that when creating a list variable, Robot Framework
automatically verifies that the value is a list or list-like, and the stored
variable value will be a new list created from the return value. When
assigning to a scalar variable, the return value is not verified and the
stored value will be the exact same object that was returned.

Assigning dictionary variables
''''''''''''''''''''''''''''''

If a keyword returns a dictionary or any dictionary-like object, it is possible
to assign it to a `dictionary variable`_:

.. sourcecode:: robotframework

   *** Test Cases ***
   Example
       &{dict} =    Create Dictionary    first=1    second=${2}    ${3}=third
       Length Should Be    ${dict}    3
       Do Something    &{dict}
       Log    ${dict.first}

Because all Robot Framework variables are stored in the same namespace, it would
also be possible to assign a dictionary into a scalar variable and use it
later as a dictionary when needed. There are, however, some actual benefits
in creating a dictionary variable explicitly. First of all, Robot Framework
verifies that the returned value is a dictionary or dictionary-like similarly
as it verifies that list variables can only get a list-like value.

A bigger benefit is that the value is converted into a special dictionary
that it uses also when `creating dictionary variables`_ in the variable table.
Values in these dictionaries can be accessed using attribute access like
`${dict.first}` in the above example. These dictionaries are also ordered, but
if the original dictionary was not ordered, the resulting order is arbitrary.

Assigning multiple variables
''''''''''''''''''''''''''''

If a keyword returns a list or a list-like object, it is possible to assign
individual values into multiple scalar variables or into scalar variables and
a list variable.

.. sourcecode:: robotframework

   *** Test Cases ***
   Assign Multiple
       ${a}    ${b}    ${c} =    Get Three
       ${first}    @{rest} =    Get Three
       @{before}    ${last} =    Get Three
       ${begin}    @{middle}    ${end} =    Get Three

Assuming that the keyword :name:`Get Three` returns a list `[1, 2, 3]`,
the following variables are created:

- `${a}`, `${b}` and `${c}` with values `1`, `2`, and `3`, respectively.
- `${first}` with value `1`, and `@{rest}` with value `[2, 3]`.
- `@{before}` with value `[1, 2]` and `${last}` with value `3`.
- `${begin}` with value `1`, `@{middle}` with value `[2]` and ${end} with
  value `3`.

It is an error if the returned list has more or less values than there are
scalar variables to assign. Additionally, only one list variable is allowed
and dictionary variables can only be assigned alone.

The support for assigning multiple variables was slightly changed in
Robot Framework 2.9. Prior to it a list variable was only allowed as
the last assigned variable, but nowadays it can be used anywhere.
Additionally, it was possible to return more values than scalar variables.
In that case the last scalar variable was magically turned into a list
containing the extra values.

Using :name:`Set Test/Suite/Global Variable` keywords
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The BuiltIn_ library has keywords :name:`Set Test Variable`,
:name:`Set Suite Variable` and :name:`Set Global Variable` which can
be used for setting variables dynamically during the test
execution. If a variable already exists within the new scope, its
value will be overwritten, and otherwise a new variable is created.

Variables set with :name:`Set Test Variable` keyword are available
everywhere within the scope of the currently executed test case. For
example, if you set a variable in a user keyword, it is available both
in the test case level and also in all other user keywords used in the
current test. Other test cases will not see variables set with this
keyword.

Variables set with :name:`Set Suite Variable` keyword are available
everywhere within the scope of the currently executed test
suite. Setting variables with this keyword thus has the same effect as
creating them using the `Variable table`_ in the test data file or
importing them from `variable files`_. Other test suites, including
possible child test suites, will not see variables set with this
keyword.

Variables set with :name:`Set Global Variable` keyword are globally
available in all test cases and suites executed after setting
them. Setting variables with this keyword thus has the same effect as
`creating from the command line`__ using the options :option:`--variable` or
:option:`--variablefile`. Because this keyword can change variables
everywhere, it should be used with care.

.. note:: :name:`Set Test/Suite/Global Variable` keywords set named
          variables directly into `test, suite or global variable scope`__
          and return nothing. On the other hand, another BuiltIn_ keyword
          :name:`Set Variable` sets local variables using `return values`__.

__ `Setting variables in command line`_
__ `Variable scopes`_
__ `Return values from keywords`_

.. _built-in variable:

Built-in variables
------------------

Robot Framework provides some built-in variables that are available
automatically.

Operating-system variables
~~~~~~~~~~~~~~~~~~~~~~~~~~

Built-in variables related to the operating system ease making the test data
operating-system-agnostic.

.. table:: Available operating-system-related built-in variables
   :class: tabular

   +------------+------------------------------------------------------------------+
   |  Variable  |                      Explanation                                 |
   +============+==================================================================+
   | ${CURDIR}  | An absolute path to the directory where the test data            |
   |            | file is located. This variable is case-sensitive.                |
   +------------+------------------------------------------------------------------+
   | ${TEMPDIR} | An absolute path to the system temporary directory. In UNIX-like |
   |            | systems this is typically :file:`/tmp`, and in Windows           |
   |            | :file:`c:\\Documents and Settings\\<user>\\Local Settings\\Temp`.|
   +------------+------------------------------------------------------------------+
   | ${EXECDIR} | An absolute path to the directory where test execution was       |
   |            | started from.                                                    |
   +------------+------------------------------------------------------------------+
   | ${/}       | The system directory path separator. `/` in UNIX-like            |
   |            | systems and :codesc:`\\` in Windows.                             |
   +------------+------------------------------------------------------------------+
   | ${:}       | The system path element separator. `:` in UNIX-like              |
   |            | systems and `;` in Windows.                                      |
   +------------+------------------------------------------------------------------+
   | ${\\n}     | The system line separator. :codesc:`\\n` in UNIX-like systems and|
   |            | :codesc:`\\r\\n` in Windows. New in version 2.7.5.               |
   +------------+------------------------------------------------------------------+

.. sourcecode:: robotframework

   *** Test Cases ***
   Example
       Create Binary File    ${CURDIR}${/}input.data    Some text here${\n}on two lines
       Set Environment Variable    CLASSPATH    ${TEMPDIR}${:}${CURDIR}${/}foo.jar

Number variables
~~~~~~~~~~~~~~~~

The variable syntax can be used for creating both integers and
floating point numbers, as illustrated in the example below. This is
useful when a keyword expects to get an actual number, and not a
string that just looks like a number, as an argument.

.. sourcecode:: robotframework

   *** Test Cases ***
   Example 1A
       Connect    example.com    80       # Connect gets two strings as arguments

   Example 1B
       Connect    example.com    ${80}    # Connect gets a string and an integer

   Example 2
       Do X    ${3.14}    ${-1e-4}        # Do X gets floating point numbers 3.14 and -0.0001

It is possible to create integers also from binary, octal, and
hexadecimal values using `0b`, `0o` and `0x` prefixes, respectively.
The syntax is case insensitive.

.. sourcecode:: robotframework

   *** Test Cases ***
   Example
       Should Be Equal    ${0b1011}    ${11}
       Should Be Equal    ${0o10}      ${8}
       Should Be Equal    ${0xff}      ${255}
       Should Be Equal    ${0B1010}    ${0XA}

Boolean and None/null variables
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Also Boolean values and Python `None` and Java `null` can
be created using the variable syntax similarly as numbers.

.. sourcecode:: robotframework

   *** Test Cases ***
   Boolean
       Set Status    ${true}               # Set Status gets Boolean true as an argument
       Create Y    something   ${false}    # Create Y gets a string and Boolean false

   None
       Do XYZ    ${None}                   # Do XYZ gets Python None as an argument

   Null
       ${ret} =    Get Value    arg        # Checking that Get Value returns Java null
       Should Be Equal    ${ret}    ${null}

These variables are case-insensitive, so for example `${True}` and
`${true}` are equivalent. Additionally, `${None}` and
`${null}` are synonyms, because when running tests on the Jython
interpreter, Jython automatically converts `None` and
`null` to the correct format when necessary.

Space and empty variables
~~~~~~~~~~~~~~~~~~~~~~~~~

It is possible to create spaces and empty strings using variables
`${SPACE}` and `${EMPTY}`, respectively. These variables are
useful, for example, when there would otherwise be a need to `escape
spaces or empty cells`__ with a backslash. If more than one space is
needed, it is possible to use the `extended variable syntax`_ like
`${SPACE * 5}`.  In the following example, :name:`Should Be
Equal` keyword gets identical arguments but those using variables are
easier to understand than those using backslashes.

.. sourcecode:: robotframework

   *** Test Cases ***
   One Space
       Should Be Equal    ${SPACE}          \ \

   Four Spaces
       Should Be Equal    ${SPACE * 4}      \ \ \ \ \

   Ten Spaces
       Should Be Equal    ${SPACE * 10}     \ \ \ \ \ \ \ \ \ \ \

   Quoted Space
       Should Be Equal    "${SPACE}"        " "

   Quoted Spaces
       Should Be Equal    "${SPACE * 2}"    " \ "

   Empty
       Should Be Equal    ${EMPTY}          \

There is also an empty `list variable`_ `@{EMPTY}` and an empty `dictionary
variable`_ `&{EMPTY}`. Because they have no content, they basically
vanish when used somewhere in the test data. They are useful, for example,
with `test templates`_ when the `template keyword is used without
arguments`__ or when overriding list or dictionary variables in different
scopes. Modifying the value of `@{EMPTY}` or `&{EMPTY}` is not possible.

.. sourcecode:: robotframework

   *** Test Cases ***
   Template
       [Template]    Some keyword
       @{EMPTY}

   Override
       Set Global Variable    @{LIST}    @{EMPTY}
       Set Suite Variable     &{DICT}    &{EMPTY}

.. note:: `@{EMPTY}` is new in Robot Framework 2.7.4 and `&{EMPTY}` in
          Robot Framework 2.9.

__ Escaping_
__ https://groups.google.com/group/robotframework-users/browse_thread/thread/ccc9e1cd77870437/4577836fe946e7d5?lnk=gst&q=templates#4577836fe946e7d5

Automatic variables
~~~~~~~~~~~~~~~~~~~

Some automatic variables can also be used in the test data. These
variables can have different values during the test execution and some
of them are not even available all the time. Altering the value of
these variables does not affect the original values, but some values
can be changed dynamically using keywords from the `BuiltIn`_ library.

.. table:: Available automatic variables
   :class: tabular

   +------------------------+-------------------------------------------------------+------------+
   |        Variable        |                    Explanation                        | Available  |
   +========================+=======================================================+============+
   | ${TEST NAME}           | The name of the current test case.                    | Test case  |
   +------------------------+-------------------------------------------------------+------------+
   | @{TEST TAGS}           | Contains the tags of the current test case in         | Test case  |
   |                        | alphabetical order. Can be modified dynamically using |            |
   |                        | :name:`Set Tags` and :name:`Remove Tags` keywords.    |            |
   +------------------------+-------------------------------------------------------+------------+
   | ${TEST DOCUMENTATION}  | The documentation of the current test case. Can be set| Test case  |
   |                        | dynamically using using :name:`Set Test Documentation`|            |
   |                        | keyword. New in Robot Framework 2.7.                  |            |
   +------------------------+-------------------------------------------------------+------------+
   | ${TEST STATUS}         | The status of the current test case, either PASS or   | `Test      |
   |                        | FAIL.                                                 | teardown`_ |
   +------------------------+-------------------------------------------------------+------------+
   | ${TEST MESSAGE}        | The message of the current test case.                 | `Test      |
   |                        |                                                       | teardown`_ |
   +------------------------+-------------------------------------------------------+------------+
   | ${PREV TEST NAME}      | The name of the previous test case, or an empty string| Everywhere |
   |                        | if no tests have been executed yet.                   |            |
   +------------------------+-------------------------------------------------------+------------+
   | ${PREV TEST STATUS}    | The status of the previous test case: either PASS,    | Everywhere |
   |                        | FAIL, or an empty string when no tests have been      |            |
   |                        | executed.                                             |            |
   +------------------------+-------------------------------------------------------+------------+
   | ${PREV TEST MESSAGE}   | The possible error message of the previous test case. | Everywhere |
   +------------------------+-------------------------------------------------------+------------+
   | ${SUITE NAME}          | The full name of the current test suite.              | Everywhere |
   +------------------------+-------------------------------------------------------+------------+
   | ${SUITE SOURCE}        | An absolute path to the suite file or directory.      | Everywhere |
   +------------------------+-------------------------------------------------------+------------+
   | ${SUITE DOCUMENTATION} | The documentation of the current test suite. Can be   | Everywhere |
   |                        | set dynamically using using :name:`Set Suite          |            |
   |                        | Documentation` keyword. New in Robot Framework 2.7.   |            |
   +------------------------+-------------------------------------------------------+------------+
   | &{SUITE METADATA}      | The free metadata of the current test suite. Can be   | Everywhere |
   |                        | set using :name:`Set Suite Metadata` keyword.         |            |
   |                        | New in Robot Framework 2.7.4.                         |            |
   +------------------------+-------------------------------------------------------+------------+
   | ${SUITE STATUS}        | The status of the current test suite, either PASS or  | `Suite     |
   |                        | FAIL.                                                 | teardown`_ |
   +------------------------+-------------------------------------------------------+------------+
   | ${SUITE MESSAGE}       | The full message of the current test suite, including | `Suite     |
   |                        | statistics.                                           | teardown`_ |
   +------------------------+-------------------------------------------------------+------------+
   | ${KEYWORD STATUS}      | The status of the current keyword, either PASS or     | `User      |
   |                        | FAIL. New in Robot Framework 2.7                      | keyword    |
   |                        |                                                       | teardown`_ |
   +------------------------+-------------------------------------------------------+------------+
   | ${KEYWORD MESSAGE}     | The possible error message of the current keyword.    | `User      |
   |                        | New in Robot Framework 2.7.                           | keyword    |
   |                        |                                                       | teardown`_ |
   +------------------------+-------------------------------------------------------+------------+
   | ${LOG LEVEL}           | Current `log level`_. New in Robot Framework 2.8.     | Everywhere |
   +------------------------+-------------------------------------------------------+------------+
   | ${OUTPUT FILE}         | An absolute path to the `output file`_.               | Everywhere |
   +------------------------+-------------------------------------------------------+------------+
   | ${LOG FILE}            | An absolute path to the `log file`_ or string NONE    | Everywhere |
   |                        | when no log file is created.                          |            |
   +------------------------+-------------------------------------------------------+------------+
   | ${REPORT FILE}         | An absolute path to the `report file`_ or string NONE | Everywhere |
   |                        | when no report is created.                            |            |
   +------------------------+-------------------------------------------------------+------------+
   | ${DEBUG FILE}          | An absolute path to the `debug file`_ or string NONE  | Everywhere |
   |                        | when no debug file is created.                        |            |
   +------------------------+-------------------------------------------------------+------------+
   | ${OUTPUT DIR}          | An absolute path to the `output directory`_.          | Everywhere |
   +------------------------+-------------------------------------------------------+------------+

Suite related variables `${SUITE SOURCE}`, `${SUITE NAME}`,
`${SUITE DOCUMENTATION}` and `&{SUITE METADATA}` are
available already when test libraries and variable files are imported,
except to Robot Framework 2.8 and 2.8.1 where this support was broken.
Possible variables in these automatic variables are not yet resolved
at the import time, though.

Variable priorities and scopes
------------------------------

Variables coming from different sources have different priorities and
are available in different scopes.

Variable priorities
~~~~~~~~~~~~~~~~~~~

*Variables from the command line*

   Variables `set in the command line`__ have the highest priority of all
   variables that can be set before the actual test execution starts. They
   override possible variables created in Variable tables in test case
   files, as well as in resource and variable files imported in the
   test data.

   Individually set variables (:option:`--variable` option) override the
   variables set using `variable files`_ (:option:`--variablefile` option).
   If you specify same individual variable multiple times, the one specified
   last will override earlier ones. This allows setting default values for
   variables in a `start-up script`_ and overriding them from the command line.
   Notice, though, that if multiple variable files have same variables, the
   ones in the file specified first have the highest priority.

__ `Setting variables in command line`_

*Variable table in a test case file*

   Variables created using the `Variable table`_ in a test case file
   are available for all the test cases in that file. These variables
   override possible variables with same names in imported resource and
   variable files.

   Variables created in the variable tables are available in all other tables
   in the file where they are created. This means that they can be used also
   in the Setting table, for example, for importing more variables from
   resource and variable files.

*Imported resource and variable files*

   Variables imported from the `resource and variable files`_ have the
   lowest priority of all variables created in the test data.
   Variables from resource files and variable files have the same
   priority. If several resource and/or variable file have same
   variables, the ones in the file imported first are taken into use.

   If a resource file imports resource files or variable files,
   variables in its own Variable table have a higher priority than
   variables it imports. All these variables are available for files that
   import this resource file.

   Note that variables imported from resource and variable files are not
   available in the Variable table of the file that imports them. This
   is due to the Variable table being processed before the Setting table
   where the resource files and variable files are imported.

*Variables set during test execution*

   Variables set during the test execution either using `return values
   from keywords`_ or `using Set Test/Suite/Global Variable keywords`_
   always override possible existing
   variables in the scope where they are set. In a sense they thus
   have the highest priority, but on the other hand they do not affect
   variables outside the scope they are defined.

*Built-in variables*

   `Built-in variables`_ like `${TEMPDIR}` and `${TEST_NAME}`
   have the highest priority of all variables. They cannot be overridden
   using Variable table or from command line, but even they can be reset during
   the test execution. An exception to this rule are `number variables`_, which
   are resolved dynamically if no variable is found otherwise. They can thus be
   overridden, but that is generally a bad idea. Additionally `${CURDIR}`
   is special because it is replaced already during the test data processing time.

Variable scopes
~~~~~~~~~~~~~~~

Depending on where and how they are created, variables can have a
global, test suite, test case or local scope.

Global scope
''''''''''''

Global variables are available everywhere in the test data. These
variables are normally `set from the command line`__ with the
:option:`--variable` and :option:`--variablefile` options, but it is also
possible to create new global variables or change the existing ones
with the BuiltIn_ keyword :name:`Set Global Variable` anywhere in
the test data. Additionally also `built-in variables`_ are global.

It is recommended to use capital letters with all global variables.

Test suite scope
''''''''''''''''

Variables with the test suite scope are available anywhere in the
test suite where they are defined or imported. They can be created
in Variable tables, imported from `resource and variable files`_,
or set during the test execution using the BuiltIn_ keyword
:name:`Set Suite Variable`.

The test suite scope *is not recursive*, which means that variables
available in a higher-level test suite *are not available* in
lower-level suites. If necessary, `resource and variable files`_ can
be used for sharing variables.

Since these variables can be considered global in the test suite where
they are used, it is recommended to use capital letters also with them.

Test case scope
'''''''''''''''

Variables with the test case scope are visible in a test case and in
all user keywords the test uses. Initially there are no variables in
this scope, but it is possible to create them by using the BuiltIn_
keyword :name:`Set Test Variable` anywhere in a test case.

Also variables in the test case scope are to some extend global. It is
thus generally recommended to use capital letters with them too.

Local scope
'''''''''''

Test cases and user keywords have a local variable scope that is not
seen by other tests or keywords. Local variables can be created using
`return values`__ from executed keywords and user keywords also get
them as arguments__.

It is recommended to use lower-case letters with local variables.

.. note:: Prior to Robot Framework 2.9 variables in the local scope
          `leaked to lower level user keywords`__. This was never an
          intended feature, and variables should be set or passed
          explicitly also with earlier versions.

__ `Setting variables in command line`_
__ `Return values from keywords`_
__ `User keyword arguments`_
__ https://github.com/robotframework/robotframework/issues/532

Advanced variable features
--------------------------

Extended variable syntax
~~~~~~~~~~~~~~~~~~~~~~~~

Extended variable syntax allows accessing attributes of an object assigned
to a variable (for example, `${object.attribute}`) and even calling
its methods (for example, `${obj.getName()}`). It works both with
scalar and list variables, but is mainly useful with the former

Extended variable syntax is a powerful feature, but it should
be used with care. Accessing attributes is normally not a problem, on
the contrary, because one variable containing an object with several
attributes is often better than having several variables. On the
other hand, calling methods, especially when they are used with
arguments, can make the test data pretty complicated to understand.
If that happens, it is recommended to move the code into a test library.

The most common usages of extended variable syntax are illustrated
in the example below. First assume that we have the following `variable file`_
and test case:

.. sourcecode:: python

   class MyObject:

       def __init__(self, name):
           self.name = name

       def eat(self, what):
           return '%s eats %s' % (self.name, what)

       def __str__(self):
           return self.name

   OBJECT = MyObject('Robot')
   DICTIONARY = {1: 'one', 2: 'two', 3: 'three'}

.. sourcecode:: robotframework

   *** Test Cases ***
   Example
       KW 1    ${OBJECT.name}
       KW 2    ${OBJECT.eat('Cucumber')}
       KW 3    ${DICTIONARY[2]}

When this test data is executed, the keywords get the arguments as
explained below:

- :name:`KW 1` gets string `Robot`
- :name:`KW 2` gets string `Robot eats Cucumber`
- :name:`KW 3` gets string `two`

The extended variable syntax is evaluated in the following order:

1. The variable is searched using the full variable name. The extended
   variable syntax is evaluated only if no matching variable
   is found.

2. The name of the base variable is created. The body of the name
   consists of all the characters after the opening `{` until
   the first occurrence of a character that is not an alphanumeric character
   or a space. For example, base variables of `${OBJECT.name}`
   and `${DICTIONARY[2]}`) are `OBJECT` and `DICTIONARY`,
   respectively.

3. A variable matching the body is searched. If there is no match, an
   exception is raised and the test case fails.

4. The expression inside the curly brackets is evaluated as a Python
   expression, so that the base variable name is replaced with its
   value. If the evaluation fails because of an invalid syntax or that
   the queried attribute does not exist, an exception is raised and
   the test fails.

5. The whole extended variable is replaced with the value returned
   from the evaluation.

If the object that is used is implemented with Java, the extended
variable syntax allows you to access attributes using so-called bean
properties. In essence, this means that if you have an object with the
`getName`  method set into a variable `${OBJ}`, then the
syntax `${OBJ.name}` is equivalent to but clearer than
`${OBJ.getName()}`. The Python object used in the previous example
could thus be replaced with the following Java implementation:

.. sourcecode:: java

 public class MyObject:

     private String name;

     public MyObject(String name) {
         name = name;
     }

     public String getName() {
         return name;
     }

     public String eat(String what) {
         return name + " eats " + what;
     }

     public String toString() {
         return name;
     }
 }

Many standard Python objects, including strings and numbers, have
methods that can be used with the extended variable syntax either
explicitly or implicitly. Sometimes this can be really useful and
reduce the need for setting temporary variables, but it is also easy
to overuse it and create really cryptic test data. Following examples
show few pretty good usages.

.. sourcecode:: robotframework

   *** Test Cases ***
   String
       ${string} =    Set Variable    abc
       Log    ${string.upper()}      # Logs 'ABC'
       Log    ${string * 2}          # Logs 'abcabc'

   Number
       ${number} =    Set Variable    ${-2}
       Log    ${number * 10}         # Logs -20
       Log    ${number.__abs__()}    # Logs 2

Note that even though `abs(number)` is recommended over
`number.__abs__()` in normal Python code, using
`${abs(number)}` does not work. This is because the variable name
must be in the beginning of the extended syntax. Using `__xxx__`
methods in the test data like this is already a bit questionable, and
it is normally better to move this kind of logic into test libraries.

Extended variable syntax works also in `list variable`_ context.
If, for example, an object assigned to a variable `${EXTENDED}` has
an attribute `attribute` that contains a list as a value, it can be
used as a list variable `@{EXTENDED.attribute}`.

Extended variable assignment
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Starting from Robot Framework 2.7, it is possible to set attributes of
objects stored to scalar variables using `keyword return values`__ and
a variation of the `extended variable syntax`_. Assuming we have
variable `${OBJECT}` from the previous examples, attributes could
be set to it like in the example below.

__ `Return values from keywords`_

.. sourcecode:: robotframework

   *** Test Cases ***
   Example
       ${OBJECT.name} =    Set Variable    New name
       ${OBJECT.new_attr} =    Set Variable    New attribute

The extended variable assignment syntax is evaluated using the
following rules:

1. The assigned variable must be a scalar variable and have at least
   one dot. Otherwise the extended assignment syntax is not used and
   the variable is assigned normally.

2. If there exists a variable with the full name
   (e.g. `${OBJECT.name}` in the example above) that variable
   will be assigned a new value and the extended syntax is not used.

3. The name of the base variable is created. The body of the name
   consists of all the characters between the opening `${` and
   the last dot, for example, `OBJECT` in `${OBJECT.name}`
   and `foo.bar` in `${foo.bar.zap}`. As the second example
   illustrates, the base name may contain normal extended variable
   syntax.

4. The name of the attribute to set is created by taking all the
   characters between the last dot and the closing `}`, for
   example, `name` in `${OBJECT.name}`. If the name does not
   start with a letter or underscore and contain only these characters
   and numbers, the attribute is considered invalid and the extended
   syntax is not used. A new variable with the full name is created
   instead.

5. A variable matching the base name is searched. If no variable is
   found, the extended syntax is not used and, instead, a new variable
   is created using the full variable name.

6. If the found variable is a string or a number, the extended syntax
   is ignored and a new variable created using the full name. This is
   done because you cannot add new attributes to Python strings or
   numbers, and this way the new syntax is also less
   backwards-incompatible.

7. If all the previous rules match, the attribute is set to the base
   variable. If setting fails for any reason, an exception is raised
   and the test fails.

.. note:: Unlike when assigning variables normally using `return
          values from keywords`_, changes to variables done using the
          extended assign syntax are not limited to the current
          scope. Because no new variable is created but instead the
          state of an existing variable is changed, all tests and
          keywords that see that variable will also see the changes.

Variables inside variables
~~~~~~~~~~~~~~~~~~~~~~~~~~

Variables are allowed also inside variables, and when this syntax is
used, variables are resolved from the inside out. For example, if you
have a variable `${var${x}}`, then `${x}` is resolved
first. If it has the value `name`, the final value is then the
value of the variable `${varname}`. There can be several nested
variables, but resolving the outermost fails, if any of them does not
exist.

In the example below, :name:`Do X` gets the value `${JOHN HOME}`
or `${JANE HOME}`, depending on if :name:`Get Name` returns
`john` or `jane`. If it returns something else, resolving
`${${name} HOME}` fails.

.. sourcecode:: robotframework

   *** Variables ***
   ${JOHN HOME}    /home/john
   ${JANE HOME}    /home/jane

   *** Test Cases ***
   Example
       ${name} =    Get Name
       Do X    ${${name} HOME}
