from json_worker import JsonObj
from obj_filters import TicketsSorter
from datetime import datetime
import json

with open('desafio-backend/tickets.json', 'r+') as file:
	tickets_list = json.load(file)

with open('desafio-backend/tickets_updated.json', 'r+') as file:
	tickets_list_up = json.load(file)


##### Priorizador
#JsonObj(tickets_list).json_priorise()

##### Tranforma a lista de dicts em lista do objetos
#lista = JsonObj(tickets_list_up).json_obj_updated()


######  TESTES ########
"""
sort = TicketsSorter(lista).sort_by_rating()

for x in sort:
	print(x['TicketID'], x['Rating'], x['Interactions'][-1]['Sender'])
"""
