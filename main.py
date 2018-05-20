from obj_filters import TicketsSorter, order_filter, tickets_list_up
from bottle import run, get, route, request, template, static_file


@route('/static/<filename>')
def server_static(filename):
    return static_file(filename, root='/home/glitchman/dev/desafio_neo/desafio-backend/static/')

@get('/')
def index():
    return template('index')

@get('/tickets.json')
def tickets_json():
    filter_by = request.query.filter_by
    order_by = request.query.order_by
    page = request.query.page
    interval1 = request.query.start
    interval2 = request.query.end
    return order_filter(tickets_list_up, filter_by, order_by, page, interval1, interval2)


@get('/ticket/<ID:int>.json')
def ticket(ID=0):
    ordered = order_filter(tickets_list_up)
    ticket_requested = [ticket for ticket in ordered['tickets'] if ticket['TicketID'] == ID]
    return { 'Tickets' : ticket_requested[0] }


    

#########  TEMPLATES  #########


@get('/tickets')
def get_tickets():
    filter_by = request.query.filter_by
    order_by = request.query.order_by
    page = request.query.page
    interval1 = request.query.start
    interval2 = request.query.end
    temp = order_filter(tickets_list_up, filter_by, order_by, page, interval1, interval2)
    return template('tickets', tickets=temp['tickets'])


@get('/ticket')
@get('/ticket/<ID:int>')
def ticket(ID=0):
    ordered = order_filter(tickets_list_up)
    ticket_requested = [ticket for ticket in ordered['tickets'] if ticket['TicketID'] == ID]
    return template('ticket', ticket=ticket_requested[0])



if __name__ == '__main__':
    run(reloader=True, debug=True)
