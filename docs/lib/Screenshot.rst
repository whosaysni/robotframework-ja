Screenshot: スクリーンショットを撮る
======================================
:Version:          3.0
:Scope:            test suite
:Named arguments:  supported

テストを実行しているマシン上で、スクリーンショットを撮るためのライブラリです。

スクリーンショットをきちんと撮るには、テストを物理ないし仮想ディスプレイ上で実行する必要があります。

.. Using with Python

Python での使い方
------------------

Python を使っている場合、スクリーンショットの撮り方は OS に依存します。
OSX では、スクリーンショットは OS 組み込みの ``screencapture`` ユーティリティで撮ります。
その他の OS では、以下のツールまたはモジュールをインストールしておく必要があります。
ライブラリのインポート時に、どのツール・モジュールを使うかを指定できます。
値を指定しない場合は、順番に各ツールを探索し、最初に見つかったものを使います。

- wxPython :: http://wxpython.org :: RIDE でも使うので、多くの Robot Framework ユーザが、このモジュールをインストール済みのはずです。
- PyGTK :: http://pygtk.org :: ほとんどの Linux ディストリビューションでは、デフォルトでこのモジュールが使えるはずです。
- Pillow :: https://python-pillow.github.io :: Windows でしか稼働しません。オリジナルの PIL パッケージもサポートしています。
- Scrot :: https://en.wikipedia.org/wiki/Scrot :: Windows では使えません。 ``apt-get install scrot`` などでインストールします。

Robot Framework 2.9.2 からは、OSX で ``screencapture`` を使うようになり、スクリーンショットモジュールを明示できるようになりました。
``scrot`` のサポートは Robot Framework 3.0 からです。

.. Using with Jython and IronPython

Jython および IronPython での使い方
-------------------------------------

Jython や IronPython では、このライブラリはそれぞれ JVM や .NET プラットフォームの API を使います。
これらの API はいつでも使えるので、外部のモジュールが必要ありません。


.. Where screenshots are saved

スクリーンショットの保存先
----------------------------

デフォルトでは、スクリーンショットはログファイルの出力先と同じディレクトリに保存されます。
ログを生成させない場合、スクリーンショットは、 XML 出力ファイルの出力先と同じディレクトリに保存されます。

スクリーンショットの保存先は、ライブラリのインポート時に、 ``screenshot_directory`` 引数で決めたり、実行時に `Set Screenshot Directory` で決めたりできます。
保存先の指定には絶対パスを使えます。


キーワード
------------


インポート
~~~~~~~~~~~
Arguments:  [screenshot_directory=None, screenshot_module=None]

スクリーンショットの保存先を設定します。

``screenshot_directory`` を指定しなかった場合、スクリーンショットはログファイルの出力先と同じディレクトリに保存されます。
このディレクトリは `Set Screenshot Directory` でも決められます。

``screenshot_module`` は、 Mac OSX で、システムの Python 以外の Python から、このライブラリを使う際に利用するモジュールやツールです。
指定できるのは、 ``wxPython``, ``PyGTK``, ``PIL``, ``scrot`` のいずれかで、大小文字を区別しません。
値を指定しない場合は、上記の順番で各ツールを探索し、最初に見つかったものを使います。
詳しくは `Using with Python` を参照してください。

例 (以下のいずれかを使ってください)::

  | =Setting= |  =Value=   |  =Value=   |
  | Library   | Screenshot |            |
  | Library   | Screenshot | ${TEMPDIR} |
  | Library   | Screenshot | screenshot_module=PyGTK |

Robot Framework 2.9.2 から、スクリーンショットモジュールを明示して指定できるようになりました。


Set Screenshot Directory
~~~~~~~~~~~~~~~~~~~~~~~~~~
Arguments:  [path]

スクリーンショットの保存先ディレクトリをセットします。

どの OS でも、 ``/`` をパス区切りに使えます。変更前のディレクトリを返します。

ディレクトリはライブラリのインポート時にも変更できます。


Take Screenshot
~~~~~~~~~~~~~~~~~
Arguments:  [name=screenshot, width=800px]

スクリーンショットを JPEG 形式で撮り、ログファイルに埋め込みます。

スクリーンショットのファイル名は、引数 ``name`` の指定値から決まります。
``name`` が拡張子 ``.jpg`` や ``.jpeg`` で終わっている場合、指定した名前そのままでスクリーンショットを保存します。
それ以外の場合は、 ``name`` にアンダースコアを付加して、ファイル名が一意となるように通し番号を振り、拡張子を付けて保存します。

``name`` は、ログファイルの出力先からの相対ディレクトリを指しているものとみなします。
絶対パスでの指定も可能です。どの OS でも、 ``/`` をパス区切りに使えます。

``width`` は、ログファイルに埋め込むときのスクリーンショットのサイズを決めます。

例: (LOGDIR はライブラリが自動的に決定します)::

  | Take Screenshot |                  |     | # LOGDIR/screenshot_1.jpg (通番は自動的に振られる) 
  | Take Screenshot | mypic            |     | # LOGDIR/mypic_1.jpg (通番は自動的に振られる) 
  | Take Screenshot | ${TEMPDIR}/mypic |     | # /tmp/mypic_1.jpg (通番は自動的に振られる) 
  | Take Screenshot | pic.jpg          |     | # LOGDIR/pic.jpg (常にこの名前で保存) 
  | Take Screenshot | images/login.jpg | 80% | # 名前と幅を指定 
  | Take Screenshot | width=550px      |     | # 幅のみ指定 

スクリーンショットを保存したパスを返します。


Take Screenshot Without Embedding
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Arguments:  [name=screenshot]

スクリーンショットを取り、ログファイルにリンクだけを出力します。

このキーワードは、 `Take Screenshot` とほとんど同じで、保存したスクリーンショットがログに埋め込まれない点が違います。ログには、アクセスできるように、リンクだけを出力します。

