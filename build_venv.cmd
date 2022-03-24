python -m venv venv
call ./venv/Scripts/activate

python -m pip install --upgrade pip

pip3 install opencv-python 
pip3 install numpy 
pip3 install matplotlib 
pip3 install black

pip3 freeze > ./requirements.txt

pause
deactivate