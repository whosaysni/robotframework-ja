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

上で考察したように、リストの保存されている変数は、 :ref:`リスト変数<list variable>` として使うことで、キーワードに引数を渡せます。
同様に、 Python の辞書や、辞書ライクなオブジェクトを保存した変数は、 `&{EXAMPLE}` の形式で辞書変数として使えます。
そして、この辞書の各値は、キーワードの :ref:`名前付き引数 <named arguments>` として渡せます。
例えば、変数 `&{USER}` の値が `{'name': 'robot', 'password': 'secret'}` のとき、以下の二つの例は同じ結果になります:

.. sourcecode:: robotframework

   *** Test Cases ***
   Constants
       Login    name=robot    password=secret

   Dict Variable
       Login    &{USER}

辞書変数は  Robot Framework 2.9 で登場しました。


.. Using dictionary variables with other data

辞書変数を他のデータと組み合わせる
''''''''''''''''''''''''''''''''''''

辞書変数は、他の引数と組み合わせて使えます。辞書同士の組み合わせも可能です。
仕様上、 :ref:`名前付き引数の記法<named argument syntax>` は、位置固定の引数を名前付き引数の前に持ってこなければならないので、辞書変数の後ろには、名前付き引数か、別の辞書変数しか指定できません。

.. sourcecode:: robotframework

   *** Test Cases ***
   Example
       Keyword    &{DICT}    named=arg
       Keyword    positional    @{LIST}    &{DICT}
       Keyword    &{DICT}    &{ANOTHER}    &{ONE MORE}


一つのセル中に、他のデータ(文字列や他の変数)と一緒に辞書変数を使った場合、その値は、変数値を文字列に変換して結合した結果になります。
結果的に、一つのセルに、他のデータと一緒にスカラ変数として指定したときと同じ値になります。

.. Accessing individual dictionary items

辞書変数の個々の要素にアクセスする
'''''''''''''''''''''''''''''''''''''

辞書中の値は、参照したい値のキーを `key` としたとき、 `&{NAME}[key]` の形式で参照できます。
キーは原則文字列ですが、変数を使えば、文字列でない値もキーにできます。
`&{NAME}[key]` の形式でアクセスした値は、スカラ変数として扱えます。

キーが文字列のとき、 `${NAME.key}` というアトリビュート的な記法でも、辞書の要素にアクセスできます。
この記法については、 :ref:`辞書変数の構築 <Creating dictionary variables>` の節を参照してください。

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

.. Using dictionary variables with settings

辞書変数を設定で使う
''''''''''''''''''''''

通常、設定には辞書変数を使えません。
例外はライブラリインポートとセットアップ・ティアダウンの引数に辞書を使う時です。

.. sourcecode:: robotframework

   *** Settings ***
   Library        ExampleLibrary    &{LIB ARGS}
   Suite Setup    Some Keyword      &{KW ARGS}     named=arg

.. _environment variable:

環境変数
~~~~~~~~~~

Robot Framework では、 `%{ENV_VAR_NAME}` という記法で、テストデータの中で環境変数を参照できます。
参照できる値は文字列に限られます。

環境変数は、テストの実行が可能になる前に、OS 側でセットされた値です。
また、実行時に、 :ref:`OperatingSystem` ライブラリの :name:`Set Environment Variable` キーワードで新たに追加したり、 :name:`Delete Environment Variable` で削除したりできます。
環境変数はグローバルな値なので、あるテストケースで環境変数をセットすると、他のテストケースでもその値を使うようになります。
ただし、テスト中に環境変数を変更しても、その影響がテスト後まで残ることはありません。

.. sourcecode:: robotframework

   *** Test Cases ***
   Env Variables
       Log    Current user: %{USER}
       Run    %{JAVA_HOME}${/}javac

.. Java system properties

Java のシステムプロパティ
~~~~~~~~~~~~~~~~~~~~~~~~~~~

テストを Jython で実行している場合、 :ref:`環境変数<environment variables>` と同じ記法で
`Java のシステムプロパティ`__ にアクセスできます。
同じ名前の環境変数とシステムプロパティが存在する場合、環境変数の値が使われます。

.. sourcecode:: robotframework

   *** Test Cases ***
   System Properties
       Log    %{user.name} running tests on %{os.name}

__ http://docs.oracle.com/javase/tutorial/essential/environment/sysprop.html

.. Creating variables

変数を定義する
------------------

変数は、様々な方法でつくられます。

.. Variable table

変数テーブル
~~~~~~~~~~~~~~

よく使うのは、 :ref:`テストケースファイル <test case files>` や :ref:`リソースファイル<resource files>` の変数テーブルを使う方法です。
変数テーブルの便利なところは、変数を、同じ場所に、テストデータと分けて定義でき、書き方も単純なところです。
一方、短所は、変数の値が文字列になってしまうこと、動的に生成できないことです。
これらの問題を解決したいときは、 :ref:`変数ファイル<variable files>` を使います。

.. Creating scalar variables

スカラ変数の定義
''''''''''''''''''

変数の代入定義で最も簡単なのは、文字列をスカラ変数に代入するというものです。
この代入文の書き方は、まず変数名を (`${}` つきで) 最初のセルに書き、第二セルに値を書きます。
第二セルが空なら、値は空文字になります。
値には、別の定義済みの変数も指定できます。

.. sourcecode:: robotframework

   *** Variables ***
   ${NAME}         Robot Framework
   ${VERSION}      2.0
   ${ROBOT}        ${NAME} ${VERSION}

あまりお勧めではありませんが、変数名の直後に `=` を付けて、変数の代入であることをちょっぴり明確にできます。

.. sourcecode:: robotframework

   *** Variables ***
   ${NAME} =       Robot Framework
   ${VERSION} =    2.0

スカラ変数の値が長すぎて記述しづらいときは、複数のカラムや :ref:`行に分けて<Dividing test data to several rows>` 書けます。
デフォルトの設定では、各セルの値の結合にはスペースを使いますが、最初のセルに `SEPARATOR=<sep>` を付ければ、セルを結合する文字を変えられます。

.. sourcecode:: robotframework

   *** Variables ***
   ${EXAMPLE}      This value is joined    together with a space
   ${MULTILINE}    SEPARATOR=\n    First line
   ...             Second line     Third line

このように長い文字列を結合できるのは Robot Framework 2.9 からです。
Robot Framework 2.8 では、スカラ変数に複数回値を入れようとするとエラーになり、それ以前のバージョンでは、リストの値が入った変数が生成されていました。


.. Creating list variables

リスト変数の定義
''''''''''''''''''

リスト変数の作成も、スカラ変数と同じくらい簡単です。
変数名は変数テーブルの最初のカラムに指定し、変数の値を以降のカラムに指定します。
リスト変数には、ゼロ個の場合も含め、任意の数の要素を入れられます。
たくさんの値を入れる必要があるときは、 :ref:`複数の行に分割 <Dividing test data to several rows>` できます。

.. sourcecode:: robotframework

   *** Variables ***
   @{NAMES}        Matti       Teppo
   @{NAMES2}       @{NAMES}    Seppo
   @{NOTHING}
   @{MANY}         one         two      three      four
   ...             five        six      seven

.. Creating dictionary variables
   
辞書変数の定義
''''''''''''''''

辞書変数は、リスト変数の定義に似た方法で定義します。
違いは、値の各要素を、 `name=value`  の記法で書くか、または既存の辞書変数で定義するという点です。
同じ名前の複数の要素を定義すると、最後に定義した値が優先します。
キーの中にリテラルの等号を入れたいときは、  `\=` のようにバックスラッシュで :ref:`エスケープ<escaping>` します。

.. sourcecode:: robotframework

   *** Variables ***
   &{USER 1}       name=Matti    address=xxx         phone=123
   &{USER 2}       name=Teppo    address=yyy         phone=456
   &{MANY}         first=1       second=${2}         ${3}=third
   &{EVEN MORE}    &{MANY}       first=override      empty=
   ...             =empty        key\=here=value

Python の辞書型と比べて、辞書変数は二つの点で拡張されています。
まず、辞書の値にアトリビュートとしてアクセスできます。
つまり、 `${VAR.key}` のような、 :ref:`拡張変数記法<extended variable syntax>` が使えます。
この記法は、キーがアトリビュート名として使える名前であって、かつ、 Python の辞書オブジェクトのアトリビュート名と被らないときにだけ使えます。例えば、 `&{USER}[name]` は `${USER.name}` でアクセス可能 (この記法では `$` が必要なことに注意) ですが、 `${MANY.3}` は使えません。

辞書変数のもう一つの特徴は、要素が順序つきで管理されているということです。
つまり、辞書の要素を順次取り出したとき、その並びは常に定義したときと同じ順になるということです。
この振る舞いは、辞書を :ref:`forループ<for loops>` で :ref:`リスト変数<list valiables>` として使った場合などに便利です。
辞書をリスト変数として使うと、その値には辞書のキーが入ります。
例えば、上の例だと、 `@{MANY}` は `['first', 'second', 3]` という値になります。

.. Variable file

変数ファイル
~~~~~~~~~~~~~

変数ファイルは変数生成の最も強力なメカニズムで、様々な種類の変数を生成できます。
変数ファイルを使えば、任意のオブジェクトを値に持つ変数を作成でき、かつ、動的に変数を生成できます。
変数ファイルの書き方とその使い方は、 :ref:`リソースファイルと変数ファイル<Resource and variable files>` で解説しています。

.. Setting variables in command line
   
コマンドラインから変数を設定する
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
