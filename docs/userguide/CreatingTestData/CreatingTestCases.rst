.. _test case:
.. _test cases:
.. _Creating test cases:

テストケースの作成
===================

この節では、テストケースの書き方を説明します。
:ref:`テストケースファイル <test case files>` と :ref:`テストケースディレクトリ<test suite directories>` を使った :ref:`テストスイート <test suite>` の作り方は、この節の次の節で説明します。

.. contents::
   :depth: 2
   :local:

.. Test case syntax:

テストケースの構文
--------------------

.. Basic syntax:

基本の構文
~~~~~~~~~~~~

テストケースは、キーワードを組み合わせたテーブル（表）として作成します。
ここでいう「テーブル」とは、「テキストをスペースやタブ、パイプ (``|``) で区切って、行と列の構造にしたもの」です。
区切られた各列を「カラム」と呼び、行の頭から区切りごとに 1 カラム目、2カラム目、...と数えていきます。
::

      *** Test Cases ***        # ヘッダ

      テストケース名1
          キーワード1   引数1   引数2   ...
          キーワード2   引数1   ...
          ...

      テストケース名2
          ...

「キーワード」は、テスト中のひとつひとつの操作の命令で、 :ref:`テストライブラリ <test libraries>` や :ref:`リソースファイル <resource files>` からインポートしたり、テストケースファイル中の :ref:`キーワードテーブル <keyword table>` で作成したりできます。

テストケーステーブルの最初のカラムにはテストケース名を入れます。
この行から、次のテストケース名の行の前まで、もしくは、テストケーステーブルの末尾に到達するまでが、ひとつのテストケースです。

テストケーステーブルの冒頭には ``*** test cases ***`` のようなヘッダが必要です。ヘッダから最初のテストケースまでの間にテストケース以外の内容を記述すると、エラーになります。

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

テストケースの2列目は、たいていはキーワード名が入っています。
例外は、2行目で :ref:`キーワードの戻り値を変数に代入 <User keyword return values>` しているような場合で、その場合は二つめのカラムに変数名が入り、その後にキーワードが続きます。
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

テストケースに設定を書く
~~~~~~~~~~~~~~~~~~~~~~~~~~

テストケースには、ケースごとの設定（テスト設定）を持たせられます。
テスト設定名は必ず2カラム目に書き、その後に設定の値を続けます。
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

テストケースに関する設定を設定テーブルに書く
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

設定テーブルにも、テストケース関連の設定を書けます。
主に設定できるのは、先に挙げたテストケースごとの設定で変更できる値のデフォルト値です。

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

これまでの例で、引数を取るキーワードがいくつかありましたが、この節では、この重要な機能について詳しく説明します。
引数を持つような :ref:`ユーザ定義のキーワード <user keyword arguments>` や :ref:`ライブラリのキーワード <Keyword arguments>` の書き方は、別の節で説明します。

キーワードは、引数をとらない場合も、複数取る場合もあります。
引数によっては、デフォルト値が存在する場合もあります。
キーワードがどのような引数を取るかは、キーワードの実装で決まっています。
あるキーワードがどんな引数を取るかを知りたければ、キーワードのドキュメントを調べるのがベストです。
この節の例で使われているキーワードのドキュメントは :ref:`Libdoc` ツールで生成できるはずですが、
``javadoc`` のような汎用のドキュメントツールでも、同じ情報が得られます。

.. _Mandatory arguments:

必須の引数
~~~~~~~~~~~~

ほとんどのキーワードには、常に指定しなければならない引数があります。
こうした引数は、キーワードのドキュメント中では、引数をカンマで区切った形式、例えば `first, second, third` のように表されています。
必須の引数の場合、引数名自体にはあまり意味はなく、ドキュメントで定義されているのと同じ数の引数を指定することだけが大事です。
引数が少なすぎても、多すぎてもエラーになります。

以下のテストでは、 :ref:`OperatingSystem` ライブラリの :name:`Create Directory` と :name:`Copy File` というキーワードを使っています。
それぞれの引数は `path` と `source, destination` です。
つまり、前者のキーワードは引数を一つ、後者は二つ取ります。
最後のキーワード、組み込み :ref:`BuiltIn` ライブラリの :name:`No Operation` は引数を取りません。

.. sourcecode:: robotframework

   *** Test Cases ***
   Example
       Create Directory    ${TEMPDIR}/stuff
       Copy File    ${CURDIR}/file.txt    ${TEMPDIR}/stuff
       No Operation

.. _devault values:

デフォルト値
~~~~~~~~~~~~~~

引数にデフォルト値が定義されている場合があります。
デフォルト値のある引数は、指定してもしなくてもかまいません。
キーワードのドキュメント中では、デフォルト値は引数名と等号で区切った `name=default value` の形式で表わされています。
Java で実装したキーワードには、同じキーワードで引数の異なる実装が :ref:`複数存在する <Default values with Java>` 場合があるので注意してください。
全引数にデフォルト値を持たせることはできますが、デフォルト値を持つ引数の後ろには、必須の引数は置けません。

デフォルト値の扱い方を以下の例に示します。この例では、引数の形式が `path, content=, encoding=UTF-8` であるような :name:`Create File` というキーワードを使っています。引数が3つ、うち一つが必須なので、引数が全く無い場合や、4つ以上引数がある場合は動作しません。

.. sourcecode:: robotframework

   *** Test Cases ***
   Example
       Create File    ${TEMPDIR}/empty.txt
       Create File    ${TEMPDIR}/utf-8.txt         Hyvä esimerkki
       Create File    ${TEMPDIR}/iso-8859-1.txt    Hyvä esimerkki    ISO-8859-1

.. _varargs:

可変個の引数
~~~~~~~~~~~~~~~~~

キーワードに任意の数の引数を持たせることも可能です。
可変個の引数は *varargs* と呼び、必須の引数やデフォルト値つきの引数の組み合わせて使えます。
ただし、可変個の引数は、必須の引数やデフォルト値つき引数の後に指定します。
キーワードのドキュメント中では、変数名の前にアスタリスクをつけた `*varargs` の形式で表されています。

例えば、 :ref:`OperatingSystem` ライブラリの :name:`Remove Files` や :name:`Join Paths` キーワードには、それぞれ `*paths` や `base, *parts` という引数があります。
前者は引数をいくつにもできますが、後者は少なくとも一つ引数が必要です。

.. sourcecode:: robotframework

   *** Test Cases ***
   Example
       Remove Files    ${TEMPDIR}/f1.txt    ${TEMPDIR}/f2.txt    ${TEMPDIR}/f3.txt
       @{paths} =    Join Paths    ${TEMPDIR}    f1.txt    f2.txt    f3.txt    f4.txt

.. _Named argument syntax:
.. _Named arguments:

引数の名前指定
~~~~~~~~~~~~~~~

引数の名前指定は、 :ref:`default values <デフォルト値>` つき引数をより柔軟に扱えるようにし、引数に何の値を指定したかを明示的に書ける記法です。

技術的には、引数の名前指定は、 Python の `キーワード引数 <http://docs.python.org/2/tutorial/controlflow.html#keyword-arguments>`_ と同じです。


.. Basic syntax

基本の記法
''''''''''''

キーワードの引数を指定する際、 `arg=value` のように、値の前に引数の名前を指定できます。
この書き方は、デフォルト値つきの引数が何個もあって、一部の引数だけに値を指定し、他はデフォルト値のままにしておきたいときにとても便利です。
例えば、あるキーワードが `arg1=a, arg2=b, arg3=c` のような3つのデフォルト値つき引数で呼び出せるとき、 `arg3=override` だけを指定してキーワードを呼び出すと、 `arg1` と `arg2` はデフォルト値のままで、 `arg3` だけ `override` にできます。
この挙動がよく理解できなければ、下の :ref:`名前付き引数の例 <named arguments example>` が助けになるかもしれません。

引数を名前指定するときは、名前に大小文字の区別があることと、スペースの扱いが厳密なことに注意してください。前者は、例えば `arg` という引数を名前指定子たければ、 `Arg=value` や `ARG=value` でなく `arg=value` とせねばならないということです。
後者は、 `=` 記号の前にはスペースを入れてはならず、 `=` の後ろに入っているスペースが、値の一部とみなされるということです。


:ref:`ユーザ定義のキーワード <user keywords>` 中で名前指定の引数を使う場合、引数名に `${}` を付ける必要はありません。例えば、 `${arg1}=first, ${arg2}=second` のように定義したユーザキーワードで引数値を指定するときは、 `arg2=override` のように指定します。

引数を名前指定で入力すると、その後ろに必須の引数は指定できません。例えば、 `| Keyword | arg=value | positional |` は動きません。
Robot Framework 2.8 からは、明にエラーになります。
名前指定で引数を指定する場合、引数の並びは問題になりません。

.. note:: 
   Robot Framework 2.8 以前では、デフォルト値を持たない引数は名前指定にできませんでした。

.. _Named arguments with variables:

名前指定の引数に変数を渡す
''''''''''''''''''''''''''''''

名前指定の引数は、名前と値のどちらにも :ref:`変数 <variables>` を使えます。
値が単一の :ref:`スカラ値 <scalar variable>` であれば、キーワードに「そのまま」渡されます。
つまり、この機能を使うと、文字列以外の任意のオブジェクトを、名前指定の引数に使えるのです。
例えば、 `arg=${object}` を指定してキーワードを呼ぶと、 `${object}`  の値を文字列に変換しないでキーワードに渡します。

名前指定の引数の名前に変数を使うと、引数名と値を結びつけるよりも前に、値の方を評価します。
この機能は Robot Framework 2.8.6 で登場しました。

名前指定の引数を使う場合、キーワードを呼び出すときの記述で、必ずリテラルの等号を書かねばなりません。
逆に言えば、変数単体では名前指定の引数扱いにはならないし、 `foo=bar` のような値を変数で渡したしても認識されないということです。
キーワードを他のキーワードでラップするときには特に注意してください。
例えば、 :ref:`可変個の引数 <variable number of arguments>`  を取るあるキーワードが、引数を `@{args}` に格納していて、それを別のキーワードにそのまま渡しているとします。
このキーワードを `named=arg` のように名前指定の引数で呼び出しても、 Robot Framework はこれをうまく解釈できません。
以下に例を挙げましょう。


.. sourcecode:: robotframework

   *** Test Cases ***
   Example
       Run Program    shell=True    # これは Run Process の名前指定引数にはならない

   *** Keywords ***
   Run Program
       [Arguments]    @{args}
       Run Process    program.py    @{args}    # @{args} の中の名前指定の引数が正しく解釈されない

名前指定の引数をキーワード間で受け渡ししたい場合は、 :ref:`フリーキーワード引数 <free keyword arguments>` を受け取るよう変更が必要です。
必須引数と名前指定引数の両方を受け渡しできるラッパーキーワードは :ref:`kwargs の例 <kwargs example>` を参照してください。

.. _Escaping named arguments syntax:

名前指定引数のエスケープ
'''''''''''''''''''''''''''''''

名前指定の引数は、引数中の等号 ``=`` の前の部分が、キーワードの引数のどれかに一致する場合にのみ使われます。
例えば、あるキーワードに、必須の引数として、 `foo=quux` というリテラルの値を渡したとします。
そのキーワードに `foo` という別の引数があったとします。
この場合、 `quux` は引数 `foo` に渡されてしまい、おそらく必須の引数の指定がないためにエラーとなるでしょう。

こういった、期待しないマッチが起きるレアケースのために、 `foo\=quux` のように、バックスラッシュによる :ref:`エスケープ <escaping>` が可能です。
エスケープすると、必須の引数に `foo=quux` という値が渡ります。
この例では、そもそも `foo` という引数がなければエスケープは必要ありませんでしたが、より明示的に書いておくために、常にエスケープしておくのがよいでしょう。


.. _Where named arguments are supported:

名前指定引数のサポート状況
'''''''''''''''''''''''''''''

これまでで解説したように、名前指定の引数はキーワード全般で使えます。
その他、 :ref:`ライブラリのインポート <importing libraries>` でも使えます。

名前指定の引数は、 :ref:`ユーザキーワード <user keywords>` と、ほとんどの :ref:`テストライブラリ <test libraries>` で使えます。
例外は :ref:`スタティックライブラリ API <static library API>` を使っている Java ベースのライブラリです。
:ref:`Libdoc` で生成したライブラリドキュメントには、ライブラリが名前指定の引数をサポートしているかどうかが記載されます。

.. note:: Robot Framework 2.8 以前では、 :ref:`dynamic library API` を使ったテストライブラリには名前指定の記法が使えませんでした。

名前指定引数の例
'''''''''''''''''''''''

名前指定の引数を、ライブラリキーワード、ユーザキーワード、 :ref:`Telnet` テストライブラリのインポートで使っている例を示します。

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

.. _Free keyword arguments:

フリーキーワード引数
~~~~~~~~~~~~~~~~~~~~~~

Robot Framework 2.8 から、 `Python スタイルのフリーキーワード引数 <http://docs.python.org/2/tutorial/controlflow.html#keyword-arguments>`_ (`**kwargs`)をサポートしています。
すなわち、 `name=value` の形式で指定した引数のうち、キーワードの引数定義にマッチしない引数全てを、引数 `kwargs` で受けられるようになりました。

フリーキーワード引数には、 :ref:`名前指定の引数 <Named arguments with variables>` と同じような形式で変数を指定できます。
実際のところ、引数の名前と値の両方に変数を指定できます。
ただし、エスケープ記号はリテラルとして扱われます。
例えば、 `foo=${bar}` と `${foo}=${bar}` は、使われている変数がきちんと定義されているかぎり、いずれも有効な書き方です。
もう一つの制限として、フリーキーワード引数の引数名は、常に文字列でなければなりません。
引数名に変数を使える機能は Robot Framework 2.8.6 で登場しました。
それ以前のバージョンでは、引数名を変数のような書き方で指定しても、変数として解決されません。

フリーキーワード引数は、もともと Python ベースのライブラリでしか使えませんでした。
Robot Framework 2.8.2 から、 :ref:`ダイナミックライブラリ API <dynamic library API>` のサポートが拡張され、 Robot Framework 2.8.3 からは Java ベースのライブラリと :ref:`リモートライブラリインタフェース <remote library interface>` もサポートしています。
. Finally, user keywords got __ in Robot Framework 2.9 からは、ユーザキーワードも :ref:`kwargsをサポート <Kwargs with user keywords>` しています。
つまり、今では全てのキーワードが kwargs をサポートしているのです。


.. _Kwargs examples:

kwargs の例
'''''''''''''''

kwargs の最初の例として、 :ref:`Process` ライブラリの :name:`Run Process` キーワードを見てみましょう。
このキーワードのシグネチャは `command, *arguments, **configuration` で、実行するコマンド (`command`),
:ref:`可変個の <variable number of arguments>` コマンドの引数 (`*arguments`), そして、オプションの設定パラメタをフリーキーワード引数 (`**configuration`) として取ります。
以下の例は、 :ref:`名前指定の引数に変数を使う <Named arguments with variables>` 方法が、フリーキーワード引数でも使えるという例にもなっています。

.. sourcecode:: robotframework

   *** Test Cases ***
   Using Kwargs
       Run Process    program.py    arg1    arg2    cwd=/home/user
       Run Process    program.py    argument    shell=True    env=${ENVIRON}

自作のテストライブラリで kwargs を使う際の情報は、 :ref:`テストライブラリの作成 <Creating test libraries>` の :ref:`フリーキーワード引数 <Free keyword arguments (**kwargs)>` の節を参照してください。

二つ目の例として、上の例の `program.py` を実行する :ref:`ユーザキーワード <user keyword>` のラッパを書いてみましょう。
ラッパのキーワードは :name:`Run Program` として、任意の数の引数と kwargs を受け取って、受け取った引数を :name:`Run Process` に渡しています。

.. sourcecode:: robotframework

   *** Test Cases ***
   Using Kwargs
       Run Program    arg1    arg2    cwd=/home/user
       Run Program    argument    shell=True    env=${ENVIRON}

   *** Keywords ***
   Run Program
       [Arguments]    @{arguments}    &{configuration}
       Run Process    program.py    @{arguments}    &{configuration}

.. _Arguments embedded to keyword names:

キーワード名への引数の埋め込み
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

きわめて特異な引数の指定方法として、キーワード名への変数の埋め込みがあります。
この記法は :ref:`テストライブラリ <Embedding arguments into keyword names>` と :ref:`ユーザキーワード<Embedding arguments into keyword name>` の両方でサポートしています。


.. _Failures:

テストケース失敗時の動作
---------------------------

.. _When test case fails:

テストケースが失敗するとき
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

テストケース中のキーワードのいずれかの実行に失敗すると、テストケースの実行は失敗します。
通常、テストケースが失敗すると、その実行を停止して、 :ref:`ティアダウン <test teadown>` があれば実行し、次のテストケースの実行に移ります。
テストケースの実行を停めたくない場合に、特別に :ref:`失敗時も実行を継続 <continue on failure>` させることもあります。

.. _Error messages:

エラーメッセージ
~~~~~~~~~~~~~~~~~~

失敗したテストケースに関するメッセージは、実行に失敗したキーワードから直接取っています。
大抵は、エラーメッセージはキーワード名自体ですが、その挙動は設定で変更できます。

例えば失敗時も実行を継続する場合など、テストケースが何度も失敗するような状況があります。
そうした場合には、最終的なメッセージは、個々のエラーを結合したものになります。
エラーメッセージが長すぎる場合には、 :ref:`レポート <reports>` を見やすくするために、メッセージを途中でカットします。
完全なエラーメッセージは、常に :ref:`ログ <log>` ファイル上で、失敗したキーワードごとのメッセージとして読めます。

デフォルトの設定では、エラーメッセージは素のテキストですが、 Robot Framework 2.8 からは :ref:`HTMLで書ける <HTML in error messages>` ようになりました。
エラーメッセージを `*HTML*` で始めることで、この機能を有効にできます。
`*HTML*` マーカー自体は、レポートやログ上の最終的なエラーメッセージ上では除去されます。
カスタムのメッセージを HTML で出力する例を、下の例の二つめのテストで示します。

.. sourcecode:: robotframework

   *** Test Cases ***
   Normal Error
       Fail    This is a rather boring example...

   HTML Error
       ${number} =    Get Number
       Should Be Equal    ${number}    42    *HTML* Number is not my <b>MAGIC</b> number.

.. _test case name:
.. _test case documentation:
.. _Test case name and documentation:

テストケースの名前とドキュメント
--------------------------------

個々のテストケースの名前は、テストケーステーブルのテストケース名に入力した内容そのものです。
一つのテストスイート中に、同じ名前のテストケースは一つしか作れません。
ちなみに、テスト名をテスト中で参照するために、 `${TEST_NAME}` という :ref:`自動変数 <automatic variable>` を使えます。
この変数は、テストが実行されている最中は、テストから呼び出されたユーザーキーワード中でも、テストのセットアップやティアダウン中でも、常に利用できます。

:setting:`[Documentation]` 設定を使うと、テストケースのドキュメントを書けます。
このテキストはコマンドラインでテストを実行したときの出力と、テスト結果のログやレポートに表示されます。
ドキュメントには簡単な :ref:`HTML タグ<HTML formatting>` を利用でき、 :ref:`変数 <variables>` で動的なドキュメントを生成できます。

ドキュメントを複数のカラムに分割した場合、一つの行中の各セルの内容はスペースで結合されます。
この仕様が有用なのは、テストケースの記述に :ref:`HTML フォーマット <HTML format>` を使っていて、カラム幅が狭いときです。
ドキュメントが :ref:`複数の行に分かれている <Dividing test data to several rows>` 場合には、各行のドキュメントを :ref:`改行で結合 <Newlines in test data>` します。
結合する行が改行で終わっている場合や、 :ref:`バックスラッシュでエスケープ <escaping backslash>` している場合には、改行は付加しません。

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

テストケースには、明解で意味の伝わる名前を与えることが重要で、そうであれば、原則、ドキュメントは不要です。
ドキュメントが必要なくらいテストケースのロジックが複雑だと感じたら、ドキュメントを追加する前に、テスト中のキーワードにもっと適切な名前をつけたり、キーワードを改良することを考えましょう。
そして、上の例で使ったような、ユーザ向けの情報や環境に関するメタデータは、実はドキュメントよりも :ref:`タグ <tags>` を使ったほうが適切です。

.. _tag:
.. _tags:
.. _test case tags:
.. _Tagging test cases:

.. _Tagging test cases:

テストケースにタグ付けする
----------------------------

Robot Framework のタグは、テストケースを分類する上で、単純ながらも強力なメカニズムを備えています。
タグは普通のテキストで記述でき、少なくとも以下の目的のために使えます:

- タグはテストの :ref:`レポート<reports>` や :ref:`ログ <logs>` に表示されます。もちろん、テストデータ中においてはメタデータとしての役割を果たします。
- テストケースの :ref:`成績の計算 <Configuring statistics>` に使います (自動的に、タグごとのテストのパス数・失敗数を計算します)。
- タグを使って、実行したいテストや除外したいテストを :ref:`絞り込み <By tag names>` できます。
- タグを使って、どれが :ref:`重要不可欠なテスト <critical>` なのかを指定できます。

この節では、テストケースにタグを指定する方法と、同じことを実現する別のやり方だけを解説しています。
ここで示す各アプローチは、自由に組み合わせて使えます。

設定テーブルで `Force Tags`:setting: を指定する
   この設定のあるテストケースファイル中の全てのテストケースに、指定のタグが付与されます。
   :ref:`テストスイートの初期化ファイル <test suite initialization file>` で使うと、テストスイートとサブスイート中の全てのテストケースに指定のタグが付与されます。

設定テーブルで `Default Tags`:setting: を指定する
   :setting:`[Tags]` 設定のないテストケースだけに、指定のタグを付与します。
   デフォルトタグは、テストスイート初期化ファイル中では使えません。

テストケーステーブルで `[Tags]`:setting: を指定する
   この設定を使うと、テストケースには指定のタグが必ず付与されます。
   さらに、 :setting:`Default Tags` で指定したタグがあっても、付与されなくなります。
   そのため、この設定に空の値を指定すれば、 :setting:`Default Tags` のタグを打ち消せます。
   `NONE` を指定することでも、デフォルトタグを打ち消せます。

コマンドラインオプションに `--settag`:option: を指定する
   このオプションを指定すると、実行されるテストにもともと付与されていたタグに加えて、指定したタグが付与されます。

`Set Tags`:name:, `Remove Tags`:name:, `Fail`:name: および `Pass Execution`:name: キーワードで指定する
   これらの :ref:`BuiltIn` ライブラリキーワードを使うと、テストの実行時に動的にタグを操作できます。

タグは普通のテキストですが、処理の過程では、全て小文字に変換してスペースを除去した形式に変換します。
一つのテストケースに同じタグが何度も定義されている場合には、最初に定義したタグ以外の重複するタグ定義を除去します。
タグは変数で作成できます。ただし、変数値が存在するときに限ります。

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

.. _Reserved tags:

予約ずみのタグ
~~~~~~~~~~~~~~~~

基本的に、ユーザはどんなタグを指定してもかまいません。
ただし、例外として、 Robot Framework の中で、ある種のタグがあらかじめ定義されていて、それらのタグを使うと、予想外の結果を招くことがあります。
Robot Framework の特殊なタグには、今後組み込まれるものも含めて、すべて `robot-` というプレフィクスがつきます。
トラブルを避けるには、特に意図して内部機能を使いたいのでない限り `robot-` ではじまるタグを使わないよう勧めます。

このドキュメントの執筆時点では、定義済みの特殊なタグは `robot-exit` のみです。
このタグは、 :ref:`テストをグレースフルに停止させる <stopping test execution gracefully>` ときに、対象のテストに自動的に付加されます。
その他の使い方も、将来増える可能性があります。

.. _test setup:
.. _test teardown:
.. _Test setup and teardown:

テストのセットアップとティアダウン
---------------------------------------

他のテスト自動化フレームワークと同様、 Robot Framework にもセットアップとティアダウンの機能があります。
簡単にいえば、セットアップはテストケースの前に実行する処理で、ティアダウンはテストケース後に実行するものです。
Robot Framework のセットアップとティアダウンは普通のキーワードとして定義でき、引数も指定できます。

セットアップとティアダウンに指定できるキーワードは、つねに一つだけです。
複数のタスクを実行したいのなら、高水準の :ref:`ユーザキーワード <user keywords>` ひとつにまとめてください。
あるいは、 :ref:`BuiltIn` キーワードの :name:`Run Keywords` を使えば、複数のキーワードを一つのキーワードから実行できます。

テストのティアダウンには、二つの特殊な働きがあります。
一つは、ティアダウンはテストケースが失敗しても実行され、テストケースの実行結果にかかわらず後始末処理を行なうところです。
もう一つは、ティアダウン中に実行されるキーワードは、たとえいずれかが失敗しても全て実行されるということです。
この :ref:`失敗しても処理を継続 <continue on failure>` する機能は、通常のキーワードの実行でも設定できますが、ティアダウンにはデフォルトで適用されています。

テストケースにセットアップやティアダウンを指定したいときは、設定テーブルに :setting:`Test Setup` や :setting:`Test Teardown` を指定するのが一番簡単です。
個々のテストケースにも、セットアップやティアダウンを指定できます。
テストケース中で :setting:`[Setup]` や:setting:`[Teardown]` を指定すると、設定テーブルなどで指定された :setting:`Test Setup` や :setting:`Test Teardown` に優先して使われます。
:setting:`[Setup]` や :setting:`[Teardown]` の引数を省略すると、セットアップやティアダウンを行わないことを表します。
`NONE` を指定した場合も同じ意味になります。

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

セットアップやティアダウンで実行するキーワードの名前は変数にできます。
この機能を使うと、例えばコマンドラインからキーワードを入力して変数に入れ、それを使うことで、実行環境毎にセットアップやティアダウンをさまざまに切り替えられます。

.. note:: :ref:`テストスイート単位でも、セットアップやティアダウンを指定できます <suite setup and teardown>` 。
   テストスイート単位のセットアップは、サブテストスイートを含む全テストスイート中の全てのテストケースのセットアップとして実行されます。
   スイートのティアダウンも同様です。

.. _test temlate:
.. _template keyword:
.. _Test templates:

テストテンプレート
----------------------

テストテンプレートを使うと、普通の :ref:`キーワード駆動 <keyword-driven>` テストを :ref:`データ駆動 <data-driven>` テストに変換できます。
キーワード駆動のテストケースがキーワードと引数によって成り立つのに対して、テンプレートを使ったテストケースは、テンプレートにするキーワードに与える引数だけが入っています。
テンプレートを使うと、テストの度に同じキーワードを何度も繰り返さず、一つのテストに一回、もしくは一つのファイルに一回だけ指定すればよくなります。

テンプレートのキーワードには、通常の必須の引数も、名前指定の引数も使えます。
また、キーワード名への埋め込み引数も使えます。
テンプレートの設定は、他のテストの設定と違い、変数を使った設定ができません。

.. Basic usage

基本の使い方
~~~~~~~~~~~~~~~

以下のテストケースの例では、必須の引数をとる普通のキーワードをテンプレートに使っています。
二つのテストケースは、機能的には全く同じです。

.. sourcecode:: robotframework

   *** Test Cases **
   Normal test case
       Example keyword    first argument    second argument

   Templated test case
       [Template]    Example keyword
       first argument    second argument

上の例からわかるように、 :setting:`[Template]` を使うことで、個別のテストケースにテンプレートを指定できます。
テンプレートの指定は、設定テーブルに :setting:`Test Template` を設定することでもできますが、その場合は、テストケースファイル中の全てのテストケースに対してテンプレートが適用されます。
:setting:`[Template]` 設定は、設定テーブルのテンプレート設定をオーバライドでき、空の値を指定したり、 `NONE` を指定した場合には、設定テーブルで :setting:`Test Template` が指定されていても、その設定を取り消せます。

テンプレートの指定されたテストケースにデータ行が複数あれば、全ての行について一つ一つテンプレートが適用されます。
つまり、各行ごとに、同じキーワードが何度も実行されていくわけです。
テンプレートつきのテストには、もう一つ特別な点があります。それは、テスト中のどこかでキーワードの実行に失敗しても、全ての行を処理し終えるまでテストケースの実行を継続するということです。
この :ref:`失敗しても処理を継続 <continue on failure>` する機能は、通常のテストの実行でも設定できますが、テンプレートつきのテストにはデフォルトで適用されています。

.. sourcecode:: robotframework

   *** Settings ***
   Test Template    Example keyword

   *** Test Cases ***
   Templated test case
       first round 1     first round 2
       second round 1    second round 2
       third round 1     third round 2

引数の :ref:`デフォルト値 <default values>` や :ref:`可変個の引数 <varargs>`, :ref:`名前指定の引数 <named arguments>`, :ref:`フリーキーワード引数 <free keyword arguments>` などは、他で使うときと同様、テンプレートでも使えます。
:ref:`変数での引数の指定 <variables>` もサポートしています。

.. _Templates with embedded arguments:

引数埋め込みのキーワードをテンプレートに使う
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Robot Framework 2.8.2 からは、テンプレートでもキーワードの :ref:`引数埋め込み <embedded argument syntax>` をサポートしています。
テンプレートで引数埋め込みキーワードを扱う場合には、キーワード名のプレースホルダを引数とみなして、テストケース中の引数をそこに割り当てます。
その結果、キーワードはプレースホルダの数分、必須の引数を取ることになります。
この挙動がよくわかる例を以下に示します:

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

引数埋め込みのキーワードがテンプレート中に使われている場合、キーワード中の「引数」の数と、テストケースに定義する引数の数を一致させせねばなりません。
引数名は、もとのキーワードの引数名と一致している必要はなく、一部の引数に固定値を入れて、引数の数を変えることもできます:

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

引数埋め込みキーワードとテンプレートの組み合わせの最大の利点は、引数名をわかりやすく定義できるところです。
通常の引数でも、カラムに名前をつけて同じような効果を得られます。
その例は、以降の :ref:`データ駆動スタイルのテストケース <data-driven style>` の節で示しています。

.. _Templates with for loops:

テンプレート中で for ループを使う
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

テンプレート中で :ref:`for ループ <for loops>` を使った場合、ループの全ステップに対してテンプレートを適用します。
その際、「失敗しても継続」モードが使われるので、途中でキーワードの実行に失敗しても、ループの全ての要素を実行するまで処理を継続します。

.. sourcecode:: robotframework

   *** Test Cases ***
   Template and for
       [Template]    Example keyword
       :FOR    ${item}    IN    @{ITEMS}
       \    ${item}    2nd arg
       :FOR    ${index}    IN RANGE    42
       \    1st arg    ${index}

.. _Different test case styles:

色々なテストケースの書き方
----------------------------

テストケースの書き方にはいくつか方法があります。
何らかの *手順 (workflow)* を記述するようなテストケースは、「キーワード駆動」または「ビヘイビア駆動」スタイルで書きます。
様々な入力データに対して同じワークフローを何度も試すようなテストは、「データ駆動」スタイルで書いてください。

.. _keyword-driven:
.. _Keyword-driven style:

キーワード駆動の書き方
~~~~~~~~~~~~~~~~~~~~~~~~

:ref:`以前のサンプル <example-tests>` で説明した :name:`Valid Login` のようなワークフローテストは、キーワードいくつかと、引数から成り立っています。
テストの通常の構成は、まずシステムを初期状態にして (:name:`Valid Login` では :name:`Open Login Page` に相当), 次にシステムに何か操作を行い (:name:`Input Name`, :name:`Input Password`, :name:`Submit Credentials`), 最後にシステムが期待通りに動作しているか検証 (:name:`Welcome Page Should Be Open`) します。


.. _earlier: example-tests_

.. _data-driven:
.. _Data-driven style:

データ駆動の書き方
~~~~~~~~~~~~~~~~~~~~~

もう一つのテストケースの書き方は、「 *データ駆動* 」アプローチでの書き方です。
この書き方では、テストケースは高水準のキーワード（通常は :ref:`ユーザキーワード <user keyword>` として定義したもの) を一つだけ使い、実際のテストワークフローを隠蔽してしまいます。
この書き方は、様々な入出力データに対して同じテストシナリオを実行する必要があるときにとても便利です。
テストごとに何度も同じキーワードを繰り返して記述してもかまいませんが、 :ref:`テストテンプレート <test template>` を使えば、キーワードの指定が一度だけで済みます。

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

.. tip:: 上の例のように、テストケーステーブルの減っだ行にカラム名を書いておくと、テストの内容を理解しやすくなります。
         ヘッダ行の最初のセル以外の内容は :ref:`無視される <ignored data>` ので、こういう書き方ができます。

上の例には、6 つのテストが入っています。それぞれが、無効なユーザIDまたはパスワードの組み合わせになっています。
一方、一つのテストだけで、上の6つの組み合わせを検証する方法を以下に示します。
:ref:`テストテンプレート <test templates>` 使った場合、仮にテスト内のいずれかの条件で検証に失敗しても、テスト内の全ての条件を検証し終えるまでテストを実行し続けます。
そのため、これらのテストは実質的にほぼ同じく機能します。
上の例では、個別の組み合わせについてテストケース名がついているので、それぞれのテストを区別しやすい反面、大量にテストケースが存在するために、テスト結果出力が台無しになるかもしれません。
状況と好みによって、うまく使い分けてください。

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


.. _Behavior-driven style:

ビヘイビア駆動の書き方
~~~~~~~~~~~~~~~~~~~~~~~~

テストケースを、技術に詳しくないプロジェクトのステークホルダでも理解できるような形の要求仕様のように書くことも可能です。
この、いわば *実行可能な要求仕様書* は、一般に `受け入れテスト駆動開発 <http://testobsessed.com/2008/12/08/acceptance-test-driven-development-atdd-an-overview>`_ (ATDD: Acceptance Test Driven Development) ないし `実例による仕様書 <http://en.wikipedia.org/wiki/Specification_by_example>`_ (SbE) と呼ばれています。

このような要求仕様書兼テストの書き方の一つに、 `ビヘイビア駆動開発 <https://ja.wikipedia.org/wiki/%E3%83%93%E3%83%98%E3%82%A4%E3%83%93%E3%82%A2%E9%A7%86%E5%8B%95%E9%96%8B%E7%99%BA>`_ でよく使われる *Given-When-Then* スタイルがあります。
*Given-When-Then* スタイルでは、テストの初期状態を :name:`Given` で始まるキーワードで書きます。
同様に、アクションは :name:`When` で始め、期待される動作は :name:`Then` で始めます。
アクションを追加するときは、 :name:`And` や :name:`But` を使います。

.. sourcecode:: robotframework

   *** Test Cases ***
   Valid Login
       Given login page is open   # ログインページが開いている「とする」
       When valid username and password are inserted   # 「もし」有効なユーザ名とパスワードがDB上にあり
       and credentials are submitted   # 「かつ」認証情報を入力した
       Then welcome page should be open    # 「ならば」ウェルカムページを表示せねばならない


:name:`Given/When/Then/And/But` プレフィクスは無視される
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

:name:`Given`, :name:`When`, :name:`Then`, :name:`And`, :name:`But` といったプレフィクスは、キーワードマッチングの際に、他に完全に一致するキーワードがライブラリやユーザ定義のキーワード中で見つからないかぎり、捨てられてしまいます。
例えば、上の例のキーワード、 :name:`Given login page is open` の場合、ユーザキーワードを定義するときには、キーワード名に :name:`Given` がついていてもいなくてもかまいません。
このことを利用すれば、一つのキーワードに対して、異なるプレフィクスを使えます。
例えば、上の例の :name:`Welcome page should be open` は :name:`And welcome page should be open` にも使えます。

.. note:: :name:`But` プレフィクスを無視するようになったのは Robot Framework 2.8.7 からです。

.. _Embedding data to keywords:

キーワードにデータを埋め込む
''''''''''''''''''''''''''''''

具体的なテストのサンプルを書いている際、実際のデータをキーワードに渡せると便利なことがあります。
ユーザ定義のキーワードは、この機能を :ref:`キーワード名に引数を埋め込む <embedding arguments into keyword name>` ことでサポートしています。
