@echo off
ECHO -- Navarro ENL whisperplayer installer --
ECHO installs pip and the needed python modules

:PROMPT
SET /P AREYOUSURE=Continue? (y/[N])
IF /I "%AREYOUSURE%" NEQ "y" GOTO END

@echo on
python -m ensurepip --upgrade
pip install pip setuptools wheel --upgrade
python -m build
pip install .
@echo off
GOTO END


:END
ENDLOCAL
PAUSE
