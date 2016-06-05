.. include:: ../roles.rst

.. _keyword table:
.. _user keyword:
.. _user keywords:
.. _higher-level keywords:
.. _Creating user keywords:

ユーザキーワードを定義する
========================

既存のキーワードを組み合わせて新しく高水準のキーワードを作るには、キーワードテーブルを使います。
新しく定義したキーワードは、テストライブラリの中で定義している、より低水準の *ライブラリキーワード* と区別するため、  *ユーザキーワード* と呼びます。
ユーザキーワードの作り方は、テストケースの作り方と非常によく似ているので、簡単に覚えられます。

.. contents::
   :depth: 2
   :local:

.. _User keyword syntax:

ユーザキーワードの構文
----------------------

.. _Basic syntax:

基本の構文
~~~~~~~~~~~~

多くの部分で、ユーザキーワードの基本的な構文は、 :ref:`テストケースの構文 <test case syntax>` と同じです。
ユーザキーワードはキーワードテーブルの中で定義します。テストケースはテストケーステーブルの中で定義し、二つを区別するのはテーブルの名前だけです。
ユーザキーワードの名前は、テストケースの名前と同じく、最初のカラムに書きます。
また、ユーザーキーワードも、テストケースと同じく、ライブラリ中のキーワードや他のユーザキーワードを組み合わせて定義します。
ユーザキーワードを構成するキーワードは、通常は2カラム目に書きます。例外は、変数にキーワードをセットするときで、その場合は3カラム目以降に書きます。

.. sourcecode:: robotframework

   *** Keywords ***
   Open Login Page
       Open Browser    http://host/login.html
       Title Should Be    Login Page

   Title Should Start With
       [Arguments]    ${expected}
       ${title} =    Get Title
       Should Start With    ${title}    ${expected}

たいていのユーザキーワードには、引数があります。
上の二つ目の例で、この重要な機能を使っています。
詳しくは :ref:`この後の節  ＜User keyword arguments>` で説明します。
:ref:`ユーザキーワードから値を返す <user keyword return values` 機能も同様です。

ユーザキーワードは、 :ref:`テストケースファイル <test case files>`, :ref:`リソースファイル<resource files>`, :ref:`テストスイート初期化ファイル <test suite initialization files>` で定義できます。
リソースファイルで定義したキーワードは、リソースファイルを取り込んだ別のファイルでも使えるようになります。
その他のファイルで定義したキーワードは、そのファイルの中でしか使えません。

.. _Settings in the Keyword table:

キーワードテーブル内で使える設定
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

ユーザキーワードは、 :ref:`テストケースの設定 <Settings in the test case table>` と似た設定を持たせられます。設定は、テストケースの場合と同様、角カッコを使った構文を使って、キーワードと区別します。
使える設定は以下に挙げた通りで、それぞれの設定についてはこの後の節で解説します。

`[Documentation]`:setting:
   :ref:`ユーザキーワードのドキュメント <user keyword documentation>` の設定に使います。

`[Tags]`:setting:
   キーワードの :ref:`タグ <User keyword tags>` の設定に使います。

`[Arguments]`:setting:
   :ref:`ユーザキーワードの引数 <user keyword arguments>` の設定に使います。

`[Return]`:setting:
   :ref:`ユーザキーワードの戻り値 <user keyword return values>` の設定に使います。

`[Teardown]`:setting:
   :ref:`ユーザキーワードのティアダウン <user keyword teardown>` の設定に使います。

`[Timeout]`:setting:
   :ref:`ユーザキーワードのタイムアウト <user keyword timeout>` の設定に使います。
   :ref:`タイムアウト <Timeouts>` については、別の節で解説しています。


.. _User keyword documentation:

.. _User keyword name and documentation:

ユーザキーワード名とドキュメント
-----------------------------

ユーザキーワードの名前は、ユーザキーワードテーブルの最初のカラムに定義します。
言うまでもなく、キーワード名はわかりやすくすべきで、長いキーワード名でもかまいません。
実際、ユースケース的なテストケースを書いていると、最も高水準のキーワードは、文章だったり、一つの段落だったりすることもあります。

:ref:`テストケースのドキュメント <test case documentation>` と同様、 :setting:`[Documentation]` 設定を使って、ユーザキーワードにドキュメントを設定できます。

この設定は、テストデータ中でユーザキーワードの説明を書くのに使います。
また、よりきちんとしたキーワードのドキュメントを :ref:`リソースファイル` から :ref:`Libdoc` ツールで生成するときにも使われます。
最後に、ドキュメントの最初の行は、 :ref:`テスト実行結果ログ <test logs>` のキーワードドキュメントとして表示されます。

キーワードは、除去されたり、新しいものに置き換わったり、何らかの理由で撤廃されたりすることがあります。ユーザキーワードのドキュメントの先頭に `*DEPRECATED*` を付けると、キーワードを使った時に警告を出力します。
詳しくは、 :ref:`キーワードを撤廃扱いにする <Deprecating keywords>` の節を参照してください。

.. _User keyword tags:

ユーザキーワードのタグ
----------------------

Robot Framework 2.9 からは、キーワードにもタグを付与できます。
ユーザキーワードのタグは :ref:`テストケースのタグ <test case tags>` と同じく、 :setting:`[Tags]` 設定で付与できますが、 :setting:`Force Tags` や :setting:`Default Tags` の影響はうけません。
さらに、キーワードのタグは、キーワードのドキュメントの最後の行に `Tags:` の後に続けて、カンマ区切りで指定する方法でも定義できます。
例えば、以下の二つのキーワードには、同じ3つのタグが付与されます。

.. sourcecode:: robotframework

   *** Keywords ***
   Settings tags using separate setting
       [Tags]    my    fine    tags
       No Operation

   Settings tags using documentation
       [Documentation]    I have documentation. And my documentation has tags.
       ...                Tags: my, fine, tags
       No Operation


キーワードのタグは、ログに表示される他、 :ref:`Libdoc` の生成するドキュメントにも記載され、タグを使ってキーワードを検索できます。
コマンドラインオプションの :ref:`--removekeywords <Removing keywords>` や :ref:`--flattenkeywords <Flattening keywords>` でも、キーワードをタグで選ぶことができます。
その他にも、新たなキーワードタグの用途が、今後のリリースで追加されるかもしれません。

:ref:`テストケースのタグ <test case tags>` と同じく、 `robot-` で始まるユーザキーワードのタグは、 Robot Framework 本体の特殊な機能のために :ref:`予約されています <Reserved Tags>` 。
そうした特殊な機能を使うのが目的でないのなら、 `robot-` で始まるタグを使ってはなりません。


.. _User keyword arguments:

ユーザキーワードの引数
----------------------

ほとんどのユーザキーワードは、何らかの引数を取ります。
引数を指定するための書き方は、おそらく Robot Framework を使う上で必要なとしては最も難解な部分ですが、それでも、大抵の場合で使う書き方は分かりやすい部類に入るでしょう。
引数は、 :setting:`[Arguments]` 設定で設定し、引数の名前は :ref:`変数 <variables>` と同じ書き方、 `${arg}` のように書きます。

.. _Positional arguments:

位置固定の引数
~~~~~~~~~~~~~~

引数定義で最も簡単なのは、 (引数を持たないのがいちばん簡単だというのは置いといて) 位置固定の引数 (positional argument) だけを持たせるやり方です。
大抵の場合、この方法で事足ります。

引数を定義するには、まず :setting:`[Arguments]` 設定を書き、その次以降のセルに引数名を並べていきます。各引数は一つ一つのセルにして、変数と同じ記法を使います。
この書き方でキーワードを定義すると、キーワードを使うとき、定義した引数と同じ個数の引数を定義せねばなりません。
フレームワークは引数の名前が何であろうと感知しませんが、ユーザの視点から、できるだけ分かりやすい名前を付けましょう。
変数名には、 `${my_arg}`, `${my arg}`, `${myArg}` のように、小文字主体の名前を付けるよう推奨します。

.. sourcecode:: robotframework

   *** Keywords ***
   One Argument
       [Arguments]    ${arg_name}
       Log    Got argument ${arg_name}

   Three Arguments
       [Arguments]    ${arg1}    ${arg2}    ${arg3}
       Log    1st argument: ${arg1}
       Log    2nd argument: ${arg2}
       Log    3rd argument: ${arg3}

.. _Default values with user keywords:

ユーザキーワードにデフォルト値を設定する
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

大抵のケースでは、位置固定の引数だけでユーザキーワードを定義できます。
とはいえ、キーワードの引数に :ref:`デフォルト値 <default values>` をもたせた方が便利なこともあります。
ユーザキーワードもまた、デフォルト値をサポートしていて、そのための新しい記法も、これまでに解説してきた基本的な記法とそれほど変わりません。

端的に言えば、デフォルト値は、引数にデフォルトの値を足しただけです。つまり、 `${arg}=default` のように、変数名の直後に等号 (`=`) を置き、その後に値を置きます。
デフォルト値つきの引数は何個でも定義できますが、必ず位置固定引数の後に定義せねばなりません。
デフォルト値には :ref:`テスト、スイート、グローバルスコープ <Variable priorities and scopes>` で定義済みの :ref:`変数 <variable>` を含めてかまいませんが、キーワードを呼び出す側でローカルに設定した変数は使えません。
Robot Framework 3.0 からは、同じ引数定義の列の中で、先に定義した変数の値を、デフォルト値として指定できるようになりました。

.. note:: デフォルト値の記法では、スペースの有無が厳しくチェックされます。 `=` の前にスペースを入れてはならず、 `=` の後にスペースを入れると、デフォルト値の一部とみなされます。

.. sourcecode:: robotframework

   *** Keywords ***
   One Argument With Default Value
       [Arguments]    ${arg}=default value
       [Documentation]    This keyword takes 0-1 arguments
       Log    Got argument ${arg}

   Two Arguments With Defaults
       [Arguments]    ${arg1}=default 1    ${arg2}=${VARIABLE}
       [Documentation]    This keyword takes 0-2 arguments
       Log    1st argument ${arg1}
       Log    2nd argument ${arg2}

   One Required And One With Default
       [Arguments]    ${required}    ${optional}=default
       [Documentation]    This keyword takes 1-2 arguments
       Log    Required: ${required}
       Log    Optional: ${optional}

    Default Based On Earlier Argument
       [Arguments]    ${a}    ${b}=${a}    ${c}=${a} and ${b}
       Should Be Equal    ${a}    ${b}
       Should Be Equal    ${c}    ${a} and ${b}

キーワードがデフォルト値つきの引数をとり、そのうちの幾つかだけをキーワードの呼び出し時に変更したいなら、 :ref:`名前付き引数 <named arguments>` 記法を使うのが便利です。
ユーザキーワードでこの記法を使うと、引数は `${}` で修飾されません。
例えば、上で定義したキーワードのうち二つ目は、以下のようにして呼び出しが可能で、このとき `${arg1}` はデフォルト値のままです。

.. sourcecode:: robotframework

   *** Test Cases ***
   Example
       Two Arguments With Defaults    arg2=new value

Python使いなら誰もが気付くはずですが、この記法の発想は、 Python の関数の引数デフォルト値の記法から大きな影響を受けています。


.. _Varargs with user keywords:

ユーザキーワードに可変引数を持たせる
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

デフォルト値や名前付き引数だけでは不十分な場合には、 :ref:`可変個の引数 <variable number of arguments>` を渡せるようにする必要があります。
ユーザキーワードでもこの機能をサポートしています。
必要なのは、 :ref:`リスト型の変数 <list variable>` を、位置固定引数の後に持たせるだけです。
この記法は、上で述べたデフォルト値との組み合わせが可能で、その場合は、引数として渡された値のうち、キーワードの引数定義にマッチしなかったもの全てが、リストに渡ります。
その結果、リストの中身は任意の個数になりえます。ゼロのときもあります。

.. sourcecode:: robotframework

   *** Keywords ***
   Any Number Of Arguments
       [Arguments]    @{varargs}
       Log Many    @{varargs}

   One Or More Arguments
       [Arguments]    ${required}    @{rest}
       Log Many    ${required}    @{rest}

   Required, Default, Varargs
       [Arguments]    ${req}    ${opt}=42    @{others}
       Log    Required: ${req}
       Log    Optional: ${opt}
       Log    Others:
       : FOR    ${item}    IN    @{others}
       \    Log    ${item}

上の例の最後のキーワードの場合、二つ以上の引数を渡すと、第二引数の `${opt}` には必ず値が渡り、デフォルト値が使われません。第二引数を空にしてもそうなるので注意が必要です。
最後の引数は、可変個の引数が渡されたときに、 :ref:`for ループ <for loops>` を使って引数を処理する例にもなっています。
この二つのやや高度な機能を組み合わせると、とても便利なケースが時々あります。

ユーザキーワードの可変引数も、Python使いなら気付くかもしれませんが、Python の関数の可変個の引数にとても似た記法です。

.. Kwargs with user keywords:

ユーザキーワードに kwargs を持たせる
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:ref:`フリーキーワード引数` もまた、ユーザキーワードにもたせられます。
フリーキーワード引数は、 `&{kwargs}` のような :ref:`辞書型の変数 <dictionary variable>` を、位置固定引数および可変個引数の後の最後の引数として定義します。
キーワードを呼び出すと、 `&{kwargs}` には、 :ref:`名前付きの引数 <named arguments>` のうち、位置固定引数にマッチしなかったもの全てが入ります。

.. sourcecode:: robotframework

   *** Keywords ***
   Kwargs Only
       [Arguments]    &{kwargs}
       Log    ${kwargs}
       Log Many    @{kwargs}

   Positional And Kwargs
       [Arguments]    ${required}    &{extra}
       Log Many    ${required}    @{extra}

   Run Program
       [Arguments]    @{varargs}    &{kwargs}
       Run Process    program.py    @{varargs}    &{kwargs}


上の例のうち最後のものは、位置固定の引数や名前付き引数を取り、それを別のキーワードに渡すような、ラッパ型キーワードの例を示しています。
:ref:`kwargs examples` で、より多くのサンプルを挙げています。

kwargs のサポートもまた、 Python の kwargs に非常によく似ています。
引数シグネチャ上の位置や、値の渡り方において、 `&{kwargs}` は Python の `**kwargs` とほぼ同じです。

.. _Embedded argument syntax:
.. _Embedding arguments into keyword name:

キーワード名の中に引数を埋め込む
-----------------------------

ここまでは、ユーザキーワードに引数を渡すために、キーワード名の後のセルに引数を指定する方法を説明してきました。
Robot Framework には、ユーザキーワードに引数を渡す方法がもう一つあります。
それは、引数をキーワード名に直接埋め込むというものです。
この方法の利点は、キーワードをより現実的で分かりやすい文章として書けるところにあります。

.. _Basic syntax:

基本の書き方
~~~~~~~~~~~~

キーワードを書くとき、 :name:`Select dog from list` や :name:`Selects cat from list` といったキーワードがあり、そのままだと、それぞれのキーワードを別々に実装せねばならないことがあります。
キーワード埋め込み引数は、 :name:`Select ${animal} from list` のような書き方を実現しよう、という発想です。

.. sourcecode:: robotframework

   *** Keywords ***
   Select ${animal} from list
       Open Page    Pet Selection
       Select Item From List    animal_list    ${animal}

埋め込み引数のキーワードは、「通常の」引数 (:setting:`[Arguments]` で設定するもの) を持たせられないことを除けば、他のユーザキーワードと変わりません。
キーワード名の中で使われている引数は、キーワードの中で普通に利用でき、キーワードを呼び出したときの名前によって値が分かります。
例えば、上の例で `${animal}` を `dog` にしたい場合、キーワードは :name:`Select dog from list` です。
言うまでもなく、定義した引数をキーワードの中で使わなくともよいので、変数にした部分は、いわばワイルドカードのようにも使えます。

この種のキーワードは、他の普通のキーワードと同じように使えますが、キーワード中のスペースやアンダースコアが厳密に扱われる点が違うので注意してください。
ただし、大小文字の区別はありません。
例えば、上のキーワードを呼び出すとき、 :name:`select x from list` のようには書けますが、 :name:`Select x fromlist` のようには書けません。

埋め込み引数には、通常のキーワードの引数で使えるような、デフォルト値や可変個の引数のサポートがありません。
キーワードを呼ぶときに、変数を指定するのはもちろん可能ですが、テストの可読性を下げてしまうかもしれません。
埋め込み引数を使えるのは、ユーザキーワードだけです。

.. _Embedded arguments matching too much:

埋め込み引数が間違ってマッチする場合
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

埋め込み引数を使う上で少々面倒なのは、キーワードを呼び出したときに、正しく値が取り出されるようにする工夫です。
とりわけ、複数の引数とそれらを分割する文字が、キーワードに渡した文字に何度も現れるような場合には、問題が発生します。
例えば、 :name:`Select ${city} ${team}` というキーワードは、 ``Select Los Angeles Lakers`` のように、 `$city` に入るべき文字列にスペースが入っているとうまく動作しません。
解決方法の一つは、キーワードの定義で引数をクオート (:name:`Select "${city}" "${team}"`) しておき、キーワードを使うときに (``Select "Los Angeles" "Lakers"`` のように) クオートつきで書くというものです。
このアプローチは、全ての変数パターンの衝突を防げるわけではありませんが、埋め込み引数を互いに区別しやすくなるので、強く推奨します。
もっと強力な反面より複雑なのは、変数を定義するときに :ref:`正規表現を使う <using custom regular expressions>` 方法で、次の節で解説します。
最後に、あまりにも複雑になってしまったら、あっさり普通の位置固定引数を使う方法に切り替えてみましょう。

埋め込み引数が間違ってマッチするような状況は、 :ref:`Given/When/Then/And/But プレフィクスを無視するキーワード <Ignoring Given/When/Then/And/But prefixes>` を書く場合によくあります。例えば、 :name:`${name} goes home` のようなキーワードを作ってしまうと、 :name:`Given Janne goes home` としたとき、 `${name}` に `Given Janne` が入ってしまいます。
:name:`"${name}" goes home` のようにクオートを入れておくと、この問題を簡単に解決できるのです。

.. _Using custom regular expressions:

埋め込み引数のマッチに正規表現を使う
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

埋め込み引数つきのキーワードを呼び出すとき、内部では :ref:`正規表現 <http://ja.wikipedia.org/wiki/正規表現>` (略して regexp) を使って引数の値を取り出しています。
デフォルトのロジックでは、どんな名前に置き換わっていてもマッチするように、パターン `.*` が使わrています。
大体はこれで問題ないのですが、前節のように、 :ref:`間違えてマッチする <Embedded arguments matching too much>` ケースがたまにあります。
この問題はクオートなどで引数を分割することで多少解消できますが、例えば、以下のテストは、 :name:`I execute "ls" with "-lh"` が二つのキーワードのどちらにもマッチしてしまうために失敗します。


.. sourcecode:: robotframework

   *** Test Cases ***
   Example
       I execute "ls"
       I execute "ls" with "-lh"

   *** Keywords ***
   I execute "${cmd}"
       Run Process    ${cmd}    shell=True

   I execute "${cmd}" with "${opts}"
       Run Process    ${cmd} ${opts}    shell=True


この問題の解消方法は、正規表現を使って、特定のコンテキストで呼び出されるべきキーワードだけがマッチするように書くことです。
この機能を使いこなし、かつこの節の例を理解するには、まずは正規表現の書き方の基礎を理解しておく必要があります。

埋め込み引数の正規表現は、引数の名前の後ろに書き、引数と正規表現の間はコロンで区切ります。
例えば、数字だけにマッチするような引数を書きたければ、 `${arg:\d+}` のようにします。
正規表現の使い方の例を、以下に示します。

.. sourcecode:: robotframework

   *** Test Cases ***
   Example
       I execute "ls"
       I execute "ls" with "-lh"
       I type 1 + 2
       I type 53 - 11
       Today is 2011-06-27

   *** Keywords ***
   I execute "${cmd:[^"]+}"
       Run Process    ${cmd}    shell=True

   I execute "${cmd}" with "${opts}"
       Run Process    ${cmd} ${opts}    shell=True

   I type ${a:\d+} ${operator:[+-]} ${b:\d+}
       Calculate    ${a}    ${operator}    ${b}

   Today is ${date:\d{4\}-\d{2\}-\d{2\}}
       Log    ${date}

この例では、 :name:`I execute "ls" with "-lh"` は :name:`I execute "${cmd}" with "${opts}"` だけにマッチします。
:name:`I execute "${cmd:[^"]}"` の `[^"]+` が、引数にクオートが入っているキーワードを除外するからです。
そのため、上の例では、他の :name:`I execute` 系に正規表現の引数を足す必要はありません。

.. tip:: 引数をクオートするとき、 `[^"]+` を使うと、引数は最初のとじカッコまでにマッチします。

.. _Supported regular expression syntax:

サポートする正規表現の記法
'''''''''''''''''''''''''

Robot Framework は Python で実装されているので、 Python の :name:`re` モジュールを使っています。
:name:`re` モジュールは、ごく標準的な :ref:`正規表現の記法 <https://docs.python.org/2/library/re.html>` を備えており、そのほぼ全てを埋め込み引数の正規表現でも全てサポートしています。ただし、拡張記法 `(?...)` だけは使えません。
埋め込み引数へのマッチは、大小文字を区別しないので注意してください。
正規表現のシンタクスが無効な場合、キーワードの生成に失敗し、エラーは :ref:`テスト実行時のエラー <Errors and warnings during execution>` として表示されます。

.. _Escaping special characters:

特殊文字のエスケープ
'''''''''''''''''''

埋め込み引数の正規表現を定義するとき、エスケープしなければならない文字がいくつかあります。
まず、パターン中の閉じ中括弧 (`}`) は、そのままだと引数の閉じ括弧とみなされてしまうので、バックスラッシュ一個でエスケープせねばなりません (`\}`)。
これは、上の :name:`Today is ${date:\\d{4\\}-\\d{2\\}-\\d{2\\}}` の例でも使われています。

バックスラッシュ自体 (:codesc:`\\`) は、 Python の正規表現における特殊文字なので、バックスラッシュそのものをリテラルとして使いたい時にはエスケープが必要です。最も確実にエスケープする方法は、4つ (`\\\\`) 並べる書き方ですが、次にくる文字によっては、二つのバックスラッシュでよいときもあります。

キーワード名や埋め込み引数は、 :ref:`テストデータのエスケープ規則 <Escaping>` に従ってエスケープしては *ならない* ので注意してください。つまり、例えば、正規表現 `${name:\w+}` の中のバックスラッシュはエスケープする必要がありません。

.. _Using variables with custom embedded argument regular expressions:

埋め込み引数の正規表現に変数を使う
'''''''''''''''''''''''''''''''

埋め込み引数の正規表現を使うとき、Robot Framework は正規表現を自動的に拡張して、テキストだけでなく、変数名もマッチするようにします。
つまり、キーワードの埋め込み引数が正規表現を使っていても、そのキーワードを変数を使って呼べるのです。
例えば、以下のテストケースは、前節の例のキーワードに値を渡しています。

.. sourcecode:: robotframework

   *** Variables ***
   ${DATE}    2011-06-27

   *** Test Cases ***
   Example
       I type ${1} + ${2}
       Today is ${DATE}

正規表現の部分に変数も自動的にマッチさせる機能のよくないところは、キーワードが引数として得た値が、実際には正規表現にマッチしないケースがあるところです。
例えば、上の例の `${DATE}` は、日付形式でない値を持つかもしれませんが、それでも :name:`Today is ${DATE}` は同じキーワードにマッチします。

.. _Behavior-driven development example:

ビヘイビアドリブンな開発の例
~~~~~~~~~~~~~~~~~~~~~~~~~~

キーワード名の中に変数を持てることの最大のメリットは、 :ref:`ビヘイビアドリブン型 <behavior-driven style>` のテストを書くときに、高水準の、文章として読めるキーワードを使いやすいことです。
以下に、その例を示しましょう。
この例では、 :name:`Given`, :name:`When`, :name:`Then` という接頭辞が、
:ref:`キーワードの定義では不要 <Ignoring Given/When/Then/And/But prefixes>` だということにも注意してください。

.. sourcecode:: robotframework

   *** Test Cases ***
   Add two numbers
       Given I have Calculator open
       When I add 2 and 40
       Then result should be 42

   Add negative numbers
       Given I have Calculator open
       When I add 1 and -2
       Then result should be -1

   *** Keywords ***
   I have ${program} open
       Start Program    ${program}

   I add ${number 1} and ${number 2}
       Input Number    ${number 1}
       Push Button     +
       Input Number    ${number 2}
       Push Button     =

   Result should be ${expected}
       ${result} =    Get Result
       Should Be Equal    ${result}    ${expected}

.. note:: Robot Framework の引数埋め込み機能は、有名な BDD ツール Cucumber__ の *ステップ定義 (step definition)* に着想を得ています。

__ http://cukes.info

.. _User keyword return values:

値を返すユーザキーワードを定義する
-------------------------------

ライブラリキーワードと同様、ユーザキーワードも値を返せます。
通常、戻り値は :setting:`[Return]` で設定できますが、 :ref:`BuiltIn` ライブラリのキーワード、 :name:`Return From Keyword` や :name:`Return From Keyword If` でも返せます。
どのやり方で返した戻り値も、テストケースや他のキーワードの中で、 :ref:`変数に代入<Return values from keywords>` して使えます。

.. _Using :setting:`[Return]` setting:

:setting:`[Return]` 設定の使い方
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

ユーザキーワードの値の返し方のうちもっとも一般的なのは、ユーザキーワードが一つの値を返して、その値をスカラ値として代入する形式です。
:setting:`[Return]` 設定を使う場合は、設定名の次のセルに返したい値を入れます。

ユーザキーワードから複数の値を返すこともできます。その場合、複数のスカラ変数に一度に代入したり、リスト変数に代入したり、スカラ変数とリスト変数に組み合わせて代入したりできます。
複数の値を返したいときは、単に :setting:`[Return]` 設定の隣のセルに、返したい値を並べていくだけです。

.. sourcecode:: robotframework

   *** Test Cases ***
   One Return Value
       ${ret} =    Return One Value    argument
       Some Keyword    ${ret}

   Multiple Values
       ${a}    ${b}    ${c} =    Return Three Values
       @{list} =    Return Three Values
       ${scalar}    @{rest} =    Return Three Values

   *** Keywords ***
   Return One Value
       [Arguments]    ${arg}
       Do Something    ${arg}
       ${value} =    Get Some Value
       [Return]    ${value}

   Return Three Values
       [Return]    foo    bar    zap

.. _Using special keywords to return:

特別なキーワードを使って戻り値を制御する
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:ref:`BuiltIn` ライブラリのキーワード、 :name:`Return From Keyword` や :name:`Return From Keyword If` を使うと、条件に応じて、ユーザキーワードの処理の途中で値を返せます。
これらのキーワードは、いずれも、戻り値をオプションの引数にもたせることができ、先の :setting:`[Return]` で返すのと同じように値を返せます。

以下の例のうち、最初のものは、前節の :setting:`[Return]` を使った例と全く同じです。
二つ目の例は、ちょっと高度なことをやっていて、 :ref:`for ループ <for loop>` の中から値を返しています。

.. sourcecode:: robotframework

   *** Test Cases ***
   One Return Value
       ${ret} =    Return One Value  argument
       Some Keyword    ${ret}

   Advanced
       @{list} =    Create List    foo    baz
       ${index} =    Find Index    baz    @{list}
       Should Be Equal    ${index}    ${1}
       ${index} =    Find Index    non existing    @{list}
       Should Be Equal    ${index}    ${-1}

   *** Keywords ***
   Return One Value
       [Arguments]    ${arg}
       Do Something    ${arg}
       ${value} =    Get Some Value
       Return From Keyword    ${value}
       Fail    ここは実行されない

   Find Index
       [Arguments]    ${element}    @{items}
       ${index} =    Set Variable    ${0}
       :FOR    ${item}    IN    @{items}
       \    Return From Keyword If    '${item}' == '${element}'    ${index}
       \    ${index} =    Set Variable    ${index + 1}
       Return From Keyword    ${-1}    # [Return] を使っても書ける

.. note:: :name:`Return From Keyword` と :name:`Return From Keyword If` は、いずれも Robot Framework 2.8 から使えるようになりました。

.. _User keyword teardown:

ユーザキーワードのティアダウン
------------------------------

:setting:`[Teardown]` を使えば、ユーザーキーワードにティアダウン処理を定義できます。

キーワードのティアダウン処理は、 :ref:`テストケースのティアダウン <test setup and teardown>` と同じように働きます。
いちばん重要な類似点は、ティアダウンに設定できるのは単一のキーワードであり、他のユーザキーワードを指定でき、キーワードが失敗したときに実行されるということです。
さらに、ティアダウンに指定したキーワードの処理は、たとえその中で失敗が発生しても、全て実行されます。
ただし、ティアダウンキーワードの実行中に失敗が発生すると、そのテストケースは失敗し、残りのテストのステップは実行されません。ティアダウン用に実行するキーワードは、変数にもできます。

.. sourcecode:: robotframework

   *** Keywords ***
   With Teardown
       Do Something
       [Teardown]    Log    keyword teardown

   Using variables
       [Documentation]    Teardown given as variable
       Do Something
       [Teardown]    ${TEARDOWN}

