email_tmpl = """
    ...: Olá, %(nome)s
    ...:
    ...: Teria interesse em comprar %(produto)s?
    ...:
    ...: Este produto é ótimo para resolver
    ...: %(texto)s
    ...:
    ...: Clique agora em %(link)s
    ...:
    ...: Apenas %(quantidade)d disponíveis!
    ...:
    ...: Preco promocional %(preco).2f
    ...: """

clientes = ["Matheus", "Loir", "Ana Carolina"]

for cliente in clientes:
    print(
        email_tmpl
        % { "nome": cliente,
            "produto": "caneta",
            "texto": "Escrever muito bem",
            "link": "https://canetaslegais.com",
            "quantidade":1,
            "preco":50.5,
        } 
    )
