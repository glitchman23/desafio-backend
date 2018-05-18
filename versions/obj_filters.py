class TicketsSorter(object):
	def __init__(self, tickets_list):
		self.tickets_list = tickets_list

	def sort_by_ID(self):
		organizado = sorted(self.tickets_list, key=lambda ticket: ticket.TicketID, reverse=False)
		return organizado

	def sort_by_rating(self):
		organizado = sorted(self.tickets_list, key=lambda ticket: ticket.Rating, reverse=True)
		return organizado

	def sort_by_created_at(self):
		organizado = sorted(self.tickets_list, key=lambda ticket: ticket.created_at(), reverse=False)
		return organizado

	def sort_by_updated_at(self):
		organizado = sorted(self.tickets_list, key=lambda ticket: ticket.updated_at(), reverse=False)
		return organizado