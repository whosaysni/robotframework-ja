.. _Boolean arguments:

ブール型引数
=================

Robot Framework の `標準ライブラリ<standard libraries>`_ の多くのキーワードは、
真または偽の値を引数に取るようになっています。そうした引数に文字列を渡した場合、
空文字列か、大小文字を区別せず `false` または `no` のときに偽とみなされます。
その他の文字列を指定すると、その内容にかかわらず真とみなされます。
文字列以外の型は `Python と同じように <http://docs.python.org/2/library/stdtypes.html#truth-value-testing>`__
解釈されます。

キーワードの中には、 `false` や `no` 以外の文字列も偽として扱うものがあります。
例えば、 BuiltIn_ ライブラリのキーワード `Should Be True` は、下記の例のように
`values` 引数に文字列 `no values` を指定した場合も、偽を指定したものとみなします。

.. sourcecode:: robotframework

   *** Keywords ***
   True examples
       Should Be Equal    ${x}    ${y}    Custom error    values=True         # 文字列の値は基本的に真
       Should Be Equal    ${x}    ${y}    Custom error    values=yes          # 上に同じ
       Should Be Equal    ${x}    ${y}    Custom error    values=${TRUE}      # Python の `True` は真
       Should Be Equal    ${x}    ${y}    Custom error    values=${42}        # 0 以外の数値も真

   False examples
       Should Be Equal    ${x}    ${y}    Custom error    values=False        # 文字列 `false` は偽
       Should Be Equal    ${x}    ${y}    Custom error    values=no           # 文字列 `no` も偽
       Should Be Equal    ${x}    ${y}    Custom error    values=${EMPTY}     # 空文字列も偽
       Should Be Equal    ${x}    ${y}    Custom error    values=${FALSE}     # Python の `False` も偽
       Should Be Equal    ${x}    ${y}    Custom error    values=no values    # このキーワードでは `no values` も偽とみなす

Robot Framework 2.9 より前のバージョンでは、ブール型の扱いに一貫性がなかったので注意してください。
上の規則に準拠しているキーワードもあれば、空文字列以外以外の文字列、つまり `false` や `no` も真とみなすものもありました。
