import nltk.corpus
import datetime
import re
from textblob import TextBlob
from nltk.tokenize import word_tokenize
from string import punctuation
from keywords import bad_keywords

stopwords = set(nltk.corpus.stopwords.words('portuguese') + list(punctuation))

#Entidade Ticket

class Ticket(object):
    def __init__(self, TicketID, CategoryID, CustomerID, CustomerName, CustomerEmail, DateCreate, DateUpdate, Interactions, Priority="Normal", Rating=0):
        """
        Gerador de objeto
        """
        self.TicketID = TicketID
        self.CategoryID = CategoryID
        self.CustomerID = CustomerID
        self.CustomerName = CustomerName
        self.CustomerEmail = CustomerEmail
        self.DateCreate = DateCreate
        self.DateUpdate = DateUpdate
        self.Interactions = Interactions
        self.Priority = Priority
        self.Rating = Rating
    
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

    ####### METODOS GERADORES DA PRIORIDADE #######

    def sub_kw_rating(self):
        """
        Estabelece a pontuação da prioridade do assunto baseado em palavra chave
        """
        peso = 0.8
        if self.whose_last_interaction() == "Customer":
            subject = self.Interactions[0]["Subject"].lower()
            if subject != "sem assunto":
                sub_tok = word_tokenize(subject, language='portuguese')
                sub_no_stop = [palavra for palavra in sub_tok if palavra not in stopwords]
                count = 0
                for raw_str in bad_keywords:
                    pat = re.compile(raw_str)
                    for w in sub_no_stop:
                        if pat.match(w):
                            count += 1
                if count == 0:
                    score = 0.6*peso
                    return score
                elif count == 1:
                    score = 1.4*peso
                    return score
                else:
                    score = 2*peso
                    return score
            else:
                return 0
        else:
            return 0

    def text_kw_rating(self):
        """
        Estabelece a pontuação da prioridade do texto da última interação baseado em palavra chave
        """
        peso = 1
        if self.whose_last_interaction() == "Customer":
            text = self.Interactions[-1]["Message"].lower()
            if text != "sem assunto":
                txt_tok = word_tokenize(text, language='portuguese')           
                txt_no_stop = [palavra for palavra in txt_tok if palavra not in stopwords]
                count = 0
                for raw_str in bad_keywords:
                    pat = re.compile(raw_str)
                    for w in txt_no_stop:
                        if pat.match(w):
                            count += 1
                if count == 0:
                    score = 0.6*peso
                    return score
                elif count == 1:
                    score = 1.4*peso
                    return score
                else:
                    score = 2*peso
                    return score
            else:
                return 0

        else:
            return 0

    def feeling_rating1(self):
        """
        Estabelece a pontuação da prioridade em relação ao sentimento na primeira interação
        """
        peso = 0.3
        texto = TextBlob(self.Interactions[0]["Message"])
        traducao = TextBlob(str(texto.translate(to='en')))
        sentimento = traducao.sentiment
        if sentimento[0] == 0:
            return 1*peso
        elif sentimento[0] > 0:
            score = 1-sentimento[0]
            return score*peso
        else:
            score = -sentimento[0]+1
            return score*peso

    def feeling_rating_last(self):
        """
        Estabelece a pontuação da prioridade em relação ao sentimento na última interação
        """
        peso = 0.5
        i = self.interactions_counter()-1
        while self.Interactions[i]["Sender"] != "Customer":
            i -= 1
        else:
            texto = TextBlob(self.Interactions[i]["Message"])
            traducao = TextBlob(str(texto.translate(to='en')))
            sentimento = traducao.sentiment
            if sentimento[0] == 0:
                return 1
            elif sentimento[0] > 0:
                score = 1-sentimento[0]
                return score*peso
            else:
                score = -sentimento[0]+1
                return score*peso
