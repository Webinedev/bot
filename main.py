import time, json
from iqoptionapi.stable_api import IQ_Option

# Testando conexão com a API
Teste=IQ_Option("nautico700@gmail.com","capiberibe")
Teste.connect()#connect to iqoption
status = Teste.check_connect()

# Seleção do mercado
goal="EURUSD"

# Exibição das velas (candles)
print("get candles")
print(json.dumps(Teste.get_candles(goal,60,10,time.time()), indent=1))