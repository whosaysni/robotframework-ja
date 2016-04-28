.. default-role:: code

.. _Robot Framework Quick Start Guide:

========================================
Robot Framework クイックスタートガイド
========================================

Copyright © Nokia Networks. Licensed under the
`Creative Commons Attribution 3.0 Unported`__ license.

__ http://creativecommons.org/licenses/by/3.0/

和訳: Yasushi Masuda (@whosaysni)

.. contents:: Table of contents:
   :local:
   :depth: 2

.. Introduction

はじめに
============

.. About this guide

このガイドについて
--------------------

*Robot Framework クイックスタートガイド* では、 `Robot Framework <http://robotframework.org>`_ の最も重要な機能を紹介します。
この文書は、単に読んでデモを眺めるだけでなく、文書のソース rst ファイルを `デモとして実行 <Executing this guide>`_ できます。
ここで紹介する各機能は、 `Robot Framework ユーザガイド <Robot Framework User Guide>`_ で詳しく説明しています。

.. _Robot Framework User Guide: http://robotframework.org/robotframework/#user-guide
.. _Robot Framework overview:

Robot Framework の概要
------------------------

`Robot Framework`_ は、受け入れテストやテスト駆動開発 (ATDD) のための、オープンソースの汎用テスト自動化フレームワークです。
簡単に扱えるテーブル形式のテストデータ記述方法を備えていて、キーワード駆動型のテストアプローチに便利です。
テスト機能は Python や Java でテストライブラリを書いて拡張できます。
ユーザは既存のキーワードを使って新しい高水準キーワードを定義でき、それを使ってテストケースを書けます。

Robot Framework は、特定の OS やアプリケーションに依存しません。
コアのフレームワークは `Python <http://python.org>`_ で書かれていて、 (Java VM で動作する) `Jython <http://jython.org>`_ や、 (.NET 上の) `IronPython <http://ironpython.net>`_ でも動作します。
Robot Framework は、別途開発された様々な汎用テストライブラリやツールに取り囲まれ、充実したエコシステムを形成しています。

Robot Framework とそのエコシステムの詳細を知りたければ、 http://robotframework.org をご覧ください。
豊富なドキュメント、デモプロジェクト、テストライブラリもろもろ、ツール類などが置かれています。

.. _Demo application:

デモアプリケーション
-----------------------

ここでは、本ガイドで扱うサンプルのアプリケーションについて解説します。
アプリケーションは、伝統的なログイン操作テストの変型で、 Python で作ったコマンドラインベースの認証サーバにログインするというものです。
このアプリケーションで、ユーザは以下の3つの操作ができます:

- 適切なパスワードでアカウントを作る
- 有効なユーザとパスワードでログインする
- 既存のアカウントのパスワードを変更する

アプリケーション本体は `<sut/login.py>`_ ファイルで、 `python sut/login.py` コマンドで実行できます。
存在しないユーザや、不正なパスワードでログインを試みた場合は、以下のメッセージを返します::

    > python sut/login.py login nobody P4ssw0rd
    Access Denied

適切なパスワードの設定されたユーザアカウントを作成した後だと、ログインに成功します::

    > python sut/login.py create fred P4ssw0rd
    SUCCESS

    > python sut/login.py login fred P4ssw0rd
    Logged In

パスワードに使う文字列には、二つの要件があります。
一つは長さが 7〜12 文字でなければならないこと、もう一つは小文字と大文字、数字が入っていて、特殊文字を含まないことです。
適切でないパスワードでユーザを作成を試みると失敗します::

    > python sut/login.py create fred short
    Creating user failed: Password must be 7-12 characters long

    > python sut/login.py create fred invalid
    Creating user failed: Password must be a combination of lowercase and
    uppercase letters and numbers

現在のパスワードに不正なパスワードを指定して、新たなパスワードの設定を試みると、不正なパスワードでログインを試みた時と同じエラーを返します。
新しいパスワードにも、パスワードの要件が適用され、不適切な場合にはエラーメッセージを返します::

    > python sut/login.py change-password fred wrong NewP4ss
    Changing password failed: Access Denied

    > python sut/login.py change-password fred P4ssw0rd short
    Changing password failed: Password must be 7-12 characters long

    > python sut/login.py change-password fred P4ssw0rd NewP4ss
    SUCCESS

このアプリケーションは、簡単なデータベースファイルを使って、ユーザの状態を保持します。
ファイルは OS 依存の一時ディレクトリ下に保管されています。

.. _Executing this guide:

ガイドを実行する
====================

以下では、ガイドのテスト内容を自分で実行する方法を解説します。
この手順を実行しない場合は、オンラインで `結果を表示 <Viewing results>`_ できません。

.. Installations:

インストール
-------------

Python_ に Robot Framework をインストールするお勧めの方法は `pip <http://pip-installer.org>`_ です。 Python と pip の両方が入っているなら、単に::

    pip install robotframework

とするだけでインストールできます。
その他のインストール方法や、インストールに関する一般的な情報は  `インストールガイド <Robot Framework installation instructions>`_  を参照してください。

この文書は `reStructuredText <http://docutils.sourceforge.net/rst.html>`_ マークアップで書かれたデモになっていて、 Robot Framework のテストデータは文書中にコードブロックとしてマークされています。
この形式のテストを実行するには、 `docutils <https://pypi.python.org/pypi/docutils>`_ モジュールのインストールも必要です::

    pip install docutils

Robot Framework 3.0 は、 Python 3 をサポートするようになった最初のバージョンです。
Python 2 と Python 3 の情報は、前述の `インストールガイド <Robot Framework installation instructions>`_  を参照してください。

.. _`Robot Framework installation instructions`:
   https://github.com/robotframework/robotframework/blob/master/INSTALL.rst
.. _`installation instructions`: `Robot Framework installation instructions`_

.. _Execution:

実行
------

Robot Framework をインストールできたら、今度はデモを手に入れます。
`リリース版のファイル`__ か `最新版のファイル`__ を手に入れて解凍するのが楽ですが、 `プロジェクトのリポジトリ`__ を clone しても入手できます。

インストールが完了して、もろもろ準備ができたら、コマンドラインで `robot` コマンドを使ってデモを実行します::

    robot QuickStart.rst

Robot Framework 2.9 以前を使っているなら、 `robot` コマンドの代わりに `pybot` を使ってください::

    pybot QuickStart.rst

設定を変えて実行したければ、コマンドラインオプションを追加します::

    robot --log custom_log.html --name Custom_Name QuickStart.rst

利用できるオプションは `robot --help` で確認できます。

__ https://github.com/robotframework/QuickStartGuide/releases
__ https://github.com/robotframework/QuickStartGuide/archive/master.zip
__ https://github.com/robotframework/QuickStartGuide

.. _Viewing results:

結果を表示する
---------------

デモを実行すると、以下の結果ファイルが生成されます。
このページのリンクは、あらかじめデモを実行して作っておいたファイルへのリンクですが、読者の手元でデモを実行したときには、結果ファイルは手元の実行環境に生成されます。

`report.html <http://robotframework.org/QuickStartGuide/report.html>`_
    高水準のテストレポート。
`log.html <http://robotframework.org/QuickStartGuide/log.html>`_
    詳しいテスト実行ログ。
`output.xml <http://robotframework.org/QuickStartGuide/output.xml>`_
    機械可読な XML のフォーマット。

.. _Test cases:

テストケース
==============

.. _Workflow tests:

ワークフローテスト
---------------------

Robot Framework のテストケースは、簡単なテーブル形式です。
（※ここでは、タブやスペースなどで区切った形式を、テーブル形式と呼んでいます）
例えば、以下のテーブルは二つのテストを定義しています:

- User can create an account and log in （ユーザはアカウントを作成してログインできる）
- User cannot log in with bad password （ユーザは不正なパスワードでログインできない）

.. code:: robotframework

    *** Test Cases ***
    User can create an account and log in
        Create Valid User    fred    P4ssw0rd
        Attempt to Login with Credentials    fred    P4ssw0rd
        Status Should Be    Logged In

    User cannot log in with bad password
        Create Valid User    betty    P4ssw0rd
        Attempt to Login with Credentials    betty    wrong
        Status Should Be    Access Denied

自動化テストのテストケース定義データというよりは、英語で書かれた手作業のテスト手順書のように読めますね。
Robot Framework はキーワード駆動型のアプローチをとっているので、自然言語のもつ特質をうまく利用した書き方ができるのです。

テストケースは、キーワードや引数を使って作られています。
Robot Framework のルールでは、キーワードと引数は、少なくとも二つ以上のスペースか、タブで区切る必要があります。
基本的には、 4 つのスペースで区切る方法を推奨しています。これは、2スペースやタブよりも区切りがはっきりしていて、引数を他の行と綺麗に揃えて書きやすいことが多いからです。
テストケースの書き方の詳細は、 `ユーザガイド <Robot Framework User Guide>`_ を参照してください。

.. _Higher-level tests:

高水準のテスト
------------------

引数をとらない高水準のテストだけでも、テストケースは書けます。
このやり方なら、技術に詳しくない顧客やプロジェクトのステークホルダに対して、ほぼ普通の文章でテスト内容のコミュニケーションができます。
この利点は `受け入れテスト駆動開発`__ (ATDD) や類似の手法で、作成したテストそのものが要求仕様も表している場合には特に重要です。

また、Robot Framework は、テストケースの書き方を何か一つに制限してはいません。
例えば、よく使われる書き方の一つは、 `ビヘイビア駆動開発`__ (BDD: behavior-driven development) の
*given-when-then* 型の書き方もできます:

.. code:: robotframework

    *** Test Cases ***
    User can change password
        Given a user has a valid account
        When she changes her password
        Then she can log in with the new password
        And she cannot use the old password anymore

__ http://en.wikipedia.org/wiki/Acceptance_test-driven_development
__ http://en.wikipedia.org/wiki/Behavior_driven_development

.. _Data-driven tests:

データ駆動テスト
-----------------

複数のテストケースが、ちょっとだけ入出力が違うことを除いて、ほとんど同じということが多々有ります。
そんな状況では、 *データ駆動テスト (data-driven test)* を使えば、ワークフローを複製することなく、テストデータだけを変えてテストできます。
Robot Framework では、 `[Template]` 設定を使うと、テストケースをデータ駆動型テストに変更でき、テストケースに列挙したデータを使って、テンプレートのキーワードを次々に実行できます:

.. code:: robotframework

    *** Test Cases ***
    Invalid password
        [Template]    Creating user with invalid password should fail
        abCD5            ${PWD INVALID LENGTH}
        abCD567890123    ${PWD INVALID LENGTH}
        123DEFG          ${PWD INVALID CONTENT}
        abcd56789        ${PWD INVALID CONTENT}
        AbCdEfGh         ${PWD INVALID CONTENT}
        abCD56+          ${PWD INVALID CONTENT}

個々のテストに `[Template]` を設定する方法の他に、このガイドの後で説明する `セットアップやティアダウン <setups and teardowns>`_ の設定のように `Test Template` を一度だけ設定しておくことも可能です。
そうすれば、例えばこのテストケースなら、「短すぎるパスワード」「長すぎるパスワード」などといった不正なケース用に、別の名前のついたテストを作りやすくなります。
とはいえ、テストファイル全体で共通のテンプレートが適用されてしまうので、同じテンプレートを使うテストだけを、別のテストファイルに移動する必要があるでしょう。

ちなみに、上のケースでは、エラーメッセージを `変数 <variables>`_ で表現しています。

.. Keywords:

キーワード
===========

テストケースに使うキーワードは、二つの場所で定義できます。一つは `ライブラリキーワード <Library keywords>`_ で、テストライブラリをインポートして使います。もう一つは `ユーザ定義キーワード <user keywords>`_ で、テストケースを作るのと同様、テーブル形式で作成するものです。

.. _Library keywords:

ライブラリキーワード
---------------------

Robot Framework では、最も低水準のキーワードは、 Python や Java のような標準的なプログラム言語で記述されています。
Robot Framework には沢山の `テストライブラリ <test libraries>`_ がありますが、大きく *標準ライブラリ* 、 *外部ライブラリ* 、 *カスタムライブラリ* の3つに分類できます。 `標準ライブラリ <standard libraries>`_ とは、フレームワーク本体と一緒に配布されている汎用のライブラリで、 `OperatingSystem` (ファイル操作など、OS 関連)、 `Screenshot` (スクリーンキャプチャ機能)、 `BuiltIn` (特に何もしなくて使える、基本機能を提供する特別なライブラリ) などがあります。
Webテストに使う Selenium2Library_ のような外部ライブラリは、手作業でインストールする必要があります。
現在入手できるテストライブラリだけで足りない時は、 `自分でライブラリを作成 <Creating test libraries>`_ できます。

テストライブラリ中のキーワードを使うには、まずライブラリの利用を宣言せねばなりません。
このガイドのテストには、 `OperatingSystem` ライブラリのキーワード (例えば `Remove File`)
と、カスタムメイドの `LoginLibrary` のキーワード (例えば `Attempt to login with credentials`) が入っています。
それぞれのライブラリは、以下のように settings テーブルでインポートします:

.. code:: robotframework

    *** Settings ***
    Library           OperatingSystem
    Library           lib/LoginLibrary.py

.. _Test libraries: http://robotframework.org/#test-libraries
.. _Standard libraries: http://robotframework.org/robotframework/#standard-libraries
.. _Selenium2Library: https://github.com/rtomac/robotframework-selenium2library/#readme

.. _User keywords:

ユーザ定義のキーワード
--------------------------

ユーザがキーワードを組み合わせて高水準のキーワードを定義できるのが、 Robot Frmework の最も強力な機能の一つです。
このキーワードの定義機能は、 *ユーザ定義のキーワード* または *ユーザキーワード* と呼びます。
ユーザキーワードは、テストケースを書くのに似た方法で定義できます。
前述のテストケースに登場した高水準のキーワードは、以下のようなキーワードテーブルで作成しています:

.. code:: robotframework

    *** Keywords ***
    Clear login database
        Remove file    ${DATABASE FILE}

    Create valid user
        [Arguments]    ${username}    ${password}
        Create user    ${username}    ${password}
        Status should be    SUCCESS

    Creating user with invalid password should fail
        [Arguments]    ${password}    ${error}
        Create user    example    ${password}
        Status should be    Creating user failed: ${error}

    Login
        [Arguments]    ${username}    ${password}
        Attempt to login with credentials    ${username}    ${password}
        Status should be    Logged In

    # 以下のキーワードは高水準のテストで使うためのもの
    # キーワードには given/when/then/and といったプレフィクスがないことに注意
    # ちなみにこれはコメントの書き方の例

    A user has a valid account
        Create valid user    ${USERNAME}    ${PASSWORD}

    She changes her password
        Change password    ${USERNAME}    ${PASSWORD}    ${NEW PASSWORD}
        Status should be    SUCCESS

    She can log in with the new password
        Login    ${USERNAME}    ${NEW PASSWORD}

    She cannot use the old password anymore
        Attempt to login with credentials    ${USERNAME}    ${PASSWORD}
        Status should be    Access Denied

ユーザ定義のキーワードには、他のユーザ定義キーワードやライブラリキーワードを含められます。
上の例でわかるように、ユーザ定義のキーワードは、パラメタを持たせたり、値を返させたりできます。
定義の中で、 FOR ループを書くことも可能です。
ともあれ、大事なことは、ユーザ定義キーワードを上手く使えば、テスト作成者は、よく使う操作手順を再利用性の高いステップとして定義できるということです。
それに、ユーザ定義キーワードを活用すれば、テストの読みやすさをキープしたり、さまざまな状況に対応するために操作をうまく抽象化できるのです。

.. _Variables:

変数
=========

.. _Defining variables:

変数を定義する
------------------

変数は、 Robot Framework の絶対不可欠な機能です。
というのも、テストで使われるデータはたびたび変更されるので、変数で定義するのがベストだからです。
変数の定義はとても簡単で、以下のように変数テーブルを書くだけです:

.. code:: robotframework

    *** Variables ***
    ${USERNAME}               janedoe
    ${PASSWORD}               J4n3D0e
    ${NEW PASSWORD}           e0D3n4J
    ${DATABASE FILE}          ${TEMPDIR}${/}robotframework-quickstart-db.txt
    ${PWD INVALID LENGTH}     Password must be 7-12 characters long
    ${PWD INVALID CONTENT}    Password must be a combination of lowercase and uppercase letters and numbers

変数の値はコマンドラインからも指定できるので、異なる環境でテストを実行するときに便利です。
例えば、上のデモを PASSWORD を指定して実行したければ、以下のようにします::

   robot --variable USERNAME:johndoe --variable PASSWORD:J0hnD0e QuickStart.rst

ユーザ定義の変数の他に、定義しなくても使える組み込みの変数があります。上の例でも使われている `${TEMPDIR}` や `${/}` がその例です。

.. _Using variables:

変数を参照する
---------------

変数は、テストデータのほとんどどこにでも使えます。
最もよく使われるのは、以下のテストケースのようなキーワードの引数です。
キーワードを実行したときの戻り値もまた、変数に代入して後で利用できます。
例えば、下の例で `Database Should Contain` という `ユーザキーワード <user keyword>`_ は、ユーザデータベースのファイルを開いて、その内容を `${database}` という変数に入れ、 BuiltIn_ ライブラリの `Should Contain` キーワードを使って検証しています。
ライブラリのキーワードもユーザキーワードもどちらも戻り値を持たせられます。

.. _User keyword: `User keywords`_
.. _BuiltIn: `Standard libraries`_

.. code:: robotframework

    *** Test Cases ***
    User status is stored in database
        [Tags]    variables    database
        Create Valid User    ${USERNAME}    ${PASSWORD}
        Database Should Contain    ${USERNAME}    ${PASSWORD}    Inactive
        Login    ${USERNAME}    ${PASSWORD}
        Database Should Contain    ${USERNAME}    ${PASSWORD}    Active

    *** Keywords ***
    Database Should Contain
        [Arguments]    ${username}    ${password}    ${status}
        ${database} =     Get File    ${DATABASE FILE}
        Should Contain    ${database}    ${username}\t${password}\t${status}\n

.. _Organizing test cases:

テストケースを組織化する
=========================

.. _Test suites:

テストスイート
----------------

Robot Framework では、複数のテストケースを集めたものをテストスイートと呼んでいます。
テストケースの入った入力ファイルそれぞれが、テストスイートです。
このガイドのソースファイルを `テストとして実行 <executing this guide>`_ したなら、コンソール出力に `QuickStart` というテストスイート名が表示されたはずです。
この名前はファイル名から決めたもので、レポートやログにもこの名前で表示されます。

テストケースファイルをディレクトリに入れ、そのディレクトリをまた別のディレクトリの下に置くといった形で、テストケースを階層化できます。
ディレクトリを階層化すると、ディレクトリの名前とテストファイルの名前に基づいて、自動的に高水準のテストスイートが構築されます。
テストスイートは単なるファイルやディレクトリなので、バージョン管理システムに簡単に取り込んで管理できます。

.. _Setups and teardowns:

セットアップとティアダウン
----------------------------

テストスイート内の全てのテストについて、テストの前後に特定のキーワードを実行したいなら、 setting テーブルの `Test Setup` や `Test Teardown` を使います。
同様に `Suite Setup` や `Suite Teardown` 使うと、テストスイート全体の前後に実行したいキーワードを指定できます。

個別のテストケースでも、 `[Setup]` や `[Teardown]` でセットアップとティアダウンのカスタマイズができます。
この設定は、 `データ駆動型テスト <data-driven tests>`_ で使った `[Template]` と同じように働きます。

このデモでは、テストスイートの実行後と、各テストの実行後には必ずデータベースを消去する必要があるので、以下のように設定します:

.. code:: robotframework

    *** Settings ***
    Suite Setup       Clear Login Database
    Test Teardown     Clear Login Database

.. _Using tags:

タグ
------

Robot Framework には、テストケースにタグを設定することで、テストのメタデータを自由に設定する機能があります。
下の例のように、 setting テーブルに `Force Tags` や `Default Tags` を設定すると、全てのテストケースに対して同じタグをつけられます。
`先ほどの`__ `User status is stored in database` のテストケースのように、個別のテストに対して `[Tags]` を付けることも可能です。

__ `Using variables`_

.. code:: robotframework

    *** Settings ***
    Force Tags        quickstart
    Default Tags      example    smoke

テストを実行してレポートを確認すると、タグのついたテストは関連付けられ、タグごとにテスト結果をまとめた情報が出力されているはずです。
タグは他の用途にも使われます。例えば、実行したいテストを選ぶという重要な用途があります。
以下のように実行すると、 ``smoke`` や ``database`` といったタグのついたテストだけを実行します::

    robot --include smoke QuickStart.rst
    robot --exclude database QuickStart.rst

.. _Creating test libraries:

テストライブラリを自作する
==============================

Robot Framework は、簡単に使えるテストライブラリ自作用 API を、 Python と Java 向けに提供しています。
また、リモートライブラリインタフェースを使えば、他の言語でも実装できます。 
`ユーザガイド <Robot Framework User Guide>`_ には、ライブラリの詳しい使い方が記載されています。

例えば、デモで使っている `LoginLibrary` テストライブラリを見てみましょう。
ライブラリは `<lib/LoginLibrary.py>`_ にありますが、同じ内容を以下に示します。
例えば、以下のコードを見れば、 `Create User` が `create_user` というメソッドにどうやって対応付けられているかがわかります。

.. code:: python

    import os.path
    import subprocess
    import sys


    class LoginLibrary(object):

        def __init__(self):
            self._sut_path = os.path.join(os.path.dirname(__file__),
                                          '..', 'sut', 'login.py')
            self._status = ''

        def create_user(self, username, password):
            self._run_command('create', username, password)

        def change_password(self, username, old_pwd, new_pwd):
            self._run_command('change-password', username, old_pwd, new_pwd)

        def attempt_to_login_with_credentials(self, username, password):
            self._run_command('login', username, password)

        def status_should_be(self, expected_status):
            if expected_status != self._status:
                raise AssertionError("Expected status to be '%s' but was '%s'."
                                     % (expected_status, self._status))

        def _run_command(self, command, *args):
            command = [sys.executable, self._sut_path, command] + list(args)
            process = subprocess.Popen(command, stdout=subprocess.PIPE,
                                       stderr=subprocess.STDOUT)
            self._status = process.communicate()[0].strip()
