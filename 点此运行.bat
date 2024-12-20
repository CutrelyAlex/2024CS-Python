REM 打开默认浏览器并访问本地服务器地址
start http://127.0.0.1:5000 

REM 激活虚拟环境并运行 Flask 应用程序
cmd /k  ".\.venv\Scripts\activate && .\.venv\Scripts\python.exe app.py"
