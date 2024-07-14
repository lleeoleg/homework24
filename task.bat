ECHO ON
set folderPath=.\venv\
if not exist %folderPath% (
    python -m venv venv
)
call venv_activate.bat
python -m pip install python-docx
pip list
pip freeze > requirements.txt

python task.py

call venv_deactivate.bat