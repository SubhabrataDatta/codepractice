@echo off
setlocal enabledelayedexpansion

:: This is a comment using double colons.
:: First ever Windows batch/cmd script that triggers a pythhon script
REM This is another way of comment using REMarks


echo === Log Analyzer ===
echo.
::Line break - i) blank space: echo. ii) next line: echo ^

pause

:: In bat %% are known as wrappers and used for variable values
:: %x:~4,2% acts as substring()

set TODAY=%DATE:~6,4%-%DATE:~3,2%-%DATE:~0,2%
echo %TODAY%
echo.
pause

::Find files of pattern ext*(today's date).log

for %%F in (input\ext*%TODAY%*.log) do (
    set FOUND=%%F
)

echo.
echo Log found %FOUND%
echo.
echo Press Enter/Any Key to Summarize %FOUND% or ALt+F4 to exit
echo.
pause

::call python

python log_analyzer.py %FOUND% >> output\summarylog.txt


echo.
echo Run Complete - Summary written at output\summarylog.txt
pause