robot.libraries.Dialogs
=======================
Version:          3.0
Scope:            global
Named arguments:  supported

A test library providing dialogs for interacting with users.

``Dialogs`` is Robot Framework's standard library that provides means
for pausing the test execution and getting input from users. The
dialogs are slightly different depending on whether tests are run on
Python, IronPython or Jython but they provide the same functionality.

Long lines in the provided messages are wrapped automatically since
Robot Framework 2.8. If you want to wrap lines manually, you can add
newlines using the ``\n`` character sequence.

The library has a known limitation that it cannot be used with timeouts
on Python. Support for IronPython was added in Robot Framework 2.9.2.

Execute Manual Step
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Arguments:  [message, default_error=]

Pauses test execution until user sets the keyword status.

User can press either ``PASS`` or ``FAIL`` button. In the latter case
execution
fails and an additional dialog is opened for defining the error message.

``message`` is the instruction shown in the initial dialog and
``default_error`` is the default value shown in the possible error message
dialog.

Get Selection From User
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Arguments:  [message, *values]

Pauses test execution and asks user to select a value.

The selected value is returned. Pressing ``Cancel`` fails the keyword.

``message`` is the instruction shown in the dialog and ``values`` are
the options given to the user.

Example:
| ${username} = | Get Selection From User | Select user name | user1 | user2 |
admin |

Get Value From User
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Arguments:  [message, default_value=, hidden=False]

Pauses test execution and asks user to input a value.

Value typed by the user, or the possible default value, is returned.
Returning an empty value is fine, but pressing ``Cancel`` fails the keyword.

``message`` is the instruction shown in the dialog and ``default_value`` is
the possible default value shown in the input field.

If ``hidden`` is given a true value, the value typed by the user is hidden.
``hidden`` is considered true if it is a non-empty string not equal to
``false`` or ``no``, case-insensitively. If it is not a string, its truth
value is got directly using same
[http://docs.python.org/2/library/stdtypes.html#truth-value-testing|rules
as in Python].

Example:
| ${username} = | Get Value From User | Input user name | default    |
| ${password} = | Get Value From User | Input password  | hidden=yes |

Possibility to hide the typed in value is new in Robot Framework 2.8.4.
Considering strings ``false`` and ``no`` to be false is new in 2.9.

Pause Execution
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Arguments:  [message=Test execution paused. Press OK to continue.]

Pauses test execution until user clicks ``Ok`` button.

``message`` is the message shown in the dialog.

