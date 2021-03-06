BuiltIn: 組み込み機能
=======================
:Version:          3.0
:Scope:            global
:Named arguments:  supported

常に利用できる標準ライブラリです。よく使うキーワードが入っています。

``BuiltIn`` は、使うことの多い汎用のキーワードセットを提供する標準ライブラリです。このライブラリは自動的にインポートされるので、いつでも使えます。キーワードの中には、検証に使えるもの (`Should Be Equal` 指定の値に等しいか検証、や `Should Contain`: 指定の値を含むか検証)、値の変換(`Convert To Integer`: 整数に変換) その他もろもろ (`Log`: ログ出力、 `Sleep`: スリープ、 `Run Keyword If`: 条件によって実行、 `Set Global Variable`: グローバル値の設定) があります。


目次
------

- `HTMLエラーメッセージ <HTML error messages>`_
- `式の評価 <Evaluating expressions>`_
- `ブール型の引数 <Boolean arguments>`_
- `複数行にわたる文字列の比較 <Multiline string comparisons>`_
- `キーワード <Keywords>`_


.. _HTML error messages:

HTMLエラーメッセージ
----------------------

キーワードの多くは、エラーメッセージのオプションを持っています。エラーメッセージは、キーワードの実行に失敗した際に使われます。 Robot Framework 2.8 からは、エラーメッセージの先頭に ``*HTML*`` を付けることで、 HTML 形式のエラーメッセージを使えるようになりました。使い方の例は `Fail` キーワードを参照してください。メッセージの HTML 化は、BuiltIn 以外のライブラリでも使えます。


.. _Evaluating expressions:

式の評価
----------

`Evaluate` や `Run Keyword If` 、 `Should Be True` といったキーワードは、引数に式を指定でき、式は Python の `eval <https://docs.python.org/2/library/functions.html#eval>`_ で評価されます。そのため、 ``len()`` や ``int`` といった Python の組み込み関数を使えます。
`Evaluate` では、自作のモジュールや実行に使う名前空間を設定できます。
キーワードの中には、自動的に `os モジュール <https://docs.python.org/2/library/os.html>`_ や
`sys モジュール <https://docs.python.org/2/library/sys.html>`_ を使えるものもあります。

例:

.. code:: robotframework

   Run Keyword If  os.sep == '/'  Log  Not on Windows
   ${random int} = Evaluate  random.randint(0, 5)  modules=random


変数を、 ``${variable}`` のような通常の書式で使うと、その値は式の評価時に「置き換わり」ます。
つまり、式の表す値は、変数値を文字列で表したもので、値そのものではないということです。
このことは、数値のように、Pythonで文字列で表した時にそのまま値になる場合は問題にはなりませんが、他のオブジェクトでは、値が文字列でどう表現されるかによって、式の意味が変わってしまいます。
とりわけ大事なことは、変数値を文字列と比較するには常にクオートする必要があること、そして改行を含む文字列は三重クオートせねばならないということです。

例:

.. code:: robotframework

   | `Should Be True` | ${rc} < 10                | # リターンコードは 10 以上 |
   | `Run Keyword If` | '${status}' == 'PASS'     | Log | # テストをパスした |
   | `Run Keyword If` | 'FAIL' in '''${output}''' | Log | # 出力に文字列 FAIL を含む |

Robot Framework 2.9 からは、変数自体を評価ネームスペース (evaluation namespace) の中で使えるようになりました。
ネームスペース中の変数は、波括弧のない ``$variable`` のような特殊な変数の書き方で表わせます。
この書き方にした変数はクオートする必要はなく、テストファイル中で一旦文字列に置き換えられたりもしません。

例:

.. code:: robotframework

   | `Should Be True` | $rc < 10          | # リターンコードは 10 以上
   | `Run Keyword If` | $status == 'PASS' | `Log` | Passed               |
   | `Run Keyword If` | 'FAIL' in $output | `Log` | Output contains FAIL |
   | `Should Be True` | len($result) > 1 and $result[1] == 'OK' |

とはいえ、複雑な式をつくるより、テストライブラリにロジックを移したほうが良いこともあるので注意しましょう。


.. _Boolean arguments:

ブール型の引数
-----------------

キーワードの中には、値を true または false のブール型として扱うものがあります。
そうしたキーワードの文字列を渡す場合、空文字と、 ``false`` または ``no`` (いずれも大小文字を区別しない) は False 扱いになります。
また、キーワードの中には、値を比較して、条件に合わないとき、エラーメッセージに期待値と実際の値を出力するかどうかをスイッチする機能をもったものがありますが、そのようなキーワードでは、 ``no values`` も False 扱いです。
それ以外の文字列は、値が何であっても True 扱いです。
その他の引数タイプでは、 :ref:`Python の流儀 <http://docs.python.org/2/library/stdtypes.html#truth-value-testing>` で True/False を決めます。

値が真になる例は以下の通りです:

.. code:: robotframework

    `Should Be Equal`  ${x}  ${y}   Custom error  values=True     # 空でない文字列は「基本的に」真
    `Should Be Equal`  ${x}  ${y}   Custom error  values=yes      # 上と同じ
    `Should Be Equal`  ${x}  ${y}   Custom error  values=${TRUE}  # Python の ``True`` は当然真
    `Should Be Equal`  ${x}  ${y}   Custom error  values=${42}    # 0 でない数も真


一方、偽になる例は以下の通りです:

.. code:: robotframework

    `Should Be Equal`  ${x}  ${y}   Custom error  values=False      # 文字列 ``false`` は偽
    `Should Be Equal`  ${x}  ${y}   Custom error  values=no         # 文字列 ``no`` は偽
    `Should Be Equal`  ${x}  ${y}   Custom error  values=${EMPTY}   # 空文字列は偽
    `Should Be Equal`  ${x}  ${y}   Custom error  values=${FALSE}   # Python の ``False`` は偽
    `Should Be Equal`  ${x}  ${y}   Custom error  values=no values  # 引数 ``values`` に限り ``no values`` は偽

Robot Framework 2.9 以前では、原則、 ``false`` や ``no`` も含め、空文字列でないものは全て True 扱いとしていました。

.. _Multiline string comparisons:

複数行からなる文字列の比較
---------------------------

Robot Framework 2.9.1 からは、 `Should Be Equal` や `Should Be Equal As Strings` は、文字列が一致しないときに、 `unified diff形式 <https://en.wikipedia.org/wiki/Diff_utility#Unified_format>`_ でメッセージを出力します。

例:

.. code:: robotframework

   | ${first} =  | `Catenate` | SEPARATOR=\n | Not in second | Same | Differs | Same |
   | ${second} = | `Catenate` | SEPARATOR=\n | Same | Differs2 | Same | Not in first |
   | `Should Be Equal` | ${first} | ${second} |

上の例は、以下のような結果を出力します:

.. code:: robotframework

   | Multiline strings are different:
   | --- first
   | +++ second
   | @@ -1,4 +1,4 @@
   | -Not in second
   |  Same
   | -Differs
   | +Differs2
   |  Same
   | +Not in first


.. _Keywords:

キーワード
-----------

Call Method
~~~~~~~~~~~~

:Arguments:  [object, method_name, \*args, \*\*kwargs]

引数を指定して、 `object` のメソッドを呼び出します。

メソッドの戻り値がある場合、キーワードの戻り値として、変数に代入できます。
`object` が指定した名前のメソッドをもたない場合や、メソッドの実行時に例外が送出された場合、キーワードは失敗します。

Robot Framework 2.9 からは、 ``**kwargs`` のサポートが追加され、 ``**kwargs`` 以外の引数で等号を使うときは、 ``\=`` のようにバックスラッシュによるエスケープが必要になりました。

例::

  | Call Method      | ${hashtable} | put          | myname  | myvalue |
  | ${isempty} =     | Call Method  | ${hashtable} | isEmpty |         |
  | Should Not Be True | ${isempty} |              |         |         |
  | ${value} =       | Call Method  | ${hashtable} | get     | myname  |
  | Should Be Equal  | ${value}     | myvalue      |         |         |
  | Call Method      | ${object}    | kwargs    | name=value | foo=bar |
  | Call Method      | ${object}    | positional   | escaped\=equals  |

Catenate
~~~~~~~~~

:Arguments:  [\*items]

`items` の内容を結合してできた文字列を返します。

デフォルトの動作では、 `items` の各要素をスペースで結合します。
最初の要素が ``SEPARATOR=<sep>`` の形式の場合、以降の各要素を  ``<sep>`` で結合します。要素が文字列でないときは、適宜文字列に変換されます。

例::

  | ${str1} = | Catenate | Hello         | world |       |
  | ${str2} = | Catenate | SEPARATOR=--- | Hello | world |
  | ${str3} = | Catenate | SEPARATOR=    | Hello | world |
  =>
  | ${str1} = 'Hello world'
  | ${str2} = 'Hello---world'
  | ${str3} = 'Helloworld'

Comment
~~~~~~~~

:Arguments:  [\*messages]

`messages` の内容をそのままログファイルに出力します。

このキーワードは、引数に対して何もせず、ただログに出力します。
引数はどんな記法であっても無視されるので、存在しない変数を参照するような内容を書いてもエラーになりません。
変数の値を出力したいときは、 `Log` や `Log Many` を使ってください。

Continue For Loop
~~~~~~~~~~~~~~~~~~

:Arguments:  []

現在の for ループ内の処理を飛ばして、次に移ります。

このキーワード以降のループ内のキーワードはスキップされます。
ループ直下でも、ループから呼び出されたキーワード内でも使えます。

例:

.. code:: robotframework
  
  | :FOR | ${var}         | IN                     | @{VALUES}         |
  |      | Run Keyword If | '${var}' == 'CONTINUE' | Continue For Loop |
  |      | Do Something   | ${var}                 |

条件に応じてループを continue したいときは、 `Continue For Loop If` を使えば、 `Run Keyword If` や他のキーワードのラッパを使わずにすみます。

Robot Framework 2.8 で追加されました。

Continue For Loop If
~~~~~~~~~~~~~~~~~~~~~

:Arguments:  [condition]

``condition`` が真ならば、現在のループ内の処理をスキップします。            

`Continue For Loop` をラップして、条件に従ってループを continue します。
``condition`` の値の評価方法は `Should Be True` キーワードと同じです。

例:

.. code:: robotframework

  | :FOR | ${var}               | IN                     | @{VALUES} |
  |      | Continue For Loop If | '${var}' == 'CONTINUE' |
  |      | Do Something         | ${var}                 |

Robot Framework 2.8 で追加されました。

Convert To Binary
~~~~~~~~~~~~~~~~~~

:Arguments:  [item, base=None, prefix=None, length=None]

``item`` の値を2進数表記の文字列に変換します。

このキーワードは、 オプションの ``base`` パラメタに基づいて、 ``item`` の値を `Convert To Integer` で内部変換します。その後、 ``1011`` のような2進数 (基数2) 表記に変換します。

戻り値には ``prefix`` オプションでプレフィクスを付加でき、 ``length`` で最小桁数 (プレフィクスと、符号がある場合はそれも除く) を指定できます。
変換後の2進値の桁数が ``length`` よりも短い場合は、ゼロでパディングします。

例::

  | ${result} = | Convert To Binary | 10 |         |           | #  Result is 1010  |
  | ${result} = | Convert To Binary | F  | base=16 | prefix=0b | # Result is 0b1111 |
  | ${result} = | Convert To Binary | -2 | prefix=B | length=4 | # Result is -B0010 |

`Convert To Integer`, `Convert To Octal`, `Convert To Hex` も参照してください。

Convert To Boolean
~~~~~~~~~~~~~~~~~~~

:Arguments:  [item]

指定値をブール型の True または False に変換します。

``True`` や ``False`` (大小文字の区別なし) は期待通りの値に変換されます。
それ以外の値に対しては、 Python の ``bool()`` メソッドによる `真偽値 <http://docs.python.org/2/library/stdtypes.html#truth>`_ を返します。

Convert To Bytes
~~~~~~~~~~~~~~~~~

:Arguments:  [input, input_type=text]

``input`` を ``input_type`` に指定した型のリテラルとみなしたときのバイト列を返します。

指定できる ``input_type`` は以下の通りです:

- ``text:`` テキストを一文字づつバイト列に変換します。
  文字のコード値が 256 より低いものだけを利用でき、これらはコード値が同じのバイト文字に変換されます。大抵の文字は、 ``\x00`` や ``\xff`` のような形式でエスケープすると指定しやすいでしょう。引数には Unicode 型と bytes 型のどちらのデータでも指定できます。

- ``int:`` 整数1バイト分づつをスペースで区切ったものを変換します。
  `Convert To Integer` と同様、先頭に ``0b``, ``0o``, ``0x`` をつければ、それぞれ2進、8進、16進数を入力できます。

- ``hex:`` 16進表記の値をバイト文字列に変換します。
  1バイトは常に2桁 (e.g. ``01``, ``FF``) でなければなりません。
  スペースは無視されるので、見栄えに合わせて適宜使えます。

- ``bin:`` 2進の値をバイト文字列に変換します。1バイトは通常 8 文字 (例: ``00001010``) です。スペースは無視されるので、見栄えに合わせて適宜使えます。

入力には、文字列の他にリストや iterable も指定できます。
その場合、要素ひとつひとつを1文字とみなして処理します。
個々の入力文字の桁数を補う必要はなく、不要なスペースを入れてはなりません。

例 (末尾カラムに戻り値になるはずのバイト列をコメントしています)::

  | ${bytes} = | Convert To Bytes | hyvä    |     | # hyv\xe4        |
  | ${bytes} = | Convert To Bytes | \xff\x07 |     | # \xff\x07      |
  | ${bytes} = | Convert To Bytes | 82 70      | int | # RF              |
  | ${bytes} = | Convert To Bytes | 0b10 0x10  | int | # \x02\x10      |
  | ${bytes} = | Convert To Bytes | ff 00 07   | hex | # \xff\x00\x07 |
  | ${bytes} = | Convert To Bytes | 5246212121 | hex | # RF!!!           |
  | ${bytes} = | Convert To Bytes | 0000 1000  | bin | # \x08           |
  | ${input} = | Create List      | 1          | 2   | 12                |
  | ${bytes} = | Convert To Bytes | ${input}   | int | # \x01\x02\x0c |
  | ${bytes} = | Convert To Bytes | ${input}   | hex | # \x01\x02\x12 |

任意のテキストエンコーディング指定でバイト列に変換したければ、 ``String`` ライブラリの `Encode String To Bytes` を使ってください。

Robot Framework 2.8.2 で追加されました。

Convert To Hex
~~~~~~~~~~~~~~~

:Arguments:  [item, base=None, prefix=None, length=None, lowercase=False]


item を整数値とみなして、16進表現の文字列に変換します。

``item`` は、まずオプション ``base`` をもとに、内部的に `Convert To Integer` で整数に変換されます。
その後、16進数 (基数16) の表現に変換され、 ``FF0A`` のような文字列になります。

戻り値にはオプションの (0x...やH...のような) ``prefix``を付加できます。
また、 ``length`` で (プレフィクスや符号を除いた) 最小の長さを指定でき、変換後の文字列が最小の長さに満たないときにゼロ詰めできます。

デフォルトの設定では、値は大文字で表現されますが、引数 ``lowercase`` を真値 (:ref:`ブール型の引数 <boolean arguments>` 参照) にすると、(プレフィクス以外の) 文字を小文字にします。

例::

  | ${result} = | Convert To Hex | 255 |           |              | # Result is FF    |
  | ${result} = | Convert To Hex | -10 | prefix=0x | length=2     | # Result is -0x0A |
  | ${result} = | Convert To Hex | 255 | prefix=X | lowercase=yes | # Result is Xff   |

`Convert To Integer`, `Convert To Binary`, `Convert To Octal` も参照してください。

Convert To Integer
~~~~~~~~~~~~~~~~~~~~

:Arguments:  [item, base=None]

item を整数に変換します。

item が文字列の場合は、通常は基数 10 の整数として変換します。
以下のような場合は、基数が変わります:

- 引数で ``base`` を明に指定した場合。

- 文字列の先頭に特定のプレフィクスが付いている場合。例えば、 ``0b`` は2進 (基数2), ``0o`` は8進 (基数 8), ``0x`` は 16 進 (基数 16) です。
  プレフィクスを解釈するのは ``base`` を指定していないときだけで、プラス・マイナス符号はプレフィクスより前に付けます。

大小文字の区別はせず、スペースを無視します。

例::

  | ${result} = | Convert To Integer | 100    |    | # Result is 100   |
  | ${result} = | Convert To Integer | FF AA  | 16 | # Result is 65450 |
  | ${result} = | Convert To Integer | 100    | 8  | # Result is 64    |
  | ${result} = | Convert To Integer | -100   | 2  | # Result is -4    |
  | ${result} = | Convert To Integer | 0b100  |    | # Result is 4     |
  | ${result} = | Convert To Integer | -0x100 |    | # Result is -256  |

`Convert To Number`, `Convert To Binary`, `Convert To Octal`,
`Convert To Hex`, `Convert To Bytes` も参照してください。

Convert To Number
~~~~~~~~~~~~~~~~~~~

:Arguments:  [item, precision=None]

item を浮動小数点数に変換します。

オプションの ``precision`` が非負の整数の場合、戻り値は少数部が指定した桁数になるよう丸められます。
負の整数を指定すると、その数の絶対値分の桁で値を丸めます。
切り捨てと切り上げの丸め誤差が等しくなる場合には、常に、値がゼロから離れる方向に切り捨て・切り上げ処理します。

例::

  | ${result} = | Convert To Number | 42.512 |    | # Result is 42.512 |
  | ${result} = | Convert To Number | 42.512 | 1  | # Result is 42.5   |
  | ${result} = | Convert To Number | 42.512 | 0  | # Result is 43.0   |
  | ${result} = | Convert To Number | 42.512 | -1 | # Result is 40.0   |

一般的に、計算機は、浮動小数点を厳密に表現できません。
そのため、変換後の値や、値丸めの結果が期待通りにならないことがあるので注意しましょう。
詳しくは、以下の文献などを参照してください:


- http://docs.python.org/2/tutorial/floatingpoint.html
- http://randomascii.wordpress.com/2012/02/25/comparing-floating-point-numbers-2012-edition

整数への変換を行いたければ `Convert To Integer` を使ってください。

Convert To Octal
~~~~~~~~~~~~~~~~~~

:Arguments:  [item, base=None, prefix=None, length=None]

item を 8 進表現の文字列に変換します。

``item`` は、まずオプション ``base`` をもとに、内部的に `Convert To Integer` で整数に変換されます。
その後、8進数 (基数 8) の表現に変換され、 ``775`` のような文字列になります。

戻り値にはオプションの (0o...やO...のような) ``prefix`` を付加できます。
また、 ``length`` で (プレフィクスや符号を除いた) 最小の長さを指定でき、変換後の文字列が最小の長さに満たないときにゼロ詰めできます。


例::

  | ${result} = | Convert To Octal | 10 |            |          | # Result is 12 |
  | ${result} = | Convert To Octal | -F | base=16    | prefix=0 | # Result is -017    |
  | ${result} = | Convert To Octal | 16 | prefix=oct | length=4 | # Result is oct0020 |

`Convert To Integer`, `Convert To Binary`, `Convert To Hex` も参照してください。


Convert To String
~~~~~~~~~~~~~~~~~~~

:Arguments:  [item]

item を Unicode 文字列に変換します。

Python オブジェクトに対しては ``__unicode__`` や ``__str__`` メソッドを、 Java オブジェクトに対しては ``toString`` を使います。

Unicode と様々なエンコーディングのバイト文字列の間で変換したいときには、 ``String`` ライブラリの `Encode String To Bytes` や `Decode Bytes To String` を使ってください。
単にバイト文字列を生成したいときには、 `Convert To Bytes` を使ってください。


Create Dictionary
~~~~~~~~~~~~~~~~~~~

:Arguments:  [\*items]

items をから辞書を生成して返します。

items は、変数テーブルで ``&{dictionary}`` 型の変数を定義するときと同様、  ``key=value`` の記法で指定します。
キーと値にはいずれも変数を利用でき、キーに等号 (`=`) が含まれる場合には、バックスラッシュでエスケープできます。
item を既存の辞書から得るには、引数に ``&{dict}`` を指定します。

同じキーを複数回指定した場合、後で指定した方を優先します。
戻り値の辞書は、キーと値を順序つきで管理しています。
キーが文字列の場合には、 ``${dict.key}`` のように、ドット付きで値にアクセスできます。

例::

  | &{dict} = | Create Dictionary | key=value | foo=bar |
  | Should Be True | ${dict} == {'key': 'value', 'foo': 'bar'} |
  | &{dict} = | Create Dictionary | ${1}=${2} | &{dict} | foo=new |
  | Should Be True | ${dict} == {1: 2, 'key': 'value', 'foo': 'new'} |
  | Should Be Equal | ${dict.key} | value |

このキーワードの仕様は、 Robot Framework 2.9 で色々変更されました:

- ``Collections`` ライブラリから ``BuiltIn`` に移動しました。
- ``key=value`` 形式で、文字列以外のキーもサポートしました。
- キーと値を分けて書く古い記法が廃止されました。
- 戻り値の辞書が、順序つき辞書になり、ドット記法でアクセスできます。


Create List
~~~~~~~~~~~~

:Arguments:  [\*items]

items からなるリストを返します。

リストは ``${scalar}``, ``@{list}`` のいずれの変数にも入れられます。

例::

  | @{list} =   | Create List | a    | b    | c    |
  | ${scalar} = | Create List | a    | b    | c    |
  | ${ints} =   | Create List | ${1} | ${2} | ${3} |

Evaluate
~~~~~~~~~~

:Arguments:  [expression, modules=None, namespace=None]

式を Python で評価して、その結果を返します。

``expression`` は、 :ref:`式の評価 <evaluating expressions>` の解説の通りに Python で評価されます。

``modules`` 引数は、カンマで区切ったリストで、Python モジュールを列挙します。
このモジュールは、式を評価するときに import され、式評価の名前空間に入ります。

``namespace`` は、式評価の名前空間を辞書で指定するときに使います。
``modules`` を指定すると、この名前空間に組み込まれます。
``namespace`` は Robot Framework 2.8.4 から使えるようになりました。

式中に ``${variable}`` のような変数が入っていると、式の評価前に置き換えられます。
置き換えではなく、評価対象の式の中で変数を参照したいときは、特殊な記法 ``$variable`` を使います。
この機能は Robot Framework 2.9 から登場し、  :ref:`式の評価 <evaluating expressions>` の節で詳しく説明しています。

例 (この例では ``${result}`` の初期値は 3.14 とします)::

  | ${status} = | Evaluate | 0 < ${result} < 10 | # 変数の値が文字列 '3.14' でもうまく動作する |
  | ${status} = | Evaluate | 0 < $result < 10   | # 文字列として置き換わるのではなく、変数値そのものが評価される |
  | ${random} = | Evaluate | random.randint(0, sys.maxint) | modules=random, sys   |
  | ${ns} =     | Create Dictionary | x=${4}    | y=${2}              |
  | ${result} = | Evaluate | x*10 + y           | namespace=${ns}     |
  =>
  | ${status} = True
  | ${random} = <random integer>
  | ${result} = 42

Exit For Loop
~~~~~~~~~~~~~~~

:Arguments:  []

実行中のforループを停止して抜けます。

実行中の for ループから抜けて、その後の処理に移ります。
for ループの中でも使えますし、ループ中で使われているキーワードからでも使えます。

例:

.. code:: robotframework

  | :FOR | ${var}         | IN                 | @{VALUES}     |
  |      | Run Keyword If | '${var}' == 'EXIT' | Exit For Loop |
  |      | Do Something   | ${var} |

`Run Keyword If` などのラッパキーワードを使わずに、条件に応じてループから抜けたい場合には、 `Exit For Loop If` を使ってください。

Exit For Loop If
~~~~~~~~~~~~~~~~~~

:Arguments:  [condition]

``condition`` の評価値が真のとき、実行中の for ループを停止して抜けます。

条件に応じて、 `Exit For Loop` を実行するラッパです。
``condition`` は `Should Be True` キーワードと同じ考え方で評価されます。

例:

.. code:: robotframework

  | :FOR | ${var}           | IN                 | @{VALUES} |
  |      | Exit For Loop If | '${var}' == 'EXIT' |
  |      | Do Something     | ${var}             |

Robot Framework 2.8 で登場しました。

Fail
~~~~~~

:Arguments:  [msg=None, \*tags]

テストを失敗させ、指定のメッセージを出力し、必要に応じてタグを変更します。

エラーメッセージは ``msg`` で指定します。
エラーメッセージを引数にとる他のキーワードと同様、メッセージを ``*HTML*`` で始めると、エラーメッセージを HTML で指定できます。

メッセージの後にタグを指定すると、現在のテストケースのタグを変更できます。
タグ名の前にハイフンをつけた場合 (e.g. ``-regression``)、そのタグは除去されます。
それ以外の場合は、指定したタグが付加されます。
タグは内部的には `Set Tags` や `Remove Tags` で操作され、タグをセットしたときや除去したときのセマンティクスは、それぞれのキーワードの仕様に準じます。

例::

  | Fail | Test not ready   |             | | # 指定メッセージを出力して失敗
  | Fail | *HTML*<b>Test not ready</b> | | | # HTML でメッセージを出力して失敗
  | Fail | Test not ready   | not-ready   | | # 'not-ready' タグを付与して失敗
  | Fail | OS not supported | -regression | | # 'regression' タグを除去する
  | Fail | My message       | tag    | -t*  | # tで始まる全てのタグを除去して、新たに 'tag' というタグを付与

テスト全体の実行を停止したいときは `Fatal Error` を使ってください。

タグの変更機能は、 Robot Framework 2.7.4 で、 HTML メッセージのサポートは 2.8 で追加されました。

Fatal Error
~~~~~~~~~~~~~

:Arguments:  [msg=None]

テスト全体の実行を停止します。

このキーワードを使ったテストやテストスイートは、指定のメッセージとともにただちに失敗し、それ以後のテストは canned メッセージで失敗します。
ティアダウンが指定されている場合は、テストの失敗に関係なく実行されます。

単体のテストケースを失敗させたいときは `Fail` を使ってください。

Get Count
~~~~~~~~~~~

:Arguments:  [item1, item2]

``item1`` 中に ``item2`` が何回出現するか返し、ログに記録します。

このキーワードは、 Python の文字列、リスト、その他 ``count`` メソッドを備えているか、 Python のリストに変換できるオブジェクト全てに使えます。

例:

.. code:: robotframework
  
  | ${count} = | Get Count | ${some item} | interesting value |
  | Should Be True | 5 < ${count} < 10 |

Get Length
~~~~~~~~~~~~

:Arguments:  [item]

item の長さを返し、ログに記録します。

item は、長さを持つものなら何でもかまいません。例えば、文字列、リスト、マップ型です。
このキーワードは、まず対象の長さを Python の ``len()`` 関数で調べ、内部では item の特殊メソッド ``__len__`` が呼ばれます。
``len()`` に失敗した場合は、 item の ``length`` または ``size`` メソッドの呼び出しを試みます。
うまく行かなければ、最後に item の ``length`` アトリビュートを取得しようとします。
いずれも失敗した場合には、キーワードは失敗します。

例::

  | ${length} = | Get Length    | Hello, world! |        |
  | Should Be Equal As Integers | ${length}     | 13     |
  | @{list} =   | Create List   | Hello,        | world! |
  | ${length} = | Get Length    | ${list}       |        |
  | Should Be Equal As Integers | ${length}     | 2      |

`Length Should Be`, `Should Be Empty`, `Should Not Be Empty` も参照してください。


Get Library Instance
~~~~~~~~~~~~~~~~~~~~~

:Arguments:  [name=None, all=False]

指定のテストライブラリのアクティブなインスタンスを返します。

このキーワードを使うと、あるライブラリを、内部状態を持った別のライブラリと簡単に連携できます。
以下に Python の例を示します::

  | from robot.libraries.BuiltIn import BuiltIn
  |
  | def title_should_start_with(expected):
  |     seleniumlib = BuiltIn().get_library_instance('SeleniumLibrary')
  |     title = seleniumlib.get_title()
  |     if not title.startswith(expected):
  |         raise AssertionError("Title '%s' did not start with '%s'"
  |                              % (title, expected))

このキーワードをテストデータ中で使って、返ってきたライブラリインスタンスを他のキーワードに渡すこともできます。
ライブラリを別の名前でインポートしている場合、 ``name`` には、元のライブラリ名ではなく、新たにつけたライブラリ名を指定せねばなりません。

オプションの引数 ``all`` を真値にすると、全てのライブラリ名をインスタンスにマップした辞書を返します。
この機能は Robot Framework 2.9.2 で登場しました。

例:

.. code:: robotframework

  | &{all libs} = | Get library instance | all=True |

Get Time
~~~~~~~~~~

:Arguments:  [format=timestamp, time_=NOW]

指定の時刻を、指定のフォーマットにして返します。

*注意:* Robot Framework 2.8.5 で追加された DateTime ライブラリには、現在の日付や時刻の取得、日時情報の操作全般が可能な、より柔軟性の高いキーワードが定義されています。

日付時刻がどのように返されるかは、 ``format`` によって決まります。
以下にその規則を説明します。
文字列のチェックが行われる場合は、大小文字を区別しません。

1) ``format`` に文字列 ``epoch`` が入っている場合、UNIX のエポック (1970-01-01 00:00:00 UTC)
   からの経過時間を秒数で返します。戻り値は常に整数です。

2) ``format`` に文字列 ``year``, ``month``, ``day``, ``hour``, ``min``, ``sec`` のいずれかが入っている場合、指定した要素だけを返します。
   戻り値中の要素の出力順は、要素を指定した順番となり、要素以外の文字列が ``format`` に入っていても無視されます。
   値はゼロ詰めされた文字列で返ります (e.g. 5月 -> ``05``) 

3) それ以外の場合 (あるいはデフォルトの設定では)、 ``2006-02-24 15:08:31`` 形式のタイムスタンプを返します。

デフォルトの設定では、このキーワードは現在の現地時刻を返しますが、その挙動は、以下のように、 ``time`` 引数を使って変更できます。
文字列のチェックが行われる場合は、大小文字を区別しません。

1) ``time`` が数値の場合や、数値に変換可能な文字列の場合は、 UNIX エポックからの経過秒数として解釈されます。
   ちなみに、このドキュメントの執筆時点で、エポックからの経過秒数は 1177654467 秒です。

2) ``time`` がタイムスタンプの場合、その値を使います。
   有効なタイムスタンプフォーマットは ``YYYY-MM-DD hh:mm:ss`` と ``YYYYMMDD hhmmss`` です。

3) ``time`` が ``NOW`` の場合(デフォルトの設定)は、現在の現地時刻を使います。
   この時刻は Python の ``time.time()`` 関数で取得します。
   function.

4) ``time`` が ``UTC`` の場合は、現在の [http://en.wikipedia.org/wiki/Coordinated_Universal_Time|UTC] 時刻を使います。
   この時刻は Python の ``time.time() + time.altzone`` で計算します。

5) ``time`` が ``NOW - 1 day`` や ``UTC + 1 hour 30 min`` などの文字列の場合、現在の現地時刻・UTC時刻に対して、文字列の表す時間を加減した日時を返します。
   時刻を表す文字列のフォーマットは、ユーザガイドの付録の節で説明しています。

例 (現在の現地時刻を 2006-03-29 15:06:21 とした場合)::

  | ${time} = | Get Time |             |  |  |
  | ${secs} = | Get Time | epoch       |  |  |
  | ${year} = | Get Time | return year |  |  |
  | ${yyyy}   | ${mm}    | ${dd} =     | Get Time | year,month,day |
  | @{time} = | Get Time | year month day hour min sec |  |  |
  | ${y}      | ${s} =   | Get Time    | seconds and year |  |
  =>
  | ${time} = '2006-03-29 15:06:21'
  | ${secs} = 1143637581
  | ${year} = '2006'
  | ${yyyy} = '2006', ${mm} = '03', ${dd} = '29'
  | @{time} = ['2006', '03', '29', '15', '06', '21']
  | ${y} = '2006'
  | ${s} = '21'

例 (現在の現地時刻が 2006-03-29 15:06:21 で、 UTC 時刻が 2006-03-29 12:06:21 の場合)::

  | ${time} = | Get Time |              | 1177654467          | # Time given as epoch seconds        |
  | ${secs} = | Get Time | sec          | 2007-04-27 09:14:27 | # Time given as a timestamp          |
  | ${year} = | Get Time | year         | NOW                 | # The local time of execution        |
  | @{time} = | Get Time | hour min sec | NOW + 1h 2min 3s    | # 1h 2min 3s added to the local time |
  | @{utc} =  | Get Time | hour min sec | UTC                 | # The UTC time of execution          |
  | ${hour} = | Get Time | hour         | UTC - 1 hour        | # 1h subtracted from the UTC  time   |
  =>
  | ${time} = '2007-04-27 09:14:27'
  | ${secs} = 27
  | ${year} = '2006'
  | @{time} = ['16', '08', '24']
  | @{utc} = ['12', '06', '21']
  | ${hour} = '11'

UTC時刻のサポートは Robot Framework 2.7.5 で追加されましたが、 2.7.7 以前は正しく動作しません。

Get Variable Value
~~~~~~~~~~~~~~~~~~~~

:Arguments:  [name, default=None]

変数の値を取得します。変数がないときには ``default`` を返します。

変数の名前は、通常の変数名 (e.g. ``${NAME}``) またはエスケープした形式 (e.g. ``\${NAME}``) です。
前者には、 `Set Suite Variable` で説明したような制限があります。

例::

  | ${x} = | Get Variable Value | ${a} | default |
  | ${y} = | Get Variable Value | ${a} | ${b}    |
  | ${z} = | Get Variable Value | ${z} |         |
  =>
  | ${x} は、 ${a} があれば ${a} の値、なければ 'default' という文字列
  | ${y} は、 ${a} があれば ${a} の値、なければ ${b} の値
  | ${z} は、まだ定義されていなければ Python の None になる

変数を動的にセットするキーワードには、他に `Set Variable If` があります。

Get Variables
~~~~~~~~~~~~~~~

:Arguments:  [no_decoration=False]

現在のスコープ中の全ての変数の入った辞書を返します。

変数は、特殊な辞書の形で返されます。この辞書は、テストデータ中の変数にアクセスするときと同様、スペースの有無、大小文字、アンダースコアの有無を区別しないで変数にアクセスできます。
辞書は、通常の Python の辞書と全く同じ操作ができる他、 Collection ライブラリを使ってアクセスしたり変更したりできます。
このキーワードが返す辞書の中身を変更しても、現在のスコープの変数の値には影響を及ぼしません。

デフォルトの設定では、変数は、変数のタイプに応じて、 ``${}``, ``@{}``, ``&{}`` で修飾されます。 ``no_decoration`` に真値を渡すと、戻り値の変数は修飾されません。
このオプションは Robot Framework 2.9 で登場しました。

例:

.. code:: robotframework
  
  | ${example_variable} =         | Set Variable | example value         |
  | ${variables} =                | Get Variables |                      |
  | Dictionary Should Contain Key | ${variables} | \${example_variable} |
  | Dictionary Should Contain Key | ${variables} | \${ExampleVariable}  |
  | Set To Dictionary             | ${variables} | \${name} | value     |
  | Variable Should Not Exist     | \${name}    |           |           |
  | ${no decoration} =            | Get Variables | no_decoration=Yes |
  | Dictionary Should Contain Key | ${no decoration} | example_variable |

Note: Robot Framework 2.7.4 以前は、変数は独自のオブジェクトで返され、辞書メソッドの一部しかサポートしていません。


Import Library
~~~~~~~~~~~~~~~~

:Arguments:  [name, \*args]

ライブラリ名を指定してインポートします。引数があれば指定できます。

このキーワードを使うと、テストの実行中に動的にライブラリをインポートできます。
ライブラリ自体が動的な性質を持っていて、テストデータを処理しないと使えないような場合に必須のキーワードです。
通常は、設定テーブルで Library 設定を使えばライブラリを使えます。

このキーワードは、ライブラリを指定するときに、ライブラリ名と、ライブラリ実装へのパスのどちらも扱えます。
パスを使う場合は、絶対パス形式にするか、 :ref:`モジュール検索パス <pythonpath-jythonpath-and-ironpythonpath>` からの相対にせねばなりません。
どの OS でも、スラッシュをパス区切りに使えます。

ライブラリがサポートしていれば、引数を渡してライブラリをインポートできます。
``WITH NAME`` 記法で、インポートしたライブラリに別の名前をつけることもできます。

例::

  | Import Library | MyLibrary |
  | Import Library | ${CURDIR}/../Library.py | arg1 | named=arg2 |
  | Import Library | ${LIBRARIES}/Lib.java | arg | WITH NAME | JavaLib |


Import Resource
~~~~~~~~~~~~~~~~~

:Arguments:  [path]

指定のパスからリソースファイルをインポートします。

このキーワードでリソースをインポートすると、設定テーブルの Resource 設定でインポートしたときと同じく、リソースはテストスイートのスコープ中にセットされます。

パスを使う場合は、絶対パス形式にするか、 :ref:`モジュール検索パス <pythonpath-jythonpath-and-ironpythonpath>` からの相対にせねばなりません。
どの OS でも、スラッシュをパス区切りに使えます。

例::

  | Import Resource | ${CURDIR}/resource.txt |
  | Import Resource | ${CURDIR}/../resources/resource.html |
  | Import Resource | found_from_pythonpath.robot |


Import Variables
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:Arguments:  [path, \*args]

指定のパスから変数ファイルをインポートします。引数があれば指定できます。

このキーワードで変数をインポートすると、設定テーブルの Variables 設定でインポートしたときと同じく、変数がテストスイートのスコープ中にセットされます。

インポートしたスコープに同じ名前の変数が存在した場合、その変数は変数ファイル上の値で上書きされます。
この挙動は、例えば、テストスイートの中で、テストを実行するたびに新たに変数を取り込んで初期化するといったテクニックに使えます。

パスを使う場合は、絶対パス形式にするか、 :ref:`モジュール検索パス <pythonpath-jythonpath-and-ironpythonpath>` からの相対にせねばなりません。
どの OS でも、スラッシュをパス区切りに使えます。


例::

  | Import Variables | ${CURDIR}/variables.py   |      |      |
  | Import Variables | ${CURDIR}/../vars/env.py | arg1 | arg2 |
  | Import Variables | file_from_pythonpath.py  |      |      |


Keyword Should Exist
~~~~~~~~~~~~~~~~~~~~~~

:Arguments:  [name, msg=None]

キーワードが現在のスコープ上に存在しない場合失敗します。

また、同じ名前のキーワードが複数存在する場合も失敗します。
短い名前 (e.g. ``Log``) 、完全指定の名前 (e.g. ``BuiltIn.Log``) の両方を扱えます。

引数 ``msg`` を指定すると、デフォルトのエラーメッセージをオーバライドできます。

`Variable Should Exist` も参照してください。


Length Should Be
~~~~~~~~~~~~~~~~~~

:Arguments:  [item, length, msg=None]

item の長さが指定通りであることを確認します。

item の長さは、 `Get Length` キーワードで調べます。
引数 ``msg`` を指定すると、デフォルトのエラーメッセージをオーバライドできます。


Log
~~~~~

:Arguments:  [message, level=INFO, html=False, console=False, repr=False]

指定のメッセージを指定のログレベルで記録します。

使えるレベルは TRACE, DEBUG, INFO (デフォルトのレベル), HTML, WARN, ERROR です。
現在のログレベルよりも低いレベルのメッセージは無視されます。
ログレベルの設定は、 `Set Log Level` キーワードや、コマンドラインオプション ``--loglevel`` を参照してください。

WARN や ERROR レベルのメッセージは、自動的にコンソールに表示される他、ログファイルの `Test Execution Errors` セクションに書き込まれます。

ログ機能は、オプションの ``html``, ``console`` および ``repr`` 引数で設定できます。
これらのオプションは、デフォルトではいずれもオフですが、引数に真値を指定すれば有効になります。
値をどのように真偽値に変換するかは、 :ref:`ブール引数 <Boolean arguments>` の節を参照してください。

引数 ``html`` の値を真にした場合、メッセージは HTML とみなされ、  ``<`` のようなマークアップ用の特殊文字をエスケープしません。例えば、  ``<img src="image.png">`` は、  ``html`` を真にすれば画像を表示しますが、そうでなければ、この文字列がそのまま表示されます。
``html`` 引数を設定する代わりに、ログレベル HTML で出力した場合も、メッセージをエスケープせず出力します。
ログレベル HTML は、実際にはメッセージを INFO レベルで出力します。

``console`` の値を真にすると、ログファイルの他に、テストの実行を行ったコンソールにもログメッセージを出力します。
このキーワードは、メッセージの出力先として必ず標準出力ストリームを使い、出力したメッセージに改行を付加します。
この挙動が望ましくないときは、 `Log To Console` を使ってください。

``repr`` 引数を真にすると、引数に渡した値を Python の ``pprint.pformat()`` に似た独自の関数で整形します。
この機能は、文字列やバイト列に印字不可の文字が入っている場合や、入れ子のデータ構造を扱いたい場合に便利です。
また、 Robot Framework 独自の機能として、Unicode 文字列の先頭から ``u`` を除去し、バイト文字列の先頭に ``b`` を付加します。

例::

  | Log | Hello, world!        |          |   | # 通常の INFO メッセージ |
  | Log | Warning, world!      | WARN     |   | # 警告                   |
  | Log | <b>Hello</b>, world! | html=yes |   | # HTML のINFO メッセージ |
  | Log | <b>Hello</b>, world! | HTML     |   | # 上と同じ               |
  | Log | <b>Hello</b>, world! | DEBUG    | html=true | # DEBUG, HTML形式 |
  | Log | Hello, console!   | console=yes | | # コンソールにも出力する   |
  | Log | Hyvä \x00     | repr=yes    | | # ``'Hyv\xe4 \x00'`` を出力    |

複数のメッセージを一挙にログに出力したいときは `Log Many` を、コンソールにだけメッセージを出力したい場合は `Log To Console` を使ってください。

引数 ``html``, ``console``, ``repr`` は Robot Framework 2.8.2 で登場しました。

``repr`` で pprint する機能は Robot Framework 2.8.6 からです。
また、 ``u`` を除去して ``b`` プレフィクスをつけるようになったのは Robot Framework 2.9 からです。

Log Many
~~~~~~~~~

:Arguments:  [\*messages]

メッセージの要素一つ一つを、それぞれ一行のログとして、ログレベル INFO で出力します。

リストや辞書の値をひとつづつ出力する機能も備えています。

例::

  | Log Many | Hello   | ${var}  |
  | Log Many | @{list} | &{dict} |

別のログレベルで出力したいとき、HTML を使いたいとき、コンソールに出力したいときは、 `Log` または `Log To Console` を使ってください。

Log To Console
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:Arguments:  [message, stream=STDOUT, no_newline=False]

指定のメッセージをコンソールに記録します。

デフォルトの設定では、出力先は標準出力ストリームです。
``stream`` を ``STDERR`` （小文字でも可）にすると、標準エラー出力に出力できます。

また、デフォルトの設定では、メッセージの後ろに改行を付加します。
この挙動は、 ``no_newline`` を真にするとオフにできます。

例::

  | Log To Console | Hello, console!             |                 |
  | Log To Console | Hello, stderr!              | STDERR          |
  | Log To Console | Message starts here and is  | no_newline=true |
  | Log To Console | continued without newline.  |                 |

このキーワードは、メッセージをログファイルに記録しません。
ログファイルにも記録したいときは、 `Log` キーワードに ``console`` 引数を指定して使ってください。

Robot Framework 2.8.2 で登場しました。


Log Variables
~~~~~~~~~~~~~~~

:Arguments:  [level=INFO]

スコープ中の全ての変数を、指定のログレベルで出力します。


No Operation
~~~~~~~~~~~~~~

:Arguments:  []

何もしません。

Pass Execution
~~~~~~~~~~~~~~~~

:Arguments:  [message, \*tags]

テスト、セットアップ、ティアダウンなどで、このキーワード以降の処理をスキップし、 PASS させます。

このキーワードは、テストデータのどこでも使えますが、使う場所によって振る舞いが多少異なります:

- セットアップやティアダウンの中で使った場合 (テストスイート、テスト、キーワードのいずれのセットアップ・ティアダウンでも) そのセットアップやティアダウンの実行結果はパスになります。
  `Pass Execution` を呼び出したキーワードに、さらにティアダウンが付与されていた場合、そのティアダウンは実行されます。
  それ以外は、実行や実行結果に影響しません。
- セットアップやティアダウンの外で使った場合は、そのテストケースだけをパスさせます。
  テストケースやキーワードにティアダウンがあれば、実行します。

このキーワードに到達した時点で、テスト失敗後の処理が行われている状態なら、そのテストの結果は失敗になります。

``message`` は必須の引数で、なぜ実行をパスさせたかを説明を入れます。
デフォルトの設定では、メッセージを平文とみなしますが、 ``*HTML*`` で文字列を開始した場合は HTML フォーマットとみなします。

`Fail` キーワードの場合と同様、 ``message`` の後に引数 ``tags`` を渡すと、テストタグを編集できます。
タグ名の前にハイフンをつけた場合 (e.g. ``-regression``)、そのタグは除去されます。
それ以外の場合は、指定したタグが付加されます。
タグは内部的には `Set Tags` や `Remove Tags` で操作され、タグをセットしたときや除去したときのセマンティクスは、それぞれのキーワードの仕様に準じます。

例::

  | Pass Execution | All features available in this version tested. |
  | Pass Execution | Deprecated test. | deprecated | -regression    |

このキーワードは、よく、 `Run Keyword If` のような、他のキーワードでラップして、条件付きで使います。
ただし、このようなケースは `Pass Execution If` でも書けます::

  | Run Keyword If    | ${rc} < 0 | Pass Execution | Negative values are cool. |
  | Pass Execution If | ${rc} < 0 | Negative values are cool. |

テストの実行中にテストをパスさせた場合でも、セットアップやティアダウンは実行されます。
安易にテストをパスさせると、最悪の場合、テスト対象システムの不具合を明らかにできたはずの処理を全部飛ばしてしまったりするので注意してください。
外部要因で時折テストを継続できないような場合には、パスさせるのではなく、一旦テストを失敗させておき、そのテストをクリティカルでないテストにしておくほうが安全です。

Robot Framework 2.8 で登場しました。

Pass Execution If
~~~~~~~~~~~~~~~~~~~

:Arguments:  [condition, message, \*tags]

テスト、セットアップ、ティアダウンなどで、条件に応じて、このキーワード以降の処理をスキップし、 PASS させます。

`Pass Execution` をラップして、 ``condition`` に応じて処理をスキップします。
``condition`` は `Should Be True` キーワードの引数と同じ方法で評価され、 ``message`` や ``*tags`` は `Pass Execution` の同名の引数と同じ意味をもちます。

例:

.. code:: robotframework

  
  | :FOR | ${var}            | IN                     | @{VALUES}
  |
  |      | Pass Execution If | '${var}' == 'EXPECTED' | Correct value was found
  |
  |      | Do Something      | ${var}                 |

Robot Framework 2.8 で登場しました。


Regexp Escape
~~~~~~~~~~~~~~~

:Arguments:  [\*patterns]

引数の文字列を正規表現用にエスケープします。

このキーワードは、 `Should Match Regexp` や `Should Not Match Regexp` といったキーワード向けに文字列をエスケープするのに使います。

エスケープ処理には Python の ``re.escape()`` を使います。

例::

  | ${escaped} = | Regexp Escape | ${original} |
  | @{strings} = | Regexp Escape | @{strings}  |


Reload Library
~~~~~~~~~~~~~~~~

:Arguments:  [name_or_instance]

指定のライブラリがどんなキーワードを提供しているか再チェックします。

テストデータや、ライブラリの提供するキーワードが変更されたときに呼び出せます。

ライブラリは、ライブラリの名前か、すでに読み込み済みのライブラリインスタンスで指定できます。
後者は、ライブラリ自体がこのキーワードを（内部的に）メソッドとして呼ぶ場合などに特に便利です。

Robot Framework 2.9 で登場しました。


Remove Tags
~~~~~~~~~~~~~

:Arguments:  [\*tags]

現在のテストや、スイート中の全テストから、 ``tags`` に指定したタグを除去します。

タグは、厳密な名前でも、 ``*`` （任意の文字列）や ``?`` （任意の1字）を使ったワイルドカードマッチでも指定できます。

このキーワードは、 `Set Tags` と同じく、使い方によって、単一のテストケース、あるいはテストスイート中の全テストに影響します。

現在の全タグを指定したければ、組み込み変数 ``@{TEST TAGS}`` があります。

例:

.. code:: robotframework
  
  | Remove Tags | mytag | something-* | ?ython |

特定のタグを追加したい場合は `Set Tags` を、任意のタグを設定・削除した後にテストケースを失敗させたいときは `Fail` を参照してください。


Repeat Keyword
~~~~~~~~~~~~~~~~

:Arguments:  [repeat, name, \*args]

指定のキーワードを複数回繰り返し実行します。

``name`` や ``args`` は、実行したいキーワードや引数で、 `Run Keyword` と同じです。
``repeat`` には、キーワードを何度繰り返すか（回数）か、実行し続けたい長さ（タイムアウト）を指定します。

``repeat`` を回数で指定した場合は、その回数キーワードを反復実行します。
``repeat`` は整数または文字列で指定でき、文字列の場合には、わかりやすさのために ``times`` や ``x`` という接尾辞をつけてかまいません（大小文字の区別はなく、スペースは無視します）。

``repeat`` をタイムアウトで指定するときは、Robot Framework 独自の時間フォーマット (e.g. ``1 minute``, ``2 min 3 s``) を使います。
数字だけ (``1`` や ``1.5``) は、うまく使えません。

``repeat`` がゼロか負の数の場合、キーワードは一切実行されません。キーワードが失敗すると、何度目の繰り返しのときでも、テストはただちに失敗します。

例::

  | Repeat Keyword | 5 times   | Go to Previous Page |
  | Repeat Keyword | ${var}    | Some Keyword | arg1 | arg2 |
  | Repeat Keyword | 2 minutes | Some Keyword | arg1 | arg2 |

Robot Framework 3.0 から、 ``repeat`` をタイムアウトで指定できます。


Replace Variables
~~~~~~~~~~~~~~~~~~~

:Arguments:  [text]

引数 ``text`` 中の変数を、現在の変数値で置き換えた文字列を返します。

``text`` の内容が変数ひとつだけの場合は、戻り値は文字列変換をうけず、変数の値そのもので置き換わります。
それ以外の場合は、常に文字列が返ります。

例:

ファイル ``template.txt`` の内容は ``Hello ${NAME}!`` とし、変数 ``${NAME}`` は ``Robot`` とします。

.. code:: robotframework

  | ${template} =   | Get File          | ${CURDIR}/template.txt |
  | ${message} =    | Replace Variables | ${template}            |
  | Should Be Equal | ${message}        | Hello Robot!           |


Return From Keyword
~~~~~~~~~~~~~~~~~~~~~

:Arguments:  [\*return_values]

ユーザキーワード中から処理を戻します。

ユーザキーワードから処理を戻し、残りの操作を飛ばして、テストをパスさせるのに使います。
また、 ``[Return]`` 設定を使った時のように値を返すこともできます。
戻り値の扱い方は、ユーザガイドを参照してください。

このキーワードのよくある使い方は、 `Run Keyword If` や `Run Keyword If Test Passed` でラップして、条件に応じて処理を戻すというものです::

  | Run Keyword If | ${rc} < 0 | Return From Keyword |
  | Run Keyword If Test Passed | Return From Keyword |

このキーワードを使えば、ループの中からも処理を戻せます。
ループからのリターンと、戻り値の例が、以下の `Find Index` キーワードに示されています。
とはいえ、この手の複雑なロジックは、テストライブラリで実装するのが賢明です::

  | ***** Variables *****
  | @{LIST} =    foo    baz
  |
  | ***** Test Cases *****
  | Example
  |     ${index} =    Find Index    baz    @{LIST}
  |     Should Be Equal    ${index}    ${1}
  |     ${index} =    Find Index    non existing    @{LIST}
  |     Should Be Equal    ${index}    ${-1}
  |
  | ***** Keywords *****
  | Find Index
  |    [Arguments]    ${element}    @{items}
  |    ${index} =    Set Variable    ${0}
  |    :FOR    ${item}    IN    @{items}
  |    \    Run Keyword If    '${item}' == '${element}'    Return From Keyword ${index}
  |    \    ${index} =    Set Variable    ${index + 1}
  |    Return From Keyword    ${-1}    # Also [Return] would work here.

「式の評価結果に応じて処理を戻し、値を返す」というもっともよくある操作については、 `Return From Keyword If` キーワードで直接実現できます。
これらのキーワードは、いずれも Robot Framework 2.8 で登場しました。

`Run Keyword And Return` や `Run Keyword And Return If` も参照してください。


Return From Keyword If
~~~~~~~~~~~~~~~~~~~~~~~

:Arguments:  [condition, \*return_values]

``condition`` が真のとき、実行中のユーザキーワードから処理を戻します。

条件に応じて処理を戻す、 `Return From Keyword` のラッパです。
``condition`` は `Should Be True` キーワードの引数と同じ方法で評価されます。

`Return From Keyword` のときと同じ例を使って、 `Find Index` キーワードを書き直すと以下のようになります::

  | ***** Keywords *****
  | Find Index
  |    [Arguments]    ${element}    @{items}
  |    ${index} =    Set Variable    ${0}
  |    :FOR    ${item}    IN    @{items}
  |    \    Return From Keyword If    '${item}' == '${element}'    ${index}
  |    \    ${index} =    Set Variable    ${index + 1}
  |    Return From Keyword    ${-1}    # ここは [Return] でもよい

`Run Keyword And Return` や `Run Keyword And Return If` も参照してください。

Robot Framework 2.8 で登場しました。

Run Keyword
~~~~~~~~~~~~~

:Arguments:  [name, \*args]

指定のキーワードを実行します。

実行するキーワードの名前を引数として渡せるので、変数、例えば、何らかのキーワードの戻り値や、コマンドラインから得た値など、動的な値を渡せます。

Run Keyword And Continue On Failure
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:Arguments:  [name, \*args]

キーワードを実行し、何らかの失敗が起きても実行を継続します。

キーワード名や引数の扱いは `Run Keyword` と同じです。

例:

.. code:: robotframework
  
  | Run Keyword And Continue On Failure | Fail | This is a stupid example |
  | Log | This keyword is executed |

記法の誤り、タイムアウト、致命的な例外の発生などで失敗した場合、実行を継続しません。
Robot Framework 2.9 からは、変数にまつわるエラーも実行継続の対象となりました。

Run Keyword And Expect Error
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:Arguments:  [expected_error, name, \*args]

キーワードを実行し、期待通りのエラーが発生するか確認します。

「期待するエラー」は、 Robot Framework のレポートに出力されるのと同じ形式で書かねばなりません。
パターンに ``?`` を含めた場合、任意の1文字に、 ``＊`` を含めた場合は任意の文字列にマッチします。
``name`` や ``\*args`` の意味は `Run Keyword` と同じです。

期待通りのエラーがおきた場合、発生したエラーのエラーメッセージを返し、必要ならばそのまま処理やテストを継続できます。
エラーが発生しないときや、期待通りのエラーでなかった場合は失敗します。

例::

  | Run Keyword And Expect Error | My error | Some Keyword | arg1 | arg2 |
  | ${msg} = | Run Keyword And Expect Error | * | My KW |
  | Should Start With | ${msg} | Once upon a time in |

記法の誤り、タイムアウト、致命的な例外の発生などで失敗した場合、実行を継続しません。
Robot Framework 2.9 からは、変数にまつわるエラーも実行継続の対象となりました。

Run Keyword And Ignore Error
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:Arguments:  [name, \*args]

キーワードを実行し、エラーが発生しても無視します。

このキーワードは二つの値を返します。最初は ``PASS`` または ``FAIL`` で、実行したキーワードの状態によって変わります。
二つ目の値は、キーワードの実行に成功したときには戻り値、失敗したときにはエラーメッセージです。
キーワード実行の成否だけを知りたいときは、 `Run Keyword And Return Status` を使ってください。

``name`` や ``\*args`` の意味は `Run Keyword` と同じです。
詳しくは `Run Keyword If` の例を参照してください。

記法の誤り、タイムアウト、致命的な例外の発生などで失敗した場合、実行を継続しません。
それ以外のエラーでは、このキーワードは失敗しません。
Robot Framework 2.9 からは、変数にまつわるエラーも実行継続の対象となりました。

Run Keyword And Return
~~~~~~~~~~~~~~~~~~~~~~~~

:Arguments:  [name, \*args]

指定のキーワードを実行した後、現在のキーワードから処理を戻します。

実行するキーワードは、 `Run Keyword` と同様、 ``name`` と ``\*args`` で指定します。
キーワードの実行後、実行したキーワードの戻り値があれば、その戻り値を現在のキーワードの戻り値にセットして、処理を戻します。

現在のキーワードからの処理の戻り方は、 `Return From Keyword` と同じです。

例:

.. code:: robotframework
  
  | `Run Keyword And Return`  | `My Keyword` | arg1 | arg2 |
  | # Above is equivalent to: |
  | ${result} =               | `My Keyword` | arg1 | arg2 |
  | `Return From Keyword`     | ${result}    |      |      |

キーワードを実行して、条件に応じて値を返したいときは、 `Run Keyword And Return If` を使ってください。

Robot Framework 2.8.2 で登場しました。

Run Keyword And Return If
~~~~~~~~~~~~~~~~~~~~~~~~~~~

:Arguments:  [condition, name, \*args]

条件が真のとき、指定のキーワードを実行して、現在のキーワードから処理を戻します。

`Run Keyword And Return` のラッパで、 ``condition`` の真偽にもとづいてキーワードを実行し、処理を戻します。
``condition`` 真偽値の扱いは `Should Be True` と同じです。

例:

.. code:: robotframework
  
  | `Run Keyword And Return If` | ${rc} > 0 | `My Keyword` | arg1 | arg2 |
  | # 上と以下は同じ:
  | `Run Keyword If`            | ${rc} > 0 | `Run Keyword And Return` | `My Keyword ` | arg1 | arg2 |

何らかの値を返したいときは `Return From Keyword If` を使ってください。

Robot Framework 2.8.2 で登場しました。

Run Keyword And Return Status
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:Arguments:  [name, \*args]

指定の引数でキーワードを実行して、その結果をブール値で返します。

キーワードの実行に成功したときは ``True`` を、失敗したときは ``False`` を返します。
`Run Keyword If` などと組み合わせて使うと便利です。
エラーメッセージや戻り値を扱いたいときは、 `Run Keyword And Ignore Error` を使ってください。

キーワード名や引数は `Run Keyword` と同じです。

例:

.. code:: robotframework
  
  | ${passed} = | `Run Keyword And Return Status` | Keyword | args |
  | `Run Keyword If` | ${passed} | Another keyword |

  
記法の誤り、タイムアウト、致命的な例外の発生などで失敗した場合、実行を継続しません。
それ以外のエラーでは、このキーワードは失敗しません。

Robot Framework 2.7.6 で登場しました。


Run Keyword If
~~~~~~~~~~~~~~~

:Arguments:  [condition, name, \*args]

条件が真のとき、指定のキーワードを実行します。

``condition`` は、 :ref:`式の評価 <evaluating expressions>` の解説の通りに Python で評価されます。
``name`` や ``args`` は、実行したいキーワードや引数で、 `Run Keyword` と同じです。

簡単な if/else の例を示します::
  | ${status} | ${value} = | `Run Keyword And Ignore Error` | `My Keyword` |
  | `Run Keyword If`     | '${status}' == 'PASS' | `Some Action`    | arg |
  | `Run Keyword Unless` | '${status}' == 'PASS' | `Another Action` |

この例では、 `My Keyword` の戻り値に応じて `Some Action` または `Another Action` のいずれかが実行されます。
`Run Keyword And Ignore Error` の代わりに、 `Run Keyword And Return Status` を使っても構いません。

式中に ``${variable}`` のような変数が入っていると、式の評価前に置き換えられます。
置き換えではなく、評価対象の式の中で変数を参照したいときは、特殊な記法 ``$variable`` を使います。
この機能は Robot Framework 2.9 から登場し、  :ref:`式の評価 <evaluating expressions>` の節で詳しく説明しています。

例:

.. code:: robotframework
  
  | `Run Keyword If` | $result is None or $result == 'FAIL' | `Keyword` |

Robot Framework 2.7.4 から、 `ELSE` および `ELSE IF` で分岐できるようになりました。
`ELSE` や `ELSE IF` は ``\*args`` に指定し、厳密に ``ELSE``, ``ELSE IF`` と書かねばなりません。
`ELSE` 分岐の後には、実行するキーワードの名前、その後に引数があれば引数を指定します。
`ELSE IF` 分岐の後には、条件、キーワード名、引数を指定します。
`ELSE` は `ELSE IF` の後に記述でき、複数の `ELSE IF` があってもかまいません。

先ほどの例は、ELSE を使うと以下のように書けます::
  | ${status} | ${value} = | `Run Keyword And Ignore Error` | My Keyword |
  | `Run Keyword If` | '${status}' == 'PASS' | `Some Action` | arg | ELSE | `Another Action` |

このキーワードの戻り値は、キーワードの中で実行されたいずれかのキーワードの戻り値です。
キーワードが実行されなかったとき (``condition`` が偽のとき) には None を返します。
従って、このキーワードを使えば、 ELSE や ELSE IF 分岐を使って、条件に応じて実行するキーワードを切り替え、その戻り値を得られます (キーワードを使わず、静的な値を切り替えたいときは、 `Set Variable If` を使ってください)。
以下に例を示します::

  | ${var1} =   | `Run Keyword If` | ${rc} == 0     | `Some keyword returning a value` |
  | ...         | ELSE IF          | 0 < ${rc} < 42 | `Another keyword` |
  | ...         | ELSE IF          | ${rc} < 0      | `Another keyword with args` | ${rc} | arg2 |
  | ...         | ELSE             | `Final keyword to handle abnormal cases` | ${rc} |
  | ${var2} =   | `Run Keyword If` | ${condition}  | `Some keyword` |

この例では、 ${condition} が偽のとき、 ${var2} は None になります。

``ELSE`` や ``ELSE IF`` は明に指定せねばならず、変数にはできないので注意してください。
文字列リテラルとして ``ELSE`` や ``ELSE IF`` を使いたいのなら、 ``\ELSE`` や ``\ELSE IF`` のようにバックスラッシュでエスケープしてください。

Robot Framework 2.8 から、 ``condition`` の評価時に、 Python の `os`__ モジュールや `sys`__ モジュールを自動的に import するようになり、式の中でモジュールの属性を使えます::

  | `Run Keyword If` | os.sep == '/' | `Unix Keyword`        |
  | ...              | ELSE IF       | sys.platform.startswith('java') | `Jython Keyword` |
  | ...              | ELSE          | `Windows Keyword`     |

__ http://docs.python.org/2/library/os.html
__ http://docs.python.org/2/library/sys.html


Run Keyword If All Critical Tests Passed
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:Arguments:  [name, \*args]

全てのクリティカルテストにパスしていれば、指定の引数でキーワードを実行します。

このキーワードは、テストスイートのティアダウンでしか使えません。
それ以外の場所で使おうとするとエラーになります。

その他の点では、 `Run Keyword` と同じです。


Run Keyword If All Tests Passed
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:Arguments:  [name, \*args]

全てのテストにパスしていれば、指定の引数でキーワードを実行します。

このキーワードは、テストスイートのティアダウンでしか使えません。
それ以外の場所で使おうとするとエラーになります。

その他の点では、 `Run Keyword` と同じです。


Run Keyword If Any Critical Tests Failed
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:Arguments:  [name, \*args]

何らかのクリティカルテストに失敗していれば、指定の引数でキーワードを実行します。

このキーワードは、テストスイートのティアダウンでしか使えません。
それ以外の場所で使おうとするとエラーになります。

その他の点では、 `Run Keyword` と同じです。


Run Keyword If Any Tests Failed
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:Arguments:  [name, \*args]

テストに失敗していれば、指定の引数でキーワードを実行します。

このキーワードは、テストスイートのティアダウンでしか使えません。
それ以外の場所で使おうとするとエラーになります。

その他の点では、 `Run Keyword` と同じです。


Run Keyword If Test Failed
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:Arguments:  [name, \*args]

テストに失敗していれば、指定の引数でキーワードを実行します。

このキーワードは、テストのティアダウンでしか使えません。
それ以外の場所で使おうとするとエラーになります。

その他の点では、 `Run Keyword` と同じです。

Robot Framework 2.9 以前では、このキーワードはテストティアダウン自体の失敗を拾いません。


Run Keyword If Test Passed
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:Arguments:  [name, \*args]

テストに成功していれば、指定の引数でキーワードを実行します。

このキーワードは、テストのティアダウンでしか使えません。
それ以外の場所で使おうとするとエラーになります。

その他の点では、 `Run Keyword` と同じです。

Robot Framework 2.9 以前では、このキーワードはテストティアダウン自体の失敗を拾いません。


Run Keyword If Timeout Occurred
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:Arguments:  [name, \*args]

テストまたはテスト中のキーワードがタイムアウトした場合、指定の引数でキーワードを実行します。

このキーワードは、テストのティアダウンでしか使えません。
それ以外の場所で使おうとするとエラーになります。

その他の点では、 `Run Keyword` と同じです。


Run Keyword Unless
~~~~~~~~~~~~~~~~~~~~

:Arguments:  [condition, name, \*args]

条件が偽のとき、指定のキーワードを実行します。

詳細や例は `Run Keyword If` を参照してください。


Run Keywords
~~~~~~~~~~~~~~

:Arguments:  [\*keywords]

指定のキーワードを順に実行します。

このキーワードは、セットアップやティアダウンで複数のアクションを実行したいが、そのためにわざわざ高水準のキーワードを定義するまでもない、といった状況で便利です。

デフォルトでは、全ての引数をキーワードとみなして実行します。

例::

  | Run Keywords | Initialize database | Start servers | Clear logs |
  | Run Keywords | ${KW 1} | ${KW 2} |
  | Run Keywords | @{KEYWORDS} |

Robot Framework 2.7.6 からは、大文字の ``AND`` という特殊な引数を使って、キーワードを分割できるようになりました。
``AND`` を使った場合、 ``AND`` で区切られた引数は、それぞれ最初がキーワード名、それ以後が引数として扱われます。

例::

  | Run Keywords | Initialize database | db1 | AND | Start servers | server1 | server2 |
  | Run Keywords | Initialize database | ${DB NAME} | AND | Start servers | @{SERVERS} | AND | Clear logs |
  | Run Keywords | ${KW} | AND | @{KW WITH ARGS} |

``AND`` 自体は、引数の分割を制御していて、変数にできないので注意してください。
リテラルの ``AND`` を引数に使いたい時は、変数を使うか、 ``\AND`` のようにバックスラッシュでエスケープしてください。


Set Global Variable
~~~~~~~~~~~~~~~~~~~~~

:Arguments:  [name, \*values]

全てのテストケースやテストスイートで使えるグローバルな変数を生成します。

このキーワードで設定した変数は、キーワード実行以後の全てのテストケースとスイートで利用できます。
このキーワードで設定した変数は、コマンドラインで ``--variable`` や ``--variablefile`` といったオプションで変数を設定したときと同じ効果を持ちます。
このキーワードは、テスト中の全ての変数値を変えてしまうので、使う時は注意してください。

`Set Suite Variable` も参照してください。


Set Library Search Order
~~~~~~~~~~~~~~~~~~~~~~~~~~

:Arguments:  [\*search_order]

ライブラリの検索順序を指定して、複数のライブラリ上に同じ名前のキーワードがあるときに、どのキーワードを優先して使うかを決めます。

ライブラリの検索順序は、テストデータ中で、あるキーワード名に対して、複数のキーワード実装があるときに、名前の衝突の解決に使います。
このキーワードで順番を指定すると、キーワードを探す際、指定した順番にライブラリやリソースを検索し、最初に見つかったキーワード実装を使います。
該当するキーワードがないときには、このキーワードを使わなかったときと同様、テストは失敗します。

このキーワードを使った場合、 ``LibraryName.Keyword Name`` のような完全指定の形式は不用になります。
例えば、以下のように書く代わりに::

  | MyLibrary.Keyword | arg |
  | MyLibrary.Another Keyword |
  | MyLibrary.Keyword | xxx |

以下のように書けます::

  | Set Library Search Order | MyLibrary |
  | Keyword | arg |
  | Another Keyword |
  | Keyword | xxx |

このキーワードは、複数のリソースファイルに同じ名前のキーワードがあるときに、その優先順位を決めるのにも使えます。
その場合、パス部分と拡張子を除いたリソースファイルの名前を順に並べます::

  | Set Library Search Order | resource | another_resource |

.. note::
   - 設定した優先順位は、このキーワードを使ったテストスイート内でのみ有効です。
   - どのように優先順位を設定しても、必ず、ライブラリよりもリソースファイル上のキーワードが優先されます。
   - このキーワードは設定前の解決順を返します。あとでそれを使って順番をリセットできます。
   - ライブラリおよびリソース名は、大小文字を区別せず、スペースを無視します。


Set Log Level
~~~~~~~~~~~~~~~

:Arguments:  [level]

ログの表示閾値を指定レベルにセットし、以前のレベルを返します。

閾値以下のメッセージはログに記録されません。
デフォルトのログレベルは INFO ですが、コマンドラインオプション ``--loglevel`` で設定できます。

指定できるログレベルは、 TRACE, DEBUG, INFO (デフォルト), WARN, ERROR, NONE (ログしない) です。


Set Suite Documentation
~~~~~~~~~~~~~~~~~~~~~~~~~

:Arguments:  [doc, append=False, top=False]

現在のテストスイートのドキュメントを設定します。

デフォルトの動作では、既存のドキュメントがあった場合上書きします。
`Set Test Message` と同様、オプションの  ``append`` 引数を指定すると、既存のドキュメントの後に ``doc`` を追加します。

デフォルトの動作では、このキーワードは現在のスイートのドキュメントを変更します。
``top`` 引数を真値にすると、トップレベルスイートのドキュメントを変更します。

現在のスイートのドキュメントは、組み込み変数 ``${SUITE DOCUMENTATION}`` で参照できます。

Robot Framework 2.7 で登場しました。 ``append`` と ``top`` は 2.7.7 で追加されました。


Set Suite Metadata
~~~~~~~~~~~~~~~~~~~~

:Arguments:  [name, value, append=False, top=False]

現在のテストスイートのメタデータをセットします。

デフォルトの動作では、既存のメタデータがあった場合上書きします。
`Set Test Message` と同様、オプションの  ``append`` 引数を指定すると、既存のメタデータの後に ``doc`` を追加します。

デフォルトの動作では、このキーワードは現在のスイートのメタデータを変更します。
``top`` 引数を真値にすると、トップレベルスイートのメタデータを変更します。

現在のスイートのメタデータは、組み込み変数 ``${SUITE METADATA}`` で参照できます。
``${SUITE METADATA}`` を変更しても、実際のスイートのメタデータには影響しないので注意してください。

Robot Framework 2.7.4 で登場しました。 ``append`` と ``top`` は 2.7.7 で追加されました。


Set Suite Variable
~~~~~~~~~~~~~~~~~~~~

:Arguments:  [name, \*values]

スイートのスコープ内のどこからでも使える変数を作成します。

このキーワードで変数をセットすると、現在実行中のテストスイートのスコープ内のどこからでもその変数にアクセスできます。
従って、このキーワードで作った変数は、テストデータファイルの変数テーブルで定義した変数や、変数ファイルからインポートした変数と同じ効果を持ちます。

デフォルトの動作では、このキーワードで設定した変数は、子のテストスイートからは見えません。
Robot Framework 2.9 からは、引数の最後に ``children=<option>`` を指定することで制御できるようになりました。
``<option>`` が空でない文字列か、 Python で True として扱われる値の場合、子のテストスイートからも変数にアクセスできます。
親のテストスイートと、兄弟のテストスイートからは、このキーワードによる変数は見えません。

変数の名前は、通常の変数名 (e.g. ``${NAME}``) か、 ``\${NAME}`` や ``$NAME`` のようなエスケープ形式にできます。
変数の値は、変数テーブルで変数を定義するときと同じ記法で定義できます。

同名の変数が新たなスコープ上にある場合、その値は上書きされます。
それ以外の場合は、新たに変数が生成されます。
同名の変数が現在のスコープ上にある場合、値を空にすると、変数は現在のスコープの値を引き継ぎます。

例::

  | Set Suite Variable | ${SCALAR} | Hello, world! |
  | Set Suite Variable | ${SCALAR} | Hello, world! | children=true |
  | Set Suite Variable | @{LIST}   | First item    | Second item   |
  | Set Suite Variable | &{DICT}   | key=value     | foo=bar       |
  | ${ID} =            | Get ID    |
  | Set Suite Variable | ${ID}     |

既存の値を空の値で上書きしたければ、組み込み変数 ``${EMPTY}``, ``@{EMPTY}``, ``&{EMPTY}`` を使います::

  | Set Suite Variable | ${SCALAR} | ${EMPTY} |
  | Set Suite Variable | @{LIST}   | @{EMPTY} | # New in RF 2.7.4 |
  | Set Suite Variable | &{DICT}   | &{EMPTY} | # New in RF 2.9   |

.. note:: 変数の値を別の変数としたいときは、変数をセットするときにエスケープ記法を使います:

.. code:: robotframework
  
  | ${NAME} =          | Set Variable | \${var} |
  | Set Suite Variable | ${NAME}      | value | # Sets variable ${var}  |
  | Set Suite Variable | \${NAME}    | value | # Sets variable ${NAME} |

`Set Test Variable`, `Set Global Variable`, `Variable Should Exist`, `Variable Should Not Exist`, `Get Variable Value` にも、同じ制約があります。



Set Tags
~~~~~~~~~~

:Arguments:  [\*tags]

現在のテスト、またはスイート中の全てのテストに ``tags`` に指定したタグを追加します。

このキーワードをテストケースの中で使うと、そのテストだけに指定のタグを付与し、他のテストには影響を与えません。

キーワードをスイートセットアップ中で使うと、そのスイート以下のテスト全てに再帰的にタグを付与します。
スイートのティアダウンにこのキーワードを使うと失敗します。

現在のタグは組み込み変数 ``@{TEST TAGS}`` で取得できます。

特定のタグを除去したい場合は `Remove Tags` を、タグを追加・削除した後にテストを失敗させたいときは `Fail` を使ってください。


Set Test Documentation
~~~~~~~~~~~~~~~~~~~~~~~~

:Arguments:  [doc, append=False]

現在実行中のテストケースのドキュメントをセットします。

デフォルトの動作では、既存のドキュメントがあった場合上書きします。
`Set Test Message` と同様、オプションの  ``append`` 引数を指定すると、既存のドキュメントの後に ``doc`` を追加します。

現在のテストのドキュメントは、組み込み変数 ``${SUITE DOCUMENTATION}`` で参照できます。
このキーワードは、スイートのセットアップやティアダウン中では使えません。

Robot Framework 2.7 で登場しました。 ``append`` は 2.7.7 で追加されました。


Set Test Message
~~~~~~~~~~~~~~~~~

:Arguments:  [message, append=False]

現在のテストケースのメッセージをセットします。

オプションの  ``append`` 引数を指定すると、既存のドキュメントがある場合、既存のドキュメントの後にスペースを挟んで ``doc`` を追加します。

テストティアダウンでこのキーワードを使ったときに限り、失敗時のメッセージを置き換えられます。
それ以外の使い方では、このキーワードでメッセージを設定しても、テストが失敗したときにメッセージが上書きされてしまいます。
ティアダウン中では、メッセージは組み込み変数 ``${TEST MESSAGE}`` で取得できます。

メッセージの先頭を ``*HTML*`` にすると、HTML 形式のメッセージにできます。

例::

  | Set Test Message | My message           |                          |
  | Set Test Message | is continued.        | append=yes               |
  | Should Be Equal  | ${TEST MESSAGE}      | My message is continued. |
  | Set Test Message | `*`HTML`*` <b>Hello!</b> |                      |

このキーワードは、スイートのセットアップやティアダウン中では使えません。

``append`` のサポートは 2.7.7 で追加されました。 HTML は 2.8 からです。


Set Test Variable
~~~~~~~~~~~~~~~~~~~

:Arguments:  [name, \*values]

現在実行中のテストのスコープ内で使える変数を作成します。

このキーワードで作成した変数は、現在実行中のテストケースのスコープ内のどこからでもアクセスできます。
例えば、ユーザキーワードの中で変数の値をセットした場合、そのテストケースのレベルの他、テストから呼び出している別のユーザキーワード内でも、その変数にアクセスできます。
このキーワードで作成した変数は、他のテストケースからは見えません。

その他、詳細や例は `Set Suite Variable` を参照してください。


Set Variable
~~~~~~~~~~~~~~

:Arguments:  [\*values]

指定の値を、変数に代入できる値にして返します。

このキーワードは、主にスカラ変数のセットに使います。
その他にも、リスト値の入ったスカラ変数をリスト変数や複数のスカラ変数に変換できます。
ただし、新たなリストを作成したいときは `Create List` を推奨します。

例::

  | ${hi} =   | Set Variable | Hello, world! |
  | ${hi2} =  | Set Variable | I said: ${hi} |
  | ${var1}   | ${var2} =    | Set Variable | Hello | world |
  | @{list} = | Set Variable | ${list with some items} |
  | ${item1}  | ${item2} =   | Set Variable  | ${list with 2 items} |

このキーワードで生成した変数は、キーワードを使ったスコープでしか利用できません。
より広いスコープで使える変数をセットしたいときは、 `Set Global Variable`, `Set Test Variable`, `Set Suite Variable` を使ってください。


Set Variable If
~~~~~~~~~~~~~~~~~

:Arguments:  [condition, \*values]

``condition`` の結果に応じて変数の値をセットします。

このキーワードの基本的な使い方は、条件式と二つの値を渡す方法です。
条件式 ``condition`` は、 `Should Be True` と同じ方法で評価されます。
条件式の結果が True なら二つの値のうち前者を、 False なら後者を返します。
二つ目の値は省略でき、その場合はデフォルト値 None になります。
以下に示す例では、 ``${rc}`` の値をゼロとします::

  | ${var1} = | Set Variable If | ${rc} == 0 | zero     | nonzero |
  | ${var2} = | Set Variable If | ${rc} > 0  | value1   | value2  |
  | ${var3} = | Set Variable If | ${rc} > 0  | whatever |         |
  =>
  | ${var1} = 'zero'
  | ${var2} = 'value2'
  | ${var3} = None

二つ目の値にも条件式を指定すると、 'else if' のような効果を得られ、さらに二つの値を後ろに追加できます。
その場合、最初の条件式が真でないときのみ、第二の条件を評価し、その真偽値に応じて、第二の条件の後の値のいずれかを返します。
この条件式の連鎖は、無制限に連続できます。

.. code:: robotframework

  | ${var} = | Set Variable If | ${rc} == 0        | zero           |
  | ...      | ${rc} > 0       | greater than zero | less then zero |
  |          |
  | ${var} = | Set Variable If |
  | ...      | ${rc} == 0      | zero              |
  | ...      | ${rc} == 1      | one               |
  | ...      | ${rc} == 2      | two               |
  | ...      | ${rc} > 2       | greater than two  |
  | ...      | ${rc} < 0       | less than zero    |

変数が存在するかどうかに応じて値をセットしたいときは `Get Variable Value` を使ってください。


Should Be Empty
~~~~~~~~~~~~~~~~~

:Arguments:  [item, msg=None]

``item`` が空であることを確認します。

``item`` の長さは、 `Get Length` キーワードで取得します。
デフォルトのエラーメッセージは、 ``msg`` 引数でオーバライドできます。


Should Be Equal
~~~~~~~~~~~~~~~~~

:Arguments:  [first, second, msg=None, values=True]

二つのオブジェクトが等しくないとき失敗します。

オプションの ``msg`` と ``values`` を使うと、キーワードが失敗したときのエラーメッセージを以下のように変更できます:

- ``msg`` を省略した場合、エラーメッセージは ``<first> != <second>`` の形式です。
- ``msg`` を指定し、 ``values`` が真値のとき、エラーメッセージは ``<msg>: <first> != <second>`` の形式です。
- ``msg`` を指定し、 ``values`` が偽値のときは、エラーメッセージは単に ``<msg>`` 形式です。

``values`` のデフォルト値は True ですが、 ``false`` や ``no values`` を指定することで偽にできます。
詳しくは :ref:`ブール型の引数<Boolean arguments>` の節を参照してください。

引数が複数行にわたる文字列のときは、 :ref:`複数行の文字列の比較方法 <multiline string comparisons>` に基づいて文字列を比較します。


Should Be Equal As Integers
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:Arguments:  [first, second, msg=None, values=True, base=None]

``first`` と ``second`` を整数に変換した後に比較し、等しくないときは失敗します。

``base`` や ``0b/0o/0x`` プレフィクスを使って基数10以外で整数変換を行う方法は `Convert To Integer` を参照してください。

``msg`` と ``values`` でデフォルトのエラーメッセージをオーバライドできます。
詳しくは `Should Be Equal` を参照してください。

例::

  | Should Be Equal As Integers | 42   | ${42} | Error message |
  | Should Be Equal As Integers | ABCD | abcd  | base=16 |
  | Should Be Equal As Integers | 0b1011 | 11  |


Should Be Equal As Numbers
~~~~~~~~~~~~~~~~~~~~~~~~~~~

:Arguments:  [first, second, msg=None, values=True, precision=6]

``first`` と ``second`` を実数に変換した後に比較し、等しくないときは失敗します。

値は ``precision`` に指定した精度で `Convert To Number` で変換されます。

例::

  | Should Be Equal As Numbers | ${x} | 1.1 | | # Passes if ${x} is 1.1 |
  | Should Be Equal As Numbers | 1.123 | 1.1 | precision=1  | # Passes |
  | Should Be Equal As Numbers | 1.123 | 1.4 | precision=0  | # Passes |
  | Should Be Equal As Numbers | 112.3 | 75  | precision=-2 | # Passes |

`Convert To Number` で考察したように、一般に計算機は浮動小数点数を厳密に保持できません。
その制限のため、浮動小数点間で等値比較を行おうとすると問題が起き、回避の方法は状況によって様々です。
このキーワードは、値を比較する前に丸めを行なうというきわめてナイーブなアプローチをとっており、それゆえに、丸め誤差を生じたり、極端に大きい・小さい値に対してうまく動作しなかったりします。
浮動小数点の比較と、状況に合った比較アルゴリズムの実装方法については、
http://randomascii.wordpress.com/2012/02/25/comparing-floating-point-numbers-2012-edition/ などを参照してください。

``msg`` と ``values`` でデフォルトのエラーメッセージをオーバライドできます。
詳しくは `Should Be Equal` を参照してください。
このキーワードの逆のバージョンが必要なら `Should Not Be Equal As Numbers` を参照してください。


Should Be Equal As Strings
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:Arguments:  [first, second, msg=None, values=True]

``first`` と ``second`` を文字列に変換した後に比較し、等しくないときは失敗します。

``msg`` と ``values`` でデフォルトのエラーメッセージをオーバライドできます。
詳しくは `Should Be Equal` を参照してください。

引数が複数行にわたる文字列のときは、 :ref:`複数行の文字列の比較方法 <multiline string comparisons>` に基づいて文字列を比較します。


Should Be True
~~~~~~~~~~~~~~~~

:Arguments:  [condition, msg=None]

指定の ``condition`` が真でないとき失敗します。

``condition`` が文字列の場合 (例えば ``${rc} < 10`` のような文字列のとき)、 :ref:`式の評価<Evaluating expressions>` で解説したように、 Python の式として評価され、その結果に基づいてキーワードの状態を決定します。
文字列でない要素を指定した場合は、 `Python における真偽値`__ から直接判定します。

__ http://docs.python.org/2/library/stdtypes.html#truth

デフォルトのエラーメッセージ (``<condition> should be true``) はお世辞にも親切とはいえませんが、 ``msg`` で変更できます。

例::

  | Should Be True | ${rc} < 10            |
  | Should Be True | '${status}' == 'PASS' | # 文字列はクオートが必要 |
  | Should Be True | ${number}   | # ${number} がゼロでないとき PASS |
  | Should Be True | ${list}     | # ${list} が空でないとき PASS |

上のように、変数を ``${variable}`` の記法で使うと、その値を文字列に置き換えてから式を評価します。
変数を特殊な記法 ``$variable`` で使えば、評価式の中の変数として使えます。
この機能は Robot Framework 2.9 で登場しました。
詳しくは :ref:`式の評価<Evaluating expressions>` で説明しています。

例::

  | Should Be True | $rc < 10          |
  | Should Be True | $status == 'PASS' | # Expected string must be quoted |

Starting from Robot Framework 2.8, `Should Be True` automatically
imports Python's [http://docs.python.org/2/library/os.html|os] and
[http://docs.python.org/2/library/sys.html|sys] modules that contain
several useful attributes::

  | Should Be True | os.linesep == '\n'             | # Unixy   |
  | Should Be True | os.linesep == '\r\n'          | # Windows |
  | Should Be True | sys.platform == 'darwin'        | # OS X    |
  | Should Be True | sys.platform.startswith('java') | # Jython  |


Should Contain
~~~~~~~~~~~~~~~~

:Arguments:  [container, item, msg=None, values=True]

``container`` に ``item`` が全く出現しないとき失敗します。 

文字列、リスト、その他 Python の ``in`` 演算子を使える任意のオブジェクトに使えます。
``msg`` と ``values`` でデフォルトのエラーメッセージをオーバライドできます。
詳しくは `Should Be Equal` を参照してください。

例::

  | Should Contain | ${output}    | PASS  |
  | Should Contain | ${some list} | value |


Should Contain X Times
~~~~~~~~~~~~~~~~~~~~~~~

:Arguments:  [item1, item2, count, msg=None]

``item1`` に ``item2`` が ``count`` 回以上出現しないとき失敗します。 
             
文字列、リスト、その他 `Get Count` で扱えるオブジェクトで使えます。
デフォルトのエラーメッセージは ``msg`` でオーバライドできます。
実際の出現回数をログに記録します。

例::

  | Should Contain X Times | ${output}    | hello  | 2 |
  | Should Contain X Times | ${some list} | value  | 3 |


Should End With
~~~~~~~~~~~~~~~~~

:Arguments:  [str1, str2, msg=None, values=True]

文字列 ``str1`` の末尾が文字列 ``str2`` でないとき失敗します。

``msg`` と ``values`` でデフォルトのエラーメッセージをオーバライドできます。
詳しくは `Should Be Equal` を参照してください。


Should Match
~~~~~~~~~~~~~~

:Arguments:  [string, pattern, msg=None, values=True]

文字列 ``string`` が ``pattern`` とマッチしないとき失敗します。

パターンマッチは、シェルのファイル名マッチと同様で、大小文字を区別します。
``*`` は任意の文字列、 ``?`` は任意の1文字にマッチします。

``msg`` と ``values`` でデフォルトのエラーメッセージをオーバライドできます。
詳しくは `Should Be Equal` を参照してください。


Should Match Regexp
~~~~~~~~~~~~~~~~~~~~~

:Arguments:  [string, pattern, msg=None, values=True]

``string`` が正規表現 ``pattern`` にマッチしないとき失敗します。

正規表現のチェックは Python の `re モジュール`__ で実装されています。
Python の正規表現の記法は Perl から導出したもので、 Java, Ruby, .NET などで使われているものともよく似ています。

__ http://docs.python.org/2/library/re.html

Robot Framework で正規表現記法を使うときは、以下に注意してください:

1) テストデータ中では、バックスラッシュをエスケープ文字として使っています。
   そのため、正規表現のパターン中にバックスラッシュを使いたい時は、さらにバックスラッシュを入れてエスケープせねばなりません (e.g. ``\\d\\w+``)。

2) 特殊文字を含むリテラル文字列を扱いたいときは `Regexp Escape` キーワードを使います。

3) パターンは文字列全体にマッチしなくてもかまいません。
   例えば、パターン ``ello`` は ``Hello world!`` にマッチします。
   全体一致が必要なときは ``^`` や ``$`` を使って文字列の先頭や末尾を表してください。
   例えば、 ``^ello$`` は ``ello`` にしかマッチしません。

4) 正規表現の解釈方法を制御するフラグ (``re.IGNORECASE``, ``re.MULTILINE`` など) を、 ``(?im)pattern`` のように、パターンのプレフィクスグループ (``(?iLmsux)``) で指定できます。
   使えるフラグは、 ``i`` (大小文字を区別しない), ``m`` (複数行モード), ``s`` (``.`` が全ての文字にマッチする), ``x`` (冗長記法), ``u`` (Unicode プロパティ依存), ``L`` (ロケール依存) です。

キーワードの実行に成功した場合、パターンにマッチした部分の文字列を返します。
また、グループを定義した場合は、キャプチャしたグループも返します。

``msg`` と ``values`` でデフォルトのエラーメッセージをオーバライドできます。
詳しくは `Should Be Equal` を参照してください。

例:

.. code:: robotframework

   | Should Match Regexp | ${output} | \\d{6}   | # 6桁の数字が含まれる
   | Should Match Regexp | ${output} | ^\\d{6}$ | # 6桁の数字だけからなる
   | ${ret} = | Should Match Regexp | Foo: 42 | (?i)foo: \\d+ |
   | ${match} | ${group1} | ${group2} = |
   | ...      | Should Match Regexp | Bar: 43 | (Foo|Bar): (\\d+) |
   =>
   | ${ret} = 'Foo: 42'
   | ${match} = 'Bar: 43'
   | ${group1} = 'Bar'
   | ${group2} = '43'


Should Not Be Empty
~~~~~~~~~~~~~~~~~~~~~

:Arguments:  [item, msg=None]

``item`` が空でないことを確認します。

``item`` の長さは、 `Get Length` キーワードで取得します。
デフォルトのエラーメッセージは、 ``msg`` 引数でオーバライドできます。


Should Not Be Equal
~~~~~~~~~~~~~~~~~~~~~

:Arguments:  [first, second, msg=None, values=True]

二つのオブジェクトが等しいとき失敗します。

``msg`` と ``values`` でデフォルトのエラーメッセージをオーバライドできます。
詳しくは `Should Be Equal` を参照してください。


Should Not Be Equal As Integers
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:Arguments:  [first, second, msg=None, values=True, base=None]

``first`` と ``second`` を整数に変換した後に比較し、等しいときは失敗します。

``base`` や ``0b/0o/0x`` プレフィクスを使って基数10以外で整数変換を行う方法は `Convert To Integer` を参照してください。

``msg`` と ``values`` でデフォルトのエラーメッセージをオーバライドできます。
詳しくは `Should Be Equal` を参照してください。

使い方は `Should Be Equal As Integers` の例を参考にしてください。


Should Not Be Equal As Numbers
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:Arguments:  [first, second, msg=None, values=True, precision=6]

``first`` と ``second`` を実数に変換した後に比較し、等しいときは失敗します。

値は ``precision`` に指定した精度で `Convert To Number` で変換されます。

``precision`` の使い方や、評価がうまくいかないときの理由を考えたいときは、 `Should Be Equal As Numbers` のサンプルを参照してください。
``msg`` と ``values`` でデフォルトのエラーメッセージをオーバライドできます。
詳しくは `Should Be Equal` を参照してください。


Should Not Be Equal As Strings
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:Arguments:  [first, second, msg=None, values=True]

``first`` と ``second`` を文字列に変換した後に比較し、等しいときは失敗します。

``msg`` と ``values`` でデフォルトのエラーメッセージをオーバライドできます。
詳しくは `Should Be Equal` を参照してください。


Should Not Be True
~~~~~~~~~~~~~~~~~~~~

:Arguments:  [condition, msg=None]

``conditiion`` が真のとき失敗します。

``condition`` の評価方法と、 ``msg`` でデフォルトエラーメッセージをオーバライドする方法は、 `Should Be True` を参照してください。


Should Not Contain
~~~~~~~~~~~~~~~~~~~~

:Arguments:  [container, item, msg=None, values=True]

``container`` に ``item`` が一回以上出現するとき失敗します。 

文字列、リスト、その他 Python の ``in`` 演算子を使える任意のオブジェクトに使えます。
``msg`` と ``values`` でデフォルトのエラーメッセージをオーバライドできます。
詳しくは `Should Be Equal` を参照してください。

例:

.. code:: robotframework

   | Should Not Contain | ${output}    | FAILED |
   | Should Not Contain | ${some list} | value  |


Should Not End With
~~~~~~~~~~~~~~~~~~~~~

:Arguments:  [str1, str2, msg=None, values=True]

文字列 ``str1`` の末尾が文字列 ``str2`` のとき失敗します。

``msg`` と ``values`` でデフォルトのエラーメッセージをオーバライドできます。
詳しくは `Should Be Equal` を参照してください。


Should Not Match
~~~~~~~~~~~~~~~~~~

:Arguments:  [string, pattern, msg=None, values=True]

``string`` がワイルドカードパターン ``pattern`` にマッチすると失敗します。

パターンマッチは、シェルのファイル名マッチと同様で、大小文字を区別します。
``*`` は任意の文字列、 ``?`` は任意の1文字にマッチします。

``msg`` と ``values`` でデフォルトのエラーメッセージをオーバライドできます。
詳しくは `Should Be Equal` を参照してください。


Should Not Match Regexp
~~~~~~~~~~~~~~~~~~~~~~~~~

:Arguments:  [string, pattern, msg=None, values=True]

``string`` が正規表現 ``pattern`` にマッチすると失敗します。

引数の詳細は `Should Match Regexp` を参照してください。


Should Not Start With
~~~~~~~~~~~~~~~~~~~~~~~

:Arguments:  [str1, str2, msg=None, values=True]

文字列 ``str1`` の先頭が文字列 ``str2`` のとき失敗します。

``msg`` と ``values`` でデフォルトのエラーメッセージをオーバライドできます。
詳しくは `Should Be Equal` を参照してください。


Should Start With
~~~~~~~~~~~~~~~~~~~

:Arguments:  [str1, str2, msg=None, values=True]

文字列 ``str1`` の先頭が文字列 ``str2`` でないとき失敗します。

``msg`` と ``values`` でデフォルトのエラーメッセージをオーバライドできます。
詳しくは `Should Be Equal` を参照してください。


Sleep
~~~~~~~

:Arguments:  [time\_, reason=None]

指定時間の間、テストの実行を停止します。

``time`` は、数または時間を表す文字列です。
時間を表す文字列は、 ``1 day 2 hours 3 minutes 4 seconds 5milliseconds`` や ``1d 2h 3m 4s 5ms`` のような形式で表現します。
使えるフォーマットは、ユーザーガイドの付録で詳しく説明しています。
オプションの `reason` は、なぜスリープするかの説明です。
スリープ時間と `reason` は、どちらもログに記録されます。


例:

.. code:: robotframework

   | Sleep | 42                   |
   | Sleep | 1.5                  |
   | Sleep | 2 minutes 10 seconds |
   | Sleep | 10s                  | Wait for a reply |


Variable Should Exist
~~~~~~~~~~~~~~~~~~~~~~~

:Arguments:  [name, msg=None]

指定の変数がスコープ内に存在しない場合に失敗します。

変数の名前は、通常の変数名 (e.g. ``${NAME}``) またはエスケープした形式 (e.g. ``\${NAME}``) です。
前者には、 `Set Suite Variable` で説明したような制限があります。

デフォルトのエラーメッセージは、 ``msg`` 引数で上書きできます。

`Variable Should Not Exist` や `Keyword Should Exist` も参照してください。


Variable Should Not Exist
~~~~~~~~~~~~~~~~~~~~~~~~~~~

:Arguments:  [name, msg=None]

指定の変数がスコープ内に存在すると失敗します。

変数の名前は、通常の変数名 (e.g. ``${NAME}``) またはエスケープした形式 (e.g. ``\${NAME}``) です。
前者には、 `Set Suite Variable` で説明したような制限があります。

デフォルトのエラーメッセージは、 ``msg`` 引数で上書きできます。

`Variable Should Exist` や `Keyword Should Exist` も参照してください。


Wait Until Keyword Succeeds
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:Arguments:  [retry, retry_interval, name, \*args]

指定のキーワードを実行し、失敗した場合にはリトライします。

``name`` および ``args`` で、実行するキーワードを定義します。 `Run Keyword` と同様です。
何回リトライさせるかは、引数 ``retry`` で、タイムアウトまたは回数で指定します。
``retry_interval`` には、キーワードの実行に失敗した際、次のリトライまでどれだけ待機するかを指定します。

``retry`` にタイムアウトを指定する場合は、 Robot Framework の時間フォーマット (e.g. ``1 minute``, ``2 min 3 s``, ``4.5``) を使います。
使えるフォーマットは、ユーザーガイドの付録で詳しく説明しています。
回数を指定する場合は、回数の後ろに ``times`` または ``x`` を付けねばなりません (e.g. ``5 times``, ``10 x``)。
``retry_interval`` は、常に時間フォーマットで指定します。

指定条件のリトライを行ったにも関わらずキーワードが成功しなければ、このキーワード自体が失敗します。
キーワードの実行に成功した場合は、その戻り値を返します。

例::

  | Wait Until Keyword Succeeds | 2 min | 5 sec | My keyword | argument |
  | ${result} = | Wait Until Keyword Succeeds | 3x | 200ms | My keyword |

キーワードを実行した際、通常の失敗がおきたときだけを、キーワードの失敗とみなします。
記法の誤りやテスト・キーワードのタイムアウト、致命的な例外の発生 (`Fatal Error` で起こしたエラーなど) は、キーワードの失敗とみなさず、リトライしません。

このキーワードを使って、同じキーワードを何度も繰り返し実行すると、出力が大量に生成され、出力ファイルがかなり大きくなってしまうでしょう。
Robot Framework 2.7 からは、コマンドラインオプション ``--RemoveKeywords WUKS`` を使って、不要なキーワードを出力から除去できます。

Robot Framework 2.9 からは、 ``retry`` にリトライ回数を指定できるようになりました。
また、変数のエラーをキーワードの失敗として捕捉するようになりました。

