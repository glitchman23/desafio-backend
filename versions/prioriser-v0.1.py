from ticket import Ticket
from json_worker import tickets_list

def prioriser():


    tickets = [Ticket(item["TicketID"], 
                      item["CategoryID"], 
                      item["CustomerID"], 
                      item["CustomerName"], 
                      item["CustomerEmail"], 
                      item["DateCreate"], 
                      item["DateUpdate"], 
                      item["Interactions"]) 
                for item in tickets_list]

    for issue in tickets:
        total_score = issue.text_kw_rating()+issue.sub_kw_rating()+issue.feeling_rating1()+issue.feeling_rating_last()
        issue.Rating += total_score

    prioridade = sorted(tickets, key=lambda ticket: ticket.Rating, reverse=True)
    for tick in prioridade:
        print(tick.Rating, tick.TicketID, tick.created_at(), tick.updated_at())


prioriser()