@echo off
REM 设置代码页为 UTF-8
chcp 65001

REM 清除屏幕
cls

REM 检查虚拟环境是否存在，如果不存在则创建
if not exist .venv\Scripts\activate.bat (
    @REM echo 创建虚拟环境...
    python -m venv .venv
)

REM 激活虚拟环境
echo 激活虚拟环境...
call .venv\Scripts\activate.bat

cls

REM 检查 requirements.txt 文件是否存在
if not exist requirements.txt (
    echo 未检测到 requirements.txt 文件，请确保文件存在并重试。
    pause
    exit /b
)

echo 安装依赖...
pip install -r requirements.txt

REM 启动应用程序
echo 启动应用程序...
start http://127.0.0.1:5000
python app.py

REM 保持命令提示符窗口打开
pause
