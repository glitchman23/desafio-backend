class Prioriser(object):

  def __init__(self, tickets):
    """
    Gerador de objeto
    """
    self.tickets = tickets

  def priority_setter(self):
    """
    Organiza a lista por ordem de rating do mais prioritário para o menos prioritário
    """
    for issue in self.tickets:
        total_score = issue.text_kw_rating()+issue.sub_kw_rating()+issue.feeling_rating1()+issue.feeling_rating_last()
        issue.Rating += round(total_score, 2)
        if total_score >1.5:
          issue.Priority = "Alta"
        else:
          issue.Priority = "Normal"
    return self.tickets
