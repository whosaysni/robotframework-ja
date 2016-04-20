.. _Installation instructions:

インストール方法
=========================

この節では、 Robot Framework のインストール・アンインストール方法と、各種 OS で必要な準備を開設しています。基本的に、  `pip <http://pip-installer.org>`_ をインストールしていれば、以下のように実行するだけです::

    pip install robotframework

.. contents::
   :depth: 2
   :local:

.. START USER GUIDE IGNORE
.. These instructions are included also in the User Guide. Following role
.. and link definitions are excluded when UG is built.
.. default-role:: code
.. role:: file(emphasis)
.. role:: option(code)
.. _supporting tools: http://robotframework.org/robotframework/#built-in-tools
.. _post-process outputs: `supporting tools`_
.. END USER GUIDE IGNORE


.. Introduction:

はじめに
------------

`Robot Framework <http://robotframework.org>`_ は `Python <http://python.org>`_ で書かれており、 `Jython <http://jython.org>`_ (JVM) や `IronPython <http://ironpython.net>`_ (.NET) でも動作します。このフレームワークをインストールするときには、 :ref:`前提条件 <precondition>` として、以下のインタプリタのいずれかが必要です。`

Robot Framework 自体のインストール方法には、以下のような様々な方法があります。これらについては、後の節でも説明します。

:ref:`pip を使う <Installing with pip>`
    Robot Framework 推奨のインストール方法です。 最近の Python, Jython, IronPython には、標準のパッケージマネジャとして pip_ が入っています。pip が使える状態なら、単に::

        pip install robotframework

    とするだけです。

:ref:`ソースコードから <Installing from source>`
    どのオペレーティングシステムでも、どの Python インタプリタでも使える方法です。ソースコードは `PyPI <https://pypi.python.org/pypi/robotframework>`_ からダウンロードして展開したり、 `GitHub リポジトリから <https://github.com/robotframework/robotframework>`_ を clone したりして取得できます。

:ref:`JAR形式 <Standalone JAR distribution>`
    Jython で実行できれば充分な場合、 `Maven central <http://search.maven.org/#search%7Cga%7C1%7Ca%3Arobotframework>`_ からスタンドアロンの ``robotframework-<version>.jar`` を取ってくるのが一番簡単です。この JAR には、 Jython と Robot Framework が両方とも入っていて、 `Java <http://java.com>`_ をインストールしておくだけで使えます。

:ref:`手作業で <Manual installation>`
    何か特別な事情があって、上の方法がどれも使えない場合には、自分で手作業で入れられます。

.. note:: Robot Framework 3.0 以前のバージョンには、 32bit 版と 64bit 版の両方の Python 向けのインストーラがありました。 Python 2.7.9 からは Windows 版にも pip_ が入っていることや、インストーラだと Python 3 向けにも二つ必要になってしまうことから、 `Windows インストーラの提供はやめました <https://github.com/robotframework/robotframework/issues/2218>`_ 。Windows版でも、 :ref:`pip を使ったインストール <using pip>` を推奨します。

.. _precondition:
.. _Preconditions:

前提条件
-------------

Robot Framework は Python_ (C Python, Python 2 と 3 の両方),  Jython_ (JVM),  IronPython (.NET), そして ``PyPy <http://pypy.org>`_ をサポートしています。フレームワークを動かすには、あらかじめいずれかのインタプリタをインストールしておく必要があります。

一般に、どのインタプリタを使うべきかは、どんなテストライブラリやテスト環境が必要かによって変わります。ライブラリによっては、 CPython 上でしか動かないものもありますし、 Java のツールを使っているために Jython でしか動かないものや、 .NET 環境が必要なため IronPython が適している場合もあります。もちろん、どのインタプリタでも問題なく動くツールやライブラリもたくさんあります。

特殊な事情がなく、まずはフレームワークを試してみたいのなら、Python をお勧めします。Python はもっとも成熟した実装で、 Jython や IronPython よりも高速 (とりわけ、起動が速い) で、ほとんどの UNIX 系 OS 上で使えます。もう一つの選択肢は、 Java さえあれば使える :ref:`スタンドアロン JAR版 <standalone JAR distribution>` です。

.. _Python 2 vs Python 3:

Python 2 か Python 3 か
~~~~~~~~~~~~~~~~~~~~~~~~~

Python 2 と Pyhton 3 は、言語としてはほとんど同じですが、お互いに完全に互換というわけではありません。
主な違いは、 Python 3 では、標準ではすべての文字列が Unicode 文字列型であるのに対して、 Python 2 では標準は実質 bytes 型に総統するということです。
他にも、後方互換性のない変更がいくつかあります。
2010 年にリリースされた Python 2.7 は Python 2 系の最後のリリースとされていて、2020 年までサポートされます。
Python 2 と 3 の違い、どちらを使うべきか、どちらのバージョンでも動くコードの書き方などは、 `Wiki <https://wiki.python.org/moin/Python2orPython3>`_ を参照するとよいでしょう。

Robot Framework 3.0 は、 Python 3 をサポートする最初のバージョンです。
このバージョンは、Python 2 もサポートしていて、 Python 2 自体が公式にサポートされている限り Python 2 に対応し続ける予定です。フレームワークのコア部分が Pyhton 3 へのサポートを始めたいま、Robot Framework のエコシステムに関わるライブラリやツールの作者にも、 Python 3 のサポートを検討していただきたいです。

.. _Python installation:

Python のインストール
~~~~~~~~~~~~~~~~~~~~~~

Linux や OS X のように、ほとんどの UNIX 系システムには、最初から Python_ がインストールされています。
Windows その他の環境では、 Python を自分でインストールする必要があります。
まずは http://python.org に行って、適切なインストーラをダウンロードしたり、 Python のインストール手順について詳しい情報を得るのが良いでしょう。

Robot Framework 3.0 は、 Python 2.6, 2.7, 3.3 以降をサポートしています。
ただし、 `バージョン 3.1 以降で Python 2.6 のサポートを打ち切る <https://github.com/robotframework/robotframework/issues/2276>`_ 予定です。
古いバージョンの Python を使いたい場合、 Robot Framework 2.5-2.8 が Python 2.5 を、 Robot Framework 2.0-2.1 が Python 2.3 および 2.4 をサポートしています。

Windows では、インストール時に、インストーラを管理者モードで起動し、全てのユーザにインストールするよう推奨します。
また、環境変数 ``PYTHONCASEOK`` は設定してはなりません。

インストール後、 PATH_ を変更して、コマンドラインから Python コマンドと ``robot``, ``rebot`` :ref:`テスト実行スクリプト <runner scripts>` を実行できるように設定する必要があるでしょう。

.. tip:: 最近の Windows 用 Pyhton インストーラには、インストールの際に ``PATH`` を設定する機能があります。この機能は標準では無効になっていて、 `Customize Python` の画面で `Add python.exe to Path` を有効にします。

.. _Jython installation:

Jython のインストール
~~~~~~~~~~~~~~~~~~~~~~~~

Java_ で書かれていたり、内部的に Java のツールを使うテストライブラリを使いたい場合には、Robot Framework を Jython_ 上で動かす必要があります。
そのため、 Java ランタイム環境 (JRE) か、 Java 開発キット (JDK) が必要です。
ここでは、 JRE や JDK のインストール方法について説明しませんが、 http://java.com などで詳しい情報が手にはいります。

Jython のインストールはとても簡単で、まずは、 http://jython.org からインストーラを取得します。
インストーラは実行可能な JAR のパッケージで、コマンドラインから `java -jar jython_installer-<version>.jar` で実行します。
システム構成によっては、インストーラをダブルクリックするだけでインストールできます。

Robot Framework 3.0 は Jython 2.7 をサポートしており、これには Java 7 以降が必要です。
古い Jython や Java が必要なら、 Robot Framework 2.5-2.8 が Jython 2.5 (Java 5 以降)、
Robot Framework 2.0-2.1 が Jython 2.2 をサポートしています。

Jython をインストールしたら、 PATH_ を変更して、コマンドラインから Python コマンドと ``robot``, ``rebot`` :ref:`テスト実行スクリプト <runner scripts>` を実行できるように設定する必要があるでしょう。


.. _IronPython installation:

IronPython のインストール
~~~~~~~~~~~~~~~~~~~~~~~~~~~

IronPython_ を使えば、 Robot Framework を `.NET platform <http://www.microsoft.com/net>`_ 上で動かしたり、 C# や他の .NET 言語とその API にアクセスできます。
サポートしているバージョンは IronPython 2.7 のみです。

IronPython を使う場合、 `elementtree <http://effbot.org/downloads/#elementtree>`_ モジュールの
1.2.7 プレビューリリース版が必要です。というのも、 IronPython の配布物に入っている ``elementtree`` の実装は `壊れている <https://github.com/IronLanguages/main/issues/968>`_ からです。
``elementtree`` をインストールするには、ソース配布物をダウンロードして解凍し、解凍先ディレクトリで ``ipy setup.py install`` を実行します。

IronPython をインストールしたら、 PATH_ を変更して、コマンドラインから Python コマンドと ``robot``, ``rebot`` :ref:`テスト実行スクリプト <runner scripts>` を実行できるように設定する必要があるでしょう。


.. _Configuring PATH:

Configuring ``PATH``
~~~~~~~~~~~~~~~~~~~~

The ``PATH`` environment variable lists locations where commands executed in
a system are searched from. To make using Robot Framework easier from the
command prompt, it is recommended to add the locations where the `runner
scripts`_ are installed into the ``PATH``. It is also often useful to have
the interpreter itself in the ``PATH`` to make executing it easy.

When using Python on UNIX-like machines both Python itself and scripts
installed with should be automatically in the ``PATH`` and no extra actions
needed. On Windows and with other interpreters the ``PATH`` must be configured
separately.

.. tip:: Latest Python Windows installers allow setting ``PATH`` as part of
         the installation. This is disabled by default, but `Add python.exe
         to Path` can be enabled on the `Customize Python` screen. It will
         add both the Python installation directory and the :file:`Scripts`
         directory to the ``PATH``.

.. _What directories to add to PATH:

What directories to add to ``PATH``
'''''''''''''''''''''''''''''''''''

What directories you need to add to the ``PATH`` depends on the interpreter and
the operating system. The first location is the installation directory of
the interpreter (e.g. :file:`C:\\Python27`) and the other is the location
where scripts are installed with that interpreter. Both Python and IronPython
install scripts to :file:`Scripts` directory under the installation directory
on Windows (e.g. :file:`C:\\Python27\\Scripts`) and Jython uses :file:`bin`
directory regardless the operating system (e.g. :file:`C:\\jython2.7.0\\bin`).

Notice that the :file:`Scripts` and :file:`bin` directories may not be created
as part of the interpreter installation, but only later when Robot Framework
or some other third party module is installed.

.. _Setting PATH on Windows:

Setting ``PATH`` on Windows
'''''''''''''''''''''''''''

On Windows you can configure ``PATH`` by following the steps below. Notice
that the exact setting names may be different on different Windows versions,
but the basic approach should still be the same.

1. Open `Control Panel > System > Advanced > Environment Variables`. There
   are `User variables` and `System variables`, and the difference between
   them is that user variables affect only the current users, whereas system
   variables affect all users.

2. To edit an existing ``PATH`` value, select `Edit` and add
   `;<InstallationDir>;<ScriptsDir>` at the end of the value (e.g.
   `;C:\Python27;C:\Python27\Scripts`). Note that the semicolons (`;`) are
   important as they separate the different entries. To add a new ``PATH``
   value, select `New` and set both the name and the value, this time without
   the leading semicolon.

3. Exit the dialog with `Ok` to save the changes.

4. Start a new command prompt for the changes to take effect.

Notice that if you have multiple Python versions installed, the executed
``robot`` or ``rebot`` `runner script`_ will always use the one that is
*first* in the ``PATH`` regardless under what Python version that script is
installed. To avoid that, you can always execute the `installed robot module
directly`__ like `C:\Python27\python.exe -m robot`.

Notice also that you should not add quotes around directories you add into
the ``PATH`` (e.g. `"C:\Python27\Scripts"`). Quotes `can cause problems with
Python programs <http://bugs.python.org/issue17023>`_ and they are not needed
in this context even if the directory path would contain spaces.

__ `Executing installed robot module`_

.. _Setting PATH on UNIX-like systems:

Setting ``PATH`` on UNIX-like systems
'''''''''''''''''''''''''''''''''''''

On UNIX-like systems you typically need to edit either some system wide or user
specific configuration file. Which file to edit and how depends on the system,
and you need to consult your operating system documentation for more details.

.. _Setting https_proxy:

Setting ``https_proxy``
~~~~~~~~~~~~~~~~~~~~~~~

If you are `installing with pip`_ and are behind a proxy, you need to set
the ``https_proxy`` environment variable. It is needed both when installing
pip itself and when using it to install Robot Framework and other Python
packages.

How to set the ``https_proxy`` depends on the operating system similarly as
`configuring PATH`_. The value of this variable must be an URL of the proxy,
for example, `http://10.0.0.42:8080`.

.. _Installing with pip:

Installing with pip
-------------------

The standard Python package manager is pip_, but there are also other
alternatives such as `Buildout <http://buildout.org>`__ and `easy_install
<http://peak.telecommunity.com/DevCenter/EasyInstall>`__. These instructions
only cover using pip, but other package managers ought be able to install
Robot Framework as well.

Latest Python, Jython and IronPython versions contain pip bundled in. Which
versions contain it and how to possibly activate it is discussed in sections
below. See pip_ project pages if for latest installation instructions if you
need to install it.

.. note:: Only Robot Framework 2.7 and newer can be installed using pip. If you
          need an older version, you must use other installation approaches.

.. _Installing pip for Python:

Installing pip for Python
~~~~~~~~~~~~~~~~~~~~~~~~~

Starting from Python 2.7.9, the standard Windows installer by default installs
and activates pip. Assuming you also have configured PATH_ and possibly
set https_proxy_, you can run `pip install robotframework` right after
Python installation.

Outside Windows and with older Python versions you need to install pip yourself.
You may be able to do it using system package managers like Apt or Yum on Linux,
but you can always use the manual installation instructions found from the pip_
project pages.

If you have multiple Python versions with pip installed, the version that is
used when the ``pip`` command is executed depends on which pip is first in the
PATH_. An alternative is executing the ``pip`` module using the selected Python
version directly:

.. sourcecode:: bash

    python -m pip install robotframework
    python3 -m pip install robotframework

.. _Installing pip for Jython:

Installing pip for Jython
~~~~~~~~~~~~~~~~~~~~~~~~~

Jython 2.7 contain pip bundled in, but it needs to be activated before using it
by running the following command:

.. sourcecode:: bash

    jython -m ensurepip

Jython installs its pip into :file:`<JythonInstallation>/bin` directory.
Does running `pip install robotframework` actually use it or possibly some
other pip version depends on which pip is first in the PATH_. An alternative
is executing the ``pip`` module using Jython directly:

.. sourcecode:: bash

    jython -m pip install robotframework

.. _Installing pip for IronPython:

Installing pip for IronPython
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

IronPython contains bundled pip starting from `version 2.7.5`__. Similarly as
with Jython, it needs to be activated first:

.. sourcecode:: bash

    ipy -X:Frames -m ensurepip

Notice that with IronPython `-X:Frames` command line option is needed both
when activating and when using pip.

IronPython installs pip into :file:`<IronPythonInstallation>/Scripts` directory.
Does running `pip install robotframework` actually use it or possibly some
other pip version depends on which pip is first in the PATH_. An alternative
is executing the ``pip`` module using IronPython directly:

.. sourcecode:: bash

    ipy -X:Frames -m pip install robotframework

IronPython versions prior to 2.7.5 do not officially support pip.

__ http://blog.ironpython.net/2014/12/pip-in-ironpython-275.html

.. _Using pip:

Using pip
~~~~~~~~~

Once you have pip_ installed, and have set https_proxy_ if you are behind
a proxy, using it on the command line is very easy. The easiest way to use
pip is by letting it find and download packages it installs from the
`Python Package Index (PyPI)`__, but it can also install packages
downloaded from the PyPI separately. The most common usages are shown below
and pip_ documentation has more information and examples.

__ PyPI_

.. sourcecode:: bash

    # Install the latest version
    pip install robotframework

    # Upgrade to the latest version
    pip install --upgrade robotframework

    # Install a specific version
    pip install robotframework==2.9.2

    # Install separately downloaded package (no network connection needed)
    pip install robotframework-3.0.tar.gz

    # Uninstall
    pip uninstall robotframework

Notice that pip 1.4 and newer will only install stable releases by default.
If you want to install an alpha, beta or release candidate, you need to either
specify the version explicitly or use the :option:`--pre` option:

.. sourcecode:: bash

    # Install 3.0 beta 1
    pip install robotframework==3.0b1

    # Upgrade to the latest version even if it is a pre-release
    pip install --pre --upgrade robotframework

.. _Installing from source:

Installing from source
----------------------

This installation method can be used on any operating system with any of the
supported interpreters. Installing *from source* can sound a bit scary, but
the procedure is actually pretty straightforward.

.. _Getting source code:

Getting source code
~~~~~~~~~~~~~~~~~~~

You typically get the source by downloading a *source distribution package*
in `.tar.gz` format. Newer packages are available on PyPI_, but Robot Framework
2.8.1 and older can be found from the old `Google Code download page
<https://code.google.com/p/robotframework/downloads/list?can=1>`_.
Once you have downloaded the package, you need to extract it somewhere and,
as a result, you get a directory named `robotframework-<version>`. The
directory contains the source code and scripts needed for installing it.

An alternative approach for getting the source code is cloning project's
`GitHub repository`_ directly. By default you will get the latest code, but
you can easily switch to different released versions or other tags.

.. _Installation:

Installation
~~~~~~~~~~~~

Robot Framework is installed from source using Python's standard ``setup.py``
script. The script is in the directory containing the sources and you can run
it from the command line using any of the supported interpreters:

.. sourcecode:: bash

   python setup.py install
   jython setup.py install
   ipy setup.py install

The ``setup.py`` script accepts several arguments allowing, for example,
installation into a non-default location that does not require administrative
rights. It is also used for creating different distribution packages. Run
`python setup.py --help` for more details.

.. _Standalone JAR distribution:

Standalone JAR distribution
---------------------------

Robot Framework is also distributed as a standalone Java archive that contains
both Jython_ and Robot Framework and only requires Java_ a dependency. It is
an easy way to get everything in one package that  requires no installation,
but has a downside that it does not work with the normal Python_ interpreter.

The package is named ``robotframework-<version>.jar`` and it is available
on the `Maven central`_. After downloading the package, you can execute tests
with it like:

.. sourcecode:: bash

  java -jar robotframework-3.0.jar mytests.robot
  java -jar robotframework-3.0.jar --variable name:value mytests.robot

If you want to `post-process outputs`_ using Rebot or use other built-in
`supporting tools`_, you need to give the command name ``rebot``, ``libdoc``,
``testdoc`` or ``tidy`` as the first argument to the JAR file:

.. sourcecode:: bash

  java -jar robotframework-3.0.jar rebot output.xml
  java -jar robotframework-3.0.jar libdoc MyLibrary list

For more information about the different commands, execute the JAR without
arguments.

In addition to the Python standard library and Robot Framework modules, the
standalone JAR versions starting from 2.9.2 also contain the PyYAML dependency
needed to handle yaml variable files.

.. _Manual installation:

Manual installation
-------------------

If you do not want to use any automatic way of installing Robot Framework,
you can always install it manually following these steps:

1. Get the source code. All the code is in a directory (a package in Python)
   called :file:`robot`. If you have a `source distribution`_ or a version
   control checkout, you can find it from the :file:`src` directory, but you
   can also get it from an earlier installation.

2. Copy the source code where you want to.

3. Decide `how to run tests`__.

__ `Executing Robot Framework`_

.. _Verifying installation:

Verifying installation
----------------------

After a successful installation, you should be able to execute the created
`runner scripts`_ with :option:`--version` option and get both Robot Framework
and interpreter versions as a result:

.. sourcecode:: bash

   $ robot --version
   Robot Framework 3.0 (Python 2.7.10 on linux2)

   $ rebot --version
   Rebot 3.0 (Python 2.7.10 on linux2)

If running the runner scripts fails with a message saying that the command is
not found or recognized, a good first step is double-checking the PATH_
configuration. If that does not help, it is a good idea to re-read relevant
sections from these instructions before searching help from the Internet or
as asking help on `robotframework-users
<http://groups.google.com/group/robotframework-users/>`__ mailing list or
elsewhere.

.. _Where files are installed:

Where files are installed
~~~~~~~~~~~~~~~~~~~~~~~~~

When an automatic installer is used, Robot Framework source code is copied
into a directory containing external Python modules. On UNIX-like operating
systems where Python is pre-installed the location of this directory varies.
If you have installed the interpreter yourself, it is normally
:file:`Lib/site-packages` under the interpreter installation directory, for
example, :file:`C:\\Python27\\Lib\\site-packages`. The actual Robot
Framework code is in a directory named :file:`robot`.

Robot Framework `runner scripts`_ are created and copied into another
platform-specific location. When using Python on UNIX-like systems, they
normally go to :file:`/usr/bin` or :file:`/usr/local/bin`. On Windows and
with Jython and IronPython, the scripts are typically either in :file:`Scripts`
or :file:`bin` directory under the interpreter installation directory.

.. _Uninstallation:

Uninstallation
--------------

The easiest way to uninstall Robot Framework is using pip_:

.. sourcecode:: bash

   pip uninstall robotframework

A nice feature in pip is that it can uninstall packages even if they are
installed from the source. If you do not have pip available or have done
a `manual installation`_ to a custom location, you need to find `where files
are installed`_ and remove them manually.

If you have set PATH_ or configured the environment otherwise, you need to
undo those changes separately.

.. _Upgrading:

Upgrading
---------

If you are using pip_, upgrading to a new version required either using
the `--upgrade` option or specifying the version to use explicitly:

.. sourcecode:: bash

   pip install --upgrade robotframework
   pip install robotframework==2.9.2

When using pip, it automatically uninstalls previous versions before
installation. If you are `installing from source`_, it should be safe to
just install over an existing installation. If you encounter problems,
uninstallation_ before installation may help.

When upgrading Robot Framework, there is always a change that the new version
contains backwards incompatible changes affecting existing tests or test
infrastructure. Such changes are very rare in minor versions like 2.8.7 or
2.9.2, but more common in major versions like 2.9 and 3.0. Backwards
incompatible changes and deprecated features are explained in the release
notes, and it is a good idea to study them especially when upgrading to
a new major version.

.. _Executing Robot Framework:

Executing Robot Framework
-------------------------

.. _runner script:
.. _runner scripts:
.. _Using robot and rebot scripts:

Using ``robot`` and ``rebot`` scripts
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Starting from Robot Framework 3.0, tests are executed using the ``robot``
script and results post-processed with the ``rebot`` script:

.. sourcecode:: bash

    robot tests.robot
    rebot output.xml

Both of these scripts are installed as part of the normal installation and
can be executed directly from the command line if PATH_ is set correctly.
They are implemented using Python except on Windows where they are batch files.

Older Robot Framework versions do not have the ``robot`` script and the
``rebot`` script is installed only with Python. Instead they have interpreter
specific scripts ``pybot``, ``jybot`` and ``ipybot`` for test execution and
``jyrebot`` and ``ipyrebot`` for post-processing outputs. These scripts still
work, but they will be deprecated and removed in the future.

.. _Executing installed robot module:

Executing installed ``robot`` module
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

An alternative way to run tests is executing the installed ``robot`` module
or its sub module ``robot.run`` directly using Python's `-m command line
option`__. This is especially useful if Robot Framework is used with multiple
Python versions:

.. sourcecode:: bash

    python -m robot tests.robot
    python3 -m robot.run tests.robot
    jython -m robot tests.robot
    /opt/jython/jython -m robot tests.robot

The support for ``python -m robot`` approach is a new feature in Robot
Framework 3.0, but the older versions support ``python -m robot.run``.
The latter must also be used with Python 2.6.

Post-processing outputs using the same approach works too, but the module to
run is ``robot.rebot``:

.. sourcecode:: bash

    python -m robot.rebot output.xml

__ https://docs.python.org/2/using/cmdline.html#cmdoption-m

.. _Executing installed robot directory:

Executing installed ``robot`` directory
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

If you know where Robot Framework is installed, you can also execute the
installed :file:`robot` directory or :file:`run.py` file inside it directly:

.. sourcecode:: bash

   python path/to/robot/ tests.robot
   jython path/to/robot/run.py tests.robot

Running the directory is a new feature in Robot Framework 3.0, but the older
versions support running the :file:`robot/run.py` file.

Post-processing outputs using the :file:`robot/rebot.py` file works the same
way too:

.. sourcecode:: bash

   python path/to/robot/rebot.py output.xml

Executing Robot Framework this way is especially handy if you have done
a `manual installation`_.

.. These aliases need an explicit target to work in GitHub
.. .. _precondition: `Preconditions`_
.. _PATH: `Configuring PATH`_
.. _https_proxy: `Setting https_proxy`_
.. _source distribution: `Getting source code`_
.. .. _runner script: `Using robot and rebot scripts`_
.. .. _runner scripts: `Using robot and rebot scripts`_
