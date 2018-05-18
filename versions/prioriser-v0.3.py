import nltk.corpus
import re
from textblob import TextBlob
from nltk.tokenize import word_tokenize
from string import punctuation
from keywords import bad_keywords

stopwords = set(nltk.corpus.stopwords.words('portuguese') + list(punctuation))


class Prioriser(object):

  def __init__(self, ticket):
    """
    Gerador de objeto, recebe um objeto ticket
    """
    self.ticket = ticket

  def sub_kw_rating(self):
      """
      Estabelece a pontuação da prioridade do assunto baseado em palavra chave
      """
      peso = 0.8
      if self.ticket.whose_last_interaction() == "Customer":
          subject = self.ticket.Interactions[0]["Subject"].lower()
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
      if self.ticket.whose_last_interaction() == "Customer":
          text = self.ticket.Interactions[-1]["Message"].lower()
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
      texto = TextBlob(self.ticket.Interactions[0]["Message"])
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
      i = self.ticket.interactions_counter()-1
      while self.ticket.Interactions[i]["Sender"] != "Customer":
          i -= 1
      else:
          texto = TextBlob(self.ticket.Interactions[i]["Message"])
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

  def priority_setter(self):
      """
      Organiza a lista por ordem de rating do mais prioritário para o menos prioritário
      """
      total_score = self.text_kw_rating()+self.sub_kw_rating()+self.feeling_rating1()+self.feeling_rating_last()
      self.ticket.Rating += round(total_score, 2)
      if total_score >1.5:
        self.ticket.Priority = "Alta"
      else:
        self.ticket.Priority = "Normal"

      return self.ticket.Priority, self.ticket.Rating
