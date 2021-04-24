@echo off 

set SUCCESSES=0
set FAILURES=0

REM PING
:ping
ping -n 1 8.8.8.8 > nul
if %errorlevel% equ 0 goto success
if %errorlevel% equ 1 goto failure

REM PING SUCCESS
:success
set /A SUCCESSES=SUCCESSES+1
cls
color 2f
echo SUCCESS 
echo 
echo (success: %SUCCESSES%, failure: %FAILURES%)
goto wait

REM PING FAILURE
:failure
set /A FAILURES=FAILURES+1
cls
color 4f
echo FAILURE
goto wait

REM WAIT
:wait
timeout 3 >nul
goto ping