@echo off
echo Checking for existing virtual environment...
if exist venv (
    echo Existing virtual environment removed.
    rmdir /s /q venv
)

echo Creating virtual environment...
python -m venv venv

echo Activating virtual environment...
call venv\Scripts\activate

echo Updating pip...
python -m pip install --upgrade pip

echo Installing requirements...
pip install -r requirements.txt

echo Venv successfully configured!