.. _Installation instructions:

インストール方法
=========================

この節では、 Robot Framework のインストール・アンインストール方法と、各種 OS で必要な準備を開設しています。基本的に、  `pip <http://pip-installer.org>`_ をインストールしていれば、以下のように実行するだけです::

    pip install robotframework

.. contents::
   :depth: 2
   :local:

.. START USER GUIDE IGNORE
.. These instructions are included also in the User Guide. Following role
.. and link definitions are excluded when UG is built.
.. default-role:: code
.. role:: file(emphasis)
.. role:: option(code)
.. _supporting tools: http://robotframework.org/robotframework/#built-in-tools
.. _post-process outputs: `supporting tools`_
.. END USER GUIDE IGNORE


.. Introduction:

はじめに
------------

`Robot Framework <http://robotframework.org>`_ は `Python <http://python.org>`_ で書かれており、 `Jython <http://jython.org>`_ (JVM) や `IronPython <http://ironpython.net>`_ (.NET) でも動作します。このフレームワークをインストールするときには、 :ref:`前提条件 <precondition>` として、以下のインタプリタのいずれかが必要です。`

Robot Framework 自体のインストール方法には、以下のような様々な方法があります。これらについては、後の節でも説明します。

:ref:`pip を使う <Installing with pip>`
    Robot Framework 推奨のインストール方法です。 最近の Python, Jython, IronPython には、標準のパッケージマネジャとして pip_ が入っています。pip が使える状態なら、単に::

        pip install robotframework

    とするだけです。

:ref:`ソースコードから <Installing from source>`
    どのオペレーティングシステムでも、どの Python インタプリタでも使える方法です。ソースコードは `PyPI <https://pypi.python.org/pypi/robotframework>`_ からダウンロードして展開したり、 `GitHub リポジトリから <https://github.com/robotframework/robotframework>`_ を clone したりして取得できます。

:ref:`JAR形式 <Standalone JAR distribution>`
    Jython で実行できれば充分な場合、 `Maven central <http://search.maven.org/#search%7Cga%7C1%7Ca%3Arobotframework>`_ からスタンドアロンの ``robotframework-<version>.jar`` を取ってくるのが一番簡単です。この JAR には、 Jython と Robot Framework が両方とも入っていて、 `Java <http://java.com>`_ をインストールしておくだけで使えます。

:ref:`手作業で <Manual installation>`
    何か特別な事情があって、上の方法がどれも使えない場合には、自分で手作業で入れられます。

.. note:: Robot Framework 3.0 以前のバージョンには、 32bit 版と 64bit 版の両方の Python 向けのインストーラがありました。 Python 2.7.9 からは Windows 版にも pip_ が入っていることや、インストーラだと Python 3 向けにも二つ必要になってしまうことから、 `Windows インストーラの提供はやめました <https://github.com/robotframework/robotframework/issues/2218>`_ 。Windows版でも、 :ref:`pip を使ったインストール <using pip>` を推奨します。

.. _precondition:
.. _Preconditions:

前提条件
-------------

Robot Framework は Python_ (C Python, Python 2 と 3 の両方),  Jython_ (JVM),  IronPython (.NET), そして `PyPy <http://pypy.org>`_ をサポートしています。フレームワークを動かすには、あらかじめいずれかのインタプリタをインストールしておく必要があります。

一般に、どのインタプリタを使うべきかは、どんなテストライブラリやテスト環境が必要かによって変わります。ライブラリによっては、 CPython 上でしか動かないものもありますし、 Java のツールを使っているために Jython でしか動かないものや、 .NET 環境が必要なため IronPython が適している場合もあります。もちろん、どのインタプリタでも問題なく動くツールやライブラリもたくさんあります。

特殊な事情がなく、まずはフレームワークを試してみたいのなら、Python をお勧めします。Python はもっとも成熟した実装で、 Jython や IronPython よりも高速 (とりわけ、起動が速い) で、ほとんどの UNIX 系 OS 上で使えます。もう一つの選択肢は、 Java さえあれば使える :ref:`スタンドアロン JAR版 <standalone JAR distribution>` です。

.. _Python 2 vs Python 3:

Python 2 か Python 3 か
~~~~~~~~~~~~~~~~~~~~~~~~~

Python 2 と Pyhton 3 は、言語としてはほとんど同じですが、お互いに完全に互換というわけではありません。
主な違いは、 Python 3 では、標準ではすべての文字列が Unicode 文字列型であるのに対して、 Python 2 では標準は実質 bytes 型に総統するということです。
他にも、後方互換性のない変更がいくつかあります。
2010 年にリリースされた Python 2.7 は Python 2 系の最後のリリースとされていて、2020 年までサポートされます。
Python 2 と 3 の違い、どちらを使うべきか、どちらのバージョンでも動くコードの書き方などは、 `Wiki <https://wiki.python.org/moin/Python2orPython3>`_ を参照するとよいでしょう。

Robot Framework 3.0 は、 Python 3 をサポートする最初のバージョンです。
このバージョンは、Python 2 もサポートしていて、 Python 2 自体が公式にサポートされている限り Python 2 に対応し続ける予定です。フレームワークのコア部分が Pyhton 3 へのサポートを始めたいま、Robot Framework のエコシステムに関わるライブラリやツールの作者にも、 Python 3 のサポートを検討していただきたいです。

.. _Python installation:

Python のインストール
~~~~~~~~~~~~~~~~~~~~~~

Linux や OS X のように、ほとんどの UNIX 系システムには、最初から Python_ がインストールされています。
Windows その他の環境では、 Python を自分でインストールする必要があります。
まずは http://python.org に行って、適切なインストーラをダウンロードしたり、 Python のインストール手順について詳しい情報を得るのが良いでしょう。

Robot Framework 3.0 は、 Python 2.6, 2.7, 3.3 以降をサポートしています。
ただし、 `バージョン 3.1 以降で Python 2.6 のサポートを打ち切る <https://github.com/robotframework/robotframework/issues/2276>`_ 予定です。
古いバージョンの Python を使いたい場合、 Robot Framework 2.5-2.8 が Python 2.5 を、 Robot Framework 2.0-2.1 が Python 2.3 および 2.4 をサポートしています。

Windows では、インストール時に、インストーラを管理者モードで起動し、全てのユーザにインストールするよう推奨します。
また、環境変数 ``PYTHONCASEOK`` は設定してはなりません。

インストール後、 PATH_ を変更して、コマンドラインから Python コマンドと ``robot``, ``rebot`` :ref:`テスト実行スクリプト <runner scripts>` を実行できるように設定する必要があるでしょう。

.. tip:: 最近の Windows 用 Pyhton インストーラには、インストールの際に ``PATH`` を設定する機能があります。この機能は標準では無効になっていて、 `Customize Python` の画面で `Add python.exe to Path` を有効にします。

.. _Jython installation:

Jython のインストール
~~~~~~~~~~~~~~~~~~~~~~~~

Java_ で書かれていたり、内部的に Java のツールを使うテストライブラリを使いたい場合には、Robot Framework を Jython_ 上で動かす必要があります。
そのため、 Java ランタイム環境 (JRE) か、 Java 開発キット (JDK) が必要です。
ここでは、 JRE や JDK のインストール方法について説明しませんが、 http://java.com などで詳しい情報が手にはいります。

Jython のインストールはとても簡単で、まずは、 http://jython.org からインストーラを取得します。
インストーラは実行可能な JAR のパッケージで、コマンドラインから `java -jar jython_installer-<version>.jar` で実行します。
システム構成によっては、インストーラをダブルクリックするだけでインストールできます。

Robot Framework 3.0 は Jython 2.7 をサポートしており、これには Java 7 以降が必要です。
古い Jython や Java が必要なら、 Robot Framework 2.5-2.8 が Jython 2.5 (Java 5 以降)、Robot Framework 2.0-2.1 が Jython 2.2 をサポートしています。

Jython をインストールしたら、 PATH_ を変更して、コマンドラインから Python コマンドと ``robot``, ``rebot`` :ref:`テスト実行スクリプト <runner scripts>` を実行できるように設定する必要があるでしょう。


.. _IronPython installation:

IronPython のインストール
~~~~~~~~~~~~~~~~~~~~~~~~~~~

IronPython_ を使えば、 Robot Framework を `.NET platform <http://www.microsoft.com/net>`_ 上で動かしたり、 C# や他の .NET 言語とその API にアクセスできます。
サポートしているバージョンは IronPython 2.7 のみです。

IronPython を使う場合、 `elementtree <http://effbot.org/downloads/#elementtree>`_ モジュールの
1.2.7 プレビューリリース版が必要です。というのも、 IronPython の配布物に入っている ``elementtree`` の実装は `壊れている <https://github.com/IronLanguages/main/issues/968>`_ からです。
``elementtree`` をインストールするには、ソース配布物をダウンロードして解凍し、解凍先ディレクトリで ``ipy setup.py install`` を実行します。

IronPython をインストールしたら、 PATH_ を変更して、コマンドラインから Python コマンドと ``robot``, ``rebot`` :ref:`テスト実行スクリプト <runner scripts>` を実行できるように設定する必要があるでしょう。


.. _Configuring PATH:

``PATH`` の設定
~~~~~~~~~~~~~~~~~~~~

環境変数 ``PATH`` は、システム上でコマンドを実行するときに、コマンドの実行ファイルがある場所を探すのに使うリストです。
コマンドプロンプトから Robot Framework を簡単に使うには、 :ref:`テスト実行スクリプト <runner scripts`> を ``PATH`` に入れておくよう勧めます。
インタプリタも ``PATH`` に入れておけば実行が楽です。

Python を UNIX 系のマシンで使う場合、 Python 自体とスクリプトは自動的に ``PATH`` 上のどこかに置かれるので、特に作業は必要ありません。
Windows などのシステムでは、 ``PATH`` を別途設定する必要があります。

.. tip::

   最新の Windows 向け Python インストーラには、インストール処理中に ``PATH`` を設定する機能があります。
   この機能はデフォルトでは無効になっていて、 `Customize Python` の画面で `Add python.exe to Path` を有効にする必要があります。
   有効にすると、Python のインストールディレクトリ直下と :file:`Scripts` ディレクトリの両方が ``PATH`` に追加されます。

.. _What directories to add to PATH:

どのディレクトリを ``PATH`` に追加すればいいの？
'''''''''''''''''''''''''''''''''''''''''''''''''''

どのディレクトリを ``PATH`` に追加すればよいかは、使っているインタプリタや OS によって違います。
最初に追加すべきは、インタプリタのインストール先 (:file:`C:\\Python27` など) で、もうひとつはスクリプトのインストール先です。
Windows 用の Python と IronPython は、スクリプトをインタプリタのインストールディレクトリの下の :file:`Scripts` (:file:`C:\\Python27\\Scripts` など) に置きます。
Jython は、オペレーティングシステムに関係なく、 :file:`bin` を使います (:file:`C:\\jython2.7.0\\bin` など)。
:file:`Scripts` や :file:`bin` は、インタプリタのインストール時にはなく、 Robot Framework やその他のサードパーティモジュールのインストール時に作成されるかもしれません。


.. _Setting PATH on Windows:

Windows の ``PATH`` の設定
'''''''''''''''''''''''''''

Windows では、以下の手順で ``PATH`` を設定します。
設定に使うメニューなどの名前は、 Windows のバージョンによって多少違うこともありますが、基本的なアプローチは同じです。

1. コントロールパネルから、「システムとセキュリティ」の「システム」メニューを選び、「システムの詳細設定」パネルで「環境変数」ボタンを押します。
   「ユーザー環境変数」と 「システム環境変数」がありますが、これはサインイン中のユーザだけの設定か、全てのユーザに影響する設定かの違いです。

2. 既存の ``PATH`` の値を変更するには、リストから ``PATH`` の項目を選んで、「編集 (E)」ボタンを押します。
   表示されたダイアログで、「変数値」の一番最後に、「 `;<インタプリタのインストールディレクトリ>;<スクリプトのインストールディレクトリ>` 」
   の形式でパスを追加します (例: `;C:\Python27;C:\Python27\Scripts`)。セミコロン (``;``) は重要なので忘れないようにしてください。
   リストに ``PATH`` がなく、新たに設定したいときは、「新規 (N)」ボタンを押して、ダイアログに変数名 ``PATH`` と変数値を入力します。
   このときは、先頭のセミコロンは要りません。

3. ダイアログを「OK」ボタンで閉じて、変更を適用します。

4. 新しくコマンドプロンプトを起動すると、変更が適用されます。

複数のバージョンの Python をインストールしている場合、 ``robot`` や ``rebot`` :ref:`テスト実行スクリプト <runner scripts>` は、常に ``PATH`` 上で **先に** 登場する Python インタプリタを、テスト実行スクリプトのパスがどこにあるかは関係なく使おうとするので注意してください。
インタプリタを指定して実行したければ、 `C:\Python27\python.exe -m robot` のように、 :ref:`インストールした robot モジュールを直接実行 <Executing installed robot module>` してください。

また、 ``PATH`` に設定するときは、(`"C:\Python27\Scripts"` のように ) 値をクオートで囲ってはなりません。
クオートすると、 `Python プログラムの実行がうまくいかない <http://bugs.python.org/issue17023>`_ ことがあります。
Windows では、ディレクトリパスにスペースが入っていても、クオートは必要ありません。


.. _Setting PATH on UNIX-like systems:

UNIX系システムでの ``PATH`` の設定
'''''''''''''''''''''''''''''''''''''

UNIX系システムでは、通常、システム全体設定用または個別ユーザ設定用の設定ファイルを編集する必要があります。
どのファイルを編集すべきかは、システムによって異なります。そのため、詳しくは OSのドキュメントを参照してください。

.. _Setting https_proxy:

``https_proxy`` の設定
~~~~~~~~~~~~~~~~~~~~~~~

`PIP でインストール <Installing with pip>`_ する場合、環境変数 ``https_proxy`` を設定する必要があります。
この環境変数は、 pip 自体のインストールと、 Robot Framework や他の Python パッケージインストールに必要です。

``https_proxy`` の設定方法は、 `PATH の設定 <configuring PATH>`_ と同様、 OS によって異なります。
変数の値は、通常は `http://10.0.0.42:8080` のようにプロキシの URL です。

.. _Installing with pip:

pip のインストール
-------------------

pip_ は Python 標準のパッケージマネジャですが、他にも
`Buildout <http://buildout.org>`_ や
`easy_install <http://peak.telecommunity.com/DevCenter/EasyInstall>`_ があります。
このドキュメントでは pip でのインストール手順しか解説しませんが、他のパッケージマネジャでも Robot Framework をインストールできます。

最新の Python , Jython, IronPython には、 pip がバンドルされています。
どのバージョンの Python に pip が入っているか、使えるようにする方法などは、以降の節で解説します。
pip の最新版が必要なときは、 pip_ のプロジェクトページを参照してください。

.. note:: 
   pip でインストールできるのは、Robot Framework 2.7 以降からです。
   それ以前のバージョンのインストールは、ソースコードからのインストールなど、他のアプローチが必要です。

.. _Installing pip for Python:

Python に pip を入れる
~~~~~~~~~~~~~~~~~~~~~~~~~

Python 2.7.9 からは、標準の Windows インストーラは pip を自動でインストールして有効にします。
PATH_ と、必要に応じて `https_proxy`_ が正しく設定されていていれば、 Python をインストールした後、すぐに `pip install robotframework` で Robot Framework をインストールできます。

Windows 以外のプラットフォームや、古いバージョンの Python では、 pip を自分でインストールせねばなりません。
Linux で、 Apt や Yum のようなパッケージマネジャが使えるなら、パッケージマネジャで pip_ をインストールできます。
とはいえ、 pip_ はいつでも pip_ のプロジェクトページから手動でインストールできます。

複数のバージョンの Python をインストールしていて、それぞれに pip をインストールしている場合、実行される ``pip`` コマンドは、 PATH_ 上で最初に見つかったものです。
pip を動かす Python のバージョンを特定したければ、その Python を使って ``pip`` モジュールを呼び出してください:

.. sourcecode:: bash

    python -m pip install robotframework
    python3 -m pip install robotframework

.. _Installing pip for Jython:

Jython に pip を入れる
~~~~~~~~~~~~~~~~~~~~~~~~~

Jython 2.7 には pip がバンドルされていますが、有効にするには以下のコマンドを実行せねばなりません:

.. sourcecode:: bash

    jython -m ensurepip

Jython は pip を :file:`<JythonInstallation>/bin` ディレクトリにインストールします。
他の Python の pip が入っている場合、 `pip install robotframework` で Jython 上にインストールできるかどうかは PATH_ の設定次第です。
pip を使う Jython を特定したければ、以下のように Jython から ``pip`` モジュールを呼び出します:

.. sourcecode:: bash

    jython -m pip install robotframework

.. _Installing pip for IronPython:

IronPython に pip を入れる
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

IronPython には、 `バージョン 2.7.5 <http://blog.ironpython.net/2014/12/pip-in-ironpython-275.html>`_ から pip がバンドルされています。
Jython と同様、まず有効にする必要があります:

.. sourcecode:: bash

    ipy -X:Frames -m ensurepip

IronPython の場合、pip を有効にするときも、使うときにも `-X:Frames` コマンドラインオプションが必要なので注意してください。

IronPython は pip を :file:`<IronPythonInstallation>/Scripts` ディレクトリに配置します。
他の Python の pip が入っている場合、 `pip install robotframework` で IronPython 上にインストールできるかどうかは PATH_ の設定次第です。
pip を使う IronPython を特定したければ、以下のように IronPython から ``pip`` モジュールを呼び出します:


.. sourcecode:: bash

    ipy -X:Frames -m pip install robotframework

バージョン 2.7.5 以前の IronPython は pip をサポートしていません。


.. _Using pip:

pip を使う
~~~~~~~~~~~~

pip_ をインストールしたら (そして、プロキシの下にいる場合は `https_proxy`_ を設定したら)、あとの使い方はとても簡単です。
最も簡単な使い方は、 pip に全てお任せして、 `Python Package Index (PyPI) <https://pypi.python.org/>`_ から必要なパッケージを見つけてダウンロードさせ、インストールさせるというものですが、 pip には PyPI 上の個別のパッケージを指定してインストールする機能もあります。
基本的な使い方は下記の通りで、 pip_ のドキュメントにはより詳しい説明やサンプルがあります。

.. sourcecode:: bash

    # 最新版をインストールする
    pip install robotframework

    # 最新版にアップグレードする
    pip install --upgrade robotframework

    # 特定のバージョンをインストールする
    pip install robotframework==2.9.2

    # 別途ダウンロードしたパッケージをインストールする (ネットワーク接続不要)
    pip install robotframework-3.0.tar.gz

    # アンインストール
    pip uninstall robotframework

pip 1.4 以降からは、デフォルトの設定で安定版しかインストールしないので注意してください。
アルファ・ベータ版やリリース候補版をインストールしたいなら、バージョンを明示するか、 :option:`--pre` を使ってください:

.. sourcecode:: bash

    # 3.0 beta 1 を入れる
    pip install robotframework==3.0b1

    # 最新版がプレリリース版でもインストールする
    pip install --pre --upgrade robotframework

.. _Installing from source:

ソースからインストールする
----------------------------

このインストール方法は、どの OS でも利用でき、全ての Python インタプリタに対応しています。
インストールを *ソースから* なんて怖そうですが、実際のところはとても単純です。

.. _Getting source code:

ソースコードを手に入れる
~~~~~~~~~~~~~~~~~~~~~~~~~~

ソースコードは通常、 ``.tar.gz`` 形式の *ソース配布パッケージ* をダウンロードして手に入れます。
新しいパッケージは PyPI にもありますが、バージョン 2.8.1 以前のバージョンは `Google Code のダウンロードページ <https://code.google.com/p/robotframework/downloads/list?can=1>`_ から手に入れねばなりません。
パッケージをダウンロードしたら、ファイルをどこかに展開してください。 `robotframework-<version>` という名前のディレクトリができるはずです。
このディレクトリには、インストール作業に必要なソースコードとスクリプトが入っています。

ソースコードは、プロジェクトの `GitHub リポジトリ <https://github.com/robotframework/robotframework>`_ から直接入手する方法もあります。
GitHub では最新のコードを配布していますが、リリースバージョンやタグを指定して、特定のバージョンにスイッチできます。

.. _Installation:

インストール
~~~~~~~~~~~~~~~

ソースコードからのビルドには、Python標準の ``setup.py`` スクリプトを使います。このスクリプトはソースコードの入ったディレクトリに置かれていて、コマンドラインからインタプリタで実行して使います:

.. sourcecode:: bash

   python setup.py install
   jython setup.py install
   ipy setup.py install

``setup.py`` スクリプトには様々な引数を指定できます。たとえば、デフォルトのインストール先以外を指定して、管理者権限をもたなくてもインストールできます。
詳しくは `python setup.py --help` を実行してみてください。

.. _Standalone JAR distribution:

スタンドアロンの JAR 配布物
-------------------------------

Robot Framework は、スタンドアロンの Java アーカイブとしても配布されています。この配布物には Jython_ と Robot Framework の両方が入っているので、 Java_ さえあればインストールできます。
JAR でのインストールは、ひとつのパッケージで必要なものが全て手に入るところですが、通常の Python_ インタプリタが使えないという欠点もあります。

パッケージのファイル名は ``robotframework-<version>.jar`` の形式で、 `Maven central`_ から入手できます。パッケージをダウンロードしたら、以下のように実行してください:

.. sourcecode:: bash

  java -jar robotframework-3.0.jar mytests.robot
  java -jar robotframework-3.0.jar --variable name:value mytests.robot

Rebot を使って :ref:`出力のポストプロセス <post-process outputs>` を実行したい場合や、組み込みの :ref:`サポートツール群 <supporting tools>` を使いたければ、 ``rebot``, ``libdoc``, ``testdoc``, ``tidy`` といったコマンド名を JAR ファイルの最初の引数に指定します:

.. sourcecode:: bash

  java -jar robotframework-3.0.jar rebot output.xml
  java -jar robotframework-3.0.jar libdoc MyLibrary list

各コマンドの詳しい説明は、引数なしで JAR コマンドを実行すると表示されます。

スタンドアロン JAR 版は、バージョン 2.9.2 から、 Python の標準ライブラリと Robot Framework モジュールの他に、 yaml でかかれた変数ファイルを扱うための PyYAML が入っています。

.. _Manual installation:

マニュアルインストール
------------------------

Robot Framework のインストールを自動で行いたくない場合、以下のステップでマニュアルインストールできます:

1. ソースコードを入手します。コードは全て、 :file:`robot` というディレクトリ (Python パッケージ) に入っています。
   `ソースコード配布物 <source distribution>`_ がある場合か、バージョン管理システムからチェックアウトした場合は、 :file:`src` ディレクトリ下にあります。

2. ソースコードを任意の場所にコピーします。

3. `テストの実行方法 <how to run tests>`_ を決めます。


.. _Verifying installation:

インストール内容を確認する
----------------------------

インストールがうまくいったら、 :ref:`テストランナースクリプト <runner scripts>` を :option:`--version` オプション付きで実行でき、 Robot Framework とインタプリタのバージョンが表示されるはずです:

.. sourcecode:: bash

   $ robot --version
   Robot Framework 3.0 (Python 2.7.10 on linux2)

   $ rebot --version
   Rebot 3.0 (Python 2.7.10 on linux2)

ランナースクリプトが「コマンドがありません」のようなメッセージで失敗する場合は、まず PATH_ の設定が正しいか調べてみてください。
解決しなければ、このドキュメントの関連する節をもう一度読み、インターネットで `robotframework-users <http://groups.google.com/group/robotframework-users/>` メーリングリストなどに助けを求めてください。


.. _Where files are installed:

ファイルのインストール先
~~~~~~~~~~~~~~~~~~~~~~~~~

自動インストーラを使った場合は、 Robot Framework のソースコードは、サードパーティの Python モジュールのインストール場所に置かれています。
UNIX 系の OS では、たいてい Python はプリインストールで、その場所はさまざまです。
Windows でインタプリタを自分でインストールしたなら、 :file:`C:\\Python27\\Lib\\site-packages` のように、インタプリタをインストールしたディレクトリの下にある :file:`Lib/site-packages` です。
Robot Framework 本体のコードは :file:`robot` という名前のディレクトリ下に収まっています。

Robot Framework の :ref:`実行スクリプト <runner scripts>` は、コードとは別に、プラットフォームごとに異なる場所に作成されます。
UNIX 系のシステムであれば、通常は :file:`/usr/bin` や :file:`/usr/local/bin` です。
Windows や Jython, IronPython の場合は、スクリプトはインタプリタのインストールディレクトリの下の :file:`Scripts` または :file:`bin` ディレクトリに配置されます。

.. _Uninstallation:

アンインストール
---------------------

Robot Framework のアンインストールには、 pip_ を使うのが一番簡単です:

.. sourcecode:: bash

   pip uninstall robotframework

pip のいいところは、ソースコードからインストールしたパッケージもアンインストールできるところです。
pip が使えないか、特定の場所に `手作業でインストール <manual installation>`_ した場合には、
`どこにファイルをインストールしたか <where files are installed>`_ を調べて、手作業で削除してください。

PATH_ などの環境変数を変更したのなら、別途元に戻してください。

.. _Upgrading:

アップグレード
--------------------

pip_ を使っているなら、新しいバージョンへのアップグレードは :option:`--upgrade` を使います。
バージョンを指定して特定のバージョンへの変更もできます:

.. sourcecode:: bash

   pip install --upgrade robotframework
   pip install robotframework==2.9.2

pip を使っている場合、以前のバージョンは自動的にアンインストールされます。
`ソースコードからインストール <installing from source>`_ した場合、既存のインストールに上書きしてかまいません。
何か問題があれば、一旦 `アンインストール <uninstallation>`_ してからインストールしなおすとうまくいくでしょう。

Robot Framework をアップグレードする場合、以前のバージョンと互換性のない変更のために、既存のテストやテスト環境に影響が及ぶかもしれません。
そのような変更は、 2.8.7 や 2.9.2 のようなマイナーバージョンではほとんどありませんが、バージョン 2.9 や 3.0 といったメジャーバージョンの変更ではよくあります。
互換性のない変更や撤廃された機能についてはリリースノートに記載してあるので、メジャーバージョンを切り替えるときにはよく調べておいてください。

.. _Executing Robot Framework:

Robot Framework の実行
-------------------------

.. _runner script:
.. _runner scripts:
.. _Using robot and rebot scripts:

``robot`` や ``rebot`` スクリプトの実行
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Robot Framework 3.0 から、 ``robot`` スクリプトでテストを実行して、 ``rebot`` スクリプトで結果を処理できるようになりました:

.. sourcecode:: bash

    robot tests.robot
    rebot output.xml

これらのスクリプトは、通常のインストール手順でインストールされ、 PATH_ が正しく設定されていれば直接実行できます。
スクリプトは Python で実装されています。ただし、 Windows では起動用のバッチファイルもあります。

以前のバージョンの Robot Framework には、 ``robot`` スクリプトがなく、 ``rebot`` ツールも別途 Python を使ってインストールせねばなりませんでした。
その代わり、テストの実行は ``pybot``,  ``jybot``,  ``ipybot``  で行い、テスト結果のポストプロセスには ``jyrebot`` や ``ipyrebot`` を使っていました。
これらのスクリプトは、現在の Robot Framework でも使えますが、将来は廃止される予定です。

.. _Executing installed robot module:

``robot`` モジュールの実行
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

テストを実行するもう一つの方法は、インストール済みの ``robot`` モジュールや、サブモジュールの ``robot.run`` を、 Python の
`-m コマンドラインオプション <https://docs.python.org/2/using/cmdline.html#cmdoption-m>`_ で実行するやりかたです。
この方法は、複数のバージョンの Python で Robot Framework を実行したい場合に特に便利です:

.. sourcecode:: bash

    python -m robot tests.robot
    python3 -m robot.run tests.robot
    jython -m robot tests.robot
    /opt/jython/jython -m robot tests.robot

``python -m robot`` は、 Robot Framework 3.0 で新たに使えるようになった書き方です。
以前のバージョンでは、 Python 2.6 以降であれば、 ``python -m robot.run`` で実行できます。

テスト結果出力のポストプロセスも同じやりかたで実行できますが、モジュール名は ``robot.rebot`` です:

.. sourcecode:: bash

    python -m robot.rebot output.xml


.. _Executing installed robot directory:

``robot`` モジュールのインストールディレクトリを指定して実行する
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Robot Framework のインストール先が分かっていれば、 :file:`robot`  ディレクトリや :file:`run.py` ファイルの場所を直接指定して実行できます:

.. sourcecode:: bash

   python path/to/robot/ tests.robot
   jython path/to/robot/run.py tests.robot

ディレクトリ指定は Robot Framework 3.0 で登場したやり方で、以前のバージョンでは :file:`robot/run.py` ファイルを指定してください。

同様に、ポストプロセスも :file:`robot/rebot.py` ファイルの指定でできます。

.. sourcecode:: bash

   python path/to/robot/rebot.py output.xml

この方法での実行は、Robot Framework を `手作業でインストール <manual installation>`_ した場合に便利です。

.. These aliases need an explicit target to work in GitHub
.. .. _precondition: `Preconditions`_
.. _PATH: `Configuring PATH`_
.. _https_proxy: `Setting https_proxy`_
.. _source distribution: `Getting source code`_
.. .. _runner script: `Using robot and rebot scripts`_
.. .. _runner scripts: `Using robot and rebot scripts`_
