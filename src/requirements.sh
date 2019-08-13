virtualenv env/venv
python3 -m venv .env
source .env/bin/activate
pip3 install pandas
pip3 install -U spacy
python3 -m spacy download en
python3 -m spacy download pt
python3 -m spacy download xx