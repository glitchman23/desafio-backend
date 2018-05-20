# Priorisador de tickets e API

## Parâmetros de análise: Em ordem de prioridade
- Último personagem a interagir
- Palavras-chave no texto da última interação
- Palavras-chave no assunto da primeira interação
- Sentimento no texto da última interação
- Sentimento no texto da primeira interação

### Implementações previstas
- Últimas emoções nas interações do cliente com a empresa

### Evolução do algoritmo 
- Uso de dados massivos para criar funções dinâmicas que melhor representem o peso das prioridades de maneira mais assertiva

### Melhorias no código
- Reescrever a classe TicketsSorter, simplificando e mergindo as funções no arquivo obj_filters.py
- Examinar bibliotecas em uso e criar ambiente enxuto

## Ambiente de desenvolvimento

- Linguagem: Python 3.6.5 :: Anaconda, Inc.
- Framework para API: Bottle v0.12.13
- Enviroment: Miniconda (olhar o arquivo spec-file.txt)

## Instruções de uso da API

### Para solicitar os json's dos tickets temos:

Todos

	/tickets.json
Por ID

	/ticket/<ID>.json

### Para acessar as views
		
Todos	

	/tickets

Por ID

	/ticket/<ID>

### Para organizar e filtrar

#### filter_by
	Possíveis parâmetros: "Alta", "Normal" 
	Default: None (sem filtros)

Ex:

	/tickets.json?filter_by=Alta
Retorna todos os tickets com prioridade alta										

#### order_by
	"ID", "rating", "created", "updated" 
	Default: "ID"

Ex:	

	/tickets.json?order_by=rating
Retorn os tickets organizados por rating descendente (mais prioritário para menos prioritário)

#### page
	Número da página
	Default: page=0 (Retona todos os tickets)

Ex:

	/tickets.json?page=1							
Retorna os 5 tickets por página

#### start
	"Y-m-d H:M:S"
Default: '1900-01-01 00:00:00'

Ex:

	/tickets.json?start=1988-10-09%2000:00:00
Retorna os tickets com a data de criação a partir de 1988-10-09 00:00:00

#### end
	"Y-m-d H:M:S"
	Default: '2100-01-01 00:00:00'

Ex:

	/tickets.json?end=2100-01-01%2000:00:00
Retorna os tickets com a data de criação até 2100-01-01 00:00:00

## OBS

Para invocar o arquivo estático om o css colocar o caminho absoluto até o arquivo em: main.py

	@route('/static/<filename>')
	def server_static(filename):
    	return static_file(filename, root='/path/to/directory/static/')