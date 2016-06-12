.. _test library:
.. _test libraries:
.. _Using test libraries:

テストライブラリを使う
===========================

テストライブラリには、「 *ライブラリキーワード* 」と呼ばれる、テスト対象システムと実際にインタラクションするより低水準なキーワードが定義されています。
テストケースは、ライブラリのキーワードや、より高水準な :ref:`ユーザキーワード <user keywords>` を使っています。
この節では、テストライブラリの使い方と、その中のキーワードの扱い方を説明します。
:ref:`テストライブラリの作り方 <creating test libraries>` は、別の節で解説します。

.. contents::
   :depth: 2
   :local:

.. Importing libraries:

ライブラリのインポート
------------------------

テストライブラリのインポートには、 :setting:`Library` 設定を使うのが普通ですが、 :name:`Import Library` キーワードでもインポートできます。


.. Using `Library` setting:
   
`Library` 設定
~~~~~~~~~~~~~~~~~

通常、テストライブラリをインポートするには、設定テーブルで :setting:`Library` を使います。
インポートしたいライブラリの名前は、 :setting:`Library` の次のカラムに書きます。
他のデータと違い、ライブラリ名は大小文字の区別があり、スペースを無視しません。
ライブラリがパッケージの場合は、パッケージ名込みの完全な名前を指定せねばなりません。

ライブラリに引数を指定する場合は、引数はライブラリ名の後のカラムに列挙します。
:ref:`キーワードの引数 <using arguments>` と同じように、デフォルト値、可変個の引数、名前付き引数を指定できます。
ライブラリ名と引数には変数を使えます。

.. sourcecode:: robotframework

   *** Settings ***
   Library    OperatingSystem 
   Library    my.package.TestLibrary
   Library    MyLibrary    arg1    arg2
   Library    ${LIBRARY}

テストライブラリは :ref:`テストケースファイル<test case file>` や :ref:`リソースファイル <resource files>`,  :ref:`テストケース初期化ファイル<test suite initialization files>`  からインポートできます。どのケースでも、インポートしたライブラリの全てのキーワードを使えるようになります。
リソースファイルからインポートした場合、インポートしたライブラリ上のキーワードは、そのリソースファイルをインポートしたファイル上でも使えるようになります。


.. Using `Import Library` keyword:

`Import Library` キーワード
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

テストライブラリを使うもう一つの方法は、 :ref:`BuiltIn` ライブラリの :name:`Import Library` キーワードです。
このキーワードは、 :setting:`Library` と同じように、ライブラリ名と引数を指定できます。
インポートしたライブラリ上のキーワードは、  :name:`Import Library` を呼び出したテストスイート上でのみ、利用できます。
キーワードを使ったインポートは、対象のテストライブラリがテスト実行時になるまで使えない場合や、他のキーワードで使えるようにする必要がある場合に便利です。

.. sourcecode:: robotframework

   *** Test Cases ***
   Example
       Do Something 
       Import Library    MyLibrary    arg1    arg2
       KW From MyLibrary

.. Specifying library to import:

インポートするライブラリを指定する
------------------------------------

インポートするライブラリは、ライブラリ名か、ライブラリへのパスで指定します。
どちらの指定方法も、 :setting:`Library` 設定と :name:`Import Library` キーワードの両方で使えます。

ライブラリ名を使う場合
~~~~~~~~~~~~~~~~~~~~~~~~

テストライブラリを指定する方法で最も一般的なのはライブラリ名で、この節のこれまでの例でも、全てライブラリ名を使ってきました。
ライブラリ名を指定した場合、 Robot Framework は、ライブラリを実装しているクラスやモジュールを :ref:`モジュールサーチパス <module search path>` から探そうとします。
何らかの手段でライブラリをインストールしていれば、モジュールサーチパス上に自動的に置かれているはずですが、そうでなければ、別途サーチパスを設定する必要があるかもしれません。

ライブラリ名指定のいちばんよいところは、 :ref:`スタートアップスクリプト<start-up script>` などでモジュールサーチパスを適切に設定している限り、普通のユーザは、どこにライブラリがインストールされているか気にしなくてよいという点です。
その半面、自分のライブラリを置きたいときは、たとえばそれが単純なものでも、サーチパスに手をいれねばなりません。

.. Using physical path to library

ライブラリのファイルパスを使う場合
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

ライブラリ指定のもう一つのメカニズムは、ファイルシステム上のパスを使う仕組みです。
パスは、ライブラリを使うテストデータファイルからの相対パスとみなされます。
:ref:`リソースファイルや変数ファイル <resource and variable files>` と同じです。
ファイルパス指定の恩恵は、モジュールサーチパスを設定しなくてよいところです。

ライブラリがファイルであれば、パスには拡張子が必要です。例えば、 Python で書かれたライブラリであれば、拡張子は :file:`.py` ですし、 Java のライブラリなら :file:`.class` や :file:`.java` です。
ただし、 :file:`.java` ファイルを指定する場合は、対応するクラスファイルにアクセスできねばなりません。
Python ライブラリがパッケージのディレクトリの場合、パスをスラッシュ(`/`) で終えねばなりません。
以下の例は、それぞれの指定方法を示しています。

.. sourcecode:: robotframework

   *** Settings ***
   Library    PythonLibrary.py
   Library    /absolute/path/JavaLibrary.java
   Library    relative/path/PythonDirLib/    possible    arguments
   Library    ${RESOURCES}/Example.class


このアプローチの制約は、 Python のクラスでライブラリを実装する際、
:ref:`クラス名とモジュールファイル名を同じにせねばならない <test library names>` 点です。
さらに、このインポート機構では、JARやZIPパッケージで配布されているライブラリのインポートはできません。

.. _With Name syntax:
.. _Setting custom name to test library:

.. Setting custom name to test library

テストライブラリの名前を変更する
--------------------------------------

ライブラリ名は、テストログの中で、キーワード名の前に表示されます。
また、複数のキーワードが同じ名前を持っている場合、区別のために、 :ref:`キーワード名の前にライブラリ名を付加 <Handling keywords with same names>` せねばなりません。
ライブラリ名は、ライブラリを実装しているモジュールやクラス名から得られますが、その名前を一時的に変更したいというケースもあります。例えば:

- 同じライブラリを、引数を変えて複数回インポートして、それぞれを区別して使いたい場合。ライブラリの名前を再定義する以外、実現する方法がありません。

- ライブラリ名が長すぎて不便な場合。 Java のライブラリが長いパッケージ名になっている場合などです。

- 変数を使って、環境によってインポートするライブラリを切り替えたいが、そのライブラリを同じ名前で参照したいとき。

- ライブラリ名がわかりにくい場合や情けない場合。もちろん、元のライブラリ名を変える方が良いのですが。

ライブラリの名前を変更するには、ライブラリ名のあとのセルに `WITH NAME` (大文字です) を置き、その次に新しい名前を続けます。
指定した名前はログに表示され、テストデータ中でライブラリ名を完全指定する場合には、新しい名前を使わねばなりません (:name:`LibraryName.Keyword Name`)。

.. sourcecode:: robotframework

   *** Settings ***
   Library    com.company.TestLib    WITH NAME    TestLib
   Library    ${LIBRARY}             WITH NAME    MyName

ライブラリの引数を指定する場合は、もとのライブラリ名と  `WITH NAME` の間に置きます。
以下では、同じライブラリを引数を変えてインポートしている例を示しています:

.. sourcecode:: robotframework

   *** Settings ***
   Library    SomeLibrary    localhost        1234    WITH NAME    LocalLib
   Library    SomeLibrary    server.domain    8080    WITH NAME    RemoteLib

   *** Test Cases ***
   My Test
       LocalLib.Some Keyword     some arg       second arg
       RemoteLib.Some Keyword    another arg    whatever
       LocalLib.Another Keyword

テストライブラリの名前の付け替えは、設定テーブルでライブラリをインポートするときと、 :name:`Import Library` でインポートするときのどちらでもできます。

.. Standard libraries

標準ライブラリ
------------------

テストライブラリの中には、 Robot Framework と一緒に配布されているものがあります。
これらのライブラリは *標準 (standard) ライブラリ* といいます。
中でも :ref:`BuiltIn` ライブラリは特別で、常に自動的にインポートされ、そのキーワードはいつでも使えます。
他の標準ライブラリは、他のライブラリ全般と同じくインポート操作が必要ですが、インストールは必要ありません。

.. Normal standard libraries

通常使える標準ライブラリ
~~~~~~~~~~~~~~~~~~~~~~~~~

通常は、以下の標準ライブラリを利用可能です:

  - BuiltIn__
  - Collections__
  - DateTime__
  - Dialogs__
  - OperatingSystem__
  - Process__
  - Screenshot__
  - String__
  - Telnet__
  - XML__

__ ../../lib/BuiltIn.html
__ ../../lib/Collections.html
__ ../../lib/DateTime.html
__ ../../lib/Dialogs.html
__ ../../lib/OperatingSystem.html
__ ../../lib/Process.html
__ ../../lib/String.html
__ ../../lib/Screenshot.html
__ ../../lib/Telnet.html
__ ../../lib/XML.html

.. Remote library

リモートライブラリ
~~~~~~~~~~~~~~~~~~~

上に挙げた標準ライブラリの他に、標準ライブラリとは全く違った性質の :name:`Remote` ライブラリがあります。
このライブラリは、それ自体はキーワードを全く持たず、他の Robot Framework と実際のテストライブラリへの、いわばプロキシとして働きます。
リモートライブラリ経由のライブラリは、フレームワークのコア部分と別のマシンで実行でき、 Robot Framework がネイティブでサポートしている言語以外でも実装できます。

詳しくは、 :ref:`リモートライブラリインタフェース<Remote library interface>` の節を参照してください。


.. External libraries

外部ライブラリ
------------------

標準ライブラリでないテストライブラリは、全て *外部 (external) ライブラリ* です。
Robot Framework のオープンソースコミュニティは、 Selenium2Library_ や
SwingLibrary_ のように、フレームワークのコア部分に入っていない、汎用のライブラリをいくつか提供しています。
公開されていて使えるライブラリのリストは http://robotframework.org にあります。

Robot Framework を使いこなせるチームなら、もちろん汎用のライブラリや、カスタムのライブラリを自作できます。
詳しくは :ref:`テストライブラリを作成する <Creating test libraries>` を参照してください。

外部ライブラリは、それぞれが独自のメカニズムを持っており、インストール方法や使い方が違います。
ライブラリ自体とは別に、インストールが必要な依存もあります。
ライブラリを提供するときは、わかりやすくインストールして使えるドキュメントを用意して、できるだけインストールを自動化してください。
