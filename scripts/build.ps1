python -m venv .venv
pip install -U pip
.venv\Scripts\Activate.ps1
pip install -r requirements.txt
New-Item "build" -Itemtype directory
Set-Location .\build
pyinstaller ..\src\main.py -F -w --clean -n "Snake"
Copy-Item ..\assets -Recurse .\dist
