REM un-comment to enable console
REM python -m PyInstaller --onefile --distpath "." -n "Folder Checker" src/Main.py

REM comment this if you want to enable console
python -m PyInstaller --onefile --noconsole --distpath "." -n "Folder Checker" src/Main.py
