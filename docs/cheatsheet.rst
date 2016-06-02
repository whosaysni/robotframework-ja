================================
Robot Framework チートシート
================================

標準ライブラリ
======================


BuiltIn
--------------------------
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
      - 条件付きでループをスキップする
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
      - 条件付きでループを抜ける
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
      - format=timestamp, time_=NOW
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
      - 条件付きでテストの実行を飛ばす
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
      - 条件付きでキーワードの実行から抜ける
    * - Run Keyword
      - name, \*args
      - キーワードを実行する
    * - Run Keyword And Continue On Failure
      - name, \*args
      - キーワードを実行して、失敗しても継続する
    * - Run Keyword And Expect Error
      - expected_error, name, \*args
      - 
    * - Run Keyword And Ignore Error
      - name, \*args
      - 
    * - Run Keyword And Return
      - name, \*args
      - 
    * - Run Keyword And Return If
      - condition, name, \*args
      - 
    * - Run Keyword And Return Status
      - name, \*args
      - 
    * - Run Keyword If
      - condition, name, \*args
      - 
    * - Run Keyword If All Critical Tests Passed
      - name, \*args
      - 
    * - Run Keyword If All Tests Passed
      - name, \*args
      - 
    * - Run Keyword If Any Critical Tests Failed
      - name, \*args
      - 
    * - Run Keyword If Any Tests Failed
      - name, \*args
      - 
    * - Run Keyword If Test Failed
      - name, \*args
      - 
    * - Run Keyword If Test Passed
      - name, \*args
      - 
    * - Run Keyword If Timeout Occurred
      - name, \*args
      - 
    * - Run Keyword Unless
      - condition, name, \*args
      - 
    * - Run Keywords
      - \*keywords
      - 
    * - Set Global Variable
      - name, \*values
      - 
    * - Set Library Search Order
      - \*search_order
      - 
    * - Set Log Level
      - level
      - 
    * - Set Suite Documentation
      - doc, append=False, top=False
      - 
    * - Set Suite Metadata
      - name, value, append=False, top=False
      - 
    * - Set Suite Variable
      - name, \*values
      - 
    * - Set Tags
      - \*tags
      - 
    * - Set Test Documentation
      - doc, append=False
      - 
    * - Set Test Message
      - message, append=False
      - 
    * - Set Test Variable
      - name, \*values
      - 
    * - Set Variable
      - \*values
      - 
    * - Set Variable If
      - condition, \*values
      - 
    * - Should Be Empty
      - item, msg=None
      - 
    * - Should Be Equal
      - first, second, msg=None, values=True
      - 
    * - Should Be Equal As Integers
      - first, second, msg=None, values=True, base=None
      - 
    * - Should Be Equal As Numbers
      - first, second, msg=None, values=True, precision=6
      - 
    * - Should Be Equal As Strings
      - first, second, msg=None, values=True
      - 
    * - Should Be True
      - condition, msg=None
      - 
    * - Should Contain
      - container, item, msg=None, values=True
      - 
    * - Should Contain X Times
      - item1, item2, count, msg=None
      - 
    * - Should End With
      - str1, str2, msg=None, values=True
      - 
    * - Should Match
      - string, pattern, msg=None, values=True
      - 
    * - Should Match Regexp
      - string, pattern, msg=None, values=True
      - 
    * - Should Not Be Empty
      - item, msg=None
      - 
    * - Should Not Be Equal
      - first, second, msg=None, values=True
      - 
    * - Should Not Be Equal As Integers
      - first, second, msg=None, values=True, base=None
      - 
    * - Should Not Be Equal As Numbers
      - first, second, msg=None, values=True, precision=6
      - 
    * - Should Not Be Equal As Strings
      - first, second, msg=None, values=True
      - 
    * - Should Not Be True
      - condition, msg=None
      - 
    * - Should Not Contain
      - container, item, msg=None, values=True
      - 
    * - Should Not End With
      - str1, str2, msg=None, values=True
      - 
    * - Should Not Match
      - string, pattern, msg=None, values=True
      - 
    * - Should Not Match Regexp
      - string, pattern, msg=None, values=True
      - 
    * - Should Not Start With
      - str1, str2, msg=None, values=True
      - 
    * - Should Start With
      - str1, str2, msg=None, values=True
      - 
    * - Sleep
      - time_, reason=None
      - 
    * - Variable Should Exist
      - name, msg=None
      - 
    * - Variable Should Not Exist
      - name, msg=None
      - 
    * - Wait Until Keyword Succeeds
      - retry, retry_interval, name, \*args
      - 

Collections
--------------------------
.. list-table::

    * - キーワード
      - 引数
      - 説明
    * - Append To List
      - list_, \*values
      - 
    * - Combine Lists
      - \*lists
      - 
    * - Convert To Dictionary
      - item
      - 
    * - Convert To List
      - item
      - 
    * - Copy Dictionary
      - dictionary
      - 
    * - Copy List
      - list_
      - 
    * - Count Values In List
      - list_, value, start=0, end=None
      - 
    * - Dictionaries Should Be Equal
      - dict1, dict2, msg=None, values=True
      - 
    * - Dictionary Should Contain Item
      - dictionary, key, value, msg=None
      - 
    * - Dictionary Should Contain Key
      - dictionary, key, msg=None
      - 
    * - Dictionary Should Contain Sub Dictionary
      - dict1, dict2, msg=None, values=True
      - 
    * - Dictionary Should Contain Value
      - dictionary, value, msg=None
      - 
    * - Dictionary Should Not Contain Key
      - dictionary, key, msg=None
      - 
    * - Dictionary Should Not Contain Value
      - dictionary, value, msg=None
      - 
    * - Get Dictionary Items
      - dictionary
      - 
    * - Get Dictionary Keys
      - dictionary
      - 
    * - Get Dictionary Values
      - dictionary
      - 
    * - Get From Dictionary
      - dictionary, key
      - 
    * - Get From List
      - list_, index
      - 
    * - Get Index From List
      - list_, value, start=0, end=None
      - 
    * - Get Match Count
      - list, pattern, case_insensitive=False, whitespace_insensitive=False
      - 
    * - Get Matches
      - list, pattern, case_insensitive=False, whitespace_insensitive=False
      - 
    * - Get Slice From List
      - list_, start=0, end=None
      - 
    * - Insert Into List
      - list_, index, value
      - 
    * - Keep In Dictionary
      - dictionary, \*keys
      - 
    * - List Should Contain Sub List
      - list1, list2, msg=None, values=True
      - 
    * - List Should Contain Value
      - list_, value, msg=None
      - 
    * - List Should Not Contain Duplicates
      - list_, msg=None
      - 
    * - List Should Not Contain Value
      - list_, value, msg=None
      - 
    * - Lists Should Be Equal
      - list1, list2, msg=None, values=True, names=None
      - 
    * - Log Dictionary
      - dictionary, level=INFO
      - 
    * - Log List
      - list_, level=INFO
      - 
    * - Pop From Dictionary
      - dictionary, key, default=
      - 
    * - Remove Duplicates
      - list_
      - 
    * - Remove From Dictionary
      - dictionary, \*keys
      - 
    * - Remove From List
      - list_, index
      - 
    * - Remove Values From List
      - list_, \*values
      - 
    * - Reverse List
      - list_
      - 
    * - Set List Value
      - list_, index, value
      - 
    * - Set To Dictionary
      - dictionary, \*key_value_pairs, \*\*items
      - 
    * - Should Contain Match
      - list, pattern, msg=None, case_insensitive=False, whitespace_insensitive=False
      - 
    * - Should Not Contain Match
      - list, pattern, msg=None, case_insensitive=False, whitespace_insensitive=False
      - 
    * - Sort List
      - list_
      - 

DateTime
--------------------------
.. list-table::

    * - キーワード
      - 引数
      - 説明
    * - Add Time To Date
      - date, time, result_format=timestamp, exclude_millis=False, date_format=None
      - 
    * - Add Time To Time
      - time1, time2, result_format=number, exclude_millis=False
      - 
    * - Convert Date
      - date, result_format=timestamp, exclude_millis=False, date_format=None
      - 
    * - Convert Time
      - time, result_format=number, exclude_millis=False
      - 
    * - Get Current Date
      - time_zone=local, increment=0, result_format=timestamp, exclude_millis=False
      - 
    * - Subtract Date From Date
      - date1, date2, result_format=number, exclude_millis=False, date1_format=None, date2_format=None
      - 
    * - Subtract Time From Date
      - date, time, result_format=timestamp, exclude_millis=False, date_format=None
      - 
    * - Subtract Time From Time
      - time1, time2, result_format=number, exclude_millis=False
      - 

Dialogs
--------------------------
.. list-table::

    * - キーワード
      - 引数
      - 説明
    * - Execute Manual Step
      - message, default_error=
      - 
    * - Get Selection From User
      - message, \*values
      - 
    * - Get Value From User
      - message, default_value=, hidden=False
      - 
    * - Pause Execution
      - message=Test execution paused. Press OK to continue.
      - 

Easter
--------------------------
.. list-table::

    * - キーワード
      - 引数
      - 説明
    * - None Shall Pass
      - who
      - 

OperatingSystem
--------------------------
.. list-table::

    * - キーワード
      - 引数
      - 説明
    * - Append To Environment Variable
      - name, \*values, \*\*config
      - 
    * - Append To File
      - path, content, encoding=UTF-8
      - 
    * - Copy Directory
      - source, destination
      - 
    * - Copy File
      - source, destination
      - 
    * - Copy Files
      - \*sources_and_destination
      - 
    * - Count Directories In Directory
      - path, pattern=None
      - 
    * - Count Files In Directory
      - path, pattern=None
      - 
    * - Count Items In Directory
      - path, pattern=None
      - 
    * - Create Binary File
      - path, content
      - 
    * - Create Directory
      - path
      - 
    * - Create File
      - path, content=, encoding=UTF-8
      - 
    * - Directory Should Be Empty
      - path, msg=None
      - 
    * - Directory Should Exist
      - path, msg=None
      - 
    * - Directory Should Not Be Empty
      - path, msg=None
      - 
    * - Directory Should Not Exist
      - path, msg=None
      - 
    * - Empty Directory
      - path
      - 
    * - Environment Variable Should Be Set
      - name, msg=None
      - 
    * - Environment Variable Should Not Be Set
      - name, msg=None
      - 
    * - File Should Be Empty
      - path, msg=None
      - 
    * - File Should Exist
      - path, msg=None
      - 
    * - File Should Not Be Empty
      - path, msg=None
      - 
    * - File Should Not Exist
      - path, msg=None
      - 
    * - Get Binary File
      - path
      - 
    * - Get Environment Variable
      - name, default=None
      - 
    * - Get Environment Variables
      -
      - 
    * - Get File
      - path, encoding=UTF-8, encoding_errors=strict
      - 
    * - Get File Size
      - path
      - 
    * - Get Modified Time
      - path, format=timestamp
      - 
    * - Grep File
      - path, pattern, encoding=UTF-8, encoding_errors=strict
      - 
    * - Join Path
      - base, \*parts
      - 
    * - Join Paths
      - base, \*paths
      - 
    * - List Directories In Directory
      - path, pattern=None, absolute=False
      - 
    * - List Directory
      - path, pattern=None, absolute=False
      - 
    * - List Files In Directory
      - path, pattern=None, absolute=False
      - 
    * - Log Environment Variables
      - level=INFO
      - 
    * - Log File
      - path, encoding=UTF-8, encoding_errors=strict
      - 
    * - Move Directory
      - source, destination
      - 
    * - Move File
      - source, destination
      - 
    * - Move Files
      - \*sources_and_destination
      - 
    * - Normalize Path
      - path
      - 
    * - Remove Directory
      - path, recursive=False
      - 
    * - Remove Environment Variable
      - \*names
      - 
    * - Remove File
      - path
      - 
    * - Remove Files
      - \*paths
      - 
    * - Run
      - command
      - 
    * - Run And Return Rc
      - command
      - 
    * - Run And Return Rc And Output
      - command
      - 
    * - Set Environment Variable
      - name, value
      - 
    * - Set Modified Time
      - path, mtime
      - 
    * - Should Exist
      - path, msg=None
      - 
    * - Should Not Exist
      - path, msg=None
      - 
    * - Split Extension
      - path
      - 
    * - Split Path
      - path
      - 
    * - Touch
      - path
      - 
    * - Wait Until Created
      - path, timeout=1 minute
      - 
    * - Wait Until Removed
      - path, timeout=1 minute
      - 

Process
--------------------------
.. list-table::

    * - キーワード
      - 引数
      - 説明
    * - Get Process Id
      - handle=None
      - 
    * - Get Process Object
      - handle=None
      - 
    * - Get Process Result
      - handle=None, rc=False, stdout=False, stderr=False, stdout_path=False, stderr_path=False
      - 
    * - Is Process Running
      - handle=None
      - 
    * - Join Command Line
      - \*args
      - 
    * - Process Should Be Running
      - handle=None, error_message=Process is not running.
      - 
    * - Process Should Be Stopped
      - handle=None, error_message=Process is running.
      - 
    * - Run Process
      - command, \*arguments, \*\*configuration
      - 
    * - Send Signal To Process
      - signal, handle=None, group=False
      - 
    * - Split Command Line
      - args, escaping=False
      - 
    * - Start Process
      - command, \*arguments, \*\*configuration
      - 
    * - Switch Process
      - handle
      - 
    * - Terminate All Processes
      - kill=False
      - 
    * - Terminate Process
      - handle=None, kill=False
      - 
    * - Wait For Process
      - handle=None, timeout=None, on_timeout=continue
      - 

Remote
--------------------------
Getting keyword names from library 'Remote' failed: Calling dynamic method 'get_keyword_names' failed: Connecting remote server at http://127.0.0.1:8270 failed: [Errno 61] Connection refused

Try --help for usage information.

Reserved
--------------------------
.. list-table::

    * - キーワード
      - 引数
      - 説明
    * - Break
      - \*varargs
      - 
    * - Continue
      - \*varargs
      - 
    * - Elif
      - \*varargs
      - 
    * - Else
      - \*varargs
      - 
    * - Else If
      - \*varargs
      - 
    * - End
      - \*varargs
      - 
    * - For
      - \*varargs
      - 
    * - If
      - \*varargs
      - 
    * - Return
      - \*varargs
      - 
    * - While
      - \*varargs
      - 

Screenshot
--------------------------
.. list-table::

    * - キーワード
      - 引数
      - 説明
    * - Set Screenshot Directory
      - path
      - 
    * - Take Screenshot
      - name=screenshot, width=800px
      - 
    * - Take Screenshot Without Embedding
      - name=screenshot
      - 

String
--------------------------
.. list-table::

    * - キーワード
      - 引数
      - 説明
    * - Convert To Lowercase
      - string
      - 
    * - Convert To Uppercase
      - string
      - 
    * - Decode Bytes To String
      - bytes, encoding, errors=strict
      - 
    * - Encode String To Bytes
      - string, encoding, errors=strict
      - 
    * - Fetch From Left
      - string, marker
      - 
    * - Fetch From Right
      - string, marker
      - 
    * - Generate Random String
      - length=8, chars=[LETTERS][NUMBERS]
      - 
    * - Get Line
      - string, line_number
      - 
    * - Get Line Count
      - string
      - 
    * - Get Lines Containing String
      - string, pattern, case_insensitive=False
      - 
    * - Get Lines Matching Pattern
      - string, pattern, case_insensitive=False
      - 
    * - Get Lines Matching Regexp
      - string, pattern, partial_match=False
      - 
    * - Get Regexp Matches
      - string, pattern, \*groups
      - 
    * - Get Substring
      - string, start, end=None
      - 
    * - Remove String
      - string, \*removables
      - 
    * - Remove String Using Regexp
      - string, \*patterns
      - 
    * - Replace String
      - string, search_for, replace_with, count=-1
      - 
    * - Replace String Using Regexp
      - string, pattern, replace_with, count=-1
      - 
    * - Should Be Byte String
      - item, msg=None
      - 
    * - Should Be Lowercase
      - string, msg=None
      - 
    * - Should Be String
      - item, msg=None
      - 
    * - Should Be Titlecase
      - string, msg=None
      - 
    * - Should Be Unicode String
      - item, msg=None
      - 
    * - Should Be Uppercase
      - string, msg=None
      - 
    * - Should Not Be String
      - item, msg=None
      - 
    * - Split String
      - string, separator=None, max_split=-1
      - 
    * - Split String From Right
      - string, separator=None, max_split=-1
      - 
    * - Split String To Characters
      - string
      - 
    * - Split To Lines
      - string, start=0, end=None
      - 
    * - Strip String
      - string, mode=both, characters=None
      - 

Telnet
--------------------------
.. list-table::

    * - キーワード
      - 引数
      - 説明
    * - Close All Connections
      -
      - 
    * - Close Connection
      - loglevel=None
      - 
    * - Execute Command
      - command, loglevel=None, strip_prompt=False
      - 
    * - Login
      - username, password, login_prompt=login: , password_prompt=Password: , login_timeout=1 second, login_incorrect=Login incorrect
      - 
    * - Open Connection
      - host, alias=None, port=23, timeout=None, newline=None, prompt=None, prompt_is_regexp=False, encoding=None, encoding_errors=None, default_log_level=None, window_size=None, environ_user=None, terminal_emulation=None, terminal_type=None, telnetlib_log_level=None, connection_timeout=None
      - 
    * - Read
      - loglevel=None
      - 
    * - Read Until
      - expected, loglevel=None
      - 
    * - Read Until Prompt
      - loglevel=None, strip_prompt=False
      - 
    * - Read Until Regexp
      - \*expected
      - 
    * - Set Default Log Level
      - level
      - 
    * - Set Encoding
      - encoding=None, errors=None
      - 
    * - Set Newline
      - newline
      - 
    * - Set Prompt
      - prompt, prompt_is_regexp=False
      - 
    * - Set Telnetlib Log Level
      - level
      - 
    * - Set Timeout
      - timeout
      - 
    * - Switch Connection
      - index_or_alias
      - 
    * - Write
      - text, loglevel=None
      - 
    * - Write Bare
      - text
      - 
    * - Write Control Character
      - character
      - 
    * - Write Until Expected Output
      - text, expected, timeout, retry_interval, loglevel=None
      - 

XML
--------------------------
.. list-table::

    * - キーワード
      - 引数
      - 説明
    * - Add Element
      - source, element, index=None, xpath=.
      - 
    * - Clear Element
      - source, xpath=., clear_tail=False
      - 
    * - Copy Element
      - source, xpath=.
      - 
    * - Element Attribute Should Be
      - source, name, expected, xpath=., message=None
      - 
    * - Element Attribute Should Match
      - source, name, pattern, xpath=., message=None
      - 
    * - Element Should Exist
      - source, xpath=., message=None
      - 
    * - Element Should Not Exist
      - source, xpath=., message=None
      - 
    * - Element Should Not Have Attribute
      - source, name, xpath=., message=None
      - 
    * - Element Text Should Be
      - source, expected, xpath=., normalize_whitespace=False, message=None
      - 
    * - Element Text Should Match
      - source, pattern, xpath=., normalize_whitespace=False, message=None
      - 
    * - Element To String
      - source, xpath=., encoding=None
      - 
    * - Elements Should Be Equal
      - source, expected, exclude_children=False, normalize_whitespace=False
      - 
    * - Elements Should Match
      - source, expected, exclude_children=False, normalize_whitespace=False
      - 
    * - Evaluate Xpath
      - source, expression, context=.
      - 
    * - Get Child Elements
      - source, xpath=.
      - 
    * - Get Element
      - source, xpath=.
      - 
    * - Get Element Attribute
      - source, name, xpath=., default=None
      - 
    * - Get Element Attributes
      - source, xpath=.
      - 
    * - Get Element Count
      - source, xpath=.
      - 
    * - Get Element Text
      - source, xpath=., normalize_whitespace=False
      - 
    * - Get Elements
      - source, xpath
      - 
    * - Get Elements Texts
      - source, xpath, normalize_whitespace=False
      - 
    * - Log Element
      - source, level=INFO, xpath=.
      - 
    * - Parse Xml
      - source, keep_clark_notation=False
      - 
    * - Remove Element
      - source, xpath=, remove_tail=False
      - 
    * - Remove Element Attribute
      - source, name, xpath=.
      - 
    * - Remove Element Attributes
      - source, xpath=.
      - 
    * - Remove Elements
      - source, xpath=, remove_tail=False
      - 
    * - Remove Elements Attribute
      - source, name, xpath=.
      - 
    * - Remove Elements Attributes
      - source, xpath=.
      - 
    * - Save Xml
      - source, path, encoding=UTF-8
      - 
    * - Set Element Attribute
      - source, name, value, xpath=.
      - 
    * - Set Element Tag
      - source, tag, xpath=.
      - 
    * - Set Element Text
      - source, text=None, tail=None, xpath=.
      - 
    * - Set Elements Attribute
      - source, name, value, xpath=.
      - 
    * - Set Elements Tag
      - source, tag, xpath=.
      - 
    * - Set Elements Text
      - source, text=None, tail=None, xpath=.
      - 

外部ライブラリ
===========================


AppiumLibrary
-------------------------
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
-------------------------
.. list-table::

    * - キーワード
      - 引数
      - 説明
    * - Archive Should Contain File
      - zfile, filename
      - 
    * - Create Tar From Files In Directory
      - directory, filename
      - 
    * - Create Zip From Files In Directory
      - directory, filename
      - 
    * - Extract Tar File
      - tfile, dest=None
      - 
    * - Extract Zip File
      - zfile, dest=None
      - 

DatabaseLibrary
-------------------------
.. list-table::

    * - キーワード
      - 引数
      - 説明
    * - Check If Exists In Database
      - selectStatement
      - 
    * - Check If Not Exists In Database
      - selectStatement
      - 
    * - Connect To Database
      - dbapiModuleName=None, dbName=None, dbUsername=None, dbPassword=None, dbHost=localhost, dbPort=5432, dbConfigFile=./resources/db.cfg
      - 
    * - Connect To Database Using Custom Params
      - dbapiModuleName=None, db_connect_string=
      - 
    * - Delete All Rows From Table
      - tableName
      - 
    * - Description
      - selectStatement
      - 
    * - Disconnect From Database
      -
      - 
    * - Execute Sql Script
      - sqlScriptFileName
      - 
    * - Execute Sql String
      - sqlString
      - 
    * - Query
      - selectStatement
      - 
    * - Row Count
      - selectStatement
      - 
    * - Row Count Is 0
      - selectStatement
      - 
    * - Row Count Is Equal To X
      - selectStatement, numRows
      - 
    * - Row Count Is Greater Than X
      - selectStatement, numRows
      - 
    * - Row Count Is Less Than X
      - selectStatement, numRows
      - 
    * - Table Must Exist
      - tableName
      - 

FtpLibrary
-------------------------
.. list-table::

    * - キーワード
      - 引数
      - 説明
    * - Cwd
      - directory, connId=default
      - 
    * - Delete
      - targetFile, connId=default
      - 
    * - Dir
      - connId=default
      - 
    * - Download File
      - remoteFileName, localFilePath=None, connId=default
      - 
    * - Ftp Close
      - connId=default
      - 
    * - Ftp Connect
      - host, user=anonymous, password=anonymous@, port=21, timeout=30, connId=default
      - 
    * - Get All Ftp Connections
      -
      - 
    * - Get Welcome
      - connId=default
      - 
    * - Mkd
      - newDirName, connId=default
      - 
    * - Pwd
      - connId=default
      - 
    * - Rename
      - targetFile, newName, connId=default
      - 
    * - Rmd
      - directory, connId=default
      - 
    * - Send Cmd
      - command, connId=default
      - 
    * - Size
      - fileToCheck, connId=default
      - 
    * - Upload File
      - localFileName, remoteFileName=None, connId=default
      - 

HttpLibrary
-------------------------
.. list-table::

    * - キーワード
      - 引数
      - 説明
    * - B 64 Encode
      - s, altchars=None
      - 
    * - Load Json
      - json_string
      - 
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
      - 
    * - Disconnect
      -
      - 
    * - Publish
      - topic, message=None, qos=0, retain=False
      - 
    * - Publish Multiple
      - msgs, hostname=localhost, port=1883, client_id=, keepalive=60, will=None, auth=None, tls=None, protocol=3
      - 
    * - Publish Single
      - topic, payload=None, qos=0, retain=False, hostname=localhost, port=1883, client_id=, keepalive=60, will=None, auth=None, tls=None, protocol=3
      - 
    * - Set Username And Password
      - username, password=None
      - 
    * - Subscribe
      - topic, qos, timeout=1, limit=1
      - 
    * - Subscribe And Validate
      - topic, qos, payload, timeout=1
      - 
    * - Unsubscribe
      - topic
      - 

Rammbock
-------------------------
.. list-table::

    * - キーワード
      - 引数
      - 説明
    * - Accept Connection
      - name=None, alias=None
      - 
    * - Array
      - size, type, name, \*parameters
      - 
    * - Bin
      - size, name, value=None
      - 
    * - Bin To Hex
      - bin_value
      - 
    * - Case
      - size, kw, \*parameters
      - 
    * - Chars
      - length, name, value=None, terminator=None
      - 
    * - Clear Message Streams
      -
      - 
    * - Client Receives Binary
      - name=None, timeout=None, label=None
      - 
    * - Client Receives Message
      - \*parameters
      - 
    * - Client Receives Without Validation
      - \*parameters
      - 
    * - Client Sends Binary
      - message, name=None, label=None
      - 
    * - Client Sends Message
      - \*parameters
      - 
    * - Conditional
      - condition, name
      - 
    * - Connect
      - host, port, name=None
      - 
    * - Container
      - name, length, type, \*parameters
      - 
    * - Embed Seqdiag Sequence
      -
      - 
    * - End Bag
      -
      - 
    * - End Binary Container
      -
      - 
    * - End Conditional
      -
      - 
    * - End Protocol
      -
      - 
    * - End Struct
      -
      - 
    * - End Tbcd Container
      -
      - 
    * - End Union
      -
      - 
    * - Get Client Protocol
      - name=None
      - 
    * - Get Client Unread Messages Count
      - client_name=None
      - 
    * - Get Message
      - \*parameters
      - 
    * - Get Server Unread Messages Count
      - server_name=None
      - 
    * - Hex To Bin
      - hex_value
      - 
    * - I 32
      - name, value=None, align=None
      - 
    * - I 8
      - name, value=None, align=None
      - 
    * - Int
      - length, name, value=None, align=None
      - 
    * - Load Copy Of Template
      - name, \*parameters
      - 
    * - Load Template
      - name, \*parameters
      - 
    * - Log Handler Messages
      -
      - 
    * - New Binary Container
      - name
      - 
    * - New Message
      - message_name, protocol=None, \*parameters
      - 
    * - New Protocol
      - protocol_name
      - 
    * - New Struct
      - type, name, \*parameters
      - 
    * - New Tbcd Container
      - name
      - 
    * - New Union
      - type, name
      - 
    * - Pdu
      - length
      - 
    * - Reset Handler Messages
      -
      - 
    * - Reset Rammbock
      -
      - 
    * - Save Template
      - name, unlocked=False
      - 
    * - Server Receives Binary
      - name=None, timeout=None, connection=None, label=None
      - 
    * - Server Receives Binary From
      - name=None, timeout=None, connection=None, label=None
      - 
    * - Server Receives Message
      - \*parameters
      - 
    * - Server Receives Without Validation
      - \*parameters
      - 
    * - Server Sends Binary
      - message, name=None, connection=None, label=None
      - 
    * - Server Sends Message
      - \*parameters
      - 
    * - Set Client Handler
      - handler_func, name=None, header_filter=None, interval=0.5
      - 
    * - Set Server Handler
      - handler_func, name=None, header_filter=None, alias=None, interval=0.5
      - 
    * - Start Bag
      - name
      - 
    * - Start Sctp Client
      - ip=None, port=None, name=None, timeout=None, protocol=None, family=ipv4
      - 
    * - Start Sctp Server
      - ip, port, name=None, timeout=None, protocol=None, family=ipv4
      - 
    * - Start Tcp Client
      - ip=None, port=None, name=None, timeout=None, protocol=None, family=ipv4
      - 
    * - Start Tcp Server
      - ip, port, name=None, timeout=None, protocol=None, family=ipv4
      - 
    * - Start Udp Client
      - ip=None, port=None, name=None, timeout=None, protocol=None, family=ipv4
      - 
    * - Start Udp Server
      - ip, port, name=None, timeout=None, protocol=None, family=ipv4
      - 
    * - Tbcd
      - size, name, value=None
      - 
    * - U 128
      - name, value=None, align=None
      - 
    * - U 16
      - name, value=None, align=None
      - 
    * - U 24
      - name, value=None, align=None
      - 
    * - U 32
      - name, value=None, align=None
      - 
    * - U 40
      - name, value=None, align=None
      - 
    * - U 64
      - name, value=None, align=None
      - 
    * - U 8
      - name, value=None, align=None
      - 
    * - Uint
      - length, name, value=None, align=None
      - 
    * - Validate Message
      - msg, \*parameters
      - 
    * - Value
      - name, value
      - 

Selenium2Library
-------------------------
.. list-table::

    * - キーワード
      - 引数
      - 説明
    * - Add Cookie
      - name, value, path=None, domain=None, secure=None, expiry=None
      - 
    * - Add Location Strategy
      - strategy_name, strategy_keyword, persist=False
      - 
    * - Alert Should Be Present
      - text=
      - 
    * - Assign Id To Element
      - locator, id
      - 
    * - Capture Page Screenshot
      - filename=None
      - 
    * - Checkbox Should Be Selected
      - locator
      - 
    * - Checkbox Should Not Be Selected
      - locator
      - 
    * - Choose Cancel On Next Confirmation
      -
      - 
    * - Choose File
      - locator, file_path
      - 
    * - Choose Ok On Next Confirmation

      - 
    * - Clear Element Text
      - locator
      - 
    * - Click Button
      - locator
      - 
    * - Click Element
      - locator
      - 
    * - Click Element At Coordinates
      - locator, xoffset, yoffset
      - 
    * - Click Image
      - locator
      - 
    * - Click Link
      - locator
      - 
    * - Close All Browsers
      -
      - 
    * - Close Browser
      -
      - 
    * - Close Window
      -
      - 
    * - Confirm Action
      -
      - 
    * - Create Webdriver
      - driver_name, alias=None, kwargs={}, \*\*init_kwargs
      - 
    * - Current Frame Contains
      - text, loglevel=INFO
      - 
    * - Current Frame Should Not Contain
      - text, loglevel=INFO
      - 
    * - Delete All Cookies
      -
      - 
    * - Delete Cookie
      - name
      - 
    * - Dismiss Alert
      - accept=True
      - 
    * - Double Click Element
      - locator
      - 
    * - Drag And Drop
      - source, target
      - 
    * - Drag And Drop By Offset
      - source, xoffset, yoffset
      - 
    * - Element Should Be Disabled
      - locator
      - 
    * - Element Should Be Enabled
      - locator
      - 
    * - Element Should Be Visible
      - locator, message=
      - 
    * - Element Should Contain
      - locator, expected, message=
      - 
    * - Element Should Not Be Visible
      - locator, message=
      - 
    * - Element Should Not Contain
      - locator, expected, message=
      - 
    * - Element Text Should Be
      - locator, expected, message=
      - 
    * - Execute Async Javascript
      - \*code
      - 
    * - Execute Javascript
      - \*code
      - 
    * - Focus
      - locator
      - 
    * - Frame Should Contain
      - locator, text, loglevel=INFO
      - 
    * - Get Alert Message
      - dismiss=True
      - 
    * - Get All Links
      -
      - 
    * - Get Cookie Value
      - name
      - 
    * - Get Cookies
      -
      - 
    * - Get Element Attribute
      - attribute_locator
      - 
    * - Get Horizontal Position
      - locator
      - 
    * - Get List Items
      - locator
      - 
    * - Get Location
      -
      - 
    * - Get Matching Xpath Count
      - xpath
      - 
    * - Get Selected List Label
      - locator
      - 
    * - Get Selected List Labels
      - locator
      - 
    * - Get Selected List Value
      - locator
      - 
    * - Get Selected List Values
      - locator
      - 
    * - Get Selenium Implicit Wait
      -
      - 
    * - Get Selenium Speed
      -
      - 
    * - Get Selenium Timeout
      -
      - 
    * - Get Source
      -
      - 
    * - Get Table Cell
      - table_locator, row, column, loglevel=INFO
      - 
    * - Get Text
      - locator
      - 
    * - Get Title
      -
      - 
    * - Get Value
      - locator
      - 
    * - Get Vertical Position
      - locator
      - 
    * - Get Webelement
      - locator
      - 
    * - Get Webelements
      - locator
      - 
    * - Get Window Identifiers
      -
      - 
    * - Get Window Names
      -
      - 
    * - Get Window Position
      -
      - 
    * - Get Window Size
      -
      - 
    * - Get Window Titles
      -
      - 
    * - Go Back
      -
      - 
    * - Go To
      - url
      - 
    * - Input Password
      - locator, text
      - 
    * - Input Text
      - locator, text
      - 
    * - Input Text Into Prompt
      - text
      - 
    * - List Selection Should Be
      - locator, \*items
      - 
    * - List Should Have No Selections
      - locator
      - 
    * - List Windows
      -
      - 
    * - Location Should Be
      - url
      - 
    * - Location Should Contain
      - expected
      - 
    * - Locator Should Match X Times
      - locator, expected_locator_count, message=, loglevel=INFO
      - 
    * - Log Location
      -
      - 
    * - Log Source
      - loglevel=INFO
      - 
    * - Log Title
      -
      - 
    * - Maximize Browser Window
      -
      - 
    * - Mouse Down
      - locator
      - 
    * - Mouse Down On Image
      - locator
      - 
    * - Mouse Down On Link
      - locator
      - 
    * - Mouse Out
      - locator
      - 
    * - Mouse Over
      - locator
      - 
    * - Mouse Up
      - locator
      - 
    * - Open Browser
      - url, browser=firefox, alias=None, remote_url=False, desired_capabilities=None, ff_profile_dir=None
      - 
    * - Open Context Menu
      - locator
      - 
    * - Page Should Contain
      - text, loglevel=INFO
      - 
    * - Page Should Contain Button
      - locator, message=, loglevel=INFO
      - 
    * - Page Should Contain Checkbox
      - locator, message=, loglevel=INFO
      - 
    * - Page Should Contain Element
      - locator, message=, loglevel=INFO
      - 
    * - Page Should Contain Image
      - locator, message=, loglevel=INFO
      - 
    * - Page Should Contain Link
      - locator, message=, loglevel=INFO
      - 
    * - Page Should Contain List
      - locator, message=, loglevel=INFO
      - 
    * - Page Should Contain Radio Button
      - locator, message=, loglevel=INFO
      - 
    * - Page Should Contain Textfield
      - locator, message=, loglevel=INFO
      - 
    * - Page Should Not Contain
      - text, loglevel=INFO
      - 
    * - Page Should Not Contain Button
      - locator, message=, loglevel=INFO
      - 
    * - Page Should Not Contain Checkbox
      - locator, message=, loglevel=INFO
      - 
    * - Page Should Not Contain Element
      - locator, message=, loglevel=INFO
      - 
    * - Page Should Not Contain Image
      - locator, message=, loglevel=INFO
      - 
    * - Page Should Not Contain Link
      - locator, message=, loglevel=INFO
      - 
    * - Page Should Not Contain List
      - locator, message=, loglevel=INFO
      - 
    * - Page Should Not Contain Radio Button
      - locator, message=, loglevel=INFO
      - 
    * - Page Should Not Contain Textfield
      - locator, message=, loglevel=INFO
      - 
    * - Press Key
      - locator, key
      - 
    * - Radio Button Should Be Set To
      - group_name, value
      - 
    * - Radio Button Should Not Be Selected
      - group_name
      - 
    * - Register Keyword To Run On Failure
      - keyword
      - 
    * - Reload Page
      -
      - 
    * - Remove Location Strategy
      - strategy_name
      - 
    * - Select All From List
      - locator
      - 
    * - Select Checkbox
      - locator
      - 
    * - Select Frame
      - locator
      - 
    * - Select From List
      - locator, \*items
      - 
    * - Select From List By Index
      - locator, \*indexes
      - 
    * - Select From List By Label
      - locator, \*labels
      - 
    * - Select From List By Value
      - locator, \*values
      - 
    * - Select Radio Button
      - group_name, value
      - 
    * - Select Window
      - locator=None
      - 
    * - Set Browser Implicit Wait
      - seconds
      - 
    * - Set Screenshot Directory
      - path, persist=False
      - 
    * - Set Selenium Implicit Wait
      - seconds
      - 
    * - Set Selenium Speed
      - seconds
      - 
    * - Set Selenium Timeout
      - seconds
      - 
    * - Set Window Position
      - x, y
      - 
    * - Set Window Size
      - width, height
      - 
    * - Simulate
      - locator, event
      - 
    * - Submit Form
      - locator=None
      - 
    * - Switch Browser
      - index_or_alias
      - 
    * - Table Cell Should Contain
      - table_locator, row, column, expected, loglevel=INFO
      - 
    * - Table Column Should Contain
      - table_locator, col, expected, loglevel=INFO
      - 
    * - Table Footer Should Contain
      - table_locator, expected, loglevel=INFO
      - 
    * - Table Header Should Contain
      - table_locator, expected, loglevel=INFO
      - 
    * - Table Row Should Contain
      - table_locator, row, expected, loglevel=INFO
      - 
    * - Table Should Contain
      - table_locator, expected, loglevel=INFO
      - 
    * - Textarea Should Contain
      - locator, expected, message=
      - 
    * - Textarea Value Should Be
      - locator, expected, message=
      - 
    * - Textfield Should Contain
      - locator, expected, message=
      - 
    * - Textfield Value Should Be
      - locator, expected, message=
      - 
    * - Title Should Be
      - title
      - 
    * - Unselect Checkbox
      - locator
      - 
    * - Unselect Frame
      -
      - 
    * - Unselect From List
      - locator, \*items
      - 
    * - Unselect From List By Index
      - locator, \*indexes
      - 
    * - Unselect From List By Label
      - locator, \*labels
      - 
    * - Unselect From List By Value
      - locator, \*values
      - 
    * - Wait For Condition
      - condition, timeout=None, error=None
      - 
    * - Wait Until Element Contains
      - locator, text, timeout=None, error=None
      - 
    * - Wait Until Element Does Not Contain
      - locator, text, timeout=None, error=None
      - 
    * - Wait Until Element Is Enabled
      - locator, timeout=None, error=None
      - 
    * - Wait Until Element Is Not Visible
      - locator, timeout=None, error=None
      - 
    * - Wait Until Element Is Visible
      - locator, timeout=None, error=None
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
    * - Xpath Should Match X Times
      - xpath, expected_xpath_count, message=, loglevel=INFO
      - 

SSHLibrary
-------------------------
.. list-table::

    * - キーワード
      - 引数
      - 説明
    * - Close All Connections
      -
      - 
    * - Close Connection
      -
      - 
    * - Directory Should Exist
      - path
      - 
    * - Directory Should Not Exist
      - path
      - 
    * - Enable Ssh Logging
      - logfile
      - 
    * - Execute Command
      - command, return_stdout=True, return_stderr=False, return_rc=False
      - 
    * - File Should Exist
      - path
      - 
    * - File Should Not Exist
      - path
      - 
    * - Get Connection
      - index_or_alias=None, index=False, host=False, alias=False, port=False, timeout=False, newline=False, prompt=False, term_type=False, width=False, height=False, encoding=False
      - 
    * - Get Connections
      -
      - 
    * - Get Directory
      - source, destination=., recursive=False
      - 
    * - Get File
      - source, destination=.
      - 
    * - List Directories In Directory
      - path, pattern=None, absolute=False
      - 
    * - List Directory
      - path, pattern=None, absolute=False
      - 
    * - List Files In Directory
      - path, pattern=None, absolute=False
      - 
    * - Login
      - username, password, delay=0.5 seconds
      - 
    * - Login With Public Key
      - username, keyfile, password=, delay=0.5 seconds
      - 
    * - Open Connection
      - host, alias=None, port=22, timeout=None, newline=None, prompt=None, term_type=None, width=None, height=None, path_separator=None, encoding=None
      - 
    * - Put Directory
      - source, destination=., mode=0744, newline=, recursive=False
      - 
    * - Put File
      - source, destination=., mode=0744, newline=
      - 
    * - Read
      - loglevel=None, delay=None
      - 
    * - Read Command Output
      - return_stdout=True, return_stderr=False, return_rc=False
      - 
    * - Read Until
      - expected, loglevel=None
      - 
    * - Read Until Prompt
      - loglevel=None
      - 
    * - Read Until Regexp
      - regexp, loglevel=None
      - 
    * - Set Client Configuration
      - timeout=None, newline=None, prompt=None, term_type=None, width=None, height=None, path_separator=None, encoding=None
      - 
    * - Set Default Configuration
      - timeout=None, newline=None, prompt=None, loglevel=None, term_type=None, width=None, height=None, path_separator=None, encoding=None
      - 
    * - Start Command
      - command
      - 
    * - Switch Connection
      - index_or_alias
      - 
    * - Write
      - text, loglevel=None
      - 
    * - Write Bare
      - text
      - 
    * - Write Until Expected Output
      - text, expected, timeout, retry_interval, loglevel=None
      - 

