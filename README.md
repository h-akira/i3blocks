# 環境構築
Arch Linuxの場合：
```
# 温度
sudo pacman -S lm_sensors
# ドル円をseleniumで取得するため
paru -S python-selenium
paru -S selenium-manager 
```
# 仮想環境
pacmanの更新をしたらseleniumがおかしくなったので、
暫定的な対応として`dollar.py`を実行するときに仮想環境を使うことにしており、以下が必要。
```
python -m venv ~/.python_venv
source ~/.python_venv/bin/activate
pip3 install selenium
```
