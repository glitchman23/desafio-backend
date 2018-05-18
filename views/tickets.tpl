<!DOCTYPE html>
<html lang="pt">
<head>
	<meta charset="UTF-8">
	<title>Api Tickets</title>
	<link rel="stylesheet" type="text/css" href="/static/main.css">
</head>
<body>
	%for ticket in tickets:
	<section>
		<h1>Ticket</h1>			
		<h4>ID do Ticket: </h4>{{ ticket["TicketID"] }}<br>
		<h4>ID da Categoria: </h4>{{ ticket["CategoryID"] }}<br>
		<h4>ID do Cliente: </h4>{{ ticket["CustomerID"] }}<br>
		<h4>Nome do cliente: </h4>{{ ticket["CustomerName"] }}<br>
		<h4>Email: </h4>{{ ticket["CustomerEmail"] }}<br>
		<h4>Data da criação: </h4>{{ ticket["DateCreate"] }}<br>
		<h4>Última atualização: </h4>{{ ticket["DateUpdate"] }}<br>
		<h4>Prioridade: </h4>{{ ticket["Priority"] }}<br>
		<h4>Pontuação: </h4>{{ ticket["Rating"] }}<br>
		<h2>Interações</h2>
			% for i in range(0, len(ticket["Interactions"])):
			<div class="interaction">
				<h4>Enviado por: </h4>{{ ticket["Interactions"][i]["Sender"] }}<br>
				<h4>Data: </h4>{{ ticket["Interactions"][i]["DateCreate"] }}<br>
				<h4>Assunto: </h4>{{ ticket["Interactions"][i]["Subject"] }}<br>
				<h4>Mensagem: </h4>{{ ticket["Interactions"][i]["Message"] }}<br><br>
			</div>
			% end
	</section>
	% end
</body>
</html>