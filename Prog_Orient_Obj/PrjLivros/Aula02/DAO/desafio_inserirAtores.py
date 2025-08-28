from autores_dao import autores, autoresDAO

A = autores()
A.nome_autor = input("Insira o nome do autor a ser adicionado:")

dao = autoresDAO()
dao.inserir(A)
print(f"Novo autor de código {A.cod_autor} inserido.")