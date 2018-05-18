from json_worker import JsonObj
from obj_filters import TicketsSorter
from bottle import run, get, route, template

#JsonObj('desafio/tickets.json').json_priorise()


lista = JsonObj('desafio/tickets_updated.json').json_obj()
sort = TicketsSorter(lista).sort_by_rating()

tickets = []
for ticket in sort:
	tickets.append(ticket.__dict__)

@route('/')
def index():
	return template('index')

@get('/tickets')
def getAllTickets():
    return tickets[0]

if __name__ == '__main__':
	run(reloader=True, debug=True)
