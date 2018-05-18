import datetime

#Entidade Ticket

class Ticket(object):
    def __init__(self, TicketID, CategoryID, CustomerID, CustomerName, CustomerEmail, DateCreate, DateUpdate, Interactions, Priority="normal", Rating=0):
        """
        Gerador de objeto, recebe os parametros do objeto
        """
        self.TicketID = TicketID
        self.CategoryID = CategoryID
        self.CustomerID = CustomerID
        self.CustomerName = CustomerName
        self.CustomerEmail = CustomerEmail
        self.DateCreate = DateCreate
        self.DateUpdate = DateUpdate
        self.Priority = Priority
        self.Rating = Rating
        self.Interactions = Interactions

    def interactions_counter(self):
        """
        Retorna quantas interações aconteceram
        """
        interactions_count = len(self.Interactions)
        return interactions_count
    
    def whose_last_interaction(self):
        """
        Retorna quem fez a ultima interação
        """
        last_interactor = self.Interactions[-1]["Sender"]
        return last_interactor

    def created_at(self):
        """
        Retorna a data como objeto
        """
        created_at = self.DateCreate
        format = "%Y-%m-%d %H:%M:%S"

        datetime_object = datetime.datetime.strptime(created_at, format)
        return datetime_object

    def updated_at(self):
        """
        Retorna a data como objeto
        """
        updated_at = self.DateUpdate
        format = "%Y-%m-%d %H:%M:%S"

        datetime_object = datetime.datetime.strptime(updated_at, format)
        return datetime_object