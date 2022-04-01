python -m venv venv
.\venv\Scripts\activate

python -m pip install --upgrade pip

pip3 install opencv-python 
pip3 install numpy 
pip3 install matplotlib
pip3 install Pillow
pip3 install black
pip3 install pytest

pip install -e ./src/

pause
deactivate