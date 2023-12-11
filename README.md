# Assistente-Amplia
Um assistente de pagamentos para auxiliar nas tarefas administrativo financeiras do Amplia FGV.

## Como usar
Para usar o assistente, primeiro é necessário instalar as dependências do projeto. Para isso, execute o seguinte comando no terminal:
```
pip install -r requirements.txt
```

Além disso, é necessário ter o arquivo de credenciais do Firebase (`serviceAccountKey.json`). Com este arquivo em mãos, basta colocá-lo na raíz do projeto.

Por fim, podemos seguir para a execução do assistente. Disponibilizamos um `Makefile` para facilitar a execução do projeto. Abaixo disponibilizamos o tutorial de como executar o assistente em cada sistema operacional (SO - ubuntu e windows).

### Ubuntu
Se você estiver utilizando o SO Ubuntu, para executar o assistente basta executar o seguinte comando no terminal:
```
make run
```

Isto irá executar o assistente no `localhost`, basta acessar o link que aparecerá no terminal.

Para executar os testes, basta executar o seguinte comando no terminal:
```
make test
```

### Windows
Se você estiver utilizando o SO Windows, para executar o assistente basta executar o seguinte comando no terminal:
```
python -m streamlit run src/interface/login.py
```

Isto irá executar o assistente no `localhost`, basta acessar o link que aparecerá no terminal.

Para executar os testes, basta executar o seguinte comando no terminal:
```
python -m unittest discover -s tests -p "*.py"
```

### Observações
Para utilizar o assistente, é necessário realizar o login com o e-mail e senha de uma conta cadastrada na base de dados do Firebase. Se você não possui uma conta, entre em contato com o administrador do sistema.
