================================
Robot Framework チートシート
================================

標準ライブラリ
==============


BuiltIn
--------
.. list-table::

    * - キーワード
      - 引数
      - 説明
    * - Call Method
      - object, method_name, \*args, \*\*kwargs
      - Pythonオブジェクトのメソッドを呼び出す
    * - Catenate
      - \*items
      - 文字列を結合する
    * - Comment
      - \*messages
      - 引数を処理せずログに出力する
    * - Continue For Loop
      - 
      - ループ処理をスキップする
    * - Continue For Loop If
      - condition
      - 条件に一致するときループをスキップする
    * - Convert To Binary
      - item, base=None, prefix=None, length=None
      - 2進表記に変換する
    * - Convert To Boolean
      - item
      - ブール型に変換する
    * - Convert To Bytes
      - input, input_type=text
      - バイト列に変換する
    * - Convert To Hex
      - item, base=None, prefix=None, length=None, lowercase=False
      - 16進表記に変換する
    * - Convert To Integer
      - item, base=None
      - 整数オブジェクトに変換する
    * - Convert To Number
      - item, precision=None
      - 数値オブジェクトに変換する
    * - Convert To Octal
      - item, base=None, prefix=None, length=None
      - 8進表記に変換する
    * - Convert To String
      - item
      - 文字列オブジェクトに変換する
    * - Create Dictionary
      - \*items
      - 辞書オブジェクトを生成する
    * - Create List
      - \*items
      - リストオブジェクトを生成する
    * - Evaluate
      - expression, modules=None, namespace=None
      - 式を評価する
    * - Exit For Loop
      -
      - ループを抜ける
    * - Exit For Loop If
      - condition
      - 条件に一致するときループを抜ける
    * - Fail
      - msg=None, \*tags
      - テストを強制的に失敗させる
    * - Fatal Error
      - msg=None
      - テストを中断する
    * - Get Count
      - item1, item2
      - 配列の特定の要素の個数を数える
    * - Get Length
      - item
      - 配列要素の個数を数える
    * - Get Library Instance
      - name=None, all=False
      - 他のライブラリインスタンスを得る
    * - Get Time
      - format=timestamp, time\_=NOW
      - 時刻を得る
    * - Get Variable Value
      - name, default=None
      - 変数の値を調べる
    * - Get Variables
      - no_decoration=False
      - スコープ中の変数リストを得る
    * - Import Library
      - name, \*args
      - ライブラリをインポートする
    * - Import Resource
      - path
      - リソースをインポートする
    * - Import Variables
      - path, \*args
      - 変数ファイルをインポートする
    * - Keyword Should Exist
      - name, msg=None
      - キーワードが定義されているか確かめる
    * - Length Should Be
      - item, length, msg=None
      - 配列の長さを検証する
    * - Log
      - message, level=INFO, html=False, console=False, repr=False
      - ログを出力する
    * - Log Many
      - \*messages
      - 長いログを出力する
    * - Log To Console
      - message, stream=STDOUT, no_newline=False
      - コンソールにログを出力する
    * - Log Variables
      - level=INFO
      - 変数をログに出力する
    * - No Operation
      -
      - 何もしない
    * - Pass Execution
      - message, \*tags
      - テストの実行を飛ばして PASS マークを付ける
    * - Pass Execution If
      - condition, message, \*tags
      - 条件に一致するときテストの実行を飛ばす
    * - Regexp Escape
      - \*patterns
      - 正規表現エスケープ済みの文字列を得る
    * - Reload Library
      - name_or_instance
      - ライブラリをロードし直す
    * - Remove Tags
      - \*tags
      - タグを除去する
    * - Repeat Keyword
      - repeat, name, \*args
      - キーワードを指定回数繰り返す
    * - Replace Variables
      - text
      - 変数を置き換える
    * - Return From Keyword
      - \*return_values
      - キーワードの実行から抜ける
    * - Return From Keyword If
      - condition, \*return_values
      - 条件に一致するときキーワードの実行から抜ける
    * - Run Keyword
      - name, \*args
      - キーワードを実行する
    * - Run Keyword And Continue On Failure
      - name, \*args
      - キーワードを実行して、失敗しても継続する
    * - Run Keyword And Expect Error
      - expected_error, name, \*args
      - キーワードを実行して、失敗するか確かめる
    * - Run Keyword And Ignore Error
      - name, \*args
      - キーワードを実行して、エラーがあっても無視する
    * - Run Keyword And Return
      - name, \*args
      - キーワードを実行して戻り値を返す
    * - Run Keyword And Return If
      - condition, name, \*args
      - 条件に一致するときキーワードを実行して戻り値を返す
    * - Run Keyword And Return Status
      - name, \*args
      - キーワードを実行して成否を返す
    * - Run Keyword If
      - condition, name, \*args
      - 条件に一致するときキーワードを実行する
    * - Run Keyword If All Critical Tests Passed
      - name, \*args
      - クリティカルテストが全て成功しているときキーワードを実行する
    * - Run Keyword If All Tests Passed
      - name, \*args
      - テストが全て成功しているときキーワードを実行する
    * - Run Keyword If Any Critical Tests Failed
      - name, \*args
      - 失敗したクリティカルテストがあるときキーワードを実行する
    * - Run Keyword If Any Tests Failed
      - name, \*args
      - 失敗したテストがあるときキーワードを実行する
    * - Run Keyword If Test Failed
      - name, \*args
      - テストに失敗したときキーワードを実行する
    * - Run Keyword If Test Passed
      - name, \*args
      - テストが成功したときキーワードを実行する
    * - Run Keyword If Timeout Occurred
      - name, \*args
      - タイムアウトが起きたときキーワードを実行する
    * - Run Keyword Unless
      - condition, name, \*args
      - 条件に一致しないときキーワードを実行する
    * - Run Keywords
      - \*keywords
      - キーワードを実行する
    * - Set Global Variable
      - name, \*values
      - グローバルな変数を設定する
    * - Set Library Search Order
      - \*search_order
      - ライブラリやリソースからキーワードを探す順番を設定する
    * - Set Log Level
      - level
      - ログレベルを設定する
    * - Set Suite Documentation
      - doc, append=False, top=False
      - テストスイートのドキュメントを設定する
    * - Set Suite Metadata
      - name, value, append=False, top=False
      - テストスイートのメタデータを設定する
    * - Set Suite Variable
      - name, \*values
      - テストスイート単位の変数を設定する
    * - Set Tags
      - \*tags
      - タグを設定する
    * - Set Test Documentation
      - doc, append=False
      - テストのドキュメントを設定する
    * - Set Test Message
      - message, append=False
      - テスト実行時のメッセージを設定する
    * - Set Test Variable
      - name, \*values
      - テスト単位の変数を設定する
    * - Set Variable
      - \*values
      - 変数を設定する
    * - Set Variable If
      - condition, \*values
      - 条件に一致するとき変数を設定する
    * - Should Be Empty
      - item, msg=None
      - 空文字列であることを確認する
    * - Should Be Equal
      - first, second, msg=None, values=True
      - 値が等しいことを確認する
    * - Should Be Equal As Integers
      - first, second, msg=None, values=True, base=None
      - 整数に変換して等しいことを確認する
    * - Should Be Equal As Numbers
      - first, second, msg=None, values=True, precision=6
      - 数値に変換して値が等しいことを確認する
    * - Should Be Equal As Strings
      - first, second, msg=None, values=True
      - 文字列に変換して値が等しいことを確認する
    * - Should Be True
      - condition, msg=None
      - 値がTrueであることを確認する
    * - Should Contain
      - container, item, msg=None, values=True
      - 指定の要素を含んでいることを確認する
    * - Should Contain X Times
      - item1, item2, count, msg=None
      - 要素が X 回出現することを確認する
    * - Should End With
      - str1, str2, msg=None, values=True
      - 文字列の末尾が一致することを確認する
    * - Should Match
      - string, pattern, msg=None, values=True
      - 文字列がワイルドカードマッチすることを確認する
    * - Should Match Regexp
      - string, pattern, msg=None, values=True
      - 文字列が正規表現マッチすることを確認する
    * - Should Not Be Empty
      - item, msg=None
      - 空文字列でないことを確認する
    * - Should Not Be Equal
      - first, second, msg=None, values=True
      - 等しくないことを確認する
    * - Should Not Be Equal As Integers
      - first, second, msg=None, values=True, base=None
      - 整数に変換して等しくないことを確認する
    * - Should Not Be Equal As Numbers
      - first, second, msg=None, values=True, precision=6
      - 数値に変換して等しくないことを確認する
    * - Should Not Be Equal As Strings
      - first, second, msg=None, values=True
      - 文字列に変換して等しくないことを確認する
    * - Should Not Be True
      - condition, msg=None
      - 値が真でないことを確認する
    * - Should Not Contain
      - container, item, msg=None, values=True
      - 指定の要素が含まれないことを確認する
    * - Should Not End With
      - str1, str2, msg=None, values=True
      - 文字列の末尾が一致しないことを確認する
    * - Should Not Match
      - string, pattern, msg=None, values=True
      - 文字列がワイルドカードマッチしないことを検証する
    * - Should Not Match Regexp
      - string, pattern, msg=None, values=True
      - 文字列が正規表現マッチしないことを検証する
    * - Should Not Start With
      - str1, str2, msg=None, values=True
      - 文字列の先頭が一致しないことを確認する
    * - Should Start With
      - str1, str2, msg=None, values=True
      - 文字列の先頭が一致することを確認する
    * - Sleep
      - time\_, reason=None
      - 指定時間実行を停止する
    * - Variable Should Exist
      - name, msg=None
      - 変数が定義されていることを確認する
    * - Variable Should Not Exist
      - name, msg=None
      - 変数が定義されていないことを確認する
    * - Wait Until Keyword Succeeds
      - retry, retry_interval, name, \*args
      - キーワードの実行に成功するまでリトライ／待機する

Collections
------------
.. list-table::

    * - キーワード
      - 引数
      - 説明
    * - Append To List
      - list\_, \*values
      - リストに要素を追加する
    * - Combine Lists
      - \*lists
      - リストを結合する
    * - Convert To Dictionary
      - item
      - 辞書に変換する
    * - Convert To List
      - item
      - リストに変換する
    * - Copy Dictionary
      - dictionary
      - 辞書を複製する
    * - Copy List
      - list\_
      - リストを複製する
    * - Count Values In List
      - list\_, value, start=0, end=None
      - リストの要素を数える
    * - Dictionaries Should Be Equal
      - dict1, dict2, msg=None, values=True
      - 辞書が部分一致または全体一致することを確認する
    * - Dictionary Should Contain Item
      - dictionary, key, value, msg=None
      - 辞書に指定のキー／値が入っていることを確認する
    * - Dictionary Should Contain Key
      - dictionary, key, msg=None
      - 辞書に指定のキーがあることを確認する
    * - Dictionary Should Contain Sub Dictionary
      - dict1, dict2, msg=None, values=True
      - 辞書の要素が別の辞書のサブセットであることを確認する
    * - Dictionary Should Contain Value
      - dictionary, value, msg=None
      - 辞書に指定の値が入っていることを確認する
    * - Dictionary Should Not Contain Key
      - dictionary, key, msg=None
      - 辞書に指定のキーが入っていないことを確認する
    * - Dictionary Should Not Contain Value
      - dictionary, value, msg=None
      - 辞書に指定の値が入っていないことを確認する
    * - Get Dictionary Items
      - dictionary
      - 辞書のキー／値を取り出す
    * - Get Dictionary Keys
      - dictionary
      - 辞書のキーを取り出す
    * - Get Dictionary Values
      - dictionary
      - 辞書の値を取り出す
    * - Get From Dictionary
      - dictionary, key
      - 辞書から指定のキーに対応する値を取り出す
    * - Get From List
      - list\_, index
      - リストから指定のインデクスの値を取り出す
    * - Get Index From List
      - list\_, value, start=0, end=None
      - リスト中の指定の要素の出現インデクスを調べる
    * - Get Match Count
      - list, pattern, case_insensitive=False, whitespace_insensitive=False
      - リスト中の指定のパターンに一致する要素の個数を数える
    * - Get Matches
      - list, pattern, case_insensitive=False, whitespace_insensitive=False
      - リストから指定のパターンに一致する要素を抽出する
    * - Get Slice From List
      - list\_, start=0, end=None
      - リストのスライスを抽出する
    * - Insert Into List
      - list\_, index, value
      - リストに要素を挿入する
    * - Keep In Dictionary
      - dictionary, \*keys
      - 辞書から指定のキー以外のキー／値を除去する
    * - List Should Contain Sub List
      - list1, list2, msg=None, values=True
      - リストが指定のサブセットを含むことを確認する
    * - List Should Contain Value
      - list\_, value, msg=None
      - リストに指定の要素があることを確認する
    * - List Should Not Contain Duplicates
      - list\_, msg=None
      - リストに要素の重複がないことを確認する
    * - List Should Not Contain Value
      - list\_, value, msg=None
      - リストが指定の値を含まないことを確認する
    * - Lists Should Be Equal
      - list1, list2, msg=None, values=True, names=None
      - 二つのリストが一致することを確認する
    * - Log Dictionary
      - dictionary, level=INFO
      - 辞書の内容をログに記録する
    * - Log List
      - list\_, level=INFO
      - リストの内容をログに記録する
    * - Pop From Dictionary
      - dictionary, key, default=
      - 辞書から指定のキーの値を取り除いて返す
    * - Remove Duplicates
      - list\_
      - リスト中の重複する要素を除去する
    * - Remove From Dictionary
      - dictionary, \*keys
      - 辞書から指定のキーの値を除去する
    * - Remove From List
      - list\_, index
      - リストから指定インデクスの要素を除去する
    * - Remove Values From List
      - list\_, \*values
      - リストから指定の値を全て除去する
    * - Reverse List
      - list\_
      - リストを反転する
    * - Set List Value
      - list\_, index, value
      - リストの指定インデクスの値を差し替える
    * - Set To Dictionary
      - dictionary, \*key_value_pairs, \*\*items
      - 辞書にキー／値を指定する
    * - Should Contain Match
      - list, pattern, msg=None, case_insensitive=False, whitespace_insensitive=False
      - リスト中に指定パターンに一致する要素があることを確認する
    * - Should Not Contain Match
      - list, pattern, msg=None, case_insensitive=False, whitespace_insensitive=False
      - リスト中に指定パターンに一致する要素がないことを確認する
    * - Sort List
      - list\_
      - リストを並べ替える

DateTime
----------
.. list-table::

    * - キーワード
      - 引数
      - 説明
    * - Add Time To Date
      - date, time, result_format=timestamp, exclude_millis=False, date_format=None
      - 時間と時刻を加算する
    * - Add Time To Time
      - time1, time2, result_format=number, exclude_millis=False
      - 時間と時間を加算する
    * - Convert Date
      - date, result_format=timestamp, exclude_millis=False, date_format=None
      - 時刻を変換する
    * - Convert Time
      - time, result_format=number, exclude_millis=False
      - 時間を変換する
    * - Get Current Date
      - time\_zone=local, increment=0, result_format=timestamp, exclude_millis=False
      - 現在時刻を得る
    * - Subtract Date From Date
      - date1, date2, result_format=number, exclude_millis=False, date1_format=None, date2_format=None
      - 二つの時刻の差の時間を得る
    * - Subtract Time From Date
      - date, time, result_format=timestamp, exclude_millis=False, date_format=None
      - 時刻から時間を差し引く
    * - Subtract Time From Time
      - time1, time2, result_format=number, exclude_millis=False
      - 時間から時間を差し引く

Dialogs
---------
.. list-table::

    * - キーワード
      - 引数
      - 説明
    * - Execute Manual Step
      - message, default_error=
      - ユーザに PASS/FAIL を決めさせ、入力に従ってテストを成功・失敗させる
    * - Get Selection From User
      - message, \*values
      - ユーザに選択肢を提示し、回答を得る
    * - Get Value From User
      - message, default_value=, hidden=False
      - ユーザに値を入力させる
    * - Pause Execution
      - message=Test execution paused. Press OK to continue.
      - テストを一時停止して、ユーザに確認ボタンを押させる

OperatingSystem
-----------------
.. list-table::

    * - キーワード
      - 引数
      - 説明
    * - Append To Environment Variable
      - name, \*values, \*\*config
      - 環境変数に値を追加する
    * - Append To File
      - path, content, encoding=UTF-8
      - ファイルに書き込む
    * - Copy Directory
      - source, destination
      - ディレクトリをコピーする
    * - Copy File
      - source, destination
      - ファイルをコピーする
    * - Copy Files
      - \*sources_and_destination
      - 複数ファイルをコピーする
    * - Count Directories In Directory
      - path, pattern=None
      - ディレクトリ内のサブディレクトリの数を数える
    * - Count Files In Directory
      - path, pattern=None
      - ディレクトリ内のファイルの数を数える
    * - Count Items In Directory
      - path, pattern=None
      - ディレクトリ内の要素の数を数える
    * - Create Binary File
      - path, content
      - バイナリファイルを作成する
    * - Create Directory
      - path
      - ディレクトリを作成する
    * - Create File
      - path, content=, encoding=UTF-8
      - テキストファイルを作成する
    * - Directory Should Be Empty
      - path, msg=None
      - ディレクトリが空であることを確認する
    * - Directory Should Exist
      - path, msg=None
      - ディレクトリが存在することを確認する
    * - Directory Should Not Be Empty
      - path, msg=None
      - ディレクトリが空でないことを確認する
    * - Directory Should Not Exist
      - path, msg=None
      - ディレクトリが存在しないことを確認する
    * - Empty Directory
      - path
      - ディレクトリの中を空にする
    * - Environment Variable Should Be Set
      - name, msg=None
      - 環境変数が設定されていることを確認する
    * - Environment Variable Should Not Be Set
      - name, msg=None
      - 環境変数がセットされていないことを確認する
    * - File Should Be Empty
      - path, msg=None
      - ファイルが空であることを確認する
    * - File Should Exist
      - path, msg=None
      - ファイルが存在することを確認する
    * - File Should Not Be Empty
      - path, msg=None
      - ファイルが空でないことを確認する
    * - File Should Not Exist
      - path, msg=None
      - ファイルが存在しないことを確認する
    * - Get Binary File
      - path
      - バイナリファイルの中身を得る
    * - Get Environment Variable
      - name, default=None
      - 環境変数の値を得る
    * - Get Environment Variables
      -
      - 全ての環境変数を得る
    * - Get File
      - path, encoding=UTF-8, encoding_errors=strict
      - テキストファイルの中身を得る
    * - Get File Size
      - path
      - ファイルサイズを得る
    * - Get Modified Time
      - path, format=timestamp
      - ファイルの更新時刻を得る
    * - Grep File
      - path, pattern, encoding=UTF-8, encoding_errors=strict
      - ファイルに grep をかけて一致する行を取り出す
    * - Join Path
      - base, \*parts
      - パス要素を結合して一つのパスにする
    * - Join Paths
      - base, \*paths
      - パス要素をリストの各要素と結合して複数のパスを一挙に作成する
    * - List Directories In Directory
      - path, pattern=None, absolute=False
      - ディレクトリ内のサブディレクトリを列挙する
    * - List Directory
      - path, pattern=None, absolute=False
      - ディレクトリ内の要素を列挙する
    * - List Files In Directory
      - path, pattern=None, absolute=False
      - ディレクトリ内のファイルを列挙する
    * - Log Environment Variables
      - level=INFO
      - 全ての環境変数をログに書き込む
    * - Log File
      - path, encoding=UTF-8, encoding_errors=strict
      - ファイルの内容をログに書き込む
    * - Move Directory
      - source, destination
      - ディレクトリを移動する
    * - Move File
      - source, destination
      - ファイルを移動する
    * - Move Files
      - \*sources_and_destination
      - 複数のファイルを移動する
    * - Normalize Path
      - path
      - ファイルパスを正規化する
    * - Remove Directory
      - path, recursive=False
      - ディレクトリを削除する
    * - Remove Environment Variable
      - \*names
      - 環境変数を除去する
    * - Remove File
      - path
      - ファイルを削除する
    * - Remove Files
      - \*paths
      - 複数ファイルを削除する
    * - Run
      - command
      - コマンドを実行して標準出力を得る
    * - Run And Return Rc
      - command
      - コマンドを実行して終了コードを得る
    * - Run And Return Rc And Output
      - command
      - コマンドを実行して終了コードと標準出力を得る
    * - Set Environment Variable
      - name, value
      - 環境変数を設定する
    * - Set Modified Time
      - path, mtime
      - ファイルの最終更新時刻をセットする
    * - Should Exist
      - path, msg=None
      - ファイルやディレクトリが存在することを確認する
    * - Should Not Exist
      - path, msg=None
      - ファイルやディレクトリが存在しないことを確認する
    * - Split Extension
      - path
      - ファイル名を本体と拡張子に分ける
    * - Split Path
      - path
      - ファイルパスを末尾部分とそれ以外に分割する
    * - Touch
      - path
      - ファイルを touch する
    * - Wait Until Created
      - path, timeout=1 minute
      - ファイルやディレクトリが生成されるまで待機する
    * - Wait Until Removed
      - path, timeout=1 minute
      - ファイルやディレクトリが除去されるまで待機する

Process
---------
.. list-table::

    * - キーワード
      - 引数
      - 説明
    * - Get Process Id
      - handle=None
      - 子プロセスのIDを得る
    * - Get Process Object
      - handle=None
      - subprocess.Popen オブジェクトを得る
    * - Get Process Result
      - handle=None, rc=False, stdout=False, stderr=False, stdout_path=False, stderr_path=False
      - 子プロセスの実行結果を得る
    * - Is Process Running
      - handle=None
      - 子プロセスが実行中か調べる
    * - Join Command Line
      - \*args
      - コマンドラインを構築する
    * - Process Should Be Running
      - handle=None, error_message=Process is not running.
      - 子プロセスが実行中であることを確認する
    * - Process Should Be Stopped
      - handle=None, error_message=Process is running.
      - 子プロセスが停止したことを確認する
    * - Run Process
      - command, \*arguments, \*\*configuration
      - 子プロセスを実行する
    * - Send Signal To Process
      - signal, handle=None, group=False
      - 子プロセスにシグナルを送信する
    * - Split Command Line
      - args, escaping=False
      - コマンドラインを各引数に分割する
    * - Start Process
      - command, \*arguments, \*\*configuration
      - 子プロセスを開始する
    * - Switch Process
      - handle
      - 子プロセスを切り替える
    * - Terminate All Processes
      - kill=False
      - テストランナが起動した全ての子プロセスを終了する
    * - Terminate Process
      - handle=None, kill=False
      - 子プロセスを終了する
    * - Wait For Process
      - handle=None, timeout=None, on_timeout=continue
      - 子プロセスの終了を待機する


Screenshot
--------------------------
.. list-table::

    * - キーワード
      - 引数
      - 説明
    * - Set Screenshot Directory
      - path
      - スクリーンショットの保存ディレクトリを設定する
    * - Take Screenshot
      - name=screenshot, width=800px
      - スクリーンショットを撮る
    * - Take Screenshot Without Embedding
      - name=screenshot
      - スクリーンショットを撮るが、ログには表示しない

String
--------------------------
.. list-table::

    * - キーワード
      - 引数
      - 説明
    * - Convert To Lowercase
      - string
      - 小文字に変換する
    * - Convert To Uppercase
      - string
      - 大文字に変換する
    * - Decode Bytes To String
      - bytes, encoding, errors=strict
      - バイト列を文字列にデコードする
    * - Encode String To Bytes
      - string, encoding, errors=strict
      - 文字列をバイト列にエンコードする
    * - Fetch From Left
      - string, marker
      - 指定のマーカーが出現するまで左側から検索し、左側文字列を返す
    * - Fetch From Right
      - string, marker
      - 指定のマーカーが出現するまで右側から検索し、右側文字列を返す
    * - Generate Random String
      - length=8, chars=[LETTERS][NUMBERS]
      - ランダムな文字列を生成する
    * - Get Line
      - string, line_number
      - 指定行目の内容を得る
    * - Get Line Count
      - string
      - 行数を数える
    * - Get Lines Containing String
      - string, pattern, case_insensitive=False
      - 指定文字列を含む行を得る
    * - Get Lines Matching Pattern
      - string, pattern, case_insensitive=False
      - ワイルドカードマッチする行を得る
    * - Get Lines Matching Regexp
      - string, pattern, partial_match=False
      - 正規表現マッチする行を得る
    * - Get Regexp Matches
      - string, pattern, \*groups
      - 正規表現マッチのマッチグループを得る
    * - Get Substring
      - string, start, end=None
      - 部分文字列を得る
    * - Remove String
      - string, \*removables
      - 文字列から指定文字列を除去する
    * - Remove String Using Regexp
      - string, \*patterns
      - 文字列から正規表現マッチする文字列を除去する
    * - Replace String
      - string, search_for, replace_with, count=-1
      - 文字列を置換する
    * - Replace String Using Regexp
      - string, pattern, replace_with, count=-1
      - 文字列を正規表現置換する
    * - Should Be Byte String
      - item, msg=None
      - バイト列であることを確認する
    * - Should Be Lowercase
      - string, msg=None
      - 全て小文字であることを確認する
    * - Should Be String
      - item, msg=None
      - 全て文字列であることを確認する
    * - Should Be Titlecase
      - string, msg=None
      - 全てタイトルケースであることを確認する
    * - Should Be Unicode String
      - item, msg=None
      - バイト列でないことを確認する
    * - Should Be Uppercase
      - string, msg=None
      - 全て大文字であることを確認する
    * - Should Not Be String
      - item, msg=None
      - 文字列でないことを確認する
    * - Split String
      - string, separator=None, max_split=-1
      - 文字列を指定のセパレータで分割する
    * - Split String From Right
      - string, separator=None, max_split=-1
      - 文字列を末尾から探索し、最初のセパレータ出現位置で分割する
    * - Split String To Characters
      - string
      - 文字列を一文字づつに分割する
    * - Split To Lines
      - string, start=0, end=None
      - 文字列を行に分割する
    * - Strip String
      - string, mode=both, characters=None
      - 文字列の前後の余分な文字をはぎ取る

Telnet
--------------------------
.. list-table::

    * - キーワード
      - 引数
      - 説明
    * - Close All Connections
      -
      - 全ての接続を閉じる
    * - Close Connection
      - loglevel=None
      - 接続を閉じる
    * - Execute Command
      - command, loglevel=None, strip_prompt=False
      - コマンドを実行する
    * - Login
      - username, password, login_prompt=login: , password_prompt=Password: , login_timeout=1 second, login_incorrect=Login incorrect
      - シェルログインする
    * - Open Connection
      - host, alias=None, port=23, timeout=None, newline=None, prompt=None, prompt_is_regexp=False, encoding=None, encoding_errors=None, default_log_level=None, window_size=None, environ_user=None, terminal_emulation=None, terminal_type=None, telnetlib_log_level=None, connection_timeout=None
      - 接続を開く
    * - Read
      - loglevel=None
      - データを読みだす
    * - Read Until
      - expected, loglevel=None
      - 指定文字列が出現するまで読み出す
    * - Read Until Prompt
      - loglevel=None, strip_prompt=False
      - プロンプトが出現するまで読み出す
    * - Read Until Regexp
      - \*expected
      - 正規表現マッチするまで読み出す
    * - Set Default Log Level
      - level
      - デフォルトのログレベルを設定する
    * - Set Encoding
      - encoding=None, errors=None
      - エンコーディングをセットする
    * - Set Newline
      - newline
      - 改行文字をセットする
    * - Set Prompt
      - prompt, prompt_is_regexp=False
      - プロンプトをセットする
    * - Set Telnetlib Log Level
      - level
      - telnetlib のログレベルをセットする
    * - Set Timeout
      - timeout
      - タイムアウトをセットする
    * - Switch Connection
      - index_or_alias
      - 接続を切り替える
    * - Write
      - text, loglevel=None
      - 改行つきで書き込む
    * - Write Bare
      - text
      - 改行を追加せず書き込む
    * - Write Control Character
      - character
      - 制御文字を書き込む
    * - Write Until Expected Output
      - text, expected, timeout, retry_interval, loglevel=None
      - 指定の応答を得るまで繰り返し書き込む

XML
--------------------------
.. list-table::

    * - キーワード
      - 引数
      - 説明
    * - Add Element
      - source, element, index=None, xpath=.
      - エレメントを追加する
    * - Clear Element
      - source, xpath=., clear_tail=False
      - エレメントを除去する
    * - Copy Element
      - source, xpath=.
      - エレメントを追加する
    * - Element Attribute Should Be
      - source, name, expected, xpath=., message=None
      - エレメントの属性が指定値であることを確認する
    * - Element Attribute Should Match
      - source, name, pattern, xpath=., message=None
      - エレメントの属性が指定パターンにマッチすることを確認する
    * - Element Should Exist
      - source, xpath=., message=None
      - エレメントが存在することを確認する
    * - Element Should Not Exist
      - source, xpath=., message=None
      - エレメントが存在しないことを確認する
    * - Element Should Not Have Attribute
      - source, name, xpath=., message=None
      - エレメントが指定属性を持たないことを確認する
    * - Element Text Should Be
      - source, expected, xpath=., normalize_whitespace=False, message=None
      - エレメントのテキストが指定値であることを確認する
    * - Element Text Should Match
      - source, pattern, xpath=., normalize_whitespace=False, message=None
      - エレメントのテキストが指定パターンにマッチすることを確認する
    * - Element To String
      - source, xpath=., encoding=None
      - エレメントを文字列に変換する
    * - Elements Should Be Equal
      - source, expected, exclude_children=False, normalize_whitespace=False
      - エレメントが一致することを確認する
    * - Elements Should Match
      - source, expected, exclude_children=False, normalize_whitespace=False
      - エレメントがパターンに一致することを確認する
    * - Evaluate Xpath
      - source, expression, context=.
      - Xpath を評価する
    * - Get Child Elements
      - source, xpath=.
      - 子エレメントを得る
    * - Get Element
      - source, xpath=.
      - エレメントを得る
    * - Get Element Attribute
      - source, name, xpath=., default=None
      - エレメントの指定属性の値を得る
    * - Get Element Attributes
      - source, xpath=.
      - エレメントの全ての属性値を得る
    * - Get Element Count
      - source, xpath=.
      - エレメントの数を数える
    * - Get Element Text
      - source, xpath=., normalize_whitespace=False
      - エレメントのテキストを得る
    * - Get Elements
      - source, xpath
      - XPath に一致する全エレメントを得る
    * - Get Elements Texts
      - source, xpath, normalize_whitespace=False
      - XPath に一致する全エレメントのテキストを得る
    * - Log Element
      - source, level=INFO, xpath=.
      - エレメントをログに出力する
    * - Parse Xml
      - source, keep_clark_notation=False
      - XML を解析する
    * - Remove Element
      - source, xpath=, remove_tail=False
      - エレメントを除去する
    * - Remove Element Attribute
      - source, name, xpath=.
      - エレメントの指定の属性を除去する
    * - Remove Element Attributes
      - source, xpath=.
      - エレメントの全属性を除去する
    * - Remove Elements
      - source, xpath=, remove_tail=False
      - エレメントを除去する
    * - Remove Elements Attribute
      - source, name, xpath=.
      - XPath に一致する全エレメントの指定の属性を除去する
    * - Remove Elements Attributes
      - source, xpath=.
      - XPath に一致する全エレメントの全属性を除去する
    * - Save Xml
      - source, path, encoding=UTF-8
      - XML を書き出す
    * - Set Element Attribute
      - source, name, value, xpath=.
      - エレメントの属性を設定する
    * - Set Element Tag
      - source, tag, xpath=.
      - エレメントのタグを設定する
    * - Set Element Text
      - source, text=None, tail=None, xpath=.
      - エレメントのテキストを設定する
    * - Set Elements Attribute
      - source, name, value, xpath=.
      - XPath に一致する全エレメントの属性を設定する
    * - Set Elements Tag
      - source, tag, xpath=.
      - XPath に一致するエレメントのタグを設定する
    * - Set Elements Text
      - source, text=None, tail=None, xpath=.
      - XPath に一致するエレメントのテキストを設定する

        
外部ライブラリ
==============


.. AppiumLibrary
  ---------------
  .. list-table::

    * - キーワード
      - 引数
      - 説明
    * - Background App
      - seconds=5
      - 
    * - Capture Page Screenshot
      - filename=None
      - 
    * - Clear Text
      - locator
      - 
    * - Click A Point
      - x=0, y=0
      - 
    * - Click Button
      - index_or_name
      - 
    * - Click Element
      - locator
      - 
    * - Close All Applications
      -
      - 
    * - Close Application
      -
      - 
    * - Element Attribute Should Match
      - locator, attr_name, match_pattern, regexp=False
      - 
    * - Element Name Should Be
      - locator, expected
      - 
    * - Element Should Be Disabled
      - locator, loglevel=INFO
      - 
    * - Element Should Be Enabled
      - locator, loglevel=INFO
      - 
    * - Element Value Should Be
      - locator, expected
      - 
    * - Get Appium Timeout
      -
      - 
    * - Get Contexts
      -
      - 
    * - Get Current Context
      -
      - 
    * - Get Element Attribute
      - locator, attribute
      - 
    * - Get Element Location
      - locator
      - 
    * - Get Element Size
      - locator
      - 
    * - Get Elements
      - locator, first_element_only=False, fail_on_error=True
      - 
    * - Get Network Connection Status
      -
      - 
    * - Get Source
      -
      - 
    * - Go Back
      -
      - 
    * - Go To Url
      - url
      - 
    * - Hide Keyboard
      - key_name=None
      - 
    * - Input Password
      - locator, text
      - 
    * - Input Text
      - locator, text
      - 
    * - Input Value
      - locator, text
      - 
    * - Landscape
      -
      - 
    * - Lock
      -
      - 
    * - Log Source
      - loglevel=INFO
      - 
    * - Long Press
      - locator
      - 
    * - Long Press Keycode
      - keycode, metastate=None
      - 
    * - Open Application
      - remote_url, alias=None, \*\*kwargs
      - 
    * - Page Should Contain Element
      - locator, loglevel=INFO
      - 
    * - Page Should Contain Text
      - text, loglevel=INFO
      - 
    * - Page Should Not Contain Element
      - locator, loglevel=INFO
      - 
    * - Page Should Not Contain Text
      - text, loglevel=INFO
      - 
    * - Pinch
      - locator, percent=200%, steps=1
      - 
    * - Portrait
      -
      - 
    * - Press Keycode
      - keycode, metastate=None
      - 
    * - Pull File
      - path, decode=False
      - 
    * - Pull Folder
      - path, decode=False
      - 
    * - Push File
      - path, data, encode=False
      - 
    * - Register Keyword To Run On Failure
      - keyword
      - 
    * - Remove Application
      - application_id
      - 
    * - Reset Application
      -
      - 
    * - Scroll
      - start_locator, end_locator
      - 
    * - Scroll To
      - locator
      - 
    * - Set Appium Timeout
      - seconds
      - 
    * - Set Network Connection Status
      - connectionStatus
      - 
    * - Shake
      -
      - 
    * - Swipe
      - start_x, start_y, end_x, end_y, duration=1000
      - 
    * - Switch Application
      - index_or_alias
      - 
    * - Switch To Context
      - context_name
      - 
    * - Tap
      - locator
      - 
    * - Wait Until Page Contains
      - text, timeout=None, error=None
      - 
    * - Wait Until Page Contains Element
      - locator, timeout=None, error=None
      - 
    * - Wait Until Page Does Not Contain
      - text, timeout=None, error=None
      - 
    * - Wait Until Page Does Not Contain Element
      - locator, timeout=None, error=None
      - 
    * - Zoom
      - locator, percent=200%, steps=1
      - 

ArchiveLibrary
----------------
.. list-table::

    * - キーワード
      - 引数
      - 説明
    * - Archive Should Contain File
      - zfile, filename
      - アーカイブに指定ファイル名があることを確認する
    * - Create Tar From Files In Directory
      - directory, filename
      - 指定ディレクトリ内のファイルを tar する
    * - Create Zip From Files In Directory
      - directory, filename
      - 指定ディレクトリ内のファイルを zip する
    * - Extract Tar File
      - tfile, dest=None
      - tar ファイルを展開する
    * - Extract Zip File
      - zfile, dest=None
      - zip ファイルを展開する

DatabaseLibrary
-----------------
.. list-table::

    * - キーワード
      - 引数
      - 説明
    * - Check If Exists In Database
      - selectStatement
      - SELECT 文を実行し、応答行があることを確認する
    * - Check If Not Exists In Database
      - selectStatement
      - SELECT 文を実行し、応答行がないことを確認する
    * - Connect To Database
      - dbapiModuleName=None, dbName=None, dbUsername=None, dbPassword=None, dbHost=localhost, dbPort=5432, dbConfigFile=./resources/db.cfg
      - データベースに接続する
    * - Connect To Database Using Custom Params
      - dbapiModuleName=None, db_connect_string=
      - DB-APIごとのカスタムパラメタを使ってデーターベースに接続する
    * - Delete All Rows From Table
      - tableName
      - テーブルの全ての行を除去する
    * - Description
      - selectStatement
      - クエリの返す応答のカラム情報を得る
    * - Disconnect From Database
      -
      - データベースへの接続を解除する
    * - Execute Sql Script
      - sqlScriptFileName
      - 任意の SQL スクリプトを実行する
    * - Execute Sql String
      - sqlString
      - 任意の SQL 文を実行する
    * - Query
      - selectStatement
      - SELECT 文を実行し、応答を行のリストで得る
    * - Row Count
      - selectStatement
      - SELECT 文を実行し、応答行数を得る
    * - Row Count Is 0
      - selectStatement
      - SELECT 文を実行し、応答行数がゼロであることを確認する
    * - Row Count Is Equal To X
      - selectStatement, numRows
      - SELECT 文を実行し、応答行数が指定行数であることを確認する
    * - Row Count Is Greater Than X
      - selectStatement, numRows
      - SELECT 文を実行し、応答行数が指定より多いいことを確認する
    * - Row Count Is Less Than X
      - selectStatement, numRows
      - SELECT 文を実行し、応答行数が指定より少ないことを確認する
    * - Table Must Exist
      - tableName
      - 指定のテーブルが存在することを確認する

FtpLibrary
-------------------------
.. list-table::

    * - キーワード
      - 引数
      - 説明
    * - Cwd
      - directory, connId=default
      - ディレクトリを移動する
    * - Delete
      - targetFile, connId=default
      - ファイルを削除する
    * - Dir
      - connId=default
      - ディレクトリ一覧を得る
    * - Download File
      - remoteFileName, localFilePath=None, connId=default
      - ファイルをダウンロードする
    * - Ftp Close
      - connId=default
      - FTP接続を閉じる
    * - Ftp Connect
      - host, user=anonymous, password=anonymous@, port=21, timeout=30, connId=default
      - FTP接続を開く
    * - Get All Ftp Connections
      -
      - 全てのFTP接続を閉じる
    * - Get Welcome
      - connId=default
      - ウェルカムメッセージを得る
    * - Mkd
      - newDirName, connId=default
      - ディレクトリを作成する
    * - Pwd
      - connId=default
      - 現在のディレクトリを得る
    * - Rename
      - targetFile, newName, connId=default
      - ファイル名を変更する
    * - Rmd
      - directory, connId=default
      - ディレクトリを削除する
    * - Send Cmd
      - command, connId=default
      - FTPコマンドを送信する
    * - Size
      - fileToCheck, connId=default
      - ファイルサイズを調べる
    * - Upload File
      - localFileName, remoteFileName=None, connId=default
      - ファイルをアップロードする

.. HttpLibrary
  -------------------------
  .. list-table::

    * - キーワード
      - 引数
      - 説明
    * - B 64 Encode
      - s, altchars=None
      - Base64 エンコードする
    * - Load Json
      - json_string
      - JSON
    * - Urlparse
      - url, scheme=, allow_fragments=True
      - 
    * - Wraps
      - wrapped, assigned=('__module__', '__name__', '__doc__'), updated=('__dict__',)
      - 

MQTTLibrary
-------------------------
.. list-table::

    * - キーワード
      - 引数
      - 説明
    * - Connect
      - broker, port=1883, client_id=, clean_session=True
      - ブローカに接続する
    * - Disconnect
      -
      - ブローカとの接続を切る
    * - Publish
      - topic, message=None, qos=0, retain=False
      - メッセージを publish する
    * - Publish Multiple
      - msgs, hostname=localhost, port=1883, client_id=, keepalive=60, will=None, auth=None, tls=None, protocol=3
      - 複数のメッセージを publish して接続を切る
    * - Publish Single
      - topic, payload=None, qos=0, retain=False, hostname=localhost, port=1883, client_id=, keepalive=60, will=None, auth=None, tls=None, protocol=3
      - 単一のメッセージを publish して接続を切る
    * - Set Username And Password
      - username, password=None
      - ユーザ名とパスワードをセットする
    * - Subscribe
      - topic, qos, timeout=1, limit=1
      - 指定トピックを subscribe し、一定時間内に受信したメッセージを得る
    * - Subscribe And Validate
      - topic, qos, payload, timeout=1
      - 指定トピックを subscribe し、指定ペイロードの受信を確認する
    * - Unsubscribe
      - topic
      - 指定トピックの subscribe を終了する

Rammbock
-------------------------
.. list-table::

    * - キーワード
      - 引数
      - 説明
    * - Accept Connection
      - name=None, alias=None
      - サーバへの接続を受け入れる
    * - Array
      - size, type, name, \*parameters
      - 新たなアレイタイプを定義する
    * - Bin
      - size, name, value=None
      - テンプレートに2進フィールドを追加する
    * - Bin To Hex
      - bin_value
      - 2進から16進に変換する
    * - Case
      - size, kw, \*parameters
      - バッグデータのエレメントを追加する
    * - Chars
      - length, name, value=None, terminator=None
      - テンプレートに文字列アレイを追加する
    * - Clear Message Streams
      -
      - 入力メッセージストリームをリセットする
    * - Client Receives Binary
      - name=None, timeout=None, label=None
      - バイナリメッセージを受信する
    * - Client Receives Message
      - \*parameters
      - テンプレートに従ってメッセージを受信し、検証する
    * - Client Receives Without Validation
      - \*parameters
      - テンプレートに従ってメッセージを受信する
    * - Client Sends Binary
      - message, name=None, label=None
      - バイナリメッセージを送信する
    * - Client Sends Message
      - \*parameters
      - メッセージを送信する
    * - Conditional
      - condition, name
      - 条件付きエレメントの定義を開始する
    * - Connect
      - host, port, name=None
      - クライアントに接続する
    * - Container
      - name, length, type, \*parameters
      - コンテナを定義する
    * - Embed Seqdiag Sequence
      -
      - シーケンスダイアグラムを生成してログファイルに保存する
    * - End Bag
      -
      - バッグデータの定義を終了する
    * - End Binary Container
      -
      - バイナリコンテナの定義を終了する
    * - End Conditional
      -
      - 条件付きエレメントの
    * - End Protocol
      -
      - プロトコルの定義を終了する
    * - End Struct
      -
      - ストラクトの定義を終了する
    * - End Tbcd Container
      -
      - TBCDコンテナの定義を終了する
    * - End Union
      -
      - ユニオンの定義を終了する
    * - Get Client Protocol
      - name=None
      - クライアントプロトコルを得る
    * - Get Client Unread Messages Count
      - client_name=None
      - クライアントから未受信のメッセージを数える
    * - Get Message
      - \*parameters
      - エンコード済みのメッセージを得る
    * - Get Server Unread Messages Count
      - server_name=None
      - サーバから未受信のメッセージを得る
    * - Hex To Bin
      - hex_value
      - 16進を2進に変換する
    * - I 32
      - name, value=None, align=None
      - テンプレートに32ビット整数フィールドを追加する
    * - I 8
      - name, value=None, align=None
      - テンプレートに8ビット整数フィールドを追加する
    * - Int
      - length, name, value=None, align=None
      - テンプレートに指定長の符号付き整数フィールドを追加する
    * - Load Copy Of Template
      - name, \*parameters
      - テンプレートのコピーをロードする
    * - Load Template
      - name, \*parameters
      - テンプレートをロードする
    * - Log Handler Messages
      -
      - ハンドラメッセージをログに記録する
    * - New Binary Container
      - name
      - 新たなバイナリコンテナを生成する
    * - New Message
      - message_name, protocol=None, \*parameters
      - 新たなメッセージを生成する
    * - New Protocol
      - protocol_name
      - 新たなプロトコルを生成する
    * - New Struct
      - type, name, \*parameters
      - 新たなストラクトを生成する
    * - New Tbcd Container
      - name
      - 新たなTBCDコンテナを生成する
    * - New Union
      - type, name
      - 新たなユニオンを生成する
    * - Pdu
      - length
      - PDUを定義する
    * - Reset Handler Messages
      -
      -
    * - Reset Rammbock
      -
      - Rammbock をリセットする
    * - Save Template
      - name, unlocked=False
      - テンプレートを保存する
    * - Server Receives Binary
      - name=None, timeout=None, connection=None, label=None
      - バイナリメッセージを受信する
    * - Server Receives Binary From
      - name=None, timeout=None, connection=None, label=None
      - バイナリメッセージをを受信し、IPとポート情報つきで返す
    * - Server Receives Message
      - \*parameters
      - メッセージを受信し、検証する
    * - Server Receives Without Validation
      - \*parameters
      - メッセージを受信する
    * - Server Sends Binary
      - message, name=None, connection=None, label=None
      - バイナリメッセージを送信する
    * - Server Sends Message
      - \*parameters
      - メッセージを送信する
    * - Set Client Handler
      - handler_func, name=None, header_filter=None, interval=0.5
      - クライアントアンドラを設定する
    * - Set Server Handler
      - handler_func, name=None, header_filter=None, alias=None, interval=0.5
      - サーバハンドラを設定する
    * - Start Bag
      - name
      - バッグの定義を開始する
    * - Start Sctp Client
      - ip=None, port=None, name=None, timeout=None, protocol=None, family=ipv4
      - SCTPクライアントを開始する
    * - Start Sctp Server
      - ip, port, name=None, timeout=None, protocol=None, family=ipv4
      - SCTPサーバを開始する
    * - Start Tcp Client
      - ip=None, port=None, name=None, timeout=None, protocol=None, family=ipv4
      - TCPクライアントを開始する
    * - Start Tcp Server
      - ip, port, name=None, timeout=None, protocol=None, family=ipv4
      - TCPサーバを開始する
    * - Start Udp Client
      - ip=None, port=None, name=None, timeout=None, protocol=None, family=ipv4
      - UDPクライアントを開始する
    * - Start Udp Server
      - ip, port, name=None, timeout=None, protocol=None, family=ipv4
      - UDPサーバを開始する
    * - Tbcd
      - size, name, value=None
      - TBCDコンテナ定義を開始する
    * - U 128
      - name, value=None, align=None
      - テンプレートに符号なし128ビット整数フィールドを追加する
    * - U 16
      - name, value=None, align=None
      - テンプレートに符号なし16ビット整数フィールドを追加する
    * - U 24
      - name, value=None, align=None
      - テンプレートに符号なしビット整数フィールドを追加する
    * - U 32
      - name, value=None, align=None
      - テンプレートに符号なし32ビット整数フィールドを追加する
    * - U 40
      - name, value=None, align=None
      - テンプレートに符号なし40ビット整数フィールドを追加する
    * - U 64
      - name, value=None, align=None
      - テンプレートに符号なし64ビット整数フィールドを追加する
    * - U 8
      - name, value=None, align=None
      - テンプレートに符号なし8ビット整数フィールドを追加する
    * - Uint
      - length, name, value=None, align=None
      - テンプレートに符号なし整数フィールドを追加する
    * - Validate Message
      - msg, \*parameters
      - メッセージを検証する
    * - Value
      - name, value
      - フィールドのデフォルト値を定義する

Selenium2Library
-------------------------
.. list-table::


    * - キーワード
      - 引数
      - 説明
    * - Add Cookie
      - name, value, path=None, domain=None, secure=None, expiry=None
      - クッキーを追加する
    * - Add Location Strategy
      - strategy_name, strategy_keyword, persist=False
      - 自作のエレメント特定方法を追加する
    * - Alert Should Be Present
      - text=
      - アラートが表示されたことを確認する
    * - Assign Id To Element
      - locator, id
      - エレメントに一時的な id を割り当てる
    * - Capture Page Screenshot
      - filename=None
      - ページのスクリーンショットを取る
    * - Checkbox Should Be Selected
      - locator
      - チェックボックスが選択されていることを確認する
    * - Checkbox Should Not Be Selected
      - locator
      - チェックボックスが非選択であることを確認する
    * - Choose Cancel On Next Confirmation
      -
      - 次に表示されるダイアログでキャンセルを押す
    * - Choose File
      - locator, file_path
      - ファイルダイアログにファイルを指定する
    * - Choose Ok On Next Confirmation
      -
      - 次に表示されるダイアログでOKを押す
    * - Clear Element Text
      - locator
      - テキスト入力の値をクリアする
    * - Click Button
      - locator
      - ボタンをクリックする
    * - Click Element
      - locator
      - 任意のエレメントをクリックする
    * - Click Element At Coordinates
      - locator, xoffset, yoffset
      - エレメントの指定の場所をクリックする
    * - Click Image
      - locator
      - 画像をクリックする
    * - Click Link
      - locator
      - リンクをクリックする
    * - Close All Browsers
      -
      - 全てのブラウザを閉じる
    * - Close Browser
      -
      - 現在のブラウザを閉じる
    * - Close Window
      -
      - ポップアップウィンドウを閉じる
    * - Confirm Action
      -
      - ダイアログのメッセージを取得して閉じる
    * - Create Webdriver
      - driver_name, alias=None, kwargs={}, \*\*init_kwargs
      - WebDriverインスタンスを生成する
    * - Current Frame Contains
      - text, loglevel=INFO
      - 現在のフレームに指定文字列があることを確認する
    * - Current Frame Should Not Contain
      - text, loglevel=INFO
      - 現在のフレームが指定文字列を含まないことを確認する
    * - Delete All Cookies
      -
      - 全てのクッキーを削除する
    * - Delete Cookie
      - name
      - 指定のクッキーを削除する
    * - Dismiss Alert
      - accept=True
      - アラートダイアログを閉じて押されたボタンを返す
    * - Double Click Element
      - locator
      - 任意のエレメントをダブルクリックする
    * - Drag And Drop
      - source, target
      - エレメントを別のエレメントにドラッグ＆ドロップする
    * - Drag And Drop By Offset
      - source, xoffset, yoffset
      - エレメントを指定の場所にドラッグ＆ドロップする
    * - Element Should Be Disabled
      - locator
      - エレメントが無効であることを確認する
    * - Element Should Be Enabled
      - locator
      - エレメントが有効であることを確認する
    * - Element Should Be Visible
      - locator, message=
      - エレメントが可視であることを確認する
    * - Element Should Contain
      - locator, expected, message=
      - エレメントのテキストに指定文字列があることを確認する
    * - Element Should Not Be Visible
      - locator, message=
      - エレメントが不可視であることを確認する
    * - Element Should Not Contain
      - locator, expected, message=
      - エレメントのテキストが指定文字列が含まないことを確認する
    * - Element Text Should Be
      - locator, expected, message=
      - エレメントのテキストが指定文字列と一致することを確認する
    * - Execute Async Javascript
      - \*code
      - 非同期でJavaScriptのコードを実行する
    * - Execute Javascript
      - \*code
      - JavaScriptのコードを実行する
    * - Focus
      - locator
      - ウィンドウやフレームをフォーカスする
    * - Frame Should Contain
      - locator, text, loglevel=INFO
      - フレームに指定文字列があることを確認する
    * - Get Alert Message
      - dismiss=True
      - アラートダイアログのメッセージを調べる
    * - Get All Links
      -
      - ページ中の全てのリンクを調べる 
    * - Get Cookie Value
      - name
      - クッキーの値を調べる
    * - Get Cookies
      -
      - クッキーを全て取り出す
    * - Get Element Attribute
      - attribute_locator
      - エレメントの属性を調べる
    * - Get Horizontal Position
      - locator
      - エレメントの水平位置を調べる
    * - Get List Items
      - locator
      - selectの全選択肢を取り出す
    * - Get Location
      -
      - 現在のURLを調べる
    * - Get Matching Xpath Count
      - xpath
      - 指定のXPathにマッチした回数を調べる
    * - Get Selected List Label
      - locator
      - selectの指定の選択肢のラベルを調べる
    * - Get Selected List Labels
      - locator
      - selectの全てのラベルを取り出す
    * - Get Selected List Value
      - locator
      - selectの指定の選択肢のvalueを調べる
    * - Get Selected List Values
      - locator
      - selectのすべての選択肢のvalueを調べる
    * - Get Selenium Implicit Wait
      -
      - Selenium の暗黙の待機時間を調べる
    * - Get Selenium Speed
      -
      - Selenium の実行ウェイトを調べる
    * - Get Selenium Timeout
      -
      - Selenium のタイムアウトを調べる
    * - Get Source
      -
      - ページのソースを調べる
    * - Get Table Cell
      - table_locator, row, column, loglevel=INFO
      - テーブルの指定のセルの中身を調べる
    * - Get Text
      - locator
      - エレメントのテキストを調べる
    * - Get Title
      -
      - ページのタイトルを調べる
    * - Get Value
      - locator
      - エレメントのvalueを調べる
    * - Get Vertical Position
      - locator
      - エレメントの垂直位置を調べる
    * - Get Webelement
      - locator
      - エレメントを WebElement として取り出す
    * - Get Webelements
      - locator
      - ページの全エレメントを WebElement として取り出す
    * - Get Window Identifiers
      -
      - 開いている全ウィンドウの識別子を調べる
    * - Get Window Names
      -
      - 開いている全ウィンドウのウィンドウ名を調べる
    * - Get Window Position
      -
      - ウィンドウの位置を調べる
    * - Get Window Size
      -
      - ウィンドウのサイズを調べる 
    * - Get Window Titles
      -
      - ウィンドウのタイトルを調べる
    * - Go Back
      -
      - ひとつ前のURLに戻る
    * - Go To
      - url
      - URLを指定する
    * - Input Password
      - locator, text
      - ログに記録しないでパスワードを入力する
    * - Input Text
      - locator, text
      - アラートダイアログにテキストを入力する
    * - Input Text Into Prompt
      - text
      - テキスト入力に入力する
    * - List Selection Should Be
      - locator, \*items
      - selectの選択内容が指定通りか確認する
    * - List Should Have No Selections
      - locator
      - selectが非選択状態であることを確認する
    * - List Windows
      -
      - ウィンドウのリストを取り出す
    * - Location Should Be
      - url
      - URLが指定通りか確認する
    * - Location Should Contain
      - expected
      - URLに指定の値が含まれるか確認する
    * - Locator Should Match X Times
      - locator, expected_locator_count, message=, loglevel=INFO
      - エレメントが指定個数入っているか書くにする
    * - Log Location
      -
      - 現在のURLをログに記録する
    * - Log Source
      - loglevel=INFO
      - ページのソースをログに記録する
    * - Log Title
      -
      - ページのタイトルをログに記録する
    * - Maximize Browser Window
      -
      - ブラウザウィンドウを最大化する
    * - Mouse Down
      - locator
      - 画像上で左ボタンを押した状態にする
    * - Mouse Down On Image
      - locator
      - リンク上で左ボタンを押した状態にする
    * - Mouse Down On Link
      - locator
      - エレメント上で左ボタンを押した状態にする
    * - Mouse Out
      - locator
      - エレメントからマウスカーソルを外す
    * - Mouse Over
      - locator
      - エレメントにマウスカーソルを重ねる
    * - Mouse Up
      - locator
      - 押していた左ボタンをリリースする
    * - Open Browser
      - url, browser=firefox, alias=None, remote_url=False, desired_capabilities=None, ff_profile_dir=None
      - 新しくブラウザウィンドウを開く
    * - Open Context Menu
      - locator
      - コンテキストメニューを開く
    * - Page Should Contain
      - text, loglevel=INFO
      - ページが指定文字列を含むことを確認する
    * - Page Should Contain Button
      - locator, message=, loglevel=INFO
      - ページに指定のボタンがあることを確認する
    * - Page Should Contain Checkbox
      - locator, message=, loglevel=INFO
      - ページに指定のチェックボックスがあることを確認する
    * - Page Should Contain Element
      - locator, message=, loglevel=INFO
      - ページに指定のエレメントがあることを確認する
    * - Page Should Contain Image
      - locator, message=, loglevel=INFO
      - ページに指定の画像があることを確認する
    * - Page Should Contain Link
      - locator, message=, loglevel=INFO
      - ページに指定のリンクがあることを確認する
    * - Page Should Contain List
      - locator, message=, loglevel=INFO
      - ページに指定のリストがあることを確認する
    * - Page Should Contain Radio Button
      - locator, message=, loglevel=INFO
      - ページに指定のラジオボタンがあることを確認する
    * - Page Should Contain Textfield
      - locator, message=, loglevel=INFO
      - ページに指定のテキスト入力があることを確認する
    * - Page Should Not Contain
      - text, loglevel=INFO
      - ページに指定の文字列がないことを確認する
    * - Page Should Not Contain Button
      - locator, message=, loglevel=INFO
      - ページに指定のボタンがないことを確認する
    * - Page Should Not Contain Checkbox
      - locator, message=, loglevel=INFO
      - ページに指定のチェックボックスがないことを確認する
    * - Page Should Not Contain Element
      - locator, message=, loglevel=INFO
      - ページに指定のエレメントがないことを確認する
    * - Page Should Not Contain Image
      - locator, message=, loglevel=INFO
      - ページに指定の画像がないことを確認する
    * - Page Should Not Contain Link
      - locator, message=, loglevel=INFO
      - ページに指定のリンクがないことを確認する
    * - Page Should Not Contain List
      - locator, message=, loglevel=INFO
      - ページに指定のリストがないことを確認する
    * - Page Should Not Contain Radio Button
      - locator, message=, loglevel=INFO
      - ページに指定のラジオボタンがないことを確認する
    * - Page Should Not Contain Textfield
      - locator, message=, loglevel=INFO
      - 指定のテキスト入力がないことを確認する
    * - Press Key
      - locator, key
      - キーを押す
    * - Radio Button Should Be Set To
      - group_name, value
      - 指定のラジオボタンが選ばれていることを確認する
    * - Radio Button Should Not Be Selected
      - group_name
      - 指定のラジオボタンが選ばれていないことを確認する
    * - Register Keyword To Run On Failure
      - keyword
      - 失敗したときに実行するキーワードを指定する
    * - Reload Page
      -
      - ページをリロードする
    * - Remove Location Strategy
      - strategy_name
      - 以前登録したエレメントの探索ストラテジを削除する
    * - Select All From List
      - locator
      - selectの全項目を選択する
    * - Select Checkbox
      - locator
      - チェックボックスを選択する
    * - Select Frame
      - locator
      - フレームを切り替える
    * - Select From List
      - locator, \*items
      - selectの項目を選択する
    * - Select From List By Index
      - locator, \*indexes
      - インデクス指定でselectの項目を選択する
    * - Select From List By Label
      - locator, \*labels
      - ラベル指定でselectの項目を選択する
    * - Select From List By Value
      - locator, \*values
      - 値指定でselectの項目を選択する
    * - Select Radio Button
      - group_name, value
      - ラジオボタンを選択する
    * - Select Window
      - locator=None
      - ウィンドウを切り替える
    * - Set Browser Implicit Wait
      - seconds
      - ブラウザ単位で暗黙待機時間を変更する
    * - Set Screenshot Directory
      - path, persist=False
      - スクリーンショットの出力先を変更する
    * - Set Selenium Implicit Wait
      - seconds
      - Selenium の暗黙待機時間を変更する
    * - Set Selenium Speed
      - seconds
      - Selenium の実行ウェイトを変更する
    * - Set Selenium Timeout
      - seconds
      - Selenium のタイムアウトを変更する
    * - Set Window Position
      - x, y
      - ウィンドウ位置を変更する
    * - Set Window Size
      - width, height
      - ウィンドウサイズを変更する
    * - Simulate
      - locator, event
      - イベント発生をシミュレートする
    * - Submit Form
      - locator=None
      - フォームを submit する
    * - Switch Browser
      - index_or_alias
      - ブラウザを切り替える
    * - Table Cell Should Contain
      - table_locator, row, column, expected, loglevel=INFO
      - テーブルのセルが指定の文字列を含むことを確認する
    * - Table Column Should Contain
      - table_locator, col, expected, loglevel=INFO
      - テーブルのカラムが指定の文字列を含むことを確認する
    * - Table Footer Should Contain
      - table_locator, expected, loglevel=INFO
      - テーブルのフッタが指定の文字列を含むことを確認する
    * - Table Header Should Contain
      - table_locator, expected, loglevel=INFO
      - テーブルのヘッダが指定の文字列を含むことを確認する
    * - Table Row Should Contain
      - table_locator, row, expected, loglevel=INFO
      - テーブルの行が指定の文字列を含むことを確認する
    * - Table Should Contain
      - table_locator, expected, loglevel=INFO
      - テーブルが指定の文字列を含むことを確認する
    * - Textarea Should Contain
      - locator, expected, message=
      - テキストエリアのテキストが指定の文字列を含むことを確認する
    * - Textarea Value Should Be
      - locator, expected, message=
      - テキストエリアの値が指定通りであることを確認する
    * - Textfield Should Contain
      - locator, expected, message=
      - テキストフィールドのテキストが指定の文字列を含むことを確認する
    * - Textfield Value Should Be
      - locator, expected, message=
      - テキストフィールドのvalueが指定通りであることを確認する
    * - Title Should Be
      - title
      - タイトルが指定通りであることを確認する
    * - Unselect Checkbox
      - locator
      - チェックボックスの選択を解除する
    * - Unselect Frame
      -
      - フレームの選択を解除する
    * - Unselect From List
      - locator, \*items
      - リストから指定の要素の選択を外す
    * - Unselect From List By Index
      - locator, \*indexes
      - インデクス指定でリストから指定の要素の選択を外す
    * - Unselect From List By Label
      - locator, \*labels
      - ラベル指定でリストから指定の要素の選択を外す
    * - Unselect From List By Value
      - locator, \*values
      - 値指定でリストから指定の要素の選択を外す
    * - Wait For Condition
      - condition, timeout=None, error=None
      - 指定の条件が満たされるまで待機する
    * - Wait Until Element Contains
      - locator, text, timeout=None, error=None
      - エレメント内に指定文字列が現れるまで待機する
    * - Wait Until Element Does Not Contain
      - locator, text, timeout=None, error=None
      - 指定文字列がエレメントからなくなるまで待機する
    * - Wait Until Element Is Enabled
      - locator, timeout=None, error=None
      - エレメントが有効状態になるまで待機する
    * - Wait Until Element Is Not Visible
      - locator, timeout=None, error=None
      - エレメントが不可視になるまで待機する
    * - Wait Until Element Is Visible
      - locator, timeout=None, error=None
      - エレメントが可視になるまで待機する
    * - Wait Until Page Contains
      - text, timeout=None, error=None
      - エレメントがページに現れるまで待機する
    * - Wait Until Page Contains Element
      - locator, timeout=None, error=None
      - 文字列がページに現れるまで待機する
    * - Wait Until Page Does Not Contain
      - text, timeout=None, error=None
      - エレメントがページからなくなるまで待機する
    * - Wait Until Page Does Not Contain Element
      - locator, timeout=None, error=None
      - 文字列がページからなくなるまで待機する
    * - Xpath Should Match X Times
      - xpath, expected_xpath_count, message=, loglevel=INFO
      - XPathにマッチするエレメントの個数が指定通りであることを確認する

SSHLibrary
-------------------------
.. list-table::

    * - キーワード
      - 引数
      - 説明
    * - Close All Connections
      -
      - 全ての接続を切る 
    * - Close Connection
      -
      - 接続を切る
    * - Directory Should Exist
      - path
      - リモートディレクトリが存在することを確認する
    * - Directory Should Not Exist
      - path
      - リモートディレクトリが存在しないことを確認する
    * - Enable Ssh Logging
      - logfile
      - SSHプロトコル出力のログ記録を有効にする
    * - Execute Command
      - command, return_stdout=True, return_stderr=False, return_rc=False
      - リモートホストでコマンドを実行する
    * - File Should Exist
      - path
      - リモートファイルが存在することを確認する
    * - File Should Not Exist
      - path
      - リモートファイルが存在しないことを確認する
    * - Get Connection
      - index_or_alias=None, index=False, host=False, alias=False, port=False, timeout=False, newline=False, prompt=False, term_type=False, width=False, height=False, encoding=False
      - 使用中の接続の情報を得る
    * - Get Connections
      -
      - 全ての接続の情報を得る
    * - Get Directory
      - source, destination=., recursive=False
      - ディレクトリを取得する
    * - Get File
      - source, destination=.
      - ファイルを取得する
    * - List Directories In Directory
      - path, pattern=None, absolute=False
      - ディレクトリ中のサブディレクトリを列挙する
    * - List Directory
      - path, pattern=None, absolute=False
      - ディレクトリ中の内容を列挙する
    * - List Files In Directory
      - path, pattern=None, absolute=False
      - ディレクトリ中のファイルを列挙する
    * - Login
      - username, password, delay=0.5 seconds
      - パスワード指定でログインする
    * - Login With Public Key
      - username, keyfile, password=, delay=0.5 seconds
      - 公開鍵指定でログインする
    * - Open Connection
      - host, alias=None, port=22, timeout=None, newline=None, prompt=None, term_type=None, width=None, height=None, path_separator=None, encoding=None
      - SSH接続を開く
    * - Put Directory
      - source, destination=., mode=0744, newline=, recursive=False
      - ディレクトリを送信する
    * - Put File
      - source, destination=., mode=0744, newline=
      - ファイルを送信する
    * - Read
      - loglevel=None, delay=None
      - リモート接続から読み出す
    * - Read Command Output
      - return_stdout=True, return_stderr=False, return_rc=False
      - コマンドの出力を読み出す
    * - Read Until
      - expected, loglevel=None
      - 指定文字列が出現するまで読み出す
    * - Read Until Prompt
      - loglevel=None
      - プロンプトに到達するまで読み出す
    * - Read Until Regexp
      - regexp, loglevel=None
      - 指定の正規表現にマッチするまで読み出す
    * - Set Client Configuration
      - timeout=None, newline=None, prompt=None, term_type=None, width=None, height=None, path_separator=None, encoding=None
      - クライアントの設定を変更する
    * - Set Default Configuration
      - timeout=None, newline=None, prompt=None, loglevel=None, term_type=None, width=None, height=None, path_separator=None, encoding=None
      - デフォルトの設定を変更する
    * - Start Command
      - command
      - リモートでコマンドの実行を開始し、終了を待たずに処理を戻す
    * - Switch Connection
      - index_or_alias
      - 接続を切り替える
    * - Write
      - text, loglevel=None
      - 改行を付加して書き込む
    * - Write Bare
      - text
      - 改行を付加せず書き込む
    * - Write Until Expected Output
      - text, expected, timeout, retry_interval, loglevel=None
      - 指定の応答を得るまで繰り返し書き込む

