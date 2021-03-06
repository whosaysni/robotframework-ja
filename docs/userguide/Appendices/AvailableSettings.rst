.. _All available settings in test data:

テストデータで使える設定
======================

.. contents::
   :depth: 2
   :local:

settings テーブル
------------------

settings テーブルは、テストライブラリやリソースファイル、変数ファイルなどのインポート、テストスイートやテストケースのメタデータの定義に使います。
settings テーブルは、テストケースファイルとリソースファイルに書けます。
ただし、リソースファイルの中では、 settings テーブルはライブラリ・リソース・変数のインポートにしか使えません。

.. table:: settings テーブルで使える設定
   :class: tabular

   +-----------------+--------------------------------------------------------+
   |       名前      |                         説明                           |
   +=================+========================================================+
   | Library         | `ライブラリのインポート`__                             |
   +-----------------+--------------------------------------------------------+
   | Resource        | `リソースファイルの利用`__                             |
   +-----------------+--------------------------------------------------------+
   | Variables       | `変数ファイルの利用`__                                 |
   +-----------------+--------------------------------------------------------+
   | Documentation   | `テストスイート`__ や `リソースファイル`__ の          |
   |                 | ドキュメント                                           |
   +-----------------+--------------------------------------------------------+
   | Metadata        | `任意のテストスイートメタデータ`__                     |
   +-----------------+--------------------------------------------------------+
   | Suite Setup     | `テストスイートのセットアップ`__                       |
   +-----------------+--------------------------------------------------------+
   | Suite Teardown  | `テストスイートのティアダウン`__                       |
   +-----------------+--------------------------------------------------------+
   | Force Tags      | `テストケースにタグを付ける`__ ときの強制タグ          |
   +-----------------+--------------------------------------------------------+
   | Default Tags    | `テストケースにタグを付ける`__ ときのデフォルトタグ    |
   +-----------------+--------------------------------------------------------+
   | Test Setup      | デフォルトの `テストセットアップ<test setup>`__        |
   +-----------------+--------------------------------------------------------+
   | Test Teardown   | デフォルトの `テストティアダウンtest teardown`__       |
   +-----------------+--------------------------------------------------------+
   | Test Template   | テストケースのデフォルトの `テンプレートキーワード`__  |
   +-----------------+--------------------------------------------------------+
   | Test Timeout    | デフォルトの `テストケースタイムアウト`__              |
   +-----------------+--------------------------------------------------------+

.. note:: 設定の名前の末尾には、 :setting:`Documentation:` のようにコロンを付加できます。プレーンテキスト形式のときなどに、読みやすくなります。

__ `importing libraries`_
__ `taking resource files into use`_
__ `taking variable files into use`_
__ `Test suite documentation`_
__ `Documenting resource files`_
__ `free test suite metadata`_
__ `suite setup`_
__ `suite teardown`_
__ `tagging test cases`_
__ `tagging test cases`_
__ `test setup`_
__ `test teardown`_
__ `template keyword`_
__ `test case timeout`_

Test Case テーブル
-------------------

テストケーステーブルの設定は、設定の書かれたテストケース内で有効です。
設定の中には、 settings テーブルで定義されたデフォルト値を上書きするものもあります。

.. table:: テストケーステーブルで使える設定
   :class: tabular

   +-----------------+--------------------------------------------------------+
   |      名前       |                         説明                           |
   +=================+========================================================+
   | [Documentation] | `テストケースのドキュメント`__ の指定                  |
   +-----------------+--------------------------------------------------------+
   | [Tags]          | `テストケースのタグ`__ の指定                          |
   +-----------------+--------------------------------------------------------+
   | [Setup]         | `テストセットアップ`__ の指定                          |
   +-----------------+--------------------------------------------------------+
   | [Teardown]      | `テストティアダウン`__ の指定                          |
   +-----------------+--------------------------------------------------------+
   | [Template]      | `テンプレートキーワード`__ の指定                      |
   +-----------------+--------------------------------------------------------+
   | [Timeout]       | `テストケースのタイムアウト`__ の指定                  |
   +-----------------+--------------------------------------------------------+

__ `test case documentation`_
__ `tagging test cases`_
__ `test setup`_
__ `test teardown`_
__ `template keyword`_
__ `test case timeout`_

キーワードテーブルの設定は、定義したユーザキーワードの中だけで有効です。

.. table:: キーワードテーブルで使える設定
   :class: tabular

   +-----------------+--------------------------------------------------------+
   |      名前       |                         説明                           |
   +=================+========================================================+
   | [Documentation] | `ユーザキーワードのドキュメント`__ の指定              |
   +-----------------+--------------------------------------------------------+
   | [Tags]          | `ユーザキーワードのタグ`__ の指定                      |
   +-----------------+--------------------------------------------------------+
   | [Arguments]     | `ユーザキーワードの引数`__ の指定                      |
   +-----------------+--------------------------------------------------------+
   | [Return]        | `ユーザキーワードの戻り値`__ の指定                    |
   +-----------------+--------------------------------------------------------+
   | [Teardown]      | `ユーザキーワードのティアダウン`__ の指定              |
   +-----------------+--------------------------------------------------------+
   | [Timeout]       | `ユーザキーワードのタイムアウト`__ の指定              |
   +-----------------+--------------------------------------------------------+

__ `user keyword documentation`_
__ `user keyword tags`_
__ `user keyword arguments`_
__ `user keyword return values`_
__ `user keyword teardown`_
__ `user keyword timeout`_
