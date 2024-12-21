@echo off
REM 设置代码页为 UTF-8
chcp 65001

REM 检查虚拟环境是否存在，如果不存在则创建
if not exist .venv\Scripts\activate.bat (
    echo 创建虚拟环境...
    python -m venv .venv
)

REM 激活虚拟环境
echo 激活虚拟环境...
call .venv\Scripts\activate.bat

REM 检查 requirements.txt 文件是否存在
if not exist requirements.txt (
    echo 未检测到 requirements.txt 文件，请确保文件存在并重试。
    pause
    exit /b
)

REM 检查 requirements.txt 文件是否为空
for /f %%i in ('find /c /v "" ^< requirements.txt') do set lines=%%i
if %lines%==0 (
    echo requirements.txt 文件为空，请添加需要安装的第三方包并重试。
    pause
    exit /b
)

REM 安装依赖
echo 安装依赖...
pip install -r requirements.txt

REM 检查 pip 安装结果
if %errorlevel% neq 0 (
    echo 安装依赖失败，请检查 requirements.txt 文件并重试。
    pause
    exit /b
)

start http://127.0.0.1:5000

REM 启动应用程序
echo 启动应用程序...
python app.py

REM 提示用户应用程序已启动
echo 应用程序已启动，请访问 http://127.0.0.1:5000

REM 保持命令提示符窗口打开
pause
