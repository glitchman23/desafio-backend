import nltk
from textblob import TextBlob
from string import punctuation

text =  "efetuei a compra de um produto e até agora nao foi entregue a mercadoria, no site de vcs nao consta o pedido como pendente, já veio debitada a compra na fatura do meu cartão, ja tentei de várias formas e não consigo soluçao, gostaria de resolver da melhor maneira possivel direto com a loja antes de tomar as providências cabíveis"

#Quebra o texto em frases e palavras
sentencas = nltk.tokenize.sent_tokenize(text, language='portuguese')
palavras = nltk.tokenize.word_tokenize(text.lower(), language='portuguese')

#Retira as palavras não analisáveis
stopwords = set(nltk.corpus.stopwords.words('portuguese') + list(punctuation))
palavras_sem_stopwords = [palavra for palavra in palavras if palavra not in stopwords]

string_limpa = " ".join(palavras_sem_stopwords)

#Analisa os sentimentos
texto_analise = TextBlob(string_limpa)
translate = TextBlob(str(texto_analise.translate(to='en')))

print(translate.sentiment)

