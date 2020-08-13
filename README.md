# QRCode Generator - Globo Brasília.

### Introdução

Um projeto feito em Django.

### Objetivo

O Site de Geração de QRCode do STF foi criado pela equipe de tecnologia da Globo Brasília para automatizar o processo de geração de QR Code para os produtos da Globo Brasília G1 e GE, além de manter uma DB com as URLs linkadas.

### Como rodar e como funciona

Para **visualizar e testar** o site, bem como suas funcionalidades, insira o seguinte comando no terminal:

```sh
docker-compose up --build -d
```

Se já está "buildado":

```sh
docker-compose up -d
```

O site estará disponível em:

http://localhost:8000

Para criar um super usuário, ou usuário administrador, os seguintes comandos devem ser feitos:

```sh
docker-compose exec web bash
```

Então, você estará no bash do container web. Use os comandos do django para criar um superusuário:

```sh
python manage.py createsuperuser
```

Após criar o usuário administrador, saia do bash com CTRL+D. Acesse a página de admin do Django com:

http://localhost:8000/admin



### Debug

Para ver o que está acontecendo:

```sh
docker-compose logs
```
