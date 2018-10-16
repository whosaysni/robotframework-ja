.. _Advanced features:

高度な機能
============

.. contents::
   :depth: 2
   :local:

.. _Handling keywords with same names:

同名のキーワードの扱いかた
-----------------------------

Robot Framework で使われているキーワードは、 :ref:`ライブラリキーワード <library keywords>` か、 :ref:`ユーザキーワード <user keywords>` です。
前者は :ref:`標準ライブラリ <standard libraries>` または :ref:`外部ライブラリ <external libraries>` で定義されています。
後者は、キーワードが使われているのと同じファイルの中で定義されていることもあれば、 :ref:`リソースファイル <resource files>` からインポートされていることもあります。
沢山のキーワードを使っていると、同じ名前をもつキーワードが出てくるのは避けられません。
この節では、そうした状況で、キーワードの衝突を回避する方法を説明します。

.. _Keyword scopes:

キーワードのスコープ
~~~~~~~~~~~~~~~~~~~~~~

あるキーワード名を使ったとき、同名の複数のキーワードが存在すると、 Robot Framework は、現在のスコープに基づいて、最もプライオリティの高いキーワードを決定しようと試みます。
キーワードのスコープは、件のキーワードがどのように作成されたかに基づいて決まります:

1. キーワードが使われているのと同じファイルで定義されたユーザキーワード。
   最も高いプライオリティをもち、他の場所で同名のキーワードが定義されていても、必ずこのキーワードが使われます。

2. リソースファイルで定義されていて、直接または間接的にインポートされたもの。
   二番目に高いプライオリティを持ちます。

3. 外部ライブラリで定義されているもの。
   同名のユーザキーワードがないときに使われます。
   ただし、標準ライブラリに同名のキーワードがあるときは、警告を表示します。

4. 標準ライブラリで定義されているキーワード。もっとも低いプライオリティを持っています。

.. _Specifying a keyword explicitly:

キーワードを明示的に指定する
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

スコープだけでは、キーワードの名前解決機能は充分とはいえません。
というのも、複数のライブラリやリソースで同名のキーワードが現れる場合がある一方で、スコープは単に最も高いプライオリティのキーワードを使うというメカニズムしか提供していないからです。
そのため、 *完全な名前* を使ってキーワードを指定できます。
キーワードの完全な名前とは、キーワードの前に、リソースやライブラリの名前を、ドットを区切りとしてつけた名前です。

ライブラリキーワードの場合、 :name:`LibraryName.Keyword Name` のような形式になります。
例えば、 OperatingSystem ライブラリの :name:`Run` キーワードは、他に :name:`Run` キーワードが定義されていても、 :name:`OperatingSystem.Run` で呼び出せます。
ライブラリがモジュールやパッケージの場合は、完全なモジュール名・パッケージ名を使わねばなりません (例: :name:`com.company.Library.Some Keyword`)。
:ref:`WITH NAME 構文<WITH NAME syntax>` を使って、ライブラリに別名をつけた場合は、完全な名前で指定するときに、新たにつけた別名を使わねばなりません。

リソースファイルも、ライブラリ名と同じように、「完全な名前」で指定できます。
リソースの名前は、ファイル拡張子とパスを除いたファイル本体の名前です。
例えば、リソースファイル :file:`myresources.html` で定義されているキーワード :name:`Example` は、 :name:`myresources.Example` で呼び出せます。
ただし、同じファイル名のリソースファイルが複数あると、この方法では区別できないので注意してください。
完全指定の名前においても、大小文字の区別はなく、スペースやアンダースコアは無視されます。


.. _Specifying explicit priority between libraries and resources:

ライブラリやリソースの優先順位を明示する
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

キーワードの衝突がいくつもある場合、全てのキーワードについていちいち完全な名前で指定していくのは大変です。
また、長い名前を使うと、利用できるライブラリやリソースに応じて動作を切り替えるような動的なテストケースやユーザキーワードを作れなくなってしまいます。
こうした問題を解決する一つの方法として、 BuiltIn ライブラリの :name:`Set Library Search Order` キーワードを使って、キーワードの優先順位を明示する方法があります。

.. note:: このキーワードには「Library」という単語が入っていますが、実際にはリソースファイルに対しても使えます。
          ただし、以前解説した通り、リソースファイル中のキーワードは、常にライブラリのキーワードより優先されます。

:name:`Set Library Search Order` は、ライブラリやリソースを順番に並べたリストを引数に取ります。
テストデータ中のキーワード名が複数のキーワードにマッチした場合、リスト中のライブラリやリソースで同名のキーワードを持つものの先頭のものが選ばれ、そのキーワードの定義を使います。
キーワード名に対応するキーワードがリスト中にない場合は、キーワードの検索順が指定されていないときと同様、キーワード名の衝突による失敗となります。

詳細や例は、 :name:`Set Library Search Order`  のドキュメントを参照してください。

.. _Timeouts:

タイムアウト
--------------

実行にとても長い時間がかかったり、たまに永遠にハングアップしてしまったりするようなキーワードは問題を引き起こします。
Robot Framework では、テストケースとユーザーキーワードの両方に対してタイムアウトを設定できます。
指定時間内にキーワードの実行が終了しない場合、実行中のキーワードは強制的に停止させられます。
こうしてキーワードを強制停止すると、テスト対象のシステムは不安定な状態になることがあるので、タイムアウトを設定するのは、他に安全な選択肢がないときだけにしましょう。
一般的に、テストライブラリは通常ハングしないように作られているか、必要に応じて独自のタイムアウトメカニズムを持っているはずです。


.. _Test case timeout:

テストケースのタイムアウト
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

テストケースのタイムアウトは、設定テーブルで  :setting:`Test Timeout` を使うか、テストケーステーブルで :setting:`[Timeout]` を使って設定できます。
:setting:`Test Timeout` はテストスイート全てのデフォルトのタイムアウトを定義し、 :setting:`[Timeout]` はデフォルト値を上書きする形で、個別のテストケースのタイムアウトを設定します。

空の値で :setting:`[Timeout]` を使うと、タイムアウトしないことを示します。
これは :setting:`Test Timeout` が設定されていても有効です。
`NONE` を値として使うことも可能です。

テストのタイムアウトをどちらで設定するにせよ、設定名の直後のセルにはタイムアウトの期間の指定が入ります。この期間の設定には Robot Framework の :ref:`時間表現<time format>` 、すなわち秒表記か、 `1 minute 30 seconds` のような形式を使います。
フレームワーク自体に若干のオーバヘッドがあるため、1秒以内のタイムアウトは推奨しないので、時間を指定するときには注意して下さい。

タイムアウト超過によって表示されるエラーメッセージのデフォルト値は
`Test timeout <time> exceeded` です。
カスタムエラーメッセージを利用したいときは、タイムアウト値の次のセルに書きます。
タイムアウト値とエラーメッセージのどちらにも変数を使えます。

タイムアウトを指定している場合、指定時間を超過したキーワードの実行は中断し、テストケースは失敗します。ただし、 :ref:`ティアダウン<test teardown>` 中のキーワードは割り込まれません。ティアダウンは通常重要なクリーンアップ処理を行っているからです。
どうしてもティアダウン中のタイムアウトが必要なら、 :ref:`ユーザキーワードのタイムアウト<user keyword timeouts>` を使って実現できます。

.. sourcecode:: robotframework

   *** Settings ***
   Test Timeout    2 minutes

   *** Test Cases ***
   Default Timeout
       [Documentation]    設定テーブルのタイムアウトが使われる
       Some Keyword    argument

   Override
       [Documentation]    デフォルト値をオーバライドし、タイムアウトは10秒
       [Timeout]    10
       Some Keyword    argument

   Custom Message
       [Documentation]    デフォルト値とエラーメッセージをオーバライド
       [Timeout]    1min 10s    This is my custom error
       Some Keyword    argument

   Variables
       [Documentation]    タイムアウト値に変数を使う
       [Timeout]    ${TIMEOUT}
       Some Keyword    argument

   No Timeout
       [Documentation]    タイムアウト値を空にすると、Test Timeout が設定されていてもタイムアウトなし扱い
       [Timeout]
       Some Keyword    argument

   No Timeout 2
       [Documentation]    NONEでもタイムアウト無効にできる。この方がより明示的
       [Timeout]    NONE
       Some Keyword    argument


.. _User keyword timeout:

ユーザキーワードのタイムアウト
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:setting:`[Timeout]` を使えば、キーワードテーブル中のユーザキーワードに対してもによるタイムアウトを設定できます。
タイムアウト設定の書き方は、 :ref:`テストケースのタイムアウト<test case timeouts>` と同じです。カスタムのエラーメッセージを指定しない場合に使われるデフォルトのエラーメッセージは `Keyword timeout <time> exceeded` です。

Robot Framework 3.0 からは、引き数で渡された変数をタイムアウトを制御できるようになりました。なお、グローバル変数を使った制御は以前のバージョンでも可能です。

.. sourcecode:: robotframework

   *** Keywords ***
   Timed Keyword
       [Documentation]    Set only the timeout value and not the custom message.
       [Timeout]    1 minute 42 seconds
       Do Something
       Do Something Else

   Wrapper With Timeout
       [Arguments]    @{args}
       [Documentation]    This keyword is a wrapper that adds a timeout to another keyword.
       [Timeout]    2 minutes    Original Keyword didn't finish in 2 minutes
       Original Keyword    @{args}

   Wrapper With Customizable Timeout
       [Arguments]    ${timeout}    @{args}
       [Documentation]    Same as the above but timeout given as an argument.
       [Timeout]    ${timeout}
       Original Keyword    @{args}

ユーザキーワードのタイムアウトが有効なのは、該当ユーザーキーワードの実行中だけです。ユーザキーワード全体の実行時間がタイムアウト値を超えると、実行中のキーワードを中断します。通常のタイムアウトはティアダウン中は無効ですが、ユーザキーワードのタイムアウトはテストケースのティアダウン中でも有効です。

テストケースと、その中で使っているキーワード (あるいは、入れ子になっている別のキーワードなど）の両方にタイムアウトが設定されている場合、関連するキーワードのタイムアウトのうち最小のものがアクティブなタイムアウト値として使われます。

.. _for loops:

for ループ
--------------

テストの自動化では、同じ動作を何度も繰り返すことがよくあります。
Robot Framework でも、テストライブラリにはどんなループ構文でも書けますし、多くの場合、繰り返し処理を書きたければテストライブラリに書くべきです。
Robot Framework 独自のループ構文もあり、複数のライブラリのキーワードを組み合わせて反復実行したい場合に使えます。

For ループはテストケースとユーザキーワードの両方で使えます。
とはいえ、よほど単純なループでないかぎり、ループ処理のもたらす複雑さを隠蔽してくれるキーワード側に実装すべきです。
基本のループ構文 `FOR item IN sequence` の由来は Python ですが、シェルスクリプトや Perl にも同じような構文があります。

.. _Normal for loop:

通常の for ループ
~~~~~~~~~~~~~~~~~~~~~

In a normal for loop, one variable is assigned from a list of values,
one value per iteration. The syntax starts with `:FOR`, where
colon is required to separate the syntax from normal keywords. The
next cell contains the loop variable, the subsequent cell must have
`IN`, and the final cells contain values over which to iterate.
These values can contain variables_, including `list variables`_.

The keywords used in the for loop are on the following rows and they must
be indented one cell to the right. When using the `plain text format`_,
the indented cells must be `escaped with a backslash`__, but with other
data formats the cells can be just left empty. The for loop ends
when the indentation returns back to normal or the table ends.

.. sourcecode:: robotframework

   *** Test Cases ***
   Example 1
       :FOR    ${animal}    IN    cat    dog
       \    Log    ${animal}
       \    Log    2nd keyword
       Log    Outside loop

   Example 2
       :FOR    ${var}    IN    one    two
       ...     ${3}    four    ${last}
       \    Log    ${var}

The for loop in :name:`Example 1` above is executed twice, so that first
the loop variable `${animal}` has the value `cat` and then
`dog`. The loop consists of two :name:`Log` keywords. In the
second example, loop values are `split into two rows`__ and the
loop is run altogether five times.

It is often convenient to use for loops with `list variables`_. This is
illustrated by the example below, where `@{ELEMENTS}` contains
an arbitrarily long list of elements and keyword :name:`Start Element` is
used with all of them one by one.

.. sourcecode:: robotframework

   *** Test Cases ***
   Example
       :FOR    ${element}    IN    @{ELEMENTS}
       \    Start Element  ${element}

Nested for loops
~~~~~~~~~~~~~~~~

Having nested for loops is not supported directly, but it is possible to use
a user keyword inside a for loop and have another for loop there.

.. sourcecode:: robotframework

   *** Keywords ***
   Handle Table
       [Arguments]    @{table}
       :FOR    ${row}    IN    @{table}
       \    Handle Row    @{row}

   Handle Row
       [Arguments]    @{row}
       :FOR    ${cell}    IN    @{row}
       \    Handle Cell    ${cell}

__ `Dividing test data to several rows`_
__ Escaping_

Using several loop variables
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

It is also possible to use several loop variables. The syntax is the
same as with the normal for loop, but all loop variables are listed in
the cells between `:FOR` and `IN`. There can be any number of loop
variables, but the number of values must be evenly dividable by the number of
variables.

If there are lot of values to iterate, it is often convenient to organize
them below the loop variables, as in the first loop of the example below:

.. sourcecode:: robotframework

   *** Test Cases ***
   Three loop variables
       :FOR    ${index}    ${english}    ${finnish}    IN
       ...     1           cat           kissa
       ...     2           dog           koira
       ...     3           horse         hevonen
       \    Add to dictionary    ${english}    ${finnish}    ${index}
       :FOR    ${name}    ${id}    IN    @{EMPLOYERS}
       \    Create    ${name}    ${id}

For-in-range loop
~~~~~~~~~~~~~~~~~

Earlier for loops always iterated over a sequence, and this is also the most
common use case. Sometimes it is still convenient to have a for loop
that is executed a certain number of times, and Robot Framework has a
special `FOR index IN RANGE limit` syntax for this purpose. This
syntax is derived from the similar Python idiom.

Similarly as other for loops, the for-in-range loop starts with
`:FOR` and the loop variable is in the next cell. In this format
there can be only one loop variable and it contains the current loop
index. The next cell must contain `IN RANGE` and the subsequent
cells loop limits.

In the simplest case, only the upper limit of the loop is
specified. In this case, loop indexes start from zero and increase by one
until, but excluding, the limit. It is also possible to give both the
start and end limits. Then indexes start from the start limit, but
increase similarly as in the simple case. Finally, it is possible to give
also the step value that specifies the increment to use. If the step
is negative, it is used as decrement.

It is possible to use simple arithmetics such as addition and subtraction
with the range limits. This is especially useful when the limits are
specified with variables.

Starting from Robot Framework 2.8.7, it is possible to use float values for
lower limit, upper limit and step.

.. sourcecode:: robotframework

   *** Test Cases ***
   Only upper limit
       [Documentation]    Loops over values from 0 to 9
       :FOR    ${index}    IN RANGE    10
       \    Log    ${index}

   Start and end
       [Documentation]  Loops over values from 1 to 10
       :FOR    ${index}    IN RANGE    1    11
       \    Log    ${index}

   Also step given
       [Documentation]  Loops over values 5, 15, and 25
       :FOR    ${index}    IN RANGE    5    26    10
       \    Log    ${index}

   Negative step
       [Documentation]  Loops over values 13, 3, and -7
       :FOR    ${index}    IN RANGE    13    -13    -10
       \    Log    ${index}

   Arithmetics
       [Documentation]  Arithmetics with variable
       :FOR    ${index}    IN RANGE    ${var}+1
       \    Log    ${index}

   Float parameters
       [Documentation]  Loops over values 3.14, 4.34, and 5.34
       :FOR    ${index}    IN RANGE    3.14    6.09    1.2
       \    Log    ${index}

For-in-enumerate loop
~~~~~~~~~~~~~~~~~~~~~

Sometimes it is useful to loop over a list and also keep track of your location
inside the list.  Robot Framework has a special
`FOR index ... IN ENUMERATE ...` syntax for this situation.
This syntax is derived from the
`Python built-in function <https://docs.python.org/2/library/functions.html#enumerate>`_.

For-in-enumerate loops work just like regular for loops,
except the cell after its loop variables must say `IN ENUMERATE`,
and they must have an additional index variable before any other loop-variables.
That index variable has a value of `0` for the first iteration, `1` for the
second, etc.

For example, the following two test cases do the same thing:

.. sourcecode:: robotframework

   *** Variables ***
   @{LIST}         a    b    c

   *** Test Cases ***
   Manage index manually
       ${index} =    Set Variable    -1
       : FOR    ${item}    IN    @{LIST}
       \    ${index} =    Evaluate    ${index} + 1
       \    My Keyword    ${index}    ${item}

   For-in-enumerate
       : FOR    ${index}    ${item}    IN ENUMERATE    @{LIST}
       \    My Keyword    ${index}    ${item}

Just like with regular for loops, you can loop over multiple values per loop
iteration as long as the number of values in your list is evenly divisible by
the number of loop-variables (excluding the first, index variable).

.. sourcecode:: robotframework

   *** Test Case ***
   For-in-enumerate with two values per iteration
       :FOR    ${index}    ${english}    ${finnish}    IN ENUMERATE
       ...    cat      kissa
       ...    dog      koira
       ...    horse    hevonen
       \    Add to dictionary    ${english}    ${finnish}    ${index}

For-in-enumerate loops are new in Robot Framework 2.9.

For-in-zip loop
~~~~~~~~~~~~~~~

Some tests build up several related lists, then loop over them together.
Robot Framework has a shortcut for this case: `FOR ... IN ZIP ...`, which
is derived from the
`Python built-in zip function <https://docs.python.org/2/library/functions.html#zip>`_.

This may be easiest to show with an example:

.. sourcecode:: robotframework

   *** Variables ***
   @{NUMBERS}      ${1}    ${2}    ${5}
   @{NAMES}        one     two     five

   *** Test Cases ***
   Iterate over two lists manually
       ${length}=    Get Length    ${NUMBERS}
       : FOR    ${idx}    IN RANGE    ${length}
       \    Number Should Be Named    ${NUMBERS}[${idx}]    ${NAMES}[${idx}]

   For-in-zip
       : FOR    ${number}    ${name}    IN ZIP    ${NUMBERS}    ${NAMES}
       \    Number Should Be Named    ${number}    ${name}

Similarly as for-in-range and for-in-enumerate loops, for-in-zip loops require
the cell after the loop variables to read `IN ZIP`.

Values used with for-in-zip loops must be lists or list-like objects, and
there must be same number of loop variables as lists to loop over. Looping
will stop when the shortest list is exhausted.

Note that any lists used with for-in-zip should usually be given as `scalar
variables`_ like `${list}`. A `list variable`_ only works if its items
themselves are lists.

For-in-zip loops are new in Robot Framework 2.9.

Exiting for loop
~~~~~~~~~~~~~~~~

Normally for loops are executed until all the loop values have been iterated
or a keyword used inside the loop fails. If there is a need to exit the loop
earlier,  BuiltIn_ keywords :name:`Exit For Loop` and :name:`Exit For Loop If`
can be used to accomplish that. They works similarly as `break`
statement in Python, Java, and many other programming languages.

:name:`Exit For Loop` and :name:`Exit For Loop If` keywords can be used
directly inside a for loop or in a keyword that the loop uses. In both cases
test execution continues after the loop. It is an error to use these keywords
outside a for loop.

.. sourcecode:: robotframework

   *** Test Cases ***
   Exit Example
       ${text} =    Set Variable    ${EMPTY}
       :FOR    ${var}    IN    one    two
       \    Run Keyword If    '${var}' == 'two'    Exit For Loop
       \    ${text} =    Set Variable    ${text}${var}
       Should Be Equal    ${text}    one

In the above example it would be possible to use :name:`Exit For Loop If`
instead of using :name:`Exit For Loop` with :name:`Run Keyword If`.
For more information about these keywords, including more usage examples,
see their documentation in the BuiltIn_ library.

.. note:: :name:`Exit For Loop If` keyword was added in Robot Framework 2.8.

Continuing for loop
~~~~~~~~~~~~~~~~~~~

In addition to exiting a for loop prematurely, it is also possible to
continue to the next iteration of the loop before all keywords have been
executed. This can be done using BuiltIn_ keywords :name:`Continue For Loop`
and :name:`Continue For Loop If`, that work like `continue` statement
in many programming languages.

:name:`Continue For Loop` and :name:`Continue For Loop If` keywords can be used
directly inside a for loop or in a keyword that the loop uses. In both cases
rest of the keywords in that iteration are skipped and execution continues
from the next iteration. If these keywords are used on the last iteration,
execution continues after the loop. It is an error to use these keywords
outside a for loop.

.. sourcecode:: robotframework

   *** Test Cases ***
   Continue Example
       ${text} =    Set Variable    ${EMPTY}
       :FOR    ${var}    IN    one    two    three
       \    Continue For Loop If    '${var}' == 'two'
       \    ${text} =    Set Variable    ${text}${var}
       Should Be Equal    ${text}    onethree

For more information about these keywords, including usage examples, see their
documentation in the BuiltIn_ library.

.. note::  Both :name:`Continue For Loop` and :name:`Continue For Loop If`
           were added in Robot Framework 2.8.

.. _Removing unnecessary keywords from outputs:

出力ファイルから不要なキーワードを除去する
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

for ループで何度も繰り返し実行を行なうと、大量の出力が生成され、 output ファイルやログファイルのサイズが相当大きくなってしまいます。
Robot Framework 2.7 からは、コマンドラインオプションに :option:`--RemoveKeywords FOR` を指定することで、 :ref:`不要なキーワードを除去 <removing and flattening keywords>` できます。

.. _Repeating single keyword:

一つのキーワードを反復実行する
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

単に一つのキーワードを反復実行したいだけのときは、for ループを使うまでもありません。
BuiltIn ライブラリのキーワード :name:`Repeat Keyword` を使うほうが簡単です。
このキーワードは、繰り返し実行したいキーワードと繰り返したい回数を引数に取ります。
記法を見やすくするために、回数には `times` や `x` を付けられます。

.. sourcecode:: robotframework

   *** Test Cases ***
   Example
       Repeat Keyword    5    Some Keyword    arg1    arg2
       Repeat Keyword    42 times    My Keyword
       Repeat Keyword    ${var}    Another Keyword    argument

.. _Conditional execution:

条件付き実行
--------------

一般に、テストケースやユーザキーワードの中に条件分岐のロジックを持たせるのはお勧めしません。
処理がわかりづらくなり、メンテナンスを困難にするからです。
その代わり、テストライブラリを書いて、この手のロジックを普通のプログラム言語の構文で書きましょう。
とはいえ、状況によっては、条件付き実行のロジックを書けたほうがよいのは確かです。
Robot Framework には、 if/else 文そのものはありませんが、同じような効果を得る方法がいくつかあります。

- :ref:`テストケース <test cases>` や :ref:`テストスイート<test suites>` に指定するキーワード名は、変数にできます。
  このことを利用すれば、コマンドラインから変数を指定することで、動作を切り替えられます。
  
- BuiltIn ライブラリのキーワード :name:`Run Keyword` は、実行するキーワードを引数で受け取り、これは変数にできます。
  変数の値は、別のキーワードで動的に生成したり、コマンドラインから指定したりできます。

- BuiltIn ライブラリのキーワード :name:`Run Keyword If` や :name:`Run Keyword Unless` は、指定の式の値が True または False のとき、指定のキーワードを実行します。
  これらのキーワードは、簡単な if/else 構造をつくるのにぴったりです。
  使い方の例は :name:`Run Keyword If` のドキュメントを参照してください。

- BuiltIn ライブラリの別のキーワード、 :name:`Set Variable If` を使えば、指定の式の値に従って動的に値を設定できます。

- その他にも、テストケースやテストスイートが成功したとき、あるいは失敗したときに、指定のキーワードを実行するためのキーワードがあります。

.. _Parallel execution of keywords:

キーワードの並列実行
----------------------

キーワードを並列で実行したい場合は、テストライブラリレベルで、コードをバックグラウンド実行する形で実装してください。
その場合、典型的なインタフェースとして、まず :name:`Start Something` のようなキーワードで実行を開始します。
このキーワードはすぐに処理を戻します。
そして、 :name:`Get Results From Something` のような別のキーワードで、実行結果を取得できるまで待機させてください。
:ref:`OperatingSystem` ライブラリのキーワード、 :name:`Start Process` や :name:`Read Process Output` を参照してください。
