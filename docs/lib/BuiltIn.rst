BuiltIn: 組み込み機能
=======================
Version:          3.0
Scope:            global
Named arguments:  supported

常に利用できる標準ライブラリです。よく使うキーワードが入っています。

``BuiltIn`` は、使うことの多い汎用のキーワードセットを提供する標準ライブラリです。このライブラリは自動的にインポートされるので、いつでも使えます。キーワードの中には、検証に使えるもの (`Should Be Equal` 指定の値に等しいか検証、や `Should Contain`: 指定の値を含むか検証)、値の変換(`Convert To Integer`: 整数に変換) その他もろもろ (`Log`: ログ出力、 `Sleep`: スリープ、 `Run Keyword If`: 条件によって実行、 `Set Global Variable`: グローバル値の設定) があります。


目次
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- `HTMLエラーメッセージ <HTML error messages>`_
- `式の評価 <Evaluating expressions>`_
- `ブール型の引数 <Boolean arguments>`_
- `複数行にわたる文字列の比較 <Multiline string comparisons>`_
- `キーワード <Keywords>`_


.. _HTML error messages:

HTMLエラーメッセージ
---------------------------------------------------

キーワードの多くは、エラーメッセージのオプションを持っています。エラーメッセージは、キーワードの実行に失敗した際に使われます。 Robot Framework 2.8 からは、エラーメッセージの先頭に ``*HTML*`` を付けることで、 HTML 形式のエラーメッセージを使えるようになりました。使い方の例は `Fail` キーワードを参照してください。メッセージの HTML 化は、BuiltIn 以外のライブラリでも使えます。


.. _Evaluating expressions:

式の評価
---------------------------------------------------

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
---------------------------------------------------

キーワードの中には、値を true または false のブール型として扱うものがあります。
そうしたキーワードの文字列を渡す場合、空文字と、 ``false`` または ``no`` (いずれも大小文字を区別しない) は False 扱いになります。
また、キーワードの中には、値を比較して、条件に合わないとき、エラーメッセージに期待値と実際の値を出力するかどうかをスイッチする機能をもったものがありますが、そのようなキーワードでは、 ``no values`` も False 扱いです。
それ以外の文字列は、値が何であっても True 扱いです。
その他の引数タイプでは、 :ref:`Python の流儀 <http://docs.python.org/2/library/stdtypes.html#truth-value-testing>` で True/False を決めます。

値が真になる例は以下の通りです:

.. code:: robotframework

   | `Should Be Equal` | ${x} | ${y}  | Custom error | values=True    | # Strings are generally true.    |
   | `Should Be Equal` | ${x} | ${y}  | Custom error | values=yes     | # Same as the above.             |
   | `Should Be Equal` | ${x} | ${y}  | Custom error | values=${TRUE} | # Python ``True`` is true.       |
   | `Should Be Equal` | ${x} | ${y}  | Custom error | values=${42}   | # Numbers other than 0 are true. |


一方、偽になる例は以下の通りです:

.. code:: robotframework

   | `Should Be Equal` | ${x} | ${y}  | Custom error | values=False     | # String ``false`` is false.   |
   | `Should Be Equal` | ${x} | ${y}  | Custom error | values=no        | # Also string ``no`` is false. |
   | `Should Be Equal` | ${x} | ${y}  | Custom error | values=${EMPTY}  | # Empty string is false.       |
   | `Should Be Equal` | ${x} | ${y}  | Custom error | values=${FALSE}  | # Python ``False`` is false.   |
   | `Should Be Equal` | ${x} | ${y}  | Custom error | values=no values | # ``no values`` works with ``values`` argument |

Robot Framework 2.9 以前では、原則、 ``false`` や ``no`` も含め、空文字列でないものは全て True 扱いとしていました。

.. _Multiline string comparisons:

複数行からなる文字列の比較
---------------------------------------------------

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
---------------------------------------------------

Call Method
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

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
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

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
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:Arguments:  [\*messages]

`messages` の内容をそのままログファイルに出力します。

このキーワードは、引数に対して何もせず、ただログに出力します。
引数はどんな記法であっても無視されるので、存在しない変数を参照するような内容を書いてもエラーになりません。
変数の値を出力したいときは、 `Log` や `Log Many` を使ってください。

Continue For Loop
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

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
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

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
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

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
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:Arguments:  [item]

指定値をブール型の True または False に変換します。

``True`` や ``False`` (大小文字の区別なし) は期待通りの値に変換されます。
それ以外の値に対しては、 Python の ``bool()`` メソッドによる `真偽値 <http://docs.python.org/2/library/stdtypes.html#truth>`_ を返します。

Convert To Bytes
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

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
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:Arguments:  [item, base=None, prefix=None, length=None, lowercase=False]

             
Converts the given item to a hexadecimal string.

The ``item``, with an optional ``base``, is first converted to an
integer using `Convert To Integer` internally. After that it
is converted to a hexadecimal number (base 16) represented as
a string such as ``FF0A``.

The returned value can contain an optional ``prefix`` and can be
required to be of minimum ``length`` (excluding the prefix and a
possible minus sign). If the value is initially shorter than
the required length, it is padded with zeros.

By default the value is returned as an upper case string, but the
``lowercase`` argument a true value (see `Boolean arguments`) turns
the value (but not the given prefix) to lower case.

例::

  | ${result} = | Convert To Hex | 255 |           |              | # Result is FF    |
  | ${result} = | Convert To Hex | -10 | prefix=0x | length=2     | # Result is -0x0A |
  | ${result} = | Convert To Hex | 255 | prefix=X | lowercase=yes | # Result is Xff   |

See also `Convert To Integer`, `Convert To Binary` and `Convert To Octal`.

Convert To Integer
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:Arguments:  [item, base=None]

Converts the given item to an integer number.

If the given item is a string, it is by default expected to be an
integer in base 10. There are two ways to convert from other bases:

- Give base explicitly to the keyword as ``base`` argument.

- Prefix the given string with the base so that ``0b`` means binary
  (base 2), ``0o`` means octal (base 8), and ``0x`` means hex (base 16).
  The prefix is considered only when ``base`` argument is not given and
  may itself be prefixed with a plus or minus sign.

The syntax is case-insensitive and possible spaces are ignored.

例::

  | ${result} = | Convert To Integer | 100    |    | # Result is 100   |
  | ${result} = | Convert To Integer | FF AA  | 16 | # Result is 65450 |
  | ${result} = | Convert To Integer | 100    | 8  | # Result is 64    |
  | ${result} = | Convert To Integer | -100   | 2  | # Result is -4    |
  | ${result} = | Convert To Integer | 0b100  |    | # Result is 4     |
  | ${result} = | Convert To Integer | -0x100 |    | # Result is -256  |

See also `Convert To Number`, `Convert To Binary`, `Convert To Octal`,
`Convert To Hex`, and `Convert To Bytes`.

Convert To Number
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:Arguments:  [item, precision=None]

Converts the given item to a floating point number.

If the optional ``precision`` is positive or zero, the returned number
is rounded to that number of decimal digits. Negative precision means
that the number is rounded to the closest multiple of 10 to the power
of the absolute precision. If a number is equally close to a certain
precision, it is always rounded away from zero.

例::

  | ${result} = | Convert To Number | 42.512 |    | # Result is 42.512 |
  | ${result} = | Convert To Number | 42.512 | 1  | # Result is 42.5   |
  | ${result} = | Convert To Number | 42.512 | 0  | # Result is 43.0   |
  | ${result} = | Convert To Number | 42.512 | -1 | # Result is 40.0   |

Notice that machines generally cannot store floating point numbers
accurately. This may cause surprises with these numbers in general
and also when they are rounded. For more information see, for example,
these resources:

- http://docs.python.org/2/tutorial/floatingpoint.html
- http://randomascii.wordpress.com/2012/02/25/comparing-floating-point-numbers-2012-edition

If you need an integer number, use `Convert To Integer` instead.

Convert To Octal
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:Arguments:  [item, base=None, prefix=None, length=None]

Converts the given item to an octal string.

The ``item``, with an optional ``base``, is first converted to an
integer using `Convert To Integer` internally. After that it
is converted to an octal number (base 8) represented as a
string such as ``775``.

The returned value can contain an optional ``prefix`` and can be
required to be of minimum ``length`` (excluding the prefix and a
possible minus sign). If the value is initially shorter than
the required length, it is padded with zeros.

例::

  | ${result} = | Convert To Octal | 10 |            |          | # Result is 12 |
  | ${result} = | Convert To Octal | -F | base=16    | prefix=0 | # Result is -017    |
  | ${result} = | Convert To Octal | 16 | prefix=oct | length=4 | # Result is oct0020 |

See also `Convert To Integer`, `Convert To Binary` and `Convert To Hex`.

Convert To String
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:Arguments:  [item]

Converts the given item to a Unicode string.

Uses ``__unicode__`` or ``__str__`` method with Python objects and
``toString`` with Java objects.

Use `Encode String To Bytes` and `Decode Bytes To String` keywords
in ``String`` library if you need to convert between Unicode and byte
strings using different encodings. Use `Convert To Bytes` if you just
want to create byte strings.

Create Dictionary
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:Arguments:  [\*items]

Creates and returns a dictionary based on given items.

Items are given using ``key=value`` syntax same way as ``&{dictionary}``
variables are created in the Variable table. Both keys and values
can contain variables, and possible equal sign in key can be escaped
with a backslash like ``escaped\=key=value``. It is also possible to
get items from existing dictionaries by simply using them like
``&{dict}``.

If same key is used multiple times, the last value has precedence.
The returned dictionary is ordered, and values with strings as keys
can also be accessed using convenient dot-access syntax like
``${dict.key}``.

例::

  | &{dict} = | Create Dictionary | key=value | foo=bar |
  | Should Be True | ${dict} == {'key': 'value', 'foo': 'bar'} |
  | &{dict} = | Create Dictionary | ${1}=${2} | &{dict} | foo=new |
  | Should Be True | ${dict} == {1: 2, 'key': 'value', 'foo': 'new'} |
  | Should Be Equal | ${dict.key} | value |

This keyword was changed in Robot Framework 2.9 in many ways:
- Moved from ``Collections`` library to ``BuiltIn``.
- Support also non-string keys in ``key=value`` syntax.
- Deprecated old syntax to give keys and values separately.
- Returned dictionary is ordered and dot-accessible.

Create List
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:Arguments:  [\*items]

Returns a list containing given items.

The returned list can be assigned both to ``${scalar}`` and ``@{list}``
variables.

例::

  | @{list} =   | Create List | a    | b    | c    |
  | ${scalar} = | Create List | a    | b    | c    |
  | ${ints} =   | Create List | ${1} | ${2} | ${3} |

Evaluate
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:Arguments:  [expression, modules=None, namespace=None]

Evaluates the given expression in Python and returns the results.

``expression`` is evaluated in Python as explained in `Evaluating
expressions`.

``modules`` argument can be used to specify a comma separated
list of Python modules to be imported and added to the evaluation
namespace.

``namespace`` argument can be used to pass a custom evaluation
namespace as a dictionary. Possible ``modules`` are added to this
namespace. This is a new feature in Robot Framework 2.8.4.

Variables used like ``${variable}`` are replaced in the expression
before evaluation. Variables are also available in the evaluation
namespace and can be accessed using special syntax ``$variable``.
This is a new feature in Robot Framework 2.9 and it is explained more
thoroughly in `Evaluating expressions`.

Examples (expecting ``${result}`` is 3.14)::

  | ${status} = | Evaluate | 0 < ${result} < 10 | # Would also work with string '3.14' |
  | ${status} = | Evaluate | 0 < $result < 10   | # Using variable itself, not string representation |
  | ${random} = | Evaluate | random.randint(0, sys.maxint) | modules=random, sys   |
  | ${ns} =     | Create Dictionary | x=${4}    | y=${2}              |
  | ${result} = | Evaluate | x*10 + y           | namespace=${ns}     |
  =>
  | ${status} = True
  | ${random} = <random integer>
  | ${result} = 42

Exit For Loop
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:Arguments:  []

Stops executing the enclosing for loop.

Exits the enclosing for loop and continues execution after it.
Can be used directly in a for loop or in a keyword that the loop uses.

例:

.. code:: robotframework

  | :FOR | ${var}         | IN                 | @{VALUES}     |
  |      | Run Keyword If | '${var}' == 'EXIT' | Exit For Loop |
  |      | Do Something   | ${var} |

See `Exit For Loop If` to conditionally exit a for loop without
using `Run Keyword If` or other wrapper keywords.

Exit For Loop If
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:Arguments:  [condition]

Stops executing the enclosing for loop if the ``condition`` is true.

A wrapper for `Exit For Loop` to exit a for loop based on
the given condition. The condition is evaluated using the same
semantics as with `Should Be True` keyword.

例:

.. code:: robotframework

  | :FOR | ${var}           | IN                 | @{VALUES} |
  |      | Exit For Loop If | '${var}' == 'EXIT' |
  |      | Do Something     | ${var}             |

New in Robot Framework 2.8.

Fail
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:Arguments:  [msg=None, \*tags]

Fails the test with the given message and optionally alters its tags.

The error message is specified using the ``msg`` argument.
It is possible to use HTML in the given error message, similarly
as with any other keyword accepting an error message, by prefixing
the error with ``*HTML*``.

It is possible to modify tags of the current test case by passing tags
after the message. Tags starting with a hyphen (e.g. ``-regression``)
are removed and others added. Tags are modified using `Set Tags` and
`Remove Tags` internally, and the semantics setting and removing them
are the same as with these keywords.

例::

  | Fail | Test not ready   |             | | # Fails with the given message.
  |
  | Fail | *HTML*<b>Test not ready</b> | | | # Fails using HTML in the message.
  | 
  | Fail | Test not ready   | not-ready   | | # Fails and adds 'not-ready' tag.
  |
  | Fail | OS not supported | -regression | | # Removes tag 'regression'.
  |
  | Fail | My message       | tag    | -t*  | # Removes all tags starting with 't' except the newly added 'tag'. |

See `Fatal Error` if you need to stop the whole test execution.

Support for modifying tags was added in Robot Framework 2.7.4 and
HTML message support in 2.8.

Fatal Error
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:Arguments:  [msg=None]

Stops the whole test execution.

The test or suite where this keyword is used fails with the provided
message, and subsequent tests fail with a canned message.
Possible teardowns will nevertheless be executed.

See `Fail` if you only want to stop one test case unconditionally.

Get Count
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:Arguments:  [item1, item2]

Returns and logs how many times ``item2`` is found from ``item1``.

This keyword works with Python strings and lists and all objects
that either have ``count`` method or can be converted to Python lists.

例:

.. code:: robotframework
  
  | ${count} = | Get Count | ${some item} | interesting value |
  | Should Be True | 5 < ${count} < 10 |

Get Length
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:Arguments:  [item]

Returns and logs the length of the given item as an integer.

The item can be anything that has a length, for example, a string,
a list, or a mapping. The keyword first tries to get the length with
the Python function ``len``, which calls the  item's ``__len__`` method
internally. If that fails, the keyword tries to call the item's
possible ``length`` and ``size`` methods directly. The final attempt is
trying to get the value of the item's ``length`` attribute. If all
these attempts are unsuccessful, the keyword fails.

例::

  | ${length} = | Get Length    | Hello, world! |        |
  | Should Be Equal As Integers | ${length}     | 13     |
  | @{list} =   | Create List   | Hello,        | world! |
  | ${length} = | Get Length    | ${list}       |        |
  | Should Be Equal As Integers | ${length}     | 2      |

See also `Length Should Be`, `Should Be Empty` and `Should Not Be
Empty`.

Get Library Instance
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:Arguments:  [name=None, all=False]

Returns the currently active instance of the specified test library.

This keyword makes it easy for test libraries to interact with
other test libraries that have state. This is illustrated by
the Python example below::

  | from robot.libraries.BuiltIn import BuiltIn
  |
  | def title_should_start_with(expected):
  |     seleniumlib = BuiltIn().get_library_instance('SeleniumLibrary')
  |     title = seleniumlib.get_title()
  |     if not title.startswith(expected):
  |         raise AssertionError("Title '%s' did not start with '%s'"
  |                              % (title, expected))

It is also possible to use this keyword in the test data and
pass the returned library instance to another keyword. If a
library is imported with a custom name, the ``name`` used to get
the instance must be that name and not the original library name.

If the optional argument ``all`` is given a true value, then a
dictionary mapping all library names to instances will be returned.
This feature is new in Robot Framework 2.9.2.

例:

.. code:: robotframework

  | &{all libs} = | Get library instance | all=True |

Get Time
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:Arguments:  [format=timestamp, time_=NOW]

Returns the given time in the requested format.

*NOTE:* DateTime library added in Robot Framework 2.8.5 contains
much more flexible keywords for getting the current date and time
and for date and time handling in general.

How time is returned is determined based on the given ``format``
string as follows. Note that all checks are case-insensitive.

1) If ``format`` contains the word ``epoch``, the time is returned
   in seconds after the UNIX epoch (1970-01-01 00:00:00 UTC).
   The return value is always an integer.

2) If ``format`` contains any of the words ``year``, ``month``,
   ``day``, ``hour``, ``min``, or ``sec``, only the selected parts are
   returned. The order of the returned parts is always the one
   in the previous sentence and the order of words in ``format``
   is not significant. The parts are returned as zero-padded
   strings (e.g. May -> ``05``).

3) Otherwise (and by default) the time is returned as a
   timestamp string in the format ``2006-02-24 15:08:31``.

By default this keyword returns the current local time, but
that can be altered using ``time`` argument as explained below.
Note that all checks involving strings are case-insensitive.

1) If ``time`` is a number, or a string that can be converted to
   a number, it is interpreted as seconds since the UNIX epoch.
   This documentation was originally written about 1177654467
   seconds after the epoch.

2) If ``time`` is a timestamp, that time will be used. Valid
   timestamp formats are ``YYYY-MM-DD hh:mm:ss`` and
   ``YYYYMMDD hhmmss``.

3) If ``time`` is equal to ``NOW`` (default), the current local
   time is used. This time is got using Python's ``time.time()``
   function.

4) If ``time`` is equal to ``UTC``, the current time in
   [http://en.wikipedia.org/wiki/Coordinated_Universal_Time|UTC]
   is used. This time is got using ``time.time() + time.altzone``
   in Python.

5) If ``time`` is in the format like ``NOW - 1 day`` or ``UTC + 1 hour
   30 min``, the current local/UTC time plus/minus the time
   specified with the time string is used. The time string format
   is described in an appendix of Robot Framework User Guide.

Examples (expecting the current local time is 2006-03-29 15:06:21)::

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

Examples (expecting the current local time is 2006-03-29 15:06:21 and
UTC time is 2006-03-29 12:06:21)::

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

Support for UTC time was added in Robot Framework 2.7.5 but it did not
work correctly until 2.7.7.

Get Variable Value
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:Arguments:  [name, default=None]

Returns variable value or ``default`` if the variable does not exist.

The name of the variable can be given either as a normal variable name
(e.g. ``${NAME}``) or in escaped format (e.g. ``\${NAME}``). Notice
that the former has some limitations explained in `Set Suite Variable`.

例::

  | ${x} = | Get Variable Value | ${a} | default |
  | ${y} = | Get Variable Value | ${a} | ${b}    |
  | ${z} = | Get Variable Value | ${z} |         |
  =>
  | ${x} gets value of ${a} if ${a} exists and string 'default' otherwise
  | ${y} gets value of ${a} if ${a} exists and value of ${b} otherwise
  | ${z} is set to Python None if it does not exist previously

See `Set Variable If` for another keyword to set variables dynamically.

Get Variables
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:Arguments:  [no_decoration=False]

Returns a dictionary containing all variables in the current scope.

Variables are returned as a special dictionary that allows accessing
variables in space, case, and underscore insensitive manner similarly
as accessing variables in the test data. This dictionary supports all
same operations as normal Python dictionaries and, for example,
Collections library can be used to access or modify it. Modifying the
returned dictionary has no effect on the variables available in the
current scope.

By default variables are returned with ``${}``, ``@{}`` or ``&{}``
decoration based on variable types. Giving a true value (see `Boolean
arguments`) to the optional argument ``no_decoration`` will return
the variables without the decoration. This option is new in Robot
Framework 2.9.

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

Note: Prior to Robot Framework 2.7.4 variables were returned as
a custom object that did not support all dictionary methods.

Import Library
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:Arguments:  [name, \*args]

Imports a library with the given name and optional arguments.

This functionality allows dynamic importing of libraries while tests
are running. That may be necessary, if the library itself is dynamic
and not yet available when test data is processed. In a normal case,
libraries should be imported using the Library setting in the Setting
table.

This keyword supports importing libraries both using library
names and physical paths. When paths are used, they must be
given in absolute format or found from
[http://robotframework.org/robotframework/latest/RobotFrameworkUserGuide.html
#pythonpath-jythonpath-and-ironpythonpath|
search path]. Forward slashes can be used as path separators in all
operating systems.

It is possible to pass arguments to the imported library and also
named argument syntax works if the library supports it. ``WITH NAME``
syntax can be used to give a custom name to the imported library.

例::

  | Import Library | MyLibrary |
  | Import Library | ${CURDIR}/../Library.py | arg1 | named=arg2 |
  | Import Library | ${LIBRARIES}/Lib.java | arg | WITH NAME | JavaLib |

Import Resource
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:Arguments:  [path]

Imports a resource file with the given path.

Resources imported with this keyword are set into the test suite scope
similarly when importing them in the Setting table using the Resource
setting.

The given path must be absolute or found from
[http://robotframework.org/robotframework/latest/RobotFrameworkUserGuide.html
#pythonpath-jythonpath-and-ironpythonpath|
search path]. Forward slashes can be used as path separator regardless
the operating system.

例::

  | Import Resource | ${CURDIR}/resource.txt |
  | Import Resource | ${CURDIR}/../resources/resource.html |
  | Import Resource | found_from_pythonpath.robot |

Import Variables
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:Arguments:  [path, \*args]

Imports a variable file with the given path and optional arguments.

Variables imported with this keyword are set into the test suite scope
similarly when importing them in the Setting table using the Variables
setting. These variables override possible existing variables with
the same names. This functionality can thus be used to import new
variables, for example, for each test in a test suite.

The given path must be absolute or found from
[http://robotframework.org/robotframework/latest/RobotFrameworkUserGuide.html
#pythonpath-jythonpath-and-ironpythonpath|
search path]. Forward slashes can be used as path separator regardless
the operating system.

例::

  | Import Variables | ${CURDIR}/variables.py   |      |      |
  | Import Variables | ${CURDIR}/../vars/env.py | arg1 | arg2 |
  | Import Variables | file_from_pythonpath.py  |      |      |

Keyword Should Exist
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:Arguments:  [name, msg=None]

Fails unless the given keyword exists in the current scope.

Fails also if there are more than one keywords with the same name.
Works both with the short name (e.g. ``Log``) and the full name
(e.g. ``BuiltIn.Log``).

The default error message can be overridden with the ``msg`` argument.

See also `Variable Should Exist`.

Length Should Be
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:Arguments:  [item, length, msg=None]

Verifies that the length of the given item is correct.

The length of the item is got using the `Get Length` keyword. The
default error message can be overridden with the ``msg`` argument.

Log
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:Arguments:  [message, level=INFO, html=False, console=False, repr=False]

Logs the given message with the given level.

Valid levels are TRACE, DEBUG, INFO (default), HTML, WARN, and ERROR.
Messages below the current active log level are ignored. See
`Set Log Level` keyword and ``--loglevel`` command line option
for more details about setting the level.

Messages logged with the WARN or ERROR levels will be automatically
visible also in the console and in the Test Execution Errors section
in the log file.

Logging can be configured using optional ``html``, ``console`` and
``repr`` arguments. They are off by default, but can be enabled
by giving them a true value. See `Boolean arguments` section for more
information about true and false values.

If the ``html`` argument is given a true value, the message will be
considered HTML and special characters such as ``<`` in it are not
escaped. For example, logging ``<img src="image.png">`` creates an
image when ``html`` is true, but otherwise the message is that exact
string. An alternative to using the ``html`` argument is using the HTML
pseudo log level. It logs the message as HTML using the INFO level.

If the ``console`` argument is true, the message will be written to
the console where test execution was started from in addition to
the log file. This keyword always uses the standard output stream
and adds a newline after the written message. Use `Log To Console`
instead if either of these is undesirable,

If the ``repr`` argument is true, the given item will be passed through
a custom version of Python's ``pprint.pformat()`` function before
logging it. This is useful, for example, when working with strings or
bytes containing invisible characters, or when working with nested data
structures. The custom version differs from the standard one so that it
omits the ``u`` prefix from Unicode strings and adds ``b`` prefix to
byte strings.

例::

  | Log | Hello, world!        |          |   | # Normal INFO message.   |
  | Log | Warning, world!      | WARN     |   | # Warning.               |
  | Log | <b>Hello</b>, world! | html=yes |   | # INFO message as HTML.  |
  | Log | <b>Hello</b>, world! | HTML     |   | # Same as above.         |
  | Log | <b>Hello</b>, world! | DEBUG    | html=true | # DEBUG as HTML. |
  | Log | Hello, console!   | console=yes | | # Log also to the console. |
  | Log | Hyvä \x00     | repr=yes    | | # Log ``'Hyv\xe4 \x00'``. |

See `Log Many` if you want to log multiple messages in one go, and
`Log To Console` if you only want to write to the console.

Arguments ``html``, ``console``, and ``repr`` are new in Robot Framework
2.8.2.

Pprint support when ``repr`` is used is new in Robot Framework 2.8.6,
and it was changed to drop the ``u`` prefix and add the ``b`` prefix
in Robot Framework 2.9.

Log Many
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:Arguments:  [\*messages]

Logs the given messages as separate entries using the INFO level.

Supports also logging list and dictionary variable items individually.

例::

  | Log Many | Hello   | ${var}  |
  | Log Many | @{list} | &{dict} |

See `Log` and `Log To Console` keywords if you want to use alternative
log levels, use HTML, or log to the console.

Log To Console
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:Arguments:  [message, stream=STDOUT, no_newline=False]

Logs the given message to the console.

By default uses the standard output stream. Using the standard error
stream is possibly by giving the ``stream`` argument value ``STDERR``
(case-insensitive).

By default appends a newline to the logged message. This can be
disabled by giving the ``no_newline`` argument a true value (see
`Boolean arguments`).

例::

  | Log To Console | Hello, console!             |                 |
  | Log To Console | Hello, stderr!              | STDERR          |
  | Log To Console | Message starts here and is  | no_newline=true |
  | Log To Console | continued without newline.  |                 |

This keyword does not log the message to the normal log file. Use
`Log` keyword, possibly with argument ``console``, if that is desired.

New in Robot Framework 2.8.2.

Log Variables
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:Arguments:  [level=INFO]

Logs all variables in the current scope with given log level.

No Operation
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:Arguments:  []

Does absolutely nothing.

Pass Execution
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:Arguments:  [message, \*tags]

Skips rest of the current test, setup, or teardown with PASS status.

This keyword can be used anywhere in the test data, but the place where
used affects the behavior:

- When used in any setup or teardown (suite, test or keyword), passes
  that setup or teardown. Possible keyword teardowns of the started
  keywords are executed. Does not affect execution or statuses
  otherwise.
- When used in a test outside setup or teardown, passes that particular
  test case. Possible test and keyword teardowns are executed.

Possible continuable failures before this keyword is used, as well as
failures in executed teardowns, will fail the execution.

It is mandatory to give a message explaining why execution was passed.
By default the message is considered plain text, but starting it with
``*HTML*`` allows using HTML formatting.

It is also possible to modify test tags passing tags after the message
similarly as with `Fail` keyword. Tags starting with a hyphen
(e.g. ``-regression``) are removed and others added. Tags are modified
using `Set Tags` and `Remove Tags` internally, and the semantics
setting and removing them are the same as with these keywords.

例::

  | Pass Execution | All features available in this version tested. |
  | Pass Execution | Deprecated test. | deprecated | -regression    |

This keyword is typically wrapped to some other keyword, such as
`Run Keyword If`, to pass based on a condition. The most common case
can be handled also with `Pass Execution If`::

  | Run Keyword If    | ${rc} < 0 | Pass Execution | Negative values are cool. |
  | Pass Execution If | ${rc} < 0 | Negative values are cool. |

Passing execution in the middle of a test, setup or teardown should be
used with care. In the worst case it leads to tests that skip all the
parts that could actually uncover problems in the tested application.
In cases where execution cannot continue do to external factors,
it is often safer to fail the test case and make it non-critical.

New in Robot Framework 2.8.

Pass Execution If
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:Arguments:  [condition, message, \*tags]

Conditionally skips rest of the current test, setup, or teardown with PASS
status.

A wrapper for `Pass Execution` to skip rest of the current test,
setup or teardown based the given ``condition``. The condition is
evaluated similarly as with `Should Be True` keyword, and ``message``
and ``*tags`` have same semantics as with `Pass Execution`.

例:

.. code:: robotframework

  
  | :FOR | ${var}            | IN                     | @{VALUES}
  |
  |      | Pass Execution If | '${var}' == 'EXPECTED' | Correct value was found
  |
  |      | Do Something      | ${var}                 |

New in Robot Framework 2.8.

Regexp Escape
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:Arguments:  [\*patterns]

Returns each argument string escaped for use as a regular expression.

This keyword can be used to escape strings to be used with
`Should Match Regexp` and `Should Not Match Regexp` keywords.

Escaping is done with Python's ``re.escape()`` function.

例::

  | ${escaped} = | Regexp Escape | ${original} |
  | @{strings} = | Regexp Escape | @{strings}  |

Reload Library
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:Arguments:  [name_or_instance]

Rechecks what keywords the specified library provides.

Can be called explicitly in the test data or by a library itself
when keywords it provides have changed.

The library can be specified by its name or as the active instance of
the library. The latter is especially useful if the library itself
calls this keyword as a method.

New in Robot Framework 2.9.

Remove Tags
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:Arguments:  [\*tags]

Removes given ``tags`` from the current test or all tests in a suite.

Tags can be given exactly or using a pattern where ``*`` matches
anything and ``?`` matches one character.

This keyword can affect either one test case or all test cases in a
test suite similarly as `Set Tags` keyword.

The current tags are available as a built-in variable ``@{TEST TAGS}``.

例:

.. code:: robotframework
  
  | Remove Tags | mytag | something-* | ?ython |

See `Set Tags` if you want to add certain tags and `Fail` if you want
to fail the test case after setting and/or removing tags.

Repeat Keyword
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:Arguments:  [repeat, name, \*args]

Executes the specified keyword multiple times.

``name`` and ``args`` define the keyword that is executed similarly as
with `Run Keyword`. ``repeat`` specifies how many times (as a count) or
how long time (as a timeout) the keyword should be executed.

If ``repeat`` is given as count, it specifies how many times the
keyword should be executed. ``repeat`` can be given as an integer or
as a string that can be converted to an integer. If it is a string,
it can have postfix ``times`` or ``x`` (case and space insensitive)
to make the expression more explicit.

If ``repeat`` is given as timeout, it must be in Robot Framework's
time format (e.g. ``1 minute``, ``2 min 3 s``). Using a number alone
(e.g. ``1`` or ``1.5``) does not work in this context.

If ``repeat`` is zero or negative, the keyword is not executed at
all. This keyword fails immediately if any of the execution
rounds fails.

例::

  | Repeat Keyword | 5 times   | Go to Previous Page |
  | Repeat Keyword | ${var}    | Some Keyword | arg1 | arg2 |
  | Repeat Keyword | 2 minutes | Some Keyword | arg1 | arg2 |

Specifying ``repeat`` as a timeout is new in Robot Framework 3.0.

Replace Variables
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:Arguments:  [text]

Replaces variables in the given text with their current values.

If the text contains undefined variables, this keyword fails.
If the given ``text`` contains only a single variable, its value is
returned as-is and it can be any object. Otherwise this keyword
always returns a string.

例:

The file ``template.txt`` contains ``Hello ${NAME}!`` and variable
``${NAME}`` has the value ``Robot``.

.. code:: robotframework

  | ${template} =   | Get File          | ${CURDIR}/template.txt |
  | ${message} =    | Replace Variables | ${template}            |
  | Should Be Equal | ${message}        | Hello Robot!           |

Return From Keyword
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:Arguments:  [\*return_values]

Returns from the enclosing user keyword.

This keyword can be used to return from a user keyword with PASS status
without executing it fully. It is also possible to return values
similarly as with the ``[Return]`` setting. For more detailed information
about working with the return values, see the User Guide.

This keyword is typically wrapped to some other keyword, such as
`Run Keyword If` or `Run Keyword If Test Passed`, to return based
on a condition::

  | Run Keyword If | ${rc} < 0 | Return From Keyword |
  | Run Keyword If Test Passed | Return From Keyword |

It is possible to use this keyword to return from a keyword also inside
a for loop. That, as well as returning values, is demonstrated by the
`Find Index` keyword in the following somewhat advanced example.
Notice that it is often a good idea to move this kind of complicated
logic into a test library.
::

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

The most common use case, returning based on an expression, can be
accomplished directly with `Return From Keyword If`. Both of these
keywords are new in Robot Framework 2.8.

See also `Run Keyword And Return` and `Run Keyword And Return If`.

Return From Keyword If
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:Arguments:  [condition, \*return_values]

Returns from the enclosing user keyword if ``condition`` is true.

A wrapper for `Return From Keyword` to return based on the given
condition. The condition is evaluated using the same semantics as
with `Should Be True` keyword.

Given the same example as in `Return From Keyword`, we can rewrite the
`Find Index` keyword as follows::

  | ***** Keywords *****
  | Find Index
  |    [Arguments]    ${element}    @{items}
  |    ${index} =    Set Variable    ${0}
  |    :FOR    ${item}    IN    @{items}
  |    \    Return From Keyword If    '${item}' == '${element}'    ${index}
  |    \    ${index} =    Set Variable    ${index + 1}
  |    Return From Keyword    ${-1}    # Also [Return] would work here.

See also `Run Keyword And Return` and `Run Keyword And Return If`.

New in Robot Framework 2.8.

Run Keyword
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:Arguments:  [name, \*args]

Executes the given keyword with the given arguments.

Because the name of the keyword to execute is given as an argument, it
can be a variable and thus set dynamically, e.g. from a return value of
another keyword or from the command line.

Run Keyword And Continue On Failure
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:Arguments:  [name, \*args]

Runs the keyword and continues execution even if a failure occurs.

The keyword name and arguments work as with `Run Keyword`.

例:

.. code:: robotframework
  
  | Run Keyword And Continue On Failure | Fail | This is a stupid example |
  | Log | This keyword is executed |

The execution is not continued if the failure is caused by invalid syntax,
timeout, or fatal exception.
Since Robot Framework 2.9, variable errors are caught by this keyword.

Run Keyword And Expect Error
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:Arguments:  [expected_error, name, \*args]

Runs the keyword and checks that the expected error occurred.

The expected error must be given in the same format as in
Robot Framework reports. It can be a pattern containing
characters ``?``, which matches to any single character and
``*``, which matches to any number of any characters. ``name`` and
``\*args`` have same semantics as with `Run Keyword`.

If the expected error occurs, the error message is returned and it can
be further processed/tested, if needed. If there is no error, or the
error does not match the expected error, this keyword fails.

例::

  | Run Keyword And Expect Error | My error | Some Keyword | arg1 | arg2 |
  | ${msg} = | Run Keyword And Expect Error | * | My KW |
  | Should Start With | ${msg} | Once upon a time in |

Errors caused by invalid syntax, timeouts, or fatal exceptions are not
caught by this keyword.
Since Robot Framework 2.9, variable errors are caught by this keyword.

Run Keyword And Ignore Error
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:Arguments:  [name, \*args]

Runs the given keyword with the given arguments and ignores possible error.

This keyword returns two values, so that the first is either string
``PASS`` or ``FAIL``, depending on the status of the executed keyword.
The second value is either the return value of the keyword or the
received error message. See `Run Keyword And Return Status` If you are
only interested in the execution status.

The keyword name and arguments work as in `Run Keyword`. See
`Run Keyword If` for a usage example.

Errors caused by invalid syntax, timeouts, or fatal exceptions are not
caught by this keyword. Otherwise this keyword itself never fails.
Since Robot Framework 2.9, variable errors are caught by this keyword.

Run Keyword And Return
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:Arguments:  [name, \*args]

Runs the specified keyword and returns from the enclosing user keyword.

The keyword to execute is defined with ``name`` and ``\*args`` exactly
like with `Run Keyword`. After running the keyword, returns from the
enclosing user keyword and passes possible return value from the
executed keyword further. Returning from a keyword has exactly same
semantics as with `Return From Keyword`.

例:

.. code:: robotframework
  
  | `Run Keyword And Return`  | `My Keyword` | arg1 | arg2 |
  | # Above is equivalent to: |
  | ${result} =               | `My Keyword` | arg1 | arg2 |
  | `Return From Keyword`     | ${result}    |      |      |

Use `Run Keyword And Return If` if you want to run keyword and return
based on a condition.

New in Robot Framework 2.8.2.

Run Keyword And Return If
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:Arguments:  [condition, name, \*args]

Runs the specified keyword and returns from the enclosing user keyword.

A wrapper for `Run Keyword And Return` to run and return based on
the given ``condition``. The condition is evaluated using the same
semantics as with `Should Be True` keyword.

例:

.. code:: robotframework
  
  | `Run Keyword And Return If` | ${rc} > 0 | `My Keyword` | arg1 | arg2 |
  | # Above is equivalent to:   |
  | `Run Keyword If`            | ${rc} > 0 | `Run Keyword And Return` | `My Keyword ` | arg1 | arg2 |

Use `Return From Keyword If` if you want to return a certain value
based on a condition.

New in Robot Framework 2.8.2.

Run Keyword And Return Status
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:Arguments:  [name, \*args]

Runs the given keyword with given arguments and returns the status as a
Boolean value.

This keyword returns Boolean ``True`` if the keyword that is executed
succeeds and ``False`` if it fails. This is useful, for example, in
combination with `Run Keyword If`. If you are interested in the error
message or return value, use `Run Keyword And Ignore Error` instead.

The keyword name and arguments work as in `Run Keyword`.

例:

.. code:: robotframework
  
  | ${passed} = | `Run Keyword And Return Status` | Keyword | args |
  | `Run Keyword If` | ${passed} | Another keyword |

Errors caused by invalid syntax, timeouts, or fatal exceptions are not
caught by this keyword. Otherwise this keyword itself never fails.

New in Robot Framework 2.7.6.


Run Keyword If
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:Arguments:  [condition, name, \*args]

Runs the given keyword with the given arguments, if ``condition`` is true.

The given ``condition`` is evaluated in Python as explained in
`Evaluating expressions`, and ``name`` and ``\*args`` have same
semantics as with `Run Keyword`.

Example, a simple if/else construct::
  | ${status} | ${value} = | `Run Keyword And Ignore Error` | `My Keyword` |
  | `Run Keyword If`     | '${status}' == 'PASS' | `Some Action`    | arg |
  | `Run Keyword Unless` | '${status}' == 'PASS' | `Another Action` |

In this example, only either `Some Action` or `Another Action` is
executed, based on the status of `My Keyword`. Instead of `Run Keyword
And Ignore Error` you can also use `Run Keyword And Return Status`.

Variables used like ``${variable}``, as in the examples above, are
replaced in the expression before evaluation. Variables are also
available in the evaluation namespace and can be accessed using special
syntax ``$variable``. This is a new feature in Robot Framework 2.9
and it is explained more thoroughly in `Evaluating expressions`.

例:

.. code:: robotframework
  
  | `Run Keyword If` | $result is None or $result == 'FAIL' | `Keyword` |

Starting from Robot version 2.7.4, this keyword supports also optional
ELSE and ELSE IF branches. Both of these are defined in ``\*args`` and
must use exactly format ``ELSE`` or ``ELSE IF``, respectively. ELSE
branches must contain first the name of the keyword to execute and then
its possible arguments. ELSE IF branches must first contain a condition,
like the first argument to this keyword, and then the keyword to execute
and its possible arguments. It is possible to have ELSE branch after
ELSE IF and to have multiple ELSE IF branches.

Given previous example, if/else construct can also be created like this::
  | ${status} | ${value} = | `Run Keyword And Ignore Error` | My Keyword |
  | `Run Keyword If` | '${status}' == 'PASS' | `Some Action` | arg | ELSE | `Another Action` |

The return value is the one of the keyword that was executed or None if
no keyword was executed (i.e. if ``condition`` was false). Hence, it is
recommended to use ELSE and/or ELSE IF branches to conditionally assign
return values from keyword to variables (to conditionally assign fixed
values to variables, see `Set Variable If`). This is illustrated by the
example below::

  | ${var1} =   | `Run Keyword If` | ${rc} == 0     | `Some keyword returning a value` |
  | ...         | ELSE IF          | 0 < ${rc} < 42 | `Another keyword` |
  | ...         | ELSE IF          | ${rc} < 0      | `Another keyword with args` | ${rc} | arg2 |
  | ...         | ELSE             | `Final keyword to handle abnormal cases` | ${rc} |
  | ${var2} =   | `Run Keyword If` | ${condition}  | `Some keyword` |

In this example, ${var2} will be set to None if ${condition} is false.

Notice that ``ELSE`` and ``ELSE IF`` control words must be used
explicitly and thus cannot come from variables. If you need to use
literal ``ELSE`` and ``ELSE IF`` strings as arguments, you can escape
them with a backslash like ``\ELSE`` and ``\ELSE IF``.

Starting from Robot Framework 2.8, Python's
[http://docs.python.org/2/library/os.html|os] and
[http://docs.python.org/2/library/sys.html|sys] modules are
automatically imported when evaluating the ``condition``.
Attributes they contain can thus be used in the condition::

  | `Run Keyword If` | os.sep == '/' | `Unix Keyword`        |
  | ...              | ELSE IF       | sys.platform.startswith('java') | `Jython Keyword` |
  | ...              | ELSE          | `Windows Keyword`     |


Run Keyword If All Critical Tests Passed
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:Arguments:  [name, \*args]

Runs the given keyword with the given arguments, if all critical tests passed.

This keyword can only be used in suite teardown. Trying to use it in
any other place will result in an error.

Otherwise, this keyword works exactly like `Run Keyword`, see its
documentation for more details.


Run Keyword If All Tests Passed
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:Arguments:  [name, \*args]

Runs the given keyword with the given arguments, if all tests passed.

This keyword can only be used in a suite teardown. Trying to use it
anywhere else results in an error.

Otherwise, this keyword works exactly like `Run Keyword`, see its
documentation for more details.


Run Keyword If Any Critical Tests Failed
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:Arguments:  [name, \*args]

Runs the given keyword with the given arguments, if any critical tests failed.

This keyword can only be used in a suite teardown. Trying to use it
anywhere else results in an error.

Otherwise, this keyword works exactly like `Run Keyword`, see its
documentation for more details.


Run Keyword If Any Tests Failed
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:Arguments:  [name, \*args]

Runs the given keyword with the given arguments, if one or more tests failed.

This keyword can only be used in a suite teardown. Trying to use it
anywhere else results in an error.

Otherwise, this keyword works exactly like `Run Keyword`, see its
documentation for more details.


Run Keyword If Test Failed
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:Arguments:  [name, \*args]

Runs the given keyword with the given arguments, if the test failed.

This keyword can only be used in a test teardown. Trying to use it
anywhere else results in an error.

Otherwise, this keyword works exactly like `Run Keyword`, see its
documentation for more details.

Prior to Robot Framework 2.9 failures in test teardown itself were
not detected by this keyword.


Run Keyword If Test Passed
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:Arguments:  [name, \*args]

Runs the given keyword with the given arguments, if the test passed.

This keyword can only be used in a test teardown. Trying to use it
anywhere else results in an error.

Otherwise, this keyword works exactly like `Run Keyword`, see its
documentation for more details.

Prior to Robot Framework 2.9 failures in test teardown itself were
not detected by this keyword.


Run Keyword If Timeout Occurred
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:Arguments:  [name, \*args]

Runs the given keyword if either a test or a keyword timeout has occurred.

This keyword can only be used in a test teardown. Trying to use it
anywhere else results in an error.

Otherwise, this keyword works exactly like `Run Keyword`, see its
documentation for more details.


Run Keyword Unless
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:Arguments:  [condition, name, \*args]

Runs the given keyword with the given arguments, if ``condition`` is false.

See `Run Keyword If` for more information and an example.


Run Keywords
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:Arguments:  [\*keywords]

Executes all the given keywords in a sequence.

This keyword is mainly useful in setups and teardowns when they need
to take care of multiple actions and creating a new higher level user
keyword would be an overkill.

By default all arguments are expected to be keywords to be executed.

例::

  | Run Keywords | Initialize database | Start servers | Clear logs |
  | Run Keywords | ${KW 1} | ${KW 2} |
  | Run Keywords | @{KEYWORDS} |

Starting from Robot Framework 2.7.6, keywords can also be run with
arguments using upper case ``AND`` as a separator between keywords.
The keywords are executed so that the first argument is the first
keyword and proceeding arguments until the first ``AND`` are arguments
to it. First argument after the first ``AND`` is the second keyword and
proceeding arguments until the next ``AND`` are its arguments. And so on.

例::

  | Run Keywords | Initialize database | db1 | AND | Start servers | server1 | server2 |
  | Run Keywords | Initialize database | ${DB NAME} | AND | Start servers | @{SERVERS} | AND | Clear logs |
  | Run Keywords | ${KW} | AND | @{KW WITH ARGS} |

Notice that the ``AND`` control argument must be used explicitly and
cannot itself come from a variable. If you need to use literal ``AND``
string as argument, you can either use variables or escape it with
a backslash like ``\AND``.


Set Global Variable
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:Arguments:  [name, \*values]

Makes a variable available globally in all tests and suites.

Variables set with this keyword are globally available in all test
cases and suites executed after setting them. Setting variables with
this keyword thus has the same effect as creating from the command line
using the options ``--variable`` or ``--variablefile``. Because this
keyword can change variables everywhere, it should be used with care.

See `Set Suite Variable` for more information and examples.


Set Library Search Order
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:Arguments:  [\*search_order]

Sets the resolution order to use when a name matches multiple keywords.

The library search order is used to resolve conflicts when a keyword
name in the test data matches multiple keywords. The first library
(or resource, see below) containing the keyword is selected and that
keyword implementation used. If the keyword is not found from any library
(or resource), test executing fails the same way as when the search
order is not set.

When this keyword is used, there is no need to use the long
``LibraryName.Keyword Name`` notation.  For example, instead of
having::

  | MyLibrary.Keyword | arg |
  | MyLibrary.Another Keyword |
  | MyLibrary.Keyword | xxx |

you can have::

  | Set Library Search Order | MyLibrary |
  | Keyword | arg |
  | Another Keyword |
  | Keyword | xxx |

This keyword can be used also to set the order of keywords in different
resource files. In this case resource names must be given without paths
or extensions like::

  | Set Library Search Order | resource | another_resource |

*NOTE:*
- The search order is valid only in the suite where this keywords is used.
- Keywords in resources always have higher priority than keywords in libraries regardless the search order.
- The old order is returned and can be used to reset the search order later.
- Library and resource names in the search order are both case and space insensitive.


Set Log Level
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:Arguments:  [level]

Sets the log threshold to the specified level and returns the old level.

Messages below the level will not logged. The default logging level is
INFO, but it can be overridden with the command line option
``--loglevel``.

The available levels: TRACE, DEBUG, INFO (default), WARN, ERROR and NONE (no
logging).


Set Suite Documentation
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:Arguments:  [doc, append=False, top=False]

Sets documentation for the current test suite.

By default the possible existing documentation is overwritten, but
this can be changed using the optional ``append`` argument similarly
as with `Set Test Message` keyword.

This keyword sets the documentation of the current suite by default.
If the optional ``top`` argument is given a true value (see `Boolean
arguments`), the documentation of the top level suite is altered
instead.

The documentation of the current suite is available as a built-in
variable ``${SUITE DOCUMENTATION}``.

New in Robot Framework 2.7. Support for ``append`` and ``top`` were
added in 2.7.7.


Set Suite Metadata
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:Arguments:  [name, value, append=False, top=False]

Sets metadata for the current test suite.

By default possible existing metadata values are overwritten, but
this can be changed using the optional ``append`` argument similarly
as with `Set Test Message` keyword.

This keyword sets the metadata of the current suite by default.
If the optional ``top`` argument is given a true value (see `Boolean
arguments`), the metadata of the top level suite is altered instead.

The metadata of the current suite is available as a built-in variable
``${SUITE METADATA}`` in a Python dictionary. Notice that modifying this
variable directly has no effect on the actual metadata the suite has.

New in Robot Framework 2.7.4. Support for ``append`` and ``top`` were
added in 2.7.7.


Set Suite Variable
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:Arguments:  [name, \*values]

Makes a variable available everywhere within the scope of the current suite.

Variables set with this keyword are available everywhere within the
scope of the currently executed test suite. Setting variables with this
keyword thus has the same effect as creating them using the Variable
table in the test data file or importing them from variable files.

Possible child test suites do not see variables set with this keyword
by default. Starting from Robot Framework 2.9, that can be controlled
by using ``children=<option>`` as the last argument. If the specified
``<option>`` is a non-empty string or any other value considered true
in Python, the variable is set also to the child suites. Parent and
sibling suites will never see variables set with this keyword.

The name of the variable can be given either as a normal variable name
(e.g. ``${NAME}``) or in escaped format as ``\${NAME}`` or ``$NAME``.
Variable value can be given using the same syntax as when variables
are created in the Variable table.

If a variable already exists within the new scope, its value will be
overwritten. Otherwise a new variable is created. If a variable already
exists within the current scope, the value can be left empty and the
variable within the new scope gets the value within the current scope.

例::

  | Set Suite Variable | ${SCALAR} | Hello, world! |
  | Set Suite Variable | ${SCALAR} | Hello, world! | children=true |
  | Set Suite Variable | @{LIST}   | First item    | Second item   |
  | Set Suite Variable | &{DICT}   | key=value     | foo=bar       |
  | ${ID} =            | Get ID    |
  | Set Suite Variable | ${ID}     |

To override an existing value with an empty value, use built-in
variables ``${EMPTY}``, ``@{EMPTY}`` or ``&{EMPTY}``::

  | Set Suite Variable | ${SCALAR} | ${EMPTY} |
  | Set Suite Variable | @{LIST}   | @{EMPTY} | # New in RF 2.7.4 |
  | Set Suite Variable | &{DICT}   | &{EMPTY} | # New in RF 2.9   |

*NOTE:* If the variable has value which itself is a variable (escaped
or not), you must always use the escaped format to set the variable:

例:

.. code:: robotframework
  
  | ${NAME} =          | Set Variable | \${var} |
  | Set Suite Variable | ${NAME}      | value | # Sets variable ${var}  |
  | Set Suite Variable | \${NAME}    | value | # Sets variable ${NAME} |

This limitation applies also to `Set Test Variable`, `Set Global
Variable`, `Variable Should Exist`, `Variable Should Not Exist` and
`Get Variable Value` keywords.


Set Tags
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:Arguments:  [\*tags]

Adds given ``tags`` for the current test or all tests in a suite.

When this keyword is used inside a test case, that test gets
the specified tags and other tests are not affected.

If this keyword is used in a suite setup, all test cases in
that suite, recursively, gets the given tags. It is a failure
to use this keyword in a suite teardown.

The current tags are available as a built-in variable ``@{TEST TAGS}``.

See `Remove Tags` if you want to remove certain tags and `Fail` if
you want to fail the test case after setting and/or removing tags.


Set Test Documentation
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:Arguments:  [doc, append=False]

Sets documentation for the current test case.

By default the possible existing documentation is overwritten, but
this can be changed using the optional ``append`` argument similarly
as with `Set Test Message` keyword.

The current test documentation is available as a built-in variable
``${TEST DOCUMENTATION}``. This keyword can not be used in suite
setup or suite teardown.

New in Robot Framework 2.7. Support for ``append`` was added in 2.7.7.


Set Test Message
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:Arguments:  [message, append=False]

Sets message for the current test case.

If the optional ``append`` argument is given a true value (see `Boolean
arguments`), the given ``message`` is added after the possible earlier
message by joining the messages with a space.

In test teardown this keyword can alter the possible failure message,
but otherwise failures override messages set by this keyword. Notice
that in teardown the message is available as a built-in variable
``${TEST MESSAGE}``.

It is possible to use HTML format in the message by starting the message
with ``*HTML*``.

例::

  | Set Test Message | My message           |                          |
  | Set Test Message | is continued.        | append=yes               |
  | Should Be Equal  | ${TEST MESSAGE}      | My message is continued. |
  | Set Test Message | `*`HTML`*` <b>Hello!</b> |                      |

This keyword can not be used in suite setup or suite teardown.

Support for ``append`` was added in Robot Framework 2.7.7 and support
for HTML format in 2.8.


Set Test Variable
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:Arguments:  [name, \*values]

Makes a variable available everywhere within the scope of the current test.

Variables set with this keyword are available everywhere within the
scope of the currently executed test case. For example, if you set a
variable in a user keyword, it is available both in the test case level
and also in all other user keywords used in the current test. Other
test cases will not see variables set with this keyword.

See `Set Suite Variable` for more information and examples.


Set Variable
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:Arguments:  [\*values]

Returns the given values which can then be assigned to a variables.

This keyword is mainly used for setting scalar variables.
Additionally it can be used for converting a scalar variable
containing a list to a list variable or to multiple scalar variables.
It is recommended to use `Create List` when creating new lists.

例::

  | ${hi} =   | Set Variable | Hello, world! |
  | ${hi2} =  | Set Variable | I said: ${hi} |
  | ${var1}   | ${var2} =    | Set Variable | Hello | world |
  | @{list} = | Set Variable | ${list with some items} |
  | ${item1}  | ${item2} =   | Set Variable  | ${list with 2 items} |

Variables created with this keyword are available only in the
scope where they are created. See `Set Global Variable`,
`Set Test Variable` and `Set Suite Variable` for information on how to
set variables so that they are available also in a larger scope.


Set Variable If
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:Arguments:  [condition, \*values]

Sets variable based on the given condition.

The basic usage is giving a condition and two values. The
given condition is first evaluated the same way as with the
`Should Be True` keyword. If the condition is true, then the
first value is returned, and otherwise the second value is
returned. The second value can also be omitted, in which case
it has a default value None. This usage is illustrated in the
examples below, where ``${rc}`` is assumed to be zero.
::

  | ${var1} = | Set Variable If | ${rc} == 0 | zero     | nonzero |
  | ${var2} = | Set Variable If | ${rc} > 0  | value1   | value2  |
  | ${var3} = | Set Variable If | ${rc} > 0  | whatever |         |
  =>
  | ${var1} = 'zero'
  | ${var2} = 'value2'
  | ${var3} = None

It is also possible to have 'else if' support by replacing the
second value with another condition, and having two new values
after it. If the first condition is not true, the second is
evaluated and one of the values after it is returned based on
its truth value. This can be continued by adding more
conditions without a limit.

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

Use `Get Variable Value` if you need to set variables
dynamically based on whether a variable exist or not.


Should Be Empty
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:Arguments:  [item, msg=None]

Verifies that the given item is empty.

The length of the item is got using the `Get Length` keyword. The
default error message can be overridden with the ``msg`` argument.


Should Be Equal
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:Arguments:  [first, second, msg=None, values=True]

Fails if the given objects are unequal.

Optional ``msg`` and ``values`` arguments specify how to construct
the error message if this keyword fails:

- If ``msg`` is not given, the error message is ``<first> != <second>``.
- If ``msg`` is given and ``values`` gets a true value, the error
  message is ``<msg>: <first> != <second>``.
- If ``msg`` is given and ``values`` gets a false value, the error
  message is simply ``<msg>``.

``values`` is true by default, but can be turned to false by using,
for example, string ``false`` or ``no values``. See `Boolean arguments`
section for more details.

If both arguments are multiline strings, the comparison is done using
`multiline string comparisons`.


Should Be Equal As Integers
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:Arguments:  [first, second, msg=None, values=True, base=None]

Fails if objects are unequal after converting them to integers.

See `Convert To Integer` for information how to convert integers from
other bases than 10 using ``base`` argument or ``0b/0o/0x`` prefixes.

See `Should Be Equal` for an explanation on how to override the default
error message with ``msg`` and ``values``.

例::

  | Should Be Equal As Integers | 42   | ${42} | Error message |
  | Should Be Equal As Integers | ABCD | abcd  | base=16 |
  | Should Be Equal As Integers | 0b1011 | 11  |


Should Be Equal As Numbers
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:Arguments:  [first, second, msg=None, values=True, precision=6]

Fails if objects are unequal after converting them to real numbers.

The conversion is done with `Convert To Number` keyword using the
given ``precision``.

例::

  | Should Be Equal As Numbers | ${x} | 1.1 | | # Passes if ${x} is 1.1 |
  | Should Be Equal As Numbers | 1.123 | 1.1 | precision=1  | # Passes |
  | Should Be Equal As Numbers | 1.123 | 1.4 | precision=0  | # Passes |
  | Should Be Equal As Numbers | 112.3 | 75  | precision=-2 | # Passes |

As discussed in the documentation of `Convert To Number`, machines
generally cannot store floating point numbers accurately. Because of
this limitation, comparing floats for equality is problematic and
a correct approach to use depends on the context. This keyword uses
a very naive approach of rounding the numbers before comparing them,
which is both prone to rounding errors and does not work very well if
numbers are really big or small. For more information about comparing
floats, and ideas on how to implement your own context specific
comparison algorithm, see
http://randomascii.wordpress.com/2012/02/25/comparing-floating-point-
numbers-2012-edition/.

See `Should Not Be Equal As Numbers` for a negative version of this
keyword and `Should Be Equal` for an explanation on how to override
the default error message with ``msg`` and ``values``.


Should Be Equal As Strings
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:Arguments:  [first, second, msg=None, values=True]

Fails if objects are unequal after converting them to strings.

See `Should Be Equal` for an explanation on how to override the default
error message with ``msg`` and ``values``.

If both arguments are multiline strings, the comparison is done using
`multiline string comparisons`.


Should Be True
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:Arguments:  [condition, msg=None]

Fails if the given condition is not true.

If ``condition`` is a string (e.g. ``${rc} < 10``), it is evaluated as
a Python expression as explained in `Evaluating expressions` and the
keyword status is decided based on the result. If a non-string item is
given, the status is got directly from its
[http://docs.python.org/2/library/stdtypes.html#truth|truth value].

The default error message (``<condition> should be true``) is not very
informative, but it can be overridden with the ``msg`` argument.

例::

  | Should Be True | ${rc} < 10            |
  | Should Be True | '${status}' == 'PASS' | # Strings must be quoted |
  | Should Be True | ${number}   | # Passes if ${number} is not zero |
  | Should Be True | ${list}     | # Passes if ${list} is not empty  |

Variables used like ``${variable}``, as in the examples above, are
replaced in the expression before evaluation. Variables are also
available in the evaluation namespace and can be accessed using special
syntax ``$variable``. This is a new feature in Robot Framework 2.9
and it is explained more thoroughly in `Evaluating expressions`.

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
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:Arguments:  [container, item, msg=None, values=True]

Fails if ``container`` does not contain ``item`` one or more times.

Works with strings, lists, and anything that supports Python's ``in``
operator. See `Should Be Equal` for an explanation on how to override
the default error message with ``msg`` and ``values``.

例::

  | Should Contain | ${output}    | PASS  |
  | Should Contain | ${some list} | value |


Should Contain X Times
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:Arguments:  [item1, item2, count, msg=None]

Fails if ``item1`` does not contain ``item2`` ``count`` times.

Works with strings, lists and all objects that `Get Count` works
with. The default error message can be overridden with ``msg`` and
the actual count is always logged.

例::

  | Should Contain X Times | ${output}    | hello  | 2 |
  | Should Contain X Times | ${some list} | value  | 3 |


Should End With
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:Arguments:  [str1, str2, msg=None, values=True]

Fails if the string ``str1`` does not end with the string ``str2``.

See `Should Be Equal` for an explanation on how to override the default
error message with ``msg`` and ``values``.


Should Match
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:Arguments:  [string, pattern, msg=None, values=True]

Fails unless the given ``string`` matches the given ``pattern``.

Pattern matching is similar as matching files in a shell, and it is
always case-sensitive. In the pattern, ``*`` matches to anything and
``?`` matches to any single character.

See `Should Be Equal` for an explanation on how to override the default
error message with ``msg`` and ``values``.


Should Match Regexp
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:Arguments:  [string, pattern, msg=None, values=True]

Fails if ``string`` does not match ``pattern`` as a regular expression.

Regular expression check is implemented using the Python
[http://docs.python.org/2/library/re.html|re module]. Python's regular
expression syntax is derived from Perl, and it is thus also very
similar to the syntax used, for example, in Java, Ruby and .NET.

Things to note about the regexp syntax in Robot Framework test data:

1) Backslash is an escape character in the test data, and possible
backslashes in the pattern must thus be escaped with another backslash
(e.g. ``\\d\\w+``).

2) Strings that may contain special characters, but should be handled
as literal strings, can be escaped with the `Regexp Escape` keyword.

3) The given pattern does not need to match the whole string. For
example, the pattern ``ello`` matches the string ``Hello world!``. If
a full match is needed, the ``^`` and ``$`` characters can be used to
denote the beginning and end of the string, respectively. For example,
``^ello$`` only matches the exact string ``ello``.

4) Possible flags altering how the expression is parsed (e.g.
``re.IGNORECASE``, ``re.MULTILINE``) can be set by prefixing the
pattern with the ``(?iLmsux)`` group like ``(?im)pattern``. The
available flags are ``i`` (case-insensitive), ``m`` (multiline mode),
``s`` (dotall mode), ``x`` (verbose), ``u`` (Unicode dependent) and
``L`` (locale dependent).

If this keyword passes, it returns the portion of the string that
matched the pattern. Additionally, the possible captured groups are
returned.

See the `Should Be Equal` keyword for an explanation on how to override
the default error message with the ``msg`` and ``values`` arguments.

例:

.. code:: robotframework

   | Should Match Regexp | ${output} | \\d{6}   | # Output contains six numbers
   |
   | Should Match Regexp | ${output} | ^\\d{6}$ | # Six numbers and nothing more
   |
   | ${ret} = | Should Match Regexp | Foo: 42 | (?i)foo: \\d+ |
   | ${match} | ${group1} | ${group2} = |
   | ...      | Should Match Regexp | Bar: 43 | (Foo|Bar): (\\d+) |
   =>
   | ${ret} = 'Foo: 42'
   | ${match} = 'Bar: 43'
   | ${group1} = 'Bar'
   | ${group2} = '43'


Should Not Be Empty
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:Arguments:  [item, msg=None]

Verifies that the given item is not empty.

The length of the item is got using the `Get Length` keyword. The
default error message can be overridden with the ``msg`` argument.


Should Not Be Equal
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:Arguments:  [first, second, msg=None, values=True]

Fails if the given objects are equal.

See `Should Be Equal` for an explanation on how to override the default
error message with ``msg`` and ``values``.


Should Not Be Equal As Integers
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:Arguments:  [first, second, msg=None, values=True, base=None]

Fails if objects are equal after converting them to integers.

See `Convert To Integer` for information how to convert integers from
other bases than 10 using ``base`` argument or ``0b/0o/0x`` prefixes.

See `Should Be Equal` for an explanation on how to override the default
error message with ``msg`` and ``values``.

See `Should Be Equal As Integers` for some usage examples.


Should Not Be Equal As Numbers
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:Arguments:  [first, second, msg=None, values=True, precision=6]

Fails if objects are equal after converting them to real numbers.

The conversion is done with `Convert To Number` keyword using the
given ``precision``.

See `Should Be Equal As Numbers` for examples on how to use
``precision`` and why it does not always work as expected. See also
`Should Be Equal` for an explanation on how to override the default
error message with ``msg`` and ``values``.


Should Not Be Equal As Strings
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:Arguments:  [first, second, msg=None, values=True]

Fails if objects are equal after converting them to strings.

See `Should Be Equal` for an explanation on how to override the default
error message with ``msg`` and ``values``.


Should Not Be True
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:Arguments:  [condition, msg=None]

Fails if the given condition is true.

See `Should Be True` for details about how ``condition`` is evaluated
and how ``msg`` can be used to override the default error message.


Should Not Contain
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:Arguments:  [container, item, msg=None, values=True]

Fails if ``container`` contains ``item`` one or more times.

Works with strings, lists, and anything that supports Python's ``in``
operator. See `Should Be Equal` for an explanation on how to override
the default error message with ``msg`` and ``values``.

例:

.. code:: robotframework

   | Should Not Contain | ${output}    | FAILED |
   | Should Not Contain | ${some list} | value  |


Should Not End With
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:Arguments:  [str1, str2, msg=None, values=True]

Fails if the string ``str1`` ends with the string ``str2``.

See `Should Be Equal` for an explanation on how to override the default
error message with ``msg`` and ``values``.


Should Not Match
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:Arguments:  [string, pattern, msg=None, values=True]

Fails if the given ``string`` matches the given ``pattern``.

Pattern matching is similar as matching files in a shell, and it is
always case-sensitive. In the pattern ``*`` matches to anything and
``?`` matches to any single character.

See `Should Be Equal` for an explanation on how to override the default
error message with ``msg`` and ``values``.


Should Not Match Regexp
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:Arguments:  [string, pattern, msg=None, values=True]

Fails if ``string`` matches ``pattern`` as a regular expression.

See `Should Match Regexp` for more information about arguments.


Should Not Start With
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:Arguments:  [str1, str2, msg=None, values=True]

Fails if the string ``str1`` starts with the string ``str2``.

See `Should Be Equal` for an explanation on how to override the default
error message with ``msg`` and ``values``.


Should Start With
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:Arguments:  [str1, str2, msg=None, values=True]

Fails if the string ``str1`` does not start with the string ``str2``.

See `Should Be Equal` for an explanation on how to override the default
error message with ``msg`` and ``values``.


Sleep
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:Arguments:  [time\_, reason=None]

Pauses the test executed for the given time.

``time`` may be either a number or a time string. Time strings are in
a format such as ``1 day 2 hours 3 minutes 4 seconds 5milliseconds`` or
``1d 2h 3m 4s 5ms``, and they are fully explained in an appendix of
Robot Framework User Guide. Optional `reason` can be used to explain why
sleeping is necessary. Both the time slept and the reason are logged.

例:

.. code:: robotframework

   | Sleep | 42                   |
   | Sleep | 1.5                  |
   | Sleep | 2 minutes 10 seconds |
   | Sleep | 10s                  | Wait for a reply |


Variable Should Exist
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:Arguments:  [name, msg=None]

Fails unless the given variable exists within the current scope.

The name of the variable can be given either as a normal variable name
(e.g. ``${NAME}``) or in escaped format (e.g. ``\${NAME}``). Notice
that the former has some limitations explained in `Set Suite Variable`.

The default error message can be overridden with the ``msg`` argument.

See also `Variable Should Not Exist` and `Keyword Should Exist`.


Variable Should Not Exist
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:Arguments:  [name, msg=None]

Fails if the given variable exists within the current scope.

The name of the variable can be given either as a normal variable name
(e.g. ``${NAME}``) or in escaped format (e.g. ``\${NAME}``). Notice
that the former has some limitations explained in `Set Suite Variable`.

The default error message can be overridden with the ``msg`` argument.

See also `Variable Should Exist` and `Keyword Should Exist`.


Wait Until Keyword Succeeds
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:Arguments:  [retry, retry_interval, name, \*args]

Runs the specified keyword and retries if it fails.

``name`` and ``args`` define the keyword that is executed similarly
as with `Run Keyword`. How long to retry running the keyword is
defined using ``retry`` argument either as timeout or count.
``retry_interval`` is the time to wait before trying to run the
keyword again after the previous run has failed.

If ``retry`` is given as timeout, it must be in Robot Framework's
time format (e.g. ``1 minute``, ``2 min 3 s``, ``4.5``) that is
explained in an appendix of Robot Framework User Guide. If it is
given as count, it must have ``times`` or ``x`` postfix (e.g.
``5 times``, ``10 x``). ``retry_interval`` must always be given in
Robot Framework's time format.

If the keyword does not succeed regardless of retries, this keyword
fails. If the executed keyword passes, its return value is returned.

例::

  | Wait Until Keyword Succeeds | 2 min | 5 sec | My keyword | argument |
  | ${result} = | Wait Until Keyword Succeeds | 3x | 200ms | My keyword |

All normal failures are caught by this keyword. Errors caused by
invalid syntax, test or keyword timeouts, or fatal exceptions (caused
e.g. by `Fatal Error`) are not caught.

Running the same keyword multiple times inside this keyword can create
lots of output and considerably increase the size of the generated
output files. Starting from Robot Framework 2.7, it is possible to
remove unnecessary keywords from the outputs using
``--RemoveKeywords WUKS`` command line option.

Support for specifying ``retry`` as a number of times to retry is
a new feature in Robot Framework 2.9.
Since Robot Framework 2.9, variable errors are caught by this keyword.

