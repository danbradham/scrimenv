@echo off
set SCRIM_SHELL=cmd.exe
set SCRIM_PATH=scrim_out.bat
set SCRIM_LOG=scrim_log.txt
set SCRIM_AUTO_WRITE=1
set SCRIM_SCRIPT=%0

rem Call real python cli
pyscrimenv.exe %*

if exist %SCRIM_PATH% (goto :try) else (goto :finally)

:try
call %SCRIM_PATH% 2> %SCRIM_LOG%
if errorlevel 1 (goto :except) else (goto :finally)

:except
echo Failed to execute scrim...
set /p err=<%SCRIM_LOG%
del %SCRIM_LOG%
echo %err%
goto :finally

:finally
if exist %SCRIM_PATH% (del %SCRIM_PATH%)
set SCRIM_SHELL=
set SCRIM_PATH=
set SCRIM_LOG=
set SCRIM_SCRIPT=
