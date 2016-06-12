Dialogs: ユーザにダイアログを表示する
========================================
Version:          3.0
Scope:            global
Named arguments:  supported

このテストライブラリは、ユーザと対話するためのダイアログ機能を提供します。

``Dialogs`` は Robot Framework の標準ライブラリで、テストを一時停止して、ユーザから入力を受け付ける手段を提供します。

テストを実行している環境が Python, IronPython, Jython のいずれかによって、表示されるダイアログは多少異なりますが、機能に違いはありません。

Robot Framework 2.8 からは、メッセージが長い場合、行を折り返すようになりました。
自分で行を折り返したければ、文字列中に改行文字 ``\n`` を入れてください。

このライブラリには、 Python ではタイムアウトと一緒に使えないという制限があります。
IronPython のサポートは Robot Framework 2.9.2 で追加されました。

キーワード
-------------

Execute Manual Step
~~~~~~~~~~~~~~~~~~~~~
Arguments:  [message, default_error=]

テストの実行を一時停止して、ユーザがキーワードの実行状態を入力するまで待ちます。

ユーザは、 ``PASS`` または ``FAIL`` ボタンを押せます。
後者を押した場合、テストは失敗し、エラーメッセージを入力するためのダイアログが表示されます。

``message`` は、最初のダイアログに表示される説明です。
``default_error`` は、エラーメッセージ入力ダイアログを表示する際の、デフォルトのエラーメッセージ内容です。


Get Selection From User
~~~~~~~~~~~~~~~~~~~~~~~~~
Arguments:  [message, *values]

テストの実行を一時停止して、ユーザに値を選ばせます。

ユーザが選んだ値を返します。
``Cancel`` ボタンを押すと、キーワードは失敗します。

``message`` は、最初のダイアログに表示される説明です。
``values`` は、ユーザに提示する選択肢です。

例::
  | ${username} = | Get Selection From User | Select user name | user1 | user2 | admin |


Get Value From User
~~~~~~~~~~~~~~~~~~~~~
Arguments:  [message, default_value=, hidden=False]

テストの実行を一時停止して、ユーザに値の入力を求めます。

ユーザが入力した値、またはデフォルト値を返します。
空の値を返してもかまいませんが、 ``Cancel`` ボタンを押すとキーワードは失敗します。

``message`` は、最初のダイアログに表示される説明です。
``default_value`` は、入力フィールドにデフォルト値として表示する値です。

``hidden`` を真値にすると、ユーザが入力した値を隠蔽します。
``hidden`` は、空でなく、かつ ``false`` や ``no`` でない文字列の場合に真になります。大小文字は区別しません。
文字列でなければ、その真偽値を `Python の流儀で`__ 決めます。

__ http://docs.python.org/2/library/stdtypes.html#truth-value-testing

例::
  | ${username} = | Get Value From User | Input user name | default    |
  | ${password} = | Get Value From User | Input password  | hidden=yes |

Robot Framework 2.8.4 から、値を隠せるようになりました。
``false`` や ``no`` を偽値とみなすのは 2.9 からです。


Pause Execution
~~~~~~~~~~~~~~~~~
Arguments:  [message=Test execution paused. Press OK to continue.]

テストの実行を停止して、ユーザが ``Ok`` ボタンを押すまで待ちます。

``message`` は、ダイアログに表示されるメッセージです。

