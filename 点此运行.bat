@echo off
chcp 65001

REM 检查虚拟环境是否存在，如果不存在则创建
if not exist .venv\Scripts\activate.bat (
    echo 创建虚拟环境...
    python -m venv .venv
)

REM 激活虚拟环境
echo 激活虚拟环境...
call .venv\Scripts\activate.bat

REM 安装依赖
echo 安装依赖...
pip install -r requirements.txt

REM 打开浏览器
start http://127.0.0.1:5000

REM 启动应用程序
echo 启动应用程序...
python app.py

REM 保持命令提示符窗口打开
pause
