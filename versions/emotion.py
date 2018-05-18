from textblob import TextBlob

texto =  "efetuei a compra de um produto e até agora nao foi entregue a mercadoria, no site de vcs nao consta o pedido como pendente, já veio debitada a compra na fatura do meu cartão, ja tentei de várias formas e não consigo soluçao, gostaria de resolver da melhor maneira possivel direto com a loja antes de tomar as providências cabíveis"

frase = TextBlob(texto)

traducao = TextBlob(str(frase.translate(to='en')))

sentimento = traducao.sentiment
print(sentimento[0])
