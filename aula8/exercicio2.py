
produto = {
    'nome': 'Notebook',
    'preco': 3500,
    'estoque': 15
}

produto.pop('estoque')
produto['preco'] = 4000

print(f"{produto['nome']}, R$ {produto['preco']}")
