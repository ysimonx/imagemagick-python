python3 -m venv ./env
source ./env/bin/activate
 pip install --upgrade pip
pip install -r requirements.txt

wget "https://numerotelephone.com/images/entreprise/267/chubb.png" -O /tmp/logo_chubb.png
wget "http://www.lefilmfrancais.com/images/com_papyrus/06a6236ee1dac1113451012a4e83d4be.jpg" -O  /tmp/logo_canal.jpg
wget "https://www.pagesjaunes.fr/media/ugc/banque_casino_03306300_114003080?w=200&h=200&crop=true" -O  /tmp/logo_casino.jpg
wget "https://compagnonsdugout.fr/wp-content/uploads/2018/06/Boucherie-Chez-Jo-facade-13500-TRETS-1024x768.jpg" -O /tmp/boucherie-jo.jpg
python ./logo_resizer_square_trim_border.py  /tmp/logo_chubb.png
python ./logo_resizer_square_trim_border.py  /tmp/logo_canal.jpg
python ./logo_resizer_square_trim_border.py  /tmp/logo_casino.jpg

python ./logo_resizer_square_trim_border.py  /tmp/boucherie-jo.jpg