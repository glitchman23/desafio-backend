import json
from ticket import Ticket
from prioriser import Prioriser

class JsonObj(object):
	def __init__(self, tickets):
		"""
		Gerador de obejtos
		"""
		self.tickets = tickets

	def json_obj(self):
		"""
		Tranforma o jason em uma lista de ticketss
		"""
		if type(self.tickets) is list:
			objects = [Ticket(item["TicketID"], 
			                  item["CategoryID"], 
			                  item["CustomerID"], 
			                  item["CustomerName"], 
			                  item["CustomerEmail"], 
			                  item["DateCreate"], 
			                  item["DateUpdate"], 
			                  item["Interactions"]) 
			            for item in self.tickets]
			return objects
		else:
			objects = [Ticket(self.tickets["TicketID"], self.tickets["CategoryID"], self.tickets["CustomerID"], self.tickets["CustomerName"], self.tickets["CustomerEmail"], self.tickets["DateCreate"], self.tickets["DateUpdate"], self.tickets["Interactions"])]
			return objects

	def json_obj_updated(self):
		"""
		Tranforma o jason em uma lista de ticketss
		"""
		if type(self.tickets) is list:
			objects = [Ticket(item["TicketID"], 
			                  item["CategoryID"], 
			                  item["CustomerID"], 
			                  item["CustomerName"], 
			                  item["CustomerEmail"], 
			                  item["DateCreate"], 
			                  item["DateUpdate"], 
			                  item["Interactions"],
			                  item["Priority"],
			                  item["Rating"]) 
			            for item in self.tickets]
			return objects
		else:
			objects = [Ticket(self.tickets["TicketID"], self.tickets["CategoryID"], self.tickets["CustomerID"], self.tickets["CustomerName"], self.tickets["CustomerEmail"], self.tickets["DateCreate"], self.tickets["DateUpdate"], self.tickets["Interactions"], self.tickets["Priority"], self.tickets["Rating"])]
			return objects

	def json_priorise(self):
		"""
		Insere a prioridade no Json
		"""
		tickets = self.json_obj()
		json_new = []
		for ticket in tickets:
			Prioriser(ticket).priority_setter()
			json_new.append(ticket.__dict__)

		with open('desafio-backend/tickets_updated.json', 'w') as outfile:
		    json.dump(json_new, outfile, ensure_ascii=False, indent=2)