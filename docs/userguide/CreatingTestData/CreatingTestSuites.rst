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

初期化ファイル
~~~~~~~~~~~~~~~~~~~~

ディレクトリでできたテストスイートにも、テストケースファイルと同じような設定を持たせられます。
ディレクトリ単体には情報をもたせられないので、設定は特殊な「テストスイート初期化ファイル」に置かねばなりません。
初期化ファイルの名前は、 :file:`__init__.ext` の形式にします。 ``ext`` は、 Robot Framework の :ref:`サポートするファイル形式 <supported file formats>` に準じます (:file:`__init__.robot`, :file:`__init__.html` など)。
このファイル名の付け方は、 Python でディレクトリをパッケージにするときに配置するファイル名に倣っています。

初期化ファイルの書き方はテストケースファイルとほぼ同じですが、テストケーステーブルがなく、設定テーブルに書けない設定がいくつかあります。
また、初期化ファイル中で作成した変数とキーワードは、他の低水準のテストスイートからは利用 *できません* 。
テストケースファイル間で変数やキーワードを共有したいのなら、 :ref:`リソースファイル <resource files>` を使ってください。
リソースファイルは初期化ファイルとテストケースファイルのどちらにもインポートできます。

初期化ファイルの主な役割は、 :ref:`テストケースファイル <test case files>` と同じ方法で、テストスイート関連の設定を行なうことにありますが、 :ref:`テストケース関連の設定 <Test case related settings in the Setting table>` も可能です。
初期化ファイルでできる設定を以下で説明します。

`Documentation`:setting:, `Metadata`:setting:, `Suite Setup`:setting:, `Suite Teardown`:setting:
   テストスイートむけの設定で、テストケースファイルに書いた時と同じ効果があります。
`Force Tags`:setting:
   この設定に書いたタグは、ディレクトリ内の全てのテストケースファイルのテストケースに付与されます。
   子ディレクトリ以下のテストスイートにも再帰的に適用します。
`Test Setup`:setting:, `Test Teardown`:setting:, `Test Timeout`:setting:
   この設定に書いたセットアップおよびティアダウンは、ディレクトリ内の全てのテストケースファイルのテストケースのデフォルト値になります。   子ディレクトリ以下のテストスイートにも再帰的に適用します。
   テストケースファイルや各テストケースレベルでオーバライドできます。
   Robot Framework 2.7 から、初期化ファイルにテストタイムアウトを定義できるようになりました。

`Default Tags`:setting:, `Test Template`:setting:
   これらの設定は、初期化ファイルには書けません。

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

.. _test suite name:
.. _test suite documentation:
.. _Test suite name and documentation:

テストスイート名とドキュメント
---------------------------------

テストスイート名は、ファイルやディレクトリの名前をもとに決まります。
ファイル名から拡張子を除去し、アンダースコアがあればスペースで置換し、小文字だけの名前はタイトルケース (各単語の先頭を大文字にする) に変換します。
例えば、 :file:`some_tests.html` は :name:`Some Tests` になり、 :file:`My_test_directory` は :name:`My test directory` です。

ファイルやディレクトリの名前はには、テストスイートの :ref:`実行順 <execution order>` を制御するプレフィクスを付与できます。
プレフィクスと名前は、二つのアンダースコアで分割して書きます。
実行時にテストスイート名を構築する際、プレフィクス部分とアンダースコアは除去されます。
例えば、テストケースファイル :file:`01__some_tests.txt` および :file:`02__more_tests.txt` は、それぞれ :name:`Some Tests`, :name:`More Tests` というテストスイートになり、前者が先に実行されます。

テストスイートのドキュメントは、設定テーブルの :setting:`Documentation` に書きます。
ドキュメントは、テストケースファイルに書くこともできますし、高水準のテストスイートでは、テストスイート初期化ファイルに書けます。
テストスイートのドキュメントは、どこに表示されるか、どう書けるかといった観点で、 :ref:`テストケースのドキュメント <test case documentation>` の節で説明したのとほぼ同じ性質を備えています。

.. sourcecode:: robotframework

   *** Settings ***
   Documentation    An example test suite documentation with *some* _formatting_.
   ...              See test documentation for more documentation examples.

トップレベルのテストスイートの名前とドキュメントは、実行時にオーバライドできます。
オーバライドするには、それぞれ、コマンドラインオプション :option:`--name` や :option:`--doc` を使います。
詳しくは :ref:`メタデータの設定 <Setting metadata>` の節で説明しています。

.. _Free test suite metadata:

テストスイートのメタデータ
----------------------------

テストスイートには、ドキュメント以外のメタデータも付与できます。
メタデータは設定テーブルに :setting:`Metadata` を使って書きます。
設定したメタデータは、テスト報告書やログに出力されます。

メタデータの名前と値は、 :setting:`Metadata` の後のカラムに書きます。
メタデータの値はドキュメントと同じように書けます。つまり、
:ref:`複数カラムに分けて <Dividing test data to several rows>` 書いたり (スペースで結合される)、 :ref:`複数行に分けて <Newlines in test data>` 書いたり (改行文字で結合される) でき、 :ref:`HTML 形式 <HTML formatting>` で書いたり :ref:`変数 <variable>` を使ったりできます。

.. sourcecode:: robotframework

   *** Settings ***
   Metadata    Version        2.0
   Metadata    More Info      For more information about *Robot Framework* see http://robotframework.org
   Metadata    Executed At    ${HOST}

トップレベルのテストスイートのメタデータは実行時にオーバライドできます。
オーバライドするには、コマンドラインオプション :option:`--metadata` を使います。
詳しくは :ref:`メタデータの設定 <Setting metadata>` の節で説明しています。

.. _suite setup:
.. _suite teardown:
.. _Suite setup and teardown:

テストスイート単位のセットアップとティアダウン
------------------------------------------------

:ref:`テストケース単位 <Test setup and teardown>` だけでなく、テストスイート単位でも、セットアップやティアダウンを指定できます。
テストスイートのセットアップは、テストスイート中の最初のテストケースを実行する前に実行し、ティアダウンは、全てのテストケースを実行した後に実行します。
どのテストスイートにも、セットアップとティアダウンを設定できます。ディレクトリでつくったスイートの場合は、設定を :ref:`テストスイート初期化ファイル <test suite initialization file>` に書いてください。

テストケースの場合と同様、スイート単位のセットアップ・ティアダウンはキーワードで指定し、キーワードには引数を指定できます。
設定値は、設定テーブルで :setting:`Suite Setup` や :setting:`Suite Teardown` といった設定名を使って指定します。
キーワード名や引数は、設定名の後のカラムに書きます。

スイート単位のセットアップの実行に失敗すると、そのスイート内の子テストスイートはただちに失敗扱いとなり、実行されません。
この仕様のため、テストケースを実行する際、必要な前提条件が整っているかどうかをチェックするのに、テストスイートのセットアップが上手く働きます。

スイート単位のティアダウンは、通常、全テストケースの実行を終了したあとの後片付けに使います。
ティアダウンは、同じスイートのセットアップの実行に失敗したときでさえ実行されます。
スイート単位のティアダウンに失敗すると、スイート内の全テストケースは、実際の実行結果と関係なく失敗扱いになります。
スイートのティアダウン中に、何らかのキーワードの実行に失敗しても、ティアダウン処理は継続するので注意してください。

セットアップやティアダウンに指定するキーワードの名前には、変数を指定できます。
そのため、環境ごとに異なるセットアップ用キーワード名を定義しておき、スイートセットアップは変数にしておいて、コマンドラインで変数の値を指定することで、キーワードを切り替えて実行する、といったことができます。
