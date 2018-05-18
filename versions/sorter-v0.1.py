import json
from json_worker import JsonObj
from bottle import request
from datetime import datetime

with open('desafio/tickets_updated.json', 'r+') as file:
    tickets_list_up = json.load(file)

class TicketsSorter(object):
    def __init__(self, tickets_list):
        """
        Gerador de objetos
        """
        self.tickets_list = tickets_list

    def sort_by_ID(self):
        """
        Organiza por ordem de ID
        """


        organizado = sorted(self.tickets_list, key=lambda ticket: ticket.TicketID, reverse=False)
        result = []
        for ticket in organizado:
            result.append(ticket.__dict__)
        return result

    def sort_by_rating(self):
        """
        Organiza por ordem de Rating
        """
        organizado = sorted(self.tickets_list, key=lambda ticket: ticket.Rating, reverse=True)
        result = []
        for ticket in organizado:
            result.append(ticket.__dict__)
        return result

    def sort_by_created_at(self):
        """
        Organiza por ordem de data de criação
        """
        organizado = sorted(self.tickets_list, key=lambda ticket: ticket.created_at(), reverse=False)
        result = []
        for ticket in organizado:
            result.append(ticket.__dict__)
        return result

    def sort_by_updated_at(self):
        """
        Organiza por ordem de data de update
        """
        
        organizado = sorted(self.tickets_list, key=lambda ticket: ticket.updated_at(), reverse=False)
        result = []
        for ticket in organizado:
            result.append(ticket.__dict__)
        return result

    def created_interval(self, interval1 = '2017-12-14 00:00:00', interval2 = '2018-05-17 00:00:00' ):

        format = "%Y-%m-%d %H:%M:%S"
        datetime_object1 = datetime.strptime(interval1, format)
        datetime_object2 = datetime.strptime(interval2, format)

        tickets = []
        for item in self.tickets_list:
            created_str = item.DateCreate
            created = datetime.strptime(created_str, format)
            if created > datetime_object1 and created < datetime_object2:
                tickets.append(item)
            else:
                pass

        return tickets


def order_filter(tickets_list, filter_by='', order_by='ID', page=0):
    lista = JsonObj(tickets_list).json_obj_updated()


    order_by_ID = TicketsSorter(lista).sort_by_ID()
    order_by_rating = TicketsSorter(lista).sort_by_rating()
    order_by_created = TicketsSorter(lista).sort_by_created_at()
    order_by_updated = TicketsSorter(lista).sort_by_updated_at()

    if order_by == 'rating':
        lista = order_by_rating
    elif order_by == 'created':
        lista = order_by_created
    elif order_by == 'updated':
        lista = order_by_updated
    else:
        lista = order_by_ID

    if request.query.page == '':
        page = 0
    else:
        page = int(request.query.page)

    if filter_by != '':
        if page > 0:
            tickets_requested = [ticket for ticket in lista if ticket['Priority'] == filter_by ]
            return { 'tickets' : tickets_requested[((page-1)*5):page*5] }
        else:
            tickets_requested = [ticket for ticket in lista if ticket['Priority'] == filter_by ]
            return { 'tickets' : tickets_requested }
    else:
        if page > 0:
            return { 'tickets' : lista[((page-1)*5):page*5] }
        else:
            return { 'tickets' : lista }