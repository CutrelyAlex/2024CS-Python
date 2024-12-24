@echo off

if not exist .venv\Scripts\activate.bat (
    echo createing a python venv
	python -m venv .venv
	)

call .venv\Scripts\activate.bat
echo finished a python venv

if not exist requirements.txt (
    echo not found the requirements.txt, please found the requirements and again it
    pause
    exit /b
)

echo installing python packages
pip install -i https://pypi.tuna.tsinghua.edu.cn/simple -r requirements.txt

echo run python flask app
start http://127.0.0.1:5000
python app.py runserver


pause
