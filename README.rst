scrimenv
========
A Virtualenv wrapper written with **click** and **scrim**

Demonstrates how scrim can help you build python cli tools that modify your shells environment.

This should work...
===================
::

    > pip install git+ssh://git@github.com/danbradham/scrimenv.git
    ...
    > scrimenv create testenv
    ...
    > deactivate
    > scrimenv activate testenv
    ...
    > deactivate
    > scrimenv run_in testenv python
    ...
    >>>

Scrim
=====
Scrimenv is being developed alongside Scrim to help me design, develop, and play with Scrim. Until Scrim supports other scripting languages, Scrimenv only supports powershell.exe and cmd.exe.

For more information on Scrim visit the `github repo <https://github.com/danbradham/scrim>`_.
