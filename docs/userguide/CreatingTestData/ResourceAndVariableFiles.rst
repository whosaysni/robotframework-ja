.. _Resource and variable files:

リソースファイルと変数ファイル
==================================

:ref:`テストケースファイル <test case files>` や :ref:`テストスイート初期化ファイル <test suite initialization files>` 中のユーザキーワードや変数は、定義したファイル中でしか使えませんが、 *リソースファイル* は、それを共有するためのメカニズムを提供します。
リソースファイルの構造はテストケースファイルの構造とよく似ているので、作成するのは簡単です。

*変数ファイル* は、変数を定義して共有するための強力なメカニズムを提供します。
例えば、変数ファイルを使えば、文字列以外の値や、動的に生成した値を変数にできます。
変数ファイルのフレキシビリティは、Python コードを使って変数を生成していることにありますが、その反面、 :ref:`変数テーブル <variable tables>` より若干複雑であることは否めません。

.. contents::
   :depth: 2
   :local:

.. _Resource files:

リソースファイル
-------------------

.. _Taking resource files into use:

リソースファイルを使う
~~~~~~~~~~~~~~~~~~~~~~~~

リソースファイルは設定テーブルで :setting:`Resource` を使ってインポートします。
リソースファイルのパスは、 :setting:`Resource` の後のセルに指定します。

パスが絶対パス表記になっていれば、そのパスをそのまま使います。
それ以外の場合は、まず最初に、インポートを行っているファイルからの相対パスでリソースファイルを探します。ファイルがなければ、 Python の :ref:`モジュールサーチパス` 上のディレクトリの相対で探します。
パスには変数を含めることができます。むしろ、変数を使って (:file:`${RESOURCES}/login_resources.html` や :file:`${RESOURCE_PATH}` のように) システムに依存しないパスにするよう勧めます。
スラッシュ (`/`) は、 Windows ではバックスラッシュ (:codesc:`\\`) に動的に変換されます。

.. sourcecode:: robotframework

   *** Settings ***
   Resource    myresources.html
   Resource    ../data/resources.html
   Resource    ${RESOURCES}/common.tsv

リソースファイルにユーザーキーワードや変数を定義すると、リソースファイルをインポートしたファイルの中で利用できます。
ライブラリをインポートすると、ライブラリ中の全てのキーワードや変数が使えるようになりますが、リソースファイルや、リソースファイルからインポートした変数ファイルの場合も同じく、全てのキーワードや変数を使えます。

.. _Resource file structure:

リソースファイルの構造
~~~~~~~~~~~~~~~~~~~~~~~

リソースファイルの大まかな構造は、テストケースファイルとほぼ同じです。
ただし、当然のことながら、テストケーステーブルは入れられません。
また、リソースファイルの設定テーブルには、インポート関連の設定 (:setting:`Library`, :setting:`Resource`, :setting:`Variables`) と :setting:`Documentation` しか設定できません。
変数テーブルやキーワードテーブルはテストケースファイルと全く同じです。

複数のリソースファイルで同じユーザキーワードを定義していた場合、それらを区別するには :ref:`キーワード名の前にリソースファイル名を付加 <Handling keywords with same names>` します (例えば、 :name:`myresources.Some Keyword` と :name:`common.Some Keyword` といった具合です)。
複数のリソースが同じ変数を定義している場合には、先にインポートしたものが使われます。

.. _Documenting resource files:

リソースファイルのドキュメント
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

リソースファイルで定義したキーワードには、 :setting:`[Documentation]` で
:ref:`ドキュメントを書けます <User keyword name and documentation>` 。
リソースファイル自体も、 :ref:`テストスイートと同様 <Test suite name and documentation>` 、設定テーブルに :setting:`Documentation` を書けます。

Libdoc_ や RIDE_ がこのドキュメントを使うほか、リソースファイルが開かれたときには、ドキュメントには普通にアクセスできます。
ドキュメントの最初の行は、キーワードを実行するときにログに記録されます。
それ以外のリソースファイルのドキュメントは、テストの実行時には無視されます。

.. _Example resource file

リソースファイルの例
~~~~~~~~~~~~~~~~~~~~~

.. sourcecode:: robotframework

   *** Settings ***
   Documentation     An example resource file
   Library           Selenium2Library
   Resource          ${RESOURCES}/common.robot

   *** Variables ***
   ${HOST}           localhost:7272
   ${LOGIN URL}      http://${HOST}/
   ${WELCOME URL}    http://${HOST}/welcome.html
   ${BROWSER}        Firefox

   *** Keywords ***
   Open Login Page
       [Documentation]    Opens browser to login page
       Open Browser    ${LOGIN URL}    ${BROWSER}
       Title Should Be    Login Page

   Input Name
       [Arguments]    ${name}
       Input Text    username_field    ${name}

   Input Password
       [Arguments]    ${password}
       Input Text    password_field    ${password}

.. _Variable files:

変数ファイル
--------------

変数ファイルには、テストデータで使う :ref:`変数 <variables>` を定義できます。
変数は変数テーブルで定義したり、コマンドライン上で指定したりできますが、変数ファイルを使うと、値を動的に生成したり、値を文字列以外の任意のオブジェクトにしたりできます。

変数ファイルは、通常は Python のモジュールとして定義します。
変数の定義方法には、以下の二種類があります:

:ref:`変数を直接定義する <Creating variables directly>`
   変数をモジュールの属性として定義します。
   書き方は単純で、プログラミングらしい作業は必要ありません。
   例えば、 `MY_VAR = 'my value'` と書くと、指定したテキストで、変数 `${MY_VAR}` を生成します。

:ref:`特別な関数で変数を得る <Getting variables from a special function>`
   変数を `get_variables` (または `getVariables`) という特別な名前のメソッドで生成します。
   このメソッドは、変数の値を辞書で返します。
   メソッドには引数を渡せるので、このアプローチはとてもフレキシブルです。

その他にも、変数ファイルを :ref:`Python や Java のクラス <Implementing variable file as Python or Java class>` で定義する方法があります。
クラスのインスタンスはフレームワークが生成します。
この方法では、変数をクラスインスタンスの属性として定義したり、特殊なメソッドから取り出したりできます。

.. _Taking variable files into use:

変数ファイルを使う
~~~~~~~~~~~~~~~~~~~~

.. _Setting table:

設定テーブル
'''''''''''''

テストデータに関するファイル全てが、設定テーブルの :setting:`Variables` 設定を使って変数ファイルを取り込めます。
取り込み方は :setting:`Resource` を使って :ref:`リソースファイルを取り込む <Taking resource files into use>` ときと同じです。
リソースファイルと同様、取り込む変数ファイルは、まず、取り込む側のファイルのあるディレクトリからの相対で探し、なければ、 :ref:`モジュールサーチパス <module search path>` から探します。
パスに変数を含めることもでき、パス区切りのスラッシュは Windows ではバックスラッシュに変換されます。
:ref:`引数ファイルが引数をとり <Getting variables from a special function>`, 引数に応じて変数が動的に生成される形になっている場合、引数はパスの後ろのセルに配置します。この引数には、変数を指定できます。


.. sourcecode:: robotframework

   *** Settings ***
   Variables    myvariables.py
   Variables    ../data/variables.py
   Variables    ${RESOURCES}/common.py
   Variables    taking_arguments.py    arg1    ${ARG2}

変数ファイルをインポートすると、その変数ファイル由来の変数は、全てインポート側の、テストデータファイルで利用できます。
複数の変数ファイルをインポートしたときに、同じ名前の変数が存在すると、最初にインポートしたファイルの変数定義が使われます。
さらに、インポート側のテストデータファイルの変数テーブル上で定義したり、コマンドラインで指定した変数値は、常に変数ファイル由来の変数値を上書きします。

.. Command line:
   
コマンドライン
''''''''''''''''

もう一つ、変数ファイルを使う方法として、 :option:`--variablefile` を使う方法があります。
オプションに指定したパスの変数ファイルが参照され、引数があるときにはコロン (`:`) でつないで指定します::

   --variablefile myvariables.py
   --variablefile path/variables.py
   --variablefile /absolute/path/common.py
   --variablefile taking_arguments.py:arg1:arg2

Robot 2.8.2 からは、コマンドラインで指定したファイルを探すときにも :ref:`モジュールサーチパス <module search path>` を使うようになりました。

変数ファイルを Windows の絶対パスとして指定する際、ドライブ文字とパスの間のコロンは、変数ファイルの引数とはみなしません::

   --variablefile C:\path\variables.py

Robot Framework 2.8.7 からは、引数の区切り文字にセミコロン (`;`)を使えるようになりました。
この機能は、引数自体にセミコロンが含まれる場合に便利ですが、UNIX系の OS では、値をクオートで囲ってやる必要があります::

   --variablefile "myvariables.py;argument:with:colons"
   --variablefile C:\path\variables.py;D:\data.xls

:option:`--variablefile` コマンドラインで指定した変数ファイル中の変数は、全てのテストデータ中で利用可能になります。これは、 :option:`--variable` で個別の変数を指定していったときと同じような挙動です。
:option:`--variablefile` と :option:`--variable` を同時に利用し、同名の変数が定義されていた場合は、 :option:`--variable` オプションの設定値が優先します。

.. _Creating variables directly:

変数を直接生成する
~~~~~~~~~~~~~~~~~~~~

Basic syntax
''''''''''''

When variable files are taken into use, they are imported as Python
modules and all their global attributes that do not start with an
underscore (`_`) are considered to be variables. Because variable
names are case-insensitive, both lower- and upper-case names are
possible, but in general, capital letters are recommended for global
variables and attributes.

.. sourcecode:: python

   VARIABLE = "An example string"
   ANOTHER_VARIABLE = "This is pretty easy!"
   INTEGER = 42
   STRINGS = ["one", "two", "kolme", "four"]
   NUMBERS = [1, INTEGER, 3.14]
   MAPPING = {"one": 1, "two": 2, "three": 3}

In the example above, variables `${VARIABLE}`, `${ANOTHER VARIABLE}`, and
so on, are created. The first two variables are strings, the third one is
an integer, then there are two lists, and the final value is a dictionary.
All these variables can be used as a `scalar variable`_, lists and the
dictionary also a `list variable`_ like `@{STRINGS}` (in the dictionary's case
that variable would only contain keys), and the dictionary also as a
`dictionary variable`_ like `&{MAPPING}`.

To make creating a list variable or a dictionary variable more explicit,
it is possible to prefix the variable name with `LIST__` or `DICT__`,
respectively:

.. sourcecode:: python

   from collections import OrderedDict

   LIST__ANIMALS = ["cat", "dog"]
   DICT__FINNISH = OrderedDict([("cat", "kissa"), ("dog", "koira")])

These prefixes will not be part of the final variable name, but they cause
Robot Framework to validate that the value actually is list-like or
dictionary-like. With dictionaries the actual stored value is also turned
into a special dictionary that is used also when `creating dictionary
variables`_ in the Variable table. Values of these dictionaries are accessible
as attributes like `${FINNISH.cat}`. These dictionaries are also ordered, but
preserving the source order requires also the original dictionary to be
ordered.

The variables in both the examples above could be created also using the
Variable table below.

.. sourcecode:: robotframework

   *** Variables ***
   ${VARIABLE}            An example string
   ${ANOTHER VARIABLE}    This is pretty easy!
   ${INTEGER}             ${42}
   @{STRINGS}             one          two           kolme         four
   @{NUMBERS}             ${1}         ${INTEGER}    ${3.14}
   &{MAPPING}             one=${1}     two=${2}      three=${3}
   @{ANIMALS}             cat          dog
   &{FINNISH}             cat=kissa    dog=koira

.. note:: Variables are not replaced in strings got from variable files.
          For example, `VAR = "an ${example}"` would create
          variable `${VAR}` with a literal string value
          `an ${example}` regardless would variable `${example}`
          exist or not.

Using objects as values
'''''''''''''''''''''''

Variables in variable files are not limited to having only strings or
other base types as values like variable tables. Instead, their
variables can contain any objects. In the example below, the variable
`${MAPPING}` contains a Java Hashtable with two values (this
example works only when running tests on Jython).

.. sourcecode:: python

    from java.util import Hashtable

    MAPPING = Hashtable()
    MAPPING.put("one", 1)
    MAPPING.put("two", 2)

The second example creates `${MAPPING}` as a Python dictionary
and also has two variables created from a custom object implemented in
the same file.

.. sourcecode:: python

    MAPPING = {'one': 1, 'two': 2}

    class MyObject:
        def __init__(self, name):
            self.name = name

    OBJ1 = MyObject('John')
    OBJ2 = MyObject('Jane')

Creating variables dynamically
''''''''''''''''''''''''''''''

Because variable files are created using a real programming language,
they can have dynamic logic for setting variables.

.. sourcecode:: python

   import os
   import random
   import time

   USER = os.getlogin()                # current login name
   RANDOM_INT = random.randint(0, 10)  # random integer in range [0,10]
   CURRENT_TIME = time.asctime()       # timestamp like 'Thu Apr  6 12:45:21 2006'
   if time.localtime()[3] > 12:
       AFTERNOON = True
   else:
       AFTERNOON = False

The example above uses standard Python libraries to set different
variables, but you can use your own code to construct the values. The
example below illustrates the concept, but similarly, your code could
read the data from a database, from an external file or even ask it from
the user.

.. sourcecode:: python

    import math

    def get_area(diameter):
        radius = diameter / 2
        area = math.pi * radius * radius
        return area

    AREA1 = get_area(1)
    AREA2 = get_area(2)

Selecting which variables to include
''''''''''''''''''''''''''''''''''''

When Robot Framework processes variable files, all their attributes
that do not start with an underscore are expected to be
variables. This means that even functions or classes created in the
variable file or imported from elsewhere are considered variables. For
example, the last example would contain the variables `${math}`
and `${get_area}` in addition to `${AREA1}` and
`${AREA2}`.

Normally the extra variables do not cause problems, but they
could override some other variables and cause hard-to-debug
errors. One possibility to ignore other attributes is prefixing them
with an underscore:

.. sourcecode:: python

    import math as _math

    def _get_area(diameter):
        radius = diameter / 2.0
        area = _math.pi * radius * radius
        return area

    AREA1 = _get_area(1)
    AREA2 = _get_area(2)

If there is a large number of other attributes, instead of prefixing
them all, it is often easier to use a special attribute
`__all__` and give it a list of attribute names to be processed
as variables.

.. sourcecode:: python

    import math

    __all__ = ['AREA1', 'AREA2']

    def get_area(diameter):
        radius = diameter / 2.0
        area = math.pi * radius * radius
        return area

    AREA1 = get_area(1)
    AREA2 = get_area(2)

.. Note:: The `__all__` attribute is also, and originally, used
          by Python to decide which attributes to import
          when using the syntax `from modulename import *`.

Getting variables from a special function
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

An alternative approach for getting variables is having a special
`get_variables` function (also camelCase syntax
`getVariables` is possible) in a variable file. If such a function
exists, Robot Framework calls it and expects to receive variables as
a Python dictionary or a Java `Map` with variable names as keys
and variable values as values. Created variables can be used as scalars,
lists, and dictionaries exactly like when `creating variables directly`_,
and it is possible to use `LIST__` and `DICT__` prefixes to make creating
list and dictionary variables more explicit. The example below is functionally
identical to the first `creating variables directly`_ example.

.. sourcecode:: python

    def get_variables():
        variables = {"VARIABLE ": "An example string",
                     "ANOTHER VARIABLE": "This is pretty easy!",
                     "INTEGER": 42,
                     "STRINGS": ["one", "two", "kolme", "four"],
                     "NUMBERS": [1, 42, 3.14],
                     "MAPPING": {"one": 1, "two": 2, "three": 3}}
        return variables

`get_variables` can also take arguments, which facilitates changing
what variables actually are created. Arguments to the function are set just
as any other arguments for a Python function. When `taking variable files
into use`_ in the test data, arguments are specified in cells after the path
to the variable file, and in the command line they are separated from the
path with a colon or a semicolon.

The dummy example below shows how to use arguments with variable files. In a
more realistic example, the argument could be a path to an external text file
or database where to read variables from.

.. sourcecode:: python

    variables1 = {'scalar': 'Scalar variable',
                  'LIST__list': ['List','variable']}
    variables2 = {'scalar' : 'Some other value',
                  'LIST__list': ['Some','other','value'],
                  'extra': 'variables1 does not have this at all'}

    def get_variables(arg):
        if arg == 'one':
            return variables1
        else:
            return variables2

Implementing variable file as Python or Java class
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Starting from Robot Framework 2.7, it is possible to implement variables files
as Python or Java classes.

Implementation
''''''''''''''

Because variable files are always imported using a file system path, creating
them as classes has some restrictions:

  - Python classes must have the same name as the module they are located.
  - Java classes must live in the default package.
  - Paths to Java classes must end with either :file:`.java` or :file:`.class`.
    The class file must exists in both cases.

Regardless the implementation language, the framework will create an instance
of the class using no arguments and variables will be gotten from the instance.
Similarly as with modules, variables can be defined as attributes directly
in the instance or gotten from a special `get_variables`
(or `getVariables`) method.

When variables are defined directly in an instance, all attributes containing
callable values are ignored to avoid creating variables from possible methods
the instance has. If you would actually need callable variables, you need
to use other approaches to create variable files.

Examples
''''''''

The first examples create variables from attributes using both Python and Java.
Both of them create variables `${VARIABLE}` and `@{LIST}` from class
attributes and `${ANOTHER VARIABLE}` from an instance attribute.

.. sourcecode:: python

    class StaticPythonExample(object):
        variable = 'value'
        LIST__list = [1, 2, 3]
        _not_variable = 'starts with an underscore'

        def __init__(self):
            self.another_variable = 'another value'

.. sourcecode:: java

    public class StaticJavaExample {
        public static String variable = "value";
        public static String[] LIST__list = {1, 2, 3};
        private String notVariable = "is private";
        public String anotherVariable;

        public StaticJavaExample() {
            anotherVariable = "another value";
        }
    }

The second examples utilizes dynamic approach for getting variables. Both of
them create only one variable `${DYNAMIC VARIABLE}`.

.. sourcecode:: python

    class DynamicPythonExample(object):

        def get_variables(self, *args):
            return {'dynamic variable': ' '.join(args)}

.. sourcecode:: java

    import java.util.Map;
    import java.util.HashMap;

    public class DynamicJavaExample {

        public Map<String, String> getVariables(String arg1, String arg2) {
            HashMap<String, String> variables = new HashMap<String, String>();
            variables.put("dynamic variable", arg1 + " " + arg2);
            return variables;
        }
    }

Variable file as YAML
~~~~~~~~~~~~~~~~~~~~~

Variable files can also be implemented as `YAML <http://yaml.org>`_ files.
YAML is a data serialization language with a simple and human-friendly syntax.
The following example demonstrates a simple YAML file:

.. sourcecode:: yaml

    string:   Hello, world!
    integer:  42
    list:
      - one
      - two
    dict:
      one: yksi
      two: kaksi
      with spaces: kolme

.. note:: Using YAML files with Robot Framework requires `PyYAML
          <http://pyyaml.org>`_ module to be installed. If you have
          pip_ installed, you can install it simply by running
          `pip install pyyaml`.

          YAML support is new in Robot Framework 2.9. Starting from
          version 2.9.2, the `standalone JAR distribution`_ has
          PyYAML included by default.

YAML variable files can be used exactly like normal variable files
from the command line using :option:`--variablefile` option, in the settings
table using :setting:`Variables` setting, and dynamically using the
:name:`Import Variables` keyword. The only thing to remember is that paths to
YAML files must always end with :file:`.yaml` extension.

If the above YAML file is imported, it will create exactly the same
variables as the following variable table:

.. sourcecode:: robotframework

   *** Variables ***
   ${STRING}     Hello, world!
   ${INTEGER}    ${42}
   @{LIST}       one         two
   &{DICT}       one=yksi    two=kaksi

YAML files used as variable files must always be mappings in the top level.
As the above example demonstrates, keys and values in the mapping become
variable names and values, respectively. Variable values can be any data
types supported by YAML syntax. If names or values contain non-ASCII
characters, YAML variables files must be UTF-8 encoded.

Mappings used as values are automatically converted to special dictionaries
that are used also when `creating dictionary variables`_ in the variable table.
Most importantly, values of these dictionaries are accessible as attributes
like `${DICT.one}`, assuming their names are valid as Python attribute names.
If the name contains spaces or is otherwise not a valid attribute name, it is
always possible to access dictionary values using syntax like
`&{DICT}[with spaces]` syntax. The created dictionaries are also ordered, but
unfortunately the original source order of in the YAML file is not preserved.
