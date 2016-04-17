.. Introduction:
Robot Framework の紹介
========================


Robot Framework は、Python ベースの拡張可能なキーワード駆動型 (keyword-driven) テスト自動化フレームワークです。
エンドツーエンドの受け入れテストや受け入れテスト駆動開発 (ATDD) に使えます。
Robot Framework は、分散・機種混合環境で、様々な技術・インタフェースを使わねばならないアプリケーションのテストに利用できます。

.. contents::
   :depth: 2
   :local:


.. Why Robot Framework?:
Robot Framework を使う理由
------------------------------

- 簡単なテーブル形式で、一貫した書き方で :ref:`テストを作成<Creating test cases>` できます。

- 定義済みのキーワードを使って、再利用性の高い :ref:`高水準のキーワード <Creating user keywords>` を作れます。

- 読みやすい HTML 形式の :ref:`結果レポート <Report file>` と :ref:`ログ <Log levels>` を出力できます。

- 特定のプラットフォームやアプリケーションに依存しません。

- Python や Java でテストライブラリを自作するための簡単な :ref:`ライブラリAPI <Creating test libraries>` を備えています。

- 既存の様々なビルドインフラ (CI: 継続開発システム) と連携できるよう、 :ref:`コマンドラインインタフェース <Executing test cases>` を持ち、 XML ベースの :ref:`出力ファイル <Output file>` を生成します。

- `Selenium を使った Web テスト <https://selenium2library-ja.readthedocs.org/ja/latest/>`_ 、 Java の GUI テスト、プロセスの実行、 Telnet, SSH 操作などをサポートしています。

- :ref:`データ駆動のテストケース <Data-driven style>` 開発をサポートしています。

- 様々な環境でテストを使う際に便利な :ref:`変数 <variables>` を組み込みでサポートしています。

- テストに :ref:`タグ付け <Tagging test cases>` して、 :ref:`テストを選択的に実行 <Selecting test cases>` できます。

- ソースコード管理との連携が容易: :ref:`テストスイート <Creating test suites>` はファイルとディレクトリだけで構成され、成果物のコードと一緒にバージョン管理できます。

- :ref:`テストケース単位 <Test setup and teardown>` と :ref:`テストスイート単位 <Suite setup and teardown>` のでセットアップ・ティアダウンを実行できます。

- モジュラーな構造をとっているため、全く違うインタフェースを複数持つようなアプリケーション向けにもテストを書けます。


.. High-level architecture:
高水準のアーキテクチャ
-----------------------

Robot Framework は、特定のアプリケーションや技術に依存しない、汎用のフレームワークです。
以下の図のように、モジュラー性の高いアーキテクチャを備えています。

.. figure:: architecture.png

   Robot Framework のアーキテクチャ

:ref:`テストデータ <Creating test data>` は、シンプルで編集しやすいテーブル形式のフォーマットです。
Robot Framework を起動すると、フレームワークがテストデータを処理し、テストデータ中の  :ref:`テストケースを実行 <Executing test cases>` して、実行ログとレポートを生成します。フレームワークのコア部分は、テスト下にあるターゲットシステムの詳細は関知せず、 :ref:`テストライブラリ <Creating test libraries>` を通じてやり取りします。ライブラリはアプリケーションのインタフェースを直接使う場合もあれば、他の低水準のテストツールをテストドライバとして使う場合もあります。


.. _Screenshots:

スクリーンショット
---------------------

以下のスクリーンショットは、 :ref:`テストデータ <test data>` と、テストを実行して得た :ref:`レポート <reports>` や :ref:`ログ <logs>` の例です。

.. figure:: testdata_screenshots.png

   テストケースファイル

.. figure:: screenshots.png

   テストレポートとログ


.. _Getting more information:

詳しい情報を探すには
------------------------

.. _Project pages:

Robot Framework プロジェクトのページ
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Robot Framework やそれをとりまくエコシステムの情報がまとまっている一番の場所は、なんといっても  http://robotframework.org です。フレームワーク自体のソースコードは `GitHub <https://github.com/robotframework/robotframework>`_ 上で管理されています。


.. _mailing list:
.. _Mailing lists:

メーリングリスト
~~~~~~~~~~~~~~~~~~

Robot Framework 関連のメーリングリストは複数あり、詳しい情報を調べたり質問したりできます。
メーリングリストのアーカイブは公開で、誰でも  (検索エンジンも) 閲覧できます。
もちろん、参加も自由です。ただし、投稿できるのはメーリングリストのメンバーだけです。
また、スパム対策のため、新規ユーザの投稿は、最初に投稿した記事が無事掲載されるまで、しばらくの間モデレーションの対象になります。メーリングリストへの投稿は歓迎ですが、
`上手な質問の仕方 <http://www.catb.org/~esr/faqs/smart-questions.html>`__ を心がけましょう。

`robotframework-users <http://groups.google.com/group/robotframework-users>`_
   Robot Framework に関する一般的な話題を扱うメーリングリストです。
   質問や問題点の議論はここに投稿しましょう。
   他のユーザに共有したい情報がある場合も、ここに投稿してください。

`robotframework-announce <http://groups.google.com/group/robotframework-announce>`_
    アナウンスのみのメーリングリストで、モデレータしか投稿できません。
    ここに投稿されるアナウンスは robotframework-users にも投稿されるので、どちらかにだけ入っておけば大丈夫です。

`robotframework-devel <http://groups.google.com/group/robotframework-devel>`_
   Robot Framework の開発に関する議論のメーリングリストです。
