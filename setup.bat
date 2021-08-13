ECHO "-- Navarro ENL whisperplayer installer --"
ECHO "installs pip and the needed python modules"
@echo off
setlocal

:PROMPT
SET /P AREYOUSURE=Continue? (y/[N])
IF /I "%AREYOUSURE%" NEQ "y" GOTO END

python -m ensurepip --upgrade
pip install setuptools
py setup.py

:END
endlocal
PAUSE
