<<<<<<< HEAD
# Considerações sobre as estratégias utilizadas

Segue a abordagem que utilizei para priorizar os atendimentos

## Parâmentros de análise: Em ordem de prioridade
	- Último personagem a interagir
	- Palavras-chave no assunto da primeira interação
	- Palavras-chave no texto da última interação
	- Sentimento no texto da primeira interação
	- Sentimento no texto da última interação

### Implementações previstas:
	- Últimas emoções nas interações do cliente com a empresa

### Evolução do algoritmo 
	- Uso de dados massivos para criar funções dinâmicas que melhor representem o peso das prioridades de maneira mais assertiva

## Ambiente de desenvolvimento

Linguagem: Python 3.6.5 :: Anaconda, Inc.
Framework para API: Bottle v0.12.13
Enviroment: Miniconda
# Name                    Version                   Build
asn1crypto                0.24.0                   py36_0  
ca-certificates           2018.03.07                    0  
certifi                   2018.4.16                py36_0  
cffi                      1.11.5           py36h9745a5d_0  
chardet                   3.0.4            py36h0f667ec_1  
cryptography              2.2.2            py36h14c3975_0  
idna                      2.6              py36h82fb2a8_1  
libedit                   3.1                  heed3624_0  
libffi                    3.2.1                hd88cf55_4  
libgcc-ng                 7.2.0                hdf63c60_3  
libstdcxx-ng              7.2.0                hdf63c60_3  
ncurses                   6.0                  h9df7e31_2  
nltk                      3.3                       <pip>
numpy                     1.14.3                    <pip>
openssl                   1.0.2o               h20670df_0  
pip                       10.0.1                   py36_0  
pycosat                   0.6.3            py36h0a5515d_0  
pycparser                 2.18             py36hf9f622e_1  
pyopenssl                 17.5.0           py36h20ba746_0  
pysocks                   1.6.8                    py36_0  
python                    3.6.5                hc3d631a_0  
readline                  7.0                  ha6073c6_4  
requests                  2.18.4           py36he2e5f8d_1  
ruamel_yaml               0.15.35          py36h14c3975_1  
setuptools                39.0.1                   py36_0  
six                       1.11.0           py36h372c433_1  
sqlite                    3.23.1               he433501_0  
textblob                  0.15.1                    <pip>
tk                        8.6.7                hc745277_3  
urllib3                   1.22             py36hbe7ace6_0  
wheel                     0.31.0                   py36_0  
xz                        5.2.3                h55aa19d_2  
yaml                      0.1.7                had09818_2  
zlib                      1.2.11               ha838bed_2  


## Instruções de uso da API

### Para solicitar os json's dos tickets temos:

		Todos		/tickets.json
		Por ID		/ticket/<ID>.json

### Para acessar as views:
		
		Todos		/tickets
		Por ID		/ticket/<ID>

###Paga organizar e filtrar (elas podem ser usadas juntas ou independentes)

#### filter_by						e.g.
Alta, Normal 						/tickets.json?filter_by=Alta

#### order_by
ID, rating, created, updated 		/tickets.json?order_by=rating

#### page
Número da página					/tickets.json?page=1

#### interval1
"Y-m-d H:M:S"						/tickets.json?interval1=1988-10-09%2000:00:00

#### interval2
"Y-m-d H:M:S"						/tickets.json?interval2=2100-01-01%2000:00:00

=======
# Desafio desenvolvedor backend

Precisamos melhorar o atendimento no Brasil, para alcançar esse resultado, precisamos de um algoritmo que classifique
nossos tickets (disponível em tickets.json) por uma ordem de prioridade, um bom parâmetro para essa ordenação é identificar o humor do consumidor.
Pensando nisso, queremos classificar nossos tickets com as seguintes prioridade: Normal e Alta.

### São exemplos:

### Prioridade Alta:
- Consumidor insatisfeito com produto ou serviço
- Prazo de resolução do ticket alta
- Consumidor sugere abrir reclamação como exemplo Procon ou ReclameAqui
    
### Prioridade Normal
- Primeira iteração do consumidor
- Consumidor não demostra irritação

Considere uma classificação com uma assertividade de no mínimo 70%, e guarde no documento (Nosso json) a prioridade e sua pontuação.

### Com base nisso, você precisará desenvolver:
- Um algoritmo que classifique nossos tickets
- Uma API que exponha nossos tickets com os seguintes recursos
  - Ordenação por: Data Criação, Data Atualização e Prioridade
  - Filtro por: Data Criação (intervalo) e Prioridade
  - Paginação
        
### Escolha as melhores ferramentas para desenvolver o desafio, as únicas regras são:
- Você deverá fornecer informações para que possamos executar e avaliar o resultado;
- Poderá ser utilizado serviços pagos (Mas gostamos bastante de projetos open source)
    
### Critérios de avaliação
- Organização de código;
- Lógica para resolver o problema (Criatividade);
- Performance
    
### Como entregar seu desafio
- Faça um Fork desse projeto, desenvolva seu conteúdo e informe no formulário (https://goo.gl/forms/5wXTDLI6JwzzvOEg2) o link do seu repositório
>>>>>>> d01926f136fadd022a0f0ce2d189a356ac4017c2
