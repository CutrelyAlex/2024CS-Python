@echo off
cls

if not exist .venv\Scripts\activate.bat (
	python -m venv .venv
	)

call .venv\Scripts\activate.bat

cls

if not exist requirements.txt (
    pause
    exit /b
)


pip install -i https://pypi.tuna.tsinghua.edu.cn/simple -r requirements.txt
start http://127.0.0.1:5000
python app.py


pause
