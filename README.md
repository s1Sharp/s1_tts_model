pip install git+https://github.com/s1Sharp/s1-tts-model --force --extra-index-url https://download.pytorch.org/whl/cpu

pip3 install -r requirements.txt --extra-index-url https://download.pytorch.org/whl/cpu

cd /tmp && git clone https://github.com/s1Sharp/s1-tts-model && \
pip3 install -e /tmp/s1-tts-model --extra-index-url https://download.pytorch.org/whl/cpu