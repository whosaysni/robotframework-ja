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

変数ファイルを使った場合、ファイルは Python モジュールとして import され、アンダースコア (`_`) で始まる名前を除く、全てのグローバルアトリビュートが変数とみなされます。
変数名は大小文字を区別しないので、変数名は大文字でも小文字でもかまいません。
ただし、一般的には、グローバルな変数やアトリビュートには大文字を勧めます。

.. sourcecode:: python

   VARIABLE = "An example string"
   ANOTHER_VARIABLE = "This is pretty easy!"
   INTEGER = 42
   STRINGS = ["one", "two", "kolme", "four"]
   NUMBERS = [1, INTEGER, 3.14]
   MAPPING = {"one": 1, "two": 2, "three": 3}

上の例では、 `${VARIABLE}`, `${ANOTHER VARIABLE}` といった変数ができます。
上の例の最初の二つは文字列、三つ目は整数、そして二つリストが続き、最後は辞書です。
定義した変数は、全て :ref:`スカラ変数 <scalar variable>` として扱えるほか、リストや辞書は、
`@{STRINGS}` のような :ref:`リスト変数 <list variable>` (辞書の場合は、キーのみの入ったリスト)、辞書の場合は `&{MAPPING}` のような :ref:`辞書変数 <dictionary variable>` として扱えます。

リスト変数や辞書変数をより明示的に定義したければ、 `LIST__` や `DICT__` といったプレフィクスを変数名に付けられます:

.. sourcecode:: python

   from collections import OrderedDict

   LIST__ANIMALS = ["cat", "dog"]
   DICT__FINNISH = OrderedDict([("cat", "kissa"), ("dog", "koira")])

プレフィクスをつけた場合、プレフィクス部分は最終的な変数名に入りません。
Robot Framework は、変数が実際にリストや辞書と同様のオブジェクトであるか検証します。
辞書の場合、実際に値を保存する辞書は、変数テーブルで :ref:`辞書変数を作成 <creating dictionary variable>` したときに使われる特殊な辞書になります。
辞書中の値は、 `${FINNISH.cat}` のようなアトリビュートでアクセスできます。
辞書中の値は順序つきで管理されていますが、辞書変数中のデータの並びを、元の辞書データ中の並びと同じにしたければ、もとの辞書も順序つき辞書にせねばなりません。

上で定義した二つの変数は、以下のように変数テーブルでも生成できます。

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

.. note:: 変数ファイルから取得した文字列中に変数が書かれていても、値の置き換えは起きません。
          例えば、変数ファイルで `VAR = "an ${example}"` と定義していた場合、変数 `${example}` が定義されているかどうかに関係なく、 `${VAR}` の値は、 `an ${example}` という文字列リテラルのままです。

.. _Using objects as values:

オブジェクトを値として使う
''''''''''''''''''''''''''''

変数テーブルで定義する変数の値の型は、文字列やその他の基本型ですが、変数ファイル中で定義される変数の値の型はそれにとどまりません。
変数ファイルの変数には、任意のオブジェクトを定義できます。下の例では、変数 `${MAPPING}` に Java のハッシュテーブルが入っていて、二つの値が定義されています (このテストは Jython でしか動きません)。

.. sourcecode:: python

    from java.util import Hashtable

    MAPPING = Hashtable()
    MAPPING.put("one", 1)
    MAPPING.put("two", 2)

二つ目の例では、 `${MAPPING}` を Python の辞書にして、加えて二つの変数を用意し、それらの値を、同じファイルで定義したカスタムオブジェクトにしています。

.. sourcecode:: python

    MAPPING = {'one': 1, 'two': 2}

    class MyObject:
        def __init__(self, name):
            self.name = name

    OBJ1 = MyObject('John')
    OBJ2 = MyObject('Jane')

.. _Creating variables dynamically:

値を動的に生成する
'''''''''''''''''''

変数ファイルは実際のプログラミング言語で書かれるので、動的なロジックを使って変数を設定できます。

.. sourcecode:: python

   import os
   import random
   import time

   USER = os.getlogin()                # 現在のログイン名
   RANDOM_INT = random.randint(0, 10)  # [0,10] の間の乱数
   CURRENT_TIME = time.asctime()       # 'Thu Apr  6 12:45:21 2006' 形式の現在時刻
   if time.localtime()[3] > 12:
       AFTERNOON = True
   else:
       AFTERNOON = False

上の例では、Python の標準ライブラリを使って色々な変数を設定していますが、実際は、自分のコードでいかようにでも値を作れます。
以下の例で、そのコンセプトを例示していますが、他にも、データベースから値を呼んだり、外部ファイルを参照したり、ユーザに入力させたりできます。

.. sourcecode:: python

    import math

    def get_area(diameter):
        radius = diameter / 2
        area = math.pi * radius * radius
        return area

    AREA1 = get_area(1)
    AREA2 = get_area(2)

.. _Selecting which variables to include:

どの値を取り込ませるか選択する
''''''''''''''''''''''''''''''''''''

Robot Framework が変数ファイルを処理する際、アンダースコアで始まるアトリビュート以外は、全て変数とみなします。
そのため、変数ファイル内で定義した関数やクラス、他のモジュールからインポートした名前は、全て変数扱いになってしまいます。
例えば、前節の例だと、 `${AREA1}` や `${AREA2}` の他に、 `${math}` や `${get_area}` が変数になってしまいます。

こうした変数が問題になることは、通常はありません。ただ、他の変数を上書きしてしまい、デバッグの難しいエラーを引き起こさないともかぎりません。
変数として取り込ませない方法の一つは、名前をアンダースコアから始めることです:

.. sourcecode:: python

    import math as _math

    def _get_area(diameter):
        radius = diameter / 2.0
        area = _math.pi * radius * radius
        return area

    AREA1 = _get_area(1)
    AREA2 = _get_area(2)

不要なアトリビュートが沢山あるときは、一つ一つにアンダースコアを付けて回る代わりに、特殊なアトリビュート `__all__` を使うほうが簡単です。
`__all__` には、変数として扱いたいアトリビュートの名前を列挙します。

.. sourcecode:: python

    import math

    __all__ = ['AREA1', 'AREA2']

    def get_area(diameter):
        radius = diameter / 2.0
        area = math.pi * radius * radius
        return area

    AREA1 = get_area(1)
    AREA2 = get_area(2)

.. Note:: `__all__` アトリビュートは、元々は、 Python で `from modulename import *` としたときに import されるアトリビュートを決めるための書き方でもあります。

.. Getting variables from a special function:

特殊な関数に変数を生成させる
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

変数を生成するもう一つの方法として、 `get_variables`  (キャメルケースの `getVariables` でも可) という名前の関数を定義する方法があります。
この名前の関数があると、 Robot Framework は関数を呼び出し、戻り値を、 Python の辞書または Java の `Map` として受け取り、そのキーと値をそれぞれ変数名と変数値とします。
変数の値は、 :ref:`直接定義した場合 <creating variables directly>` と同様、スカラー、リスト、辞書にでき、 `LIST__` や `DICT__` プレフィクスを使って、リストや辞書型の変数を明示できます。
下の例は、 :ref:`直接定義した場合 <creating variables directly>` の例と機能的に同じです。

.. sourcecode:: python

    def get_variables():
        variables = {"VARIABLE ": "An example string",
                     "ANOTHER VARIABLE": "This is pretty easy!",
                     "INTEGER": 42,
                     "STRINGS": ["one", "two", "kolme", "four"],
                     "NUMBERS": [1, 42, 3.14],
                     "MAPPING": {"one": 1, "two": 2, "three": 3}}
        return variables

`get_variables` には引数を渡せて、引数に応じて生成される変数を変えられます。
関数の引数は、Pythonの関数に引数を渡すときと同じように指定します。
テストデータで :ref:`変数ファイルを使う <taking variable files into use>` 際、引数を変数ファイル名の後のセルに指定できます。
また、コマンドラインでも、変数ファイルのパスの後に、コロンやセミコロンで区切って変数を渡せます。

以下のダミーのサンプルは、引数付きの変数ファイルの例です。
より現実的な例だと、引数は外部のテキストファイルへのパスだったり、値を参照する先のデータベースを示していたりするでしょう。

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

.. Implementing variable file as Python or Java class:

変数ファイルを Python や Java のクラスとして実装する
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Robot Framework 2.7 からは、変数ファイルを Python や Java のクラスで定義できます。

.. Implementation:

実装方法
''''''''''

変数ファイルはファイルシステム上のパスを指定して import されるので、クラスで実装するときには、以下のような制約があります:

  - クラスの名前は、クラスの置かれたモジュールと同じ名前にせねばなりません。
  - Java のクラスは、デフォルトパッケージ内に入っていなければなりません。
  - Java のクラスは、 :file:`.java` または :file:`.class` で終わるファイル名にせねばならず、いずれのケースでも、クラスファイルは必ず必要です。

どの言語で実装した場合でも、フレームワークはクラスのインスタンスを引数なしで生成し、そのインスタンスから変数を得ます。
モジュールのときと同様、変数は直接インスタンスのアトリビュートとして定義したり、 `get_variables`
(や、 `getVariables`) といった特殊メソッドで定義したりできます。

変数をインスタンスのアトリビュートとして直接定義した場合、インスタンスのメソッドが何でもかんでも変数として生成されてしまわないように、呼び出し可能なアトリビュートは除外されます。
呼び出し可能オブジェクトの変数が明に必要な場合は、変数ファイルを別のやり方で定義してください。

.. Examples:

例
'''''

最初の例では、 Python や Java を使って変数を生成しています。
いずれも、クラスのアトリビュートから `${VARIABLE}` と `@{LIST}` を、インスタンスアトリビュートから `${ANOTHER VARIABLE}` を生成しています。

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

次の例では、動的に変数を生成する機能を使っています。
いずれの言語も、 `${DYNAMIC VARIABLE}` という変数を生成しています。

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

.. _Variable file as YAML:

YAML 形式の変数ファイル
~~~~~~~~~~~~~~~~~~~~~~~~~~

変数ファイルは `YAML <http://yaml.org>`_ 形式でも書けます。
YAML はデータを永続化するための記述言語で、簡単で人間の理解しやすい構文を備えています。
以下の例は、簡単な YAML ファイルの使い方です:

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

.. note:: Robot Framework で YAML を扱うには、 `PyYAML <http://pyyaml.org>`_ モジュールが必要です。
          pip_ をインストールしているなら、 `pip install pyyaml` でインストールできます。

          YAML のサポートは Robot Framework 2.9 からです。
          version 2.9.2 からは、 :ref:`スタンドアロン JAR <standalone JAR distribution>` にデフォルトで PyYAML が入っています。

YAML の変数ファイルの扱い方は通常の変数ファイルと同じで、 :option:`--variablefile`  オプションや、設定ファイルの  :setting:`Variables`, :name:`Import Variables` キーワードで使えます。
ただし、YAML ファイルのパスは、拡張子  :file:`.yaml` にせねばなりません。

上の YAML ファイルを取り込んだ場合、以下の変数テーブルで生成するのと同じ変数が生成されます:

.. sourcecode:: robotframework

   *** Variables ***
   ${STRING}     Hello, world!
   ${INTEGER}    ${42}
   @{LIST}       one         two
   &{DICT}       one=yksi    two=kaksi

変数の定義に使う YAML ファイルは、必ずトップレベルがマップの定義でなければなりません。
上の例で示したように、マップのキーと値が、それぞれ変数の名前と値になります。
変数の値は、 YAML がサポートする型ならなんでも構いません。
名前や値に非ASCII文字を入れたければ、 YAML ファイルを UTF-8 でエンコードせねばなりません。

値がマップのときは、自動的に、変数テーブルで :ref:`辞書変数を作成 <creating dictionary variable>` したときに使われる特殊な辞書になります。
ここで大事なのは、辞書の値は、あたかも Python のアトリビュート名のように、 `${DICT.one}` のようなアトリビュートとしてアクセスできるということです。
名前にスペースが入っていたり、Python のアトリビュート名として正しくない名前を使った場合には、辞書の値には `&{DICT}[with spaces]` のような記法でしかアクセスできません。
生成された辞書は順序つき辞書にはなっていますが、残念ながら YAML ファイル中の記述順序は保存されません。
