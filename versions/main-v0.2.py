from json_worker import JsonObj
from obj_filters import TicketsSorter
from bottle import run, get, route, request, response, template, static_file


lista = JsonObj('desafio/tickets_updated.json').json_obj()

order_by_ID = TicketsSorter(lista).sort_by_ID()
order_by_rating = TicketsSorter(lista).sort_by_rating()
order_by_created = TicketsSorter(lista).sort_by_created_at()
order_by_updated = TicketsSorter(lista).sort_by_updated_at()


@route('/static/<filename>')
def server_static(filename):
    return static_file(filename, root='/home/glitchman/dev/neotest/static/')

@get('/')
def index():
    return template('index')

@get('/tickets.json')
def tickets_json():

    
    filter_by = request.query.filter_by

    if request.query.order_by == '':
        order_by = 'ID'
    else:
        order_by = request.query.order_by

    if request.query.page == '':
        page = 0
    else:
        page = int(request.query.page)

    if order_by == 'rating' and page >= 0:
        if filter_by != '':
            if page > 0:
                tickets_requested = [ticket for ticket in order_by_rating if ticket['Priority'] == filter_by ]
                return { 'tickets' : tickets_requested[((page-1)*5):page*5] }
            else:
                tickets_requested = [ticket for ticket in order_by_rating if ticket['Priority'] == filter_by ]
                return { 'tickets' : tickets_requested }
        else:
            if page > 0:
                return { 'tickets' : order_by_rating[((page-1)*5):page*5] }
            else:
                return { 'tickets' : order_by_rating }

    elif order_by == 'created' and page >= 0:
        if filter_by != '':
            if page > 0:
                tickets_requested = [ticket for ticket in order_by_created if ticket['Priority'] == filter_by ]
                return { 'tickets' : tickets_requested[((page-1)*5):page*5] }
            else:
                tickets_requested = [ticket for ticket in order_by_created if ticket['Priority'] == filter_by ]
                return { 'tickets' : tickets_requested }
        else:
            if page > 0:
                return { 'tickets' : order_by_created[((page-1)*5):page*5] }
            else:
                return { 'tickets' : order_by_created }

    elif order_by == 'updated' and page >= 0:
        if filter_by != '':
            if page > 0:
                tickets_requested = [ticket for ticket in order_by_updated if ticket['Priority'] == filter_by ]
                return { 'tickets' : tickets_requested[((page-1)*5):page*5] }
            else:
                tickets_requested = [ticket for ticket in order_by_updated if ticket['Priority'] == filter_by ]
                return { 'tickets' : tickets_requested }
        else:
            if page > 0:
                return { 'tickets' : order_by_updated[((page-1)*5):page*5] }
            else:
                return { 'tickets' : order_by_updated }

    elif order_by == 'ID' and page >= 0:
        if filter_by != '':
            if page > 0:
                tickets_requested = [ticket for ticket in order_by_ID if ticket['Priority'] == filter_by ]
                return { 'tickets' : tickets_requested[((page-1)*5):page*5] }
            else:
                tickets_requested = [ticket for ticket in order_by_ID if ticket['Priority'] == filter_by ]
                return { 'tickets' : tickets_requested }
        else:
            if page > 0:
                return { 'tickets' : order_by_ID[((page-1)*5):page*5] }
            else:
                return { 'tickets' : order_by_ID }

@get('/ticket/<ID:int>.json')
def ticket(ID=0):
    ticket_requested = [ticket for ticket in order_by_ID if ticket['TicketID'] == ID]
    return { 'Tickets' : ticket_requested[0] }

'''
#########  TEMPLATES  #########
'''

@get('/tickets')
def get_tickets():
    order_by = request.query.order_by
    if request.query.page == '':
        page = 0
    else:
        page = int(request.query.page)
    
    if order_by == 'rating' and page > 0:
        return template('tickets', tickets=order_by_rating[((page-1)*5):page*5])
    elif order_by == 'rating':
        return template('tickets', tickets=order_by_rating)

    elif order_by == 'created' and page > 0:
        return template('tickets', tickets=order_by_created[((page-1)*5):page*5])
    elif order_by == 'created':
        return template('tickets', tickets=order_by_created)

    elif order_by == 'updated' and page > 0:
        return template('tickets', tickets=order_by_updated[((page-1)*5):page*5])
    elif order_by == 'updated':
        return template('tickets', tickets=order_by_updated)

    elif order_by == 'ID' and page > 0:
        return template('tickets', tickets=order_by_ID[((page-1)*5):page*5])
    else:
        return template('tickets', tickets=order_by_ID)

@get('/ticket')
@get('/ticket/<ID:int>')
def ticket(ID=order_by_ID[0]['TicketID']):
    ticket_requested = [ticket for ticket in order_by_ID if ticket['TicketID'] == ID]
    return template('ticket', ticket=ticket_requested[0])


if __name__ == '__main__':
    run(reloader=True, debug=True)
