@echo off

set true=1==1
set false=1==0

set DEBUG=%false%

GOTO:Main

:CheckIfPackageInstalled
    set packageName=%~1
    pip show %packageName% >nul 2>&1
    if %errorlevel% equ 0 (
        echo %packageName% is installed.
    ) else (
        echo %packageName% is not installed.
        pip install %packageName%
    )
    EXIT /B 0

:CheckPackages
    echo Checking packages.
    call:CheckIfPackageInstalled "customtkinter"
    call:CheckIfPackageInstalled "pillow"
    call:CheckIfPackageInstalled "pyinstaller"
    EXIT /B 0

:Build
    echo Building exe.
    if %DEBUG% (
        python -m PyInstaller --onefile --debug --distpath "." -n "Folder Checker" src/Main.py
    ) else (
        python -m PyInstaller --onefile --noconsole --distpath "." -n "Folder Checker" src/Main.py
    )
    EXIT /B 0

:Main
    call:CheckPackages
    call:Build
    EXIT /B 0
