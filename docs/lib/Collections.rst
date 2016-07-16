Collections: リストと辞書の操作
====================================
:Version:          3.0
:Scope:            global
:Named arguments:  supported


``Collections`` は、Robot Framework の標準ライブラリの一つで、リストや辞書を扱うためのキーワードを定義しています。
このライブラリには、例えば、リストや辞書の値を変更したり、値を取り出したりするキーワード
(e.g. `Append To List`, `Get From Dictionary`) のほか、値を検証するためのキーワード (e.g. `Lists
Should Be Equal`, `Dictionary Should Contain Value`) が定義されています。

.. _`Related keywords in BuiltIn`:

BuiltIn の関連キーワード
----------------------------

BuilIn ライブラリの以下のキーワードも、リストや辞書を扱えます::
::

    =============================  =======  =====================================
    キーワード名                   対象     コメント                        
    =============================  =======  =====================================
    `Create List`                  リスト                                  
    `Create Dictionary`            辞書      RFW 2.9 まで Collections に収録
    `Get Length`                   両方   
    `Length Should Be`             両方   
    `Should Be Empty`              両方   
    `Should Not Be Empty`          両方   
    `Should Contain`               両方   
    `Should Not Contain`           両方   
    `Should Contain X Times`       リスト 
    `Should Not Contain X Times`   リスト 
    `Get Count`                    リスト 
    =============================  =======  =====================================


.. _`Using with list-like and dictionary-like objects`:

リスト／辞書ライクなオブジェクトを扱う
----------------------------------------

リストを対象とするキーワードのうち、リストの中身を変更しないものは、タプルや、他の iterable にも使えます。
タプルや iterable を Python の ``list`` オブジェクトに変換するには、 `Convert To List` を使います。

同様に、辞書を扱うキーワードも、ほとんどが他のマップ型を扱えます。
Python の ``dict`` オブジェクトに変換が必要なときは `Convert To Dictionary` を使ってください。

.. _`Boolean arguments`:

ブール型の引数
--------------------

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


.. _`Data in examples`:

Data in examples
------------------

このドキュメントでは、リスト関連のキーワードの例に ``${Lx}`` のような変数を使うことがあります。
そのとき、 ``${Lx}`` は ``x`` 個のアルファベットからなるリストを仮定しています。
例えば、リスト ``${L1}`` は ``['a']`` で、 ``${L3}`` は ``['a', 'b', 'c']`` です。

辞書を扱うキーワードの例でも、同様に、 ``${Dx}`` のような変数を使います。
このとき、 ``${D1}`` は ``{'a': 1}`` 、 ``${D3}`` は ``{'a': 1, 'b': 2, 'c': 3}`` です。


.. _`collection-Keywords`:
   
キーワード
-----------

Append To List
~~~~~~~~~~~~~~~~


引数:  [ :ref:`list` , \*values]

``list`` の末尾に ``values`` を追加します。

例::

  | Append To List | ${L1} | xxx |   |   |
  | Append To List | ${L2} | x   | y | z |
  =>
  | ${L1} = ['a', 'xxx']
  | ${L2} = ['a', 'b', 'x', 'y', 'z']

Combine Lists
~~~~~~~~~~~~~~

引数:  [\*lists]

``lists`` に指定した複数のリストを結合した結果を返します。

引数に指定した元のリストは変更しません。

例::

  | ${x} = | Combine List | ${L1} | ${L2} |       |
  | ${y} = | Combine List | ${L1} | ${L2} | ${L1} |
  =>
  | ${x} = ['a', 'a', 'b']
  | ${y} = ['a', 'a', 'b', 'a']
  | ${L1} and ${L2} are not changed.

Convert To Dictionary
~~~~~~~~~~~~~~~~~~~~~~~

引数:  [item]

``item`` を Python の ``dict`` 型に変換します。

他のマップ型から辞書へ変換するときに便利です。
新たな辞書オブジェクトを生成したいときは BuiltIn ライブラリの  `Create Dictionary` を使ってください。

Robot Framework 2.9 で登場しました。

Convert To List
~~~~~~~~~~~~~~~~

引数:  [item]

``item`` を Python の ``list`` 型に変換します。

タプルやその他 iterable をリストに変換するときに便利です。
新たなリストオブジェクトを生成したいときは BuiltIn ライブラリの `Create List` を使ってください。

Copy Dictionary
~~~~~~~~~~~~~~~~

引数:  [dictionary]

辞書をコピーして返します。

このキーワードは引数に渡した辞書を変更しません。

Copy List
~~~~~~~~~~~

引数:  [ :ref:`list` ]

リストをコピーして返します。

このキーワードは引数に渡したリストを変更しません。

Count Values In List
~~~~~~~~~~~~~~~~~~~~~~

引数:  [ :ref:`list` , value, start=0, end=None]

``list`` 中に ``value`` が何回出現するか数えます。

`Get Slice From List` と同様、 ``start`` と ``end`` にインデクスを指定すると、検索の範囲を狭められます。
このキーワードは引数に渡したリストを変更しません。

例::

  | ${x} = | Count Values In List | ${L3} | b |
  =>
  | ${x} = 1
  | ${L3} is not changed

Dictionaries Should Be Equal
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

引数:  [dict1, dict2, msg=None, values=True]

指定の二つの辞書が同じでないとき失敗します。

比較の際は、まず二つの辞書のキーが同じかを調べ、その後でキーと値のペアが全て同じかどうかを調べます。
値の違いがあれば、エラーメッセージに表示します。
辞書の型は同じでなくてもかまいません。

エラーメッセージの出力方法を ``msg`` や ``values`` で設定する方法は、 `Lists Should Be Equal` を参照してください。

このキーワードは引数に渡した辞書を変更しません。

Dictionary Should Contain Item
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

引数:  [dictionary, key, value, msg=None]

指定の ``key`` と ``value`` のペアが `dictionary` 中にないとき失敗します。

比較の際、値を unicode 型に変換します。

``msg`` の説明は `Lists Should Be Equal` を参照してください。

このキーワードは引数に渡した辞書を変更しません。

Dictionary Should Contain Key
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

引数:  [dictionary, key, msg=None]

指定の ``key`` が `dictionary` 中にないとき失敗します。

``msg`` の説明は `Lists Should Contain Value` を参照してください。

このキーワードは引数に渡した辞書を変更しません。

Dictionary Should Contain Sub Dictionary
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

引数:  [dict1, dict2, msg=None, values=True]

Fails unless all items in ``dict2`` are found from ``dict1``.

See `Lists Should Be Equal` for more information about configuring
the error message with ``msg`` and ``values`` arguments.

このキーワードは引数に渡した辞書を変更しません。

Dictionary Should Contain Value
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

引数:  [dictionary, value, msg=None]

Fails if ``value`` is not found from ``dictionary``.

See `List Should Contain Value` for an explanation of ``msg``.

このキーワードは引数に渡した辞書を変更しません。

Dictionary Should Not Contain Key
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

引数:  [dictionary, key, msg=None]

Fails if ``key`` is found from ``dictionary``.

See `List Should Contain Value` for an explanation of ``msg``.

このキーワードは引数に渡した辞書を変更しません。

Dictionary Should Not Contain Value
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

引数:  [dictionary, value, msg=None]

Fails if ``value`` is found from ``dictionary``.

See `List Should Contain Value` for an explanation of ``msg``.

このキーワードは引数に渡した辞書を変更しません。

Get Dictionary Items
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

引数:  [dictionary]

Returns items of the given ``dictionary``.

Items are returned sorted by keys. The given ``dictionary`` is not
altered by this keyword.

例::

  | ${items} = | Get Dictionary Items | ${D3} |
  =>
  | ${items} = ['a', 1, 'b', 2, 'c', 3]

Get Dictionary Keys
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

引数:  [dictionary]

Returns keys of the given ``dictionary``.

If keys are sortable, they are returned in sorted order. The given
``dictionary`` is never altered by this keyword.

例::

  | ${keys} = | Get Dictionary Keys | ${D3} |
  =>
  | ${keys} = ['a', 'b', 'c']

Get Dictionary Values
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

引数:  [dictionary]

Returns values of the given dictionary.

Values are returned sorted according to keys. The given dictionary is
never altered by this keyword.

例::

  | ${values} = | Get Dictionary Values | ${D3} |
  =>
  | ${values} = [1, 2, 3]

Get From Dictionary
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

引数:  [dictionary, key]

Returns a value from the given ``dictionary`` based on the given ``key``.

If the given ``key`` cannot be found from the ``dictionary``, this
keyword fails.

このキーワードは引数に渡した辞書を変更しません。

例::

  | ${value} = | Get From Dictionary | ${D3} | b |
  =>
  | ${value} = 2

Get From List
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

引数:  [ :ref:`list` , index]

Returns the value specified with an ``index`` from ``list``.

このキーワードは引数に渡したリストを変更しません。

Index ``0`` means the first position, ``1`` the second, and so on.
Similarly, ``-1`` is the last position, ``-2`` the second last, and so on.
Using an index that does not exist on the list causes an error.
The index can be either an integer or a string that can be converted
to an integer.

Examples (including Python equivalents in comments)::
  | ${x} = | Get From List | ${L5} | 0  | # L5[0]  |
  | ${y} = | Get From List | ${L5} | -2 | # L5[-2] |
  =>
  | ${x} = 'a'
  | ${y} = 'd'
  | ${L5} is not changed

Get Index From List
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

引数:  [ :ref:`list` , value, start=0, end=None]

Returns the index of the first occurrence of the ``value`` on the list.

The search can be narrowed to the selected sublist by the ``start`` and
``end`` indexes having the same semantics as with `Get Slice From List`
keyword. In case the value is not found, -1 is returned. The given list
is never altered by this keyword.

例::

  | ${x} = | Get Index From List | ${L5} | d |
  =>
  | ${x} = 3
  | ${L5} is not changed

Get Match Count
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

引数:  [list, pattern, case_insensitive=False,
            whitespace_insensitive=False]

Returns the count of matches to ``pattern`` in ``list``.

For more information on ``pattern``, ``case_insensitive``, and
``whitespace_insensitive``, see `Should Contain Match`.

Examples::
  | ${count}= | Get Match Count | ${list} | a* | # ${count} will be the count of strings beginning with 'a' |
  | ${count}= | Get Match Count | ${list} | regexp=a.* | # ${matches} will be the count of strings beginning with 'a' (regexp version) |
  | ${count}= | Get Match Count | ${list} | a* | case_insensitive=${True} | # ${matches} will be the count of strings beginning with 'a' or 'A' |

Robot Framework 2.8.6 で登場しました。

Get Matches
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

引数:  [list, pattern, case_insensitive=False,
            whitespace_insensitive=False]

Returns a list of matches to ``pattern`` in ``list``.

For more information on ``pattern``, ``case_insensitive``, and
``whitespace_insensitive``, see `Should Contain Match`.

Examples::
  | ${matches}= | Get Matches | ${list} | a* | # ${matches} will contain any string beginning with 'a' |
  | ${matches}= | Get Matches | ${list} | regexp=a.* | # ${matches} will contain any string beginning with 'a' (regexp version) |
  | ${matches}= | Get Matches | ${list} | a* | case_insensitive=${True} | # ${matches} will contain any string beginning with 'a' or 'A' |

Robot Framework 2.8.6 で登場しました。

Get Slice From List
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

引数:  [ :ref:`list` , start=0, end=None]

Returns a slice of the given list between ``start`` and ``end`` indexes.

このキーワードは引数に渡したリストを変更しません。

If both ``start`` and ``end`` are given, a sublist containing values
from ``start`` to ``end`` is returned. This is the same as
``list[start:end]`` in Python. To get all items from the beginning,
use 0 as the start value, and to get all items until and including
the end, use ``None`` (default) as the end value.

Using ``start`` or ``end`` not found on the list is the same as using
the largest (or smallest) available index.

Examples (incl. Python equivalents in comments)::
  | ${x} = | Get Slice From List | ${L5} | 2 | 4  | # L5[2:4]    |
  | ${y} = | Get Slice From List | ${L5} | 1 |    | # L5[1:None] |
  | ${z} = | Get Slice From List | ${L5} |   | -2 | # L5[0:-2]   |
  =>
  | ${x} = ['c', 'd']
  | ${y} = ['b', 'c', 'd', 'e']
  | ${z} = ['a', 'b', 'c']
  | ${L5} is not changed

Insert Into List
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

引数:  [ :ref:`list` , index, value]

Inserts ``value`` into ``list`` to the position specified with ``index``.

Index ``0`` adds the value into the first position, ``1`` to the second,
and so on. Inserting from right works with negative indices so that
``-1`` is the second last position, ``-2`` third last, and so on. Use
`Append To List` to add items to the end of the list.

If the absolute value of the index is greater than
the length of the list, the value is added at the end
(positive index) or the beginning (negative index). An index
can be given either as an integer or a string that can be
converted to an integer.

例::

  | Insert Into List | ${L1} | 0     | xxx |
  | Insert Into List | ${L2} | ${-1} | xxx |
  =>
  | ${L1} = ['xxx', 'a']
  | ${L2} = ['a', 'xxx', 'b']

Keep In Dictionary
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


引数:  [dictionary, \*keys]

Keeps the given ``keys`` in the ``dictionary`` and removes all other.

If the given ``key`` cannot be found from the ``dictionary``, it
is ignored.

例::

  | Keep In Dictionary | ${D5} | b | x | d |
  =>
  | ${D5} = {'b': 2, 'd': 4}

List Should Contain Sub List
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

引数:  [list1, list2, msg=None, values=True]

Fails if not all of the elements in ``list2`` are found in ``list1``.

The order of values and the number of values are not taken into
account.

See `Lists Should Be Equal` for more information about configuring
the error message with ``msg`` and ``values`` arguments.

List Should Contain Value
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

引数:  [ :ref:`list` , value, msg=None]

Fails if the ``value`` is not found from ``list``.

If the keyword fails, the default error messages is ``<list> does
not contain value '<value>'``. A custom message can be given using
the ``msg`` argument.

List Should Not Contain Duplicates
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

引数:  [ :ref:`list` , msg=None]

Fails if any element in the ``list`` is found from it more than once.

The default error message lists all the elements that were found
from the ``list`` multiple times, but it can be overridden by giving
a custom ``msg``. All multiple times found items and their counts are
also logged.

This keyword works with all iterables that can be converted to a list.
The original iterable is never altered.

List Should Not Contain Value
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

引数:  [ :ref:`list` , value, msg=None]

Fails if the ``value`` is not found from ``list``.

See `List Should Contain Value` for an explanation of ``msg``.

Lists Should Be Equal
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

引数:  [list1, list2, msg=None, values=True, names=None]

Fails if given lists are unequal.

The keyword first verifies that the lists have equal lengths, and then
it checks are all their values equal. Possible differences between the
values are listed in the default error message like ``Index 4: ABC !=
Abc``. The types of the lists do not need to be the same. For example,
Python tuple and list with same content are considered equal.


The error message can be configured using ``msg`` and ``values``
arguments:
- If ``msg`` is not given, the default error message is used.
- If ``msg`` is given and ``values`` gets a value considered true (see `Boolean arguments`), the error message starts with the given ``msg`` followed by a newline and the default message.
- If ``msg`` is given and ``values``  is not given a true value, the error message is just the given ``msg``.

Optional ``names`` argument can be used for naming the indices shown in
the default error message. It can either be a list of names matching
the indices in the lists or a dictionary where keys are indices that
need to be named. It is not necessary to name all of the indices.  When
using a dictionary, keys can be either integers or strings that can be
converted to integers.

Examples::
  | ${names} = | Create List | First Name | Family Name | Email |
  | Lists Should Be Equal | ${people1} | ${people2} | names=${names} |
  | ${names} = | Create Dictionary | 0=First Name | 2=Email |
  | Lists Should Be Equal | ${people1} | ${people2} | names=${names} |

If the items in index 2 would differ in the above examples, the error
message would contain a row like ``Index 2 (email): name@foo.com !=
name@bar.com``.

Log Dictionary
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

引数:  [dictionary, level=INFO]

Logs the size and contents of the ``dictionary`` using given ``level``.

Valid levels are TRACE, DEBUG, INFO (default), and WARN.

If you only want to log the size, use keyword `Get Length` from
the BuiltIn library.

Log List
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

引数:  [ :ref:`list` , level=INFO]

Logs the length and contents of the ``list`` using given ``level``.

Valid levels are TRACE, DEBUG, INFO (default), and WARN.

If you only want to the length, use keyword `Get Length` from
the BuiltIn library.

Pop From Dictionary
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

引数:  [dictionary, key, default=]

Pops the given ``key`` from the ``dictionary`` and returns its value.

By default the keyword fails if the given ``key`` cannot be found from
the ``dictionary``. If optional ``default`` value is given, it will be
returned instead of failing.

例::

  | ${val}= | Pop From Dictionary | ${D3} | b |
  =>
  | ${val} = 2
  | ${D3} = {'a': 1, 'c': 3}

Robot Framework 2.9.2 で登場しました。

Remove Duplicates
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

引数:  [ :ref:`list` ]

Returns a list without duplicates based on the given ``list``.

Creates and returns a new list that contains all items in the given
list so that one item can appear only once. Order of the items in
the new list is the same as in the original except for missing
duplicates. Number of the removed duplicates is logged.

Robot Framework 2.7.5 で登場しました。

Remove From Dictionary
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

引数:  [dictionary, \*keys]

Removes the given ``keys`` from the ``dictionary``.

If the given ``key`` cannot be found from the ``dictionary``, it
is ignored.

例::

  | Remove From Dictionary | ${D3} | b | x | y |
  =>
  | ${D3} = {'a': 1, 'c': 3}

Remove From List
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

引数:  [ :ref:`list` , index]

Removes and returns the value specified with an ``index`` from ``list``.

Index ``0`` means the first position, ``1`` the second and so on.
Similarly, ``-1`` is the last position, ``-2`` the second last, and so on.
Using an index that does not exist on the list causes an error.
The index can be either an integer or a string that can be converted
to an integer.

例::

  | ${x} = | Remove From List | ${L2} | 0 |
  =>
  | ${x} = 'a'
  | ${L2} = ['b']

Remove Values From List
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

引数:  [ :ref:`list` , \*values]

Removes all occurrences of given ``values`` from ``list``.

It is not an error if a value does not exist in the list at all.

例::

  | Remove Values From List | ${L4} | a | c | e | f |
  =>
  | ${L4} = ['b', 'd']

Reverse List
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

引数:  [ :ref:`list` ]

Reverses the given list in place.

Note that the given list is changed and nothing is returned. Use
`Copy List` first, if you need to keep also the original order.
::

  | Reverse List | ${L3} |
  =>
  | ${L3} = ['c', 'b', 'a']

Set List Value
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

引数:  [ :ref:`list` , index, value]

Sets the value of ``list`` specified by ``index`` to the given ``value``.

Index ``0`` means the first position, ``1`` the second and so on.
Similarly, ``-1`` is the last position, ``-2`` second last, and so on.
Using an index that does not exist on the list causes an error.
The index can be either an integer or a string that can be converted to
an integer.

例::

  | Set List Value | ${L3} | 1  | xxx |
  | Set List Value | ${L3} | -1 | yyy |
  =>
  | ${L3} = ['a', 'xxx', 'yyy']

Set To Dictionary
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

引数:  [dictionary, \*key_value_pairs, \*\*items]

Adds the given ``key_value_pairs`` and ``items`` to the ``dictionary``.

Giving items as ``key_value_pairs`` means giving keys and values
as separate arguments::

  | Set To Dictionary | ${D1} | key | value | second | ${2} |
  =>
  | ${D1} = {'a': 1, 'key': 'value', 'second': 2}

Starting from Robot Framework 2.8.1, items can also be given as kwargs
using ``key=value`` syntax::

  | Set To Dictionary | ${D1} | key=value | second=${2} |

The latter syntax is typically more convenient to use, but it has
a limitation that keys must be strings.

If given keys already exist in the dictionary, their values are updated.

Should Contain Match
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

引数:  [list, pattern, msg=None, case_insensitive=False,
            whitespace_insensitive=False]

Fails if ``pattern`` is not found in ``list``.

See `List Should Contain Value` for an explanation of ``msg``.

By default, pattern matching is similar to matching files in a shell
and is case-sensitive and whitespace-sensitive. In the pattern syntax,
``*`` matches to anything and ``?`` matches to any single character. You
can also prepend ``glob=`` to your pattern to explicitly use this pattern
matching behavior.

If you prepend ``regexp=`` to your pattern, your pattern will be used
according to the Python
[http://docs.python.org/2/library/re.html|re module] regular expression
syntax. Important note: Backslashes are an escape character, and must
be escaped with another backslash (e.g. ``regexp=\\d{6}`` to search for
``\d{6}``). See `BuiltIn.Should Match Regexp` for more details.

If ``case_insensitive`` is given a true value (see `Boolean arguments`),
the pattern matching will ignore case.

If ``whitespace_insensitive`` is given a true value (see `Boolean
arguments`), the pattern matching will ignore whitespace.

Non-string values in lists are ignored when matching patterns.

このキーワードは引数に渡したリストを変更しません。

See also ``Should Not Contain Match``.

Examples::
  | Should Contain Match | ${list} | a*              | | | # Match strings beginning with 'a'. |
  | Should Contain Match | ${list} | regexp=a.*      | | | # Same as the above but with regexp. |
  | Should Contain Match | ${list} | regexp=\\d{6} | | | # Match strings containing six digits. |
  | Should Contain Match | ${list} | a*  | case_insensitive=True       | | # Match strings beginning with 'a' or 'A'. |
  | Should Contain Match | ${list} | ab* | whitespace_insensitive=yes  | | # Match strings beginning with 'ab' with possible whitespace ignored. |
  | Should Contain Match | ${list} | ab* | whitespace_insensitive=true | case_insensitive=true | # Same as the above but also ignore case. |

Robot Framework 2.8.6 で登場しました。

Should Not Contain Match
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

引数:  [list, pattern, msg=None, case_insensitive=False,
            whitespace_insensitive=False]

Fails if ``pattern`` is found in ``list``.

Exact opposite of `Should Contain Match` keyword. See that keyword
for information about arguments and usage in general.

Robot Framework 2.8.6 で登場しました。

Sort List
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

引数:  [ :ref:`list` ]

Sorts the given list in place.

The strings are sorted alphabetically and the numbers numerically.

Note that the given list is changed and nothing is returned. Use
`Copy List` first, if you need to keep also the original order.
::

  ${L} = [2,1,'a','c','b']

  | Sort List | ${L} |
  =>
  | ${L} = [1, 2, 'a', 'b', 'c']

