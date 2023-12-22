## Cadastro

### Pré-requisitos

Certifique-se de que as dependências de desenvolvimento Python estejam instaladas:

```
sudo apt-get install build-essential python3-dev libpq-dev
```

Instale a ferramenta cross-env globalmente:

```
npm install --global cross-env
```

Recomendamos o uso de um ambiente virtual para isolar as dependências do projeto.
Para configurar um ambiente virtual, execute os seguintes comandos: (https://docs.python.org/3/library/venv.html)

```
python3 -m virtualenv venv

source venv/bin/activate
```

### Instalação do Projeto

Com o ambiente virtual ativado, instale as dependências do projeto:

```
pip install -r requirements.txt
pip install -r requirements-dev.txt
```

### Configuração das Variáveis de Ambiente
Verifique as variáveis de ambiente necessárias no arquivo .env.example e crie um arquivo chamado .env na raiz do projeto para configurá-las. As informações podem ser obtidas no Portainer.

Nota: Não compartilhe informações sensíveis publicamente.

### Execução Local

Para executar o projeto localmente, são necessários dois terminais.

**Terminal 1**: Inicie o servidor Django para renderizar as páginas:
```
python manage.py runserver
```

**Terminal 2**: S Inicie o script Node.js responsável por compilar o TailwindCSS. Certifique-se de usar a versão 18 do Node:
```
nvm use 18

cd theme/

npm i

npm run dev
```

Acesse o projeto em http://127.0.0.1:8000/

## Capacitação Moodle

Utilizamos a plataforma Moodle para realizar a capacitação das voluntárias (psicólogas e advogadas). As orientações sobre modificações na plataforma estão [nessa documentação](https://github.com/mapadoacolhimento/cadastro/tree/feature/moodle-training/moodle-training).

## Static Analysis

### Format

Execute o seguinte comando para formatar todos os arquivos .py:

```bash
black . --extend-exclude="/(theme|cypress|\.github|moodle-training|deploy|migrations)/"
```

### Linting

Execute o seguinte comando para realizar a análise estática dos arquivos .py:

```bash
pylint --load-plugins pylint_django --django-settings-module=project.settings --rcfile=.pylintrc  $(git ls-files '*.py')
```

## Migrações

### Configuração do Banco de Dados Local

Antes de publicar alterações nos bancos de STG ou PROD, altere a variável de ambiente DATABASE_URL para a URI do seu banco local.

### Execução das Migrações

Ao fazer alterações nos arquivos models do seu aplicativo, crie uma migração para registrar essas alterações:

```bash
python manage.py makemigrations --name [nome da sua migration]
```

Após rodar esse comando, um arquivo será gerado dentro da pasta `[app name]/migrations`.

Em seguida, aplique as alterações no banco de dados:

```bash
python manage.py migrate
```
