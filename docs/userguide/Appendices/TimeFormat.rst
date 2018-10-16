.. _Time format:

時刻のフォーマット
====================

Robot Framework では、時刻を表現するための、わかりやすく柔軟性のある独自のフォーマットを持っています。
このフォーマットは一部のキーワード (例えば BuiltIn_ ライブラリの :name:`Sleep` や
:name:`Wait Until Keyword Succeeds`), DateTime_ ライブラリ、そして `タイムアウト <timeouts>`_
の表現に使われます。

.. _Time as number:

時間の数値表現
----------------

時間を数値で表した場合は、秒数とみなされます。整数でも浮動小数点でも使えます。
また、実際の数値オブジェクトでも、数を表す文字列でも表せます。


.. _Time as time string:

時間の文字列表現
-------------------

時間の文字列表現とは、 `2 minutes 42 seconds` のような形式の文字列で時間を表すことです。
この表現だと、秒で表すよりも時間がわかりやすいときがあります。例えば、秒で `4200` と表すより、
`1 hour 10 minutes` のほうが、どのくらいの長さか理解しやすいはずです。

この表現方法の基本的な考え方は、まず数値、そしてその後ろに数値の表す時間単位がくるというものです。
数値は整数でも浮動小数点でもよく、大小文字やスペースの数を区別しません。負の値を表したいときには
先頭に `-` をつけられます。時間の単位として使えるのは以下です:

* days, day, d
* hours, hour, h
* minutes, minute, mins, min, m
* seconds, second, secs, sec, s
* milliseconds, millisecond, millis, ms

例::

   1 min 30 secs
   1.5 minutes
   90 s
   1 day 2 hours 3 minutes 4 seconds 5 milliseconds
   1d 2h 3m 4s 5ms
   - 10 seconds

.. _Time as "timer" string:

「タイマー」形式の文字列
--------------------------

Robot Framework 2.8.5 から、時間を `hh:mm:ss.mil` 形式で表せるようになりました。
この形式では、時部分とミリ秒部分は省略できます。先頭と末尾のゼロは、意味を
もたないときは無視され、負の値は `-` をつけることで表せます。
例えば、以下の表のように、タイマー形式と文字列の時間表現が対応しています:

.. table:: タイマー形式と時間文字列の対応例
   :class: tabular

   ============  ======================================
      Timer                   Time string
   ============  ======================================
   00:00:01      1 second
   01:02:03      1 hour 2 minutes 3 seconds
   1:00:00       1 hour
   100:00:00     100 hours
   00:02         2 seconds
   42:00         42 minutes
   00:01:02.003  1 minute 2 seconds 3 milliseconds
   00:01.5       1.5 seconds
   -01:02.345    \- 1 minute 2 seconds 345 milliseconds
   ============  ======================================
