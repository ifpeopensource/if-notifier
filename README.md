<h1 align="center">
	IF Notifier
</h1>

<p align="center">
  <img alt="Contador de linguagens" src="https://img.shields.io/github/languages/count/ifpeopensource/if-notifier?color=%2304D361">

  <img alt="Tamanho do repositório" src="https://img.shields.io/github/repo-size/ifpeopensource/if-notifier">
	
  <a href="https://www.github.com/gvinfinity">
    <img alt="Feito por Gvinfinity)" src="https://img.shields.io/badge/Feito%20por-Gvinfinity-%2304D361">
  </a>



  <a href="https://ifpeopensource.com.br">
    <img src="https://img.shields.io/badge/IFPE Open Source-0a0a0a?logo=data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCAyNTUgMjUyIj48ZGVmcz48c3R5bGU+LmNscy0xe2ZpbGw6IzJmOWU0MTt9LmNscy0ye2ZpbGw6I2M4MTkxZTt9PC9zdHlsZT48L2RlZnM+PHRpdGxlPkJyYW5kIElGUEUgT3BlbiBTb3VyY2U8L3RpdGxlPjxnIGlkPSJMb2dvbWFyayI+PGcgaWQ9IkxvZ29tYXJrLTIiIGRhdGEtbmFtZT0iTG9nb21hcmsiPjxyZWN0IGNsYXNzPSJjbHMtMSIgeD0iMTQyLjMiIHk9IjEwLjUyIiB3aWR0aD0iMTA3LjIiIGhlaWdodD0iMTA3LjIiIHJ4PSI5Ii8+PHJlY3QgY2xhc3M9ImNscy0xIiB4PSIxNDIuMyIgeT0iMTM5LjE2IiB3aWR0aD0iMTA3LjIiIGhlaWdodD0iMTA3LjIiIHJ4PSI5Ii8+PHJlY3QgY2xhc3M9ImNscy0xIiB4PSIxMy42NiIgeT0iMTM5LjE2IiB3aWR0aD0iMTA3LjIiIGhlaWdodD0iMTA3LjIiIHJ4PSI5Ii8+PGcgaWQ9Ik9wZW5fU291cmNlX1N5bWJvbCIgZGF0YS1uYW1lPSJPcGVuIFNvdXJjZSBTeW1ib2wiPjxwYXRoIGNsYXNzPSJjbHMtMiIgZD0iTTY2LjczLDUuNjRBNjAuODUsNjAuODUsMCwwLDAsNDQuOSwxMjMuM2EzLjc0LDMuNzQsMCwwLDAsMy0uMTMsMy44NSwzLjg1LDAsMCwwLDItMi4yOUw2MS4zMSw4NC40MkEzLjgxLDMuODEsMCwwLDAsNTkuNTIsODAsMTUuMjMsMTUuMjMsMCwxLDEsNzQsODBhMy44LDMuOCwwLDAsMC0xLjc5LDQuNDdsMTEuNDIsMzYuNDZhMy44NCwzLjg0LDAsMCwwLDIsMi4zLDMuOTEsMy45MSwwLDAsMCwxLjY2LjM4LDQsNCwwLDAsMCwxLjM2LS4yNUE2MC44NSw2MC44NSwwLDAsMCw2Ni43Myw1LjY0WiIvPjwvZz48L2c+PC9nPjwvc3ZnPg=="></img>
  </a>

  <a href="https://github.com/ifpe-open-source/if-notifier/commits/master">
    <img alt="Último commit" src="https://img.shields.io/github/last-commit/ifpeopensource/if-notifier">
  </a>

  <a href="https://github.com/ifpe-open-source/modelo/issues">
    <img alt="Issues" src="https://img.shields.io/github/issues/ifpeopensource/if-notifier">
  </a>
  <a href="https://github.com/ifpe-open-source/modelo/blob/master/LICENSE" target="_blank">
    <img alt="License" src="https://img.shields.io/badge/licença-MIT-brightgreen"/>
  </a>
</p>

## Projeto

Esse bot :robot: foi feito como uma forma de deixar os estudantes que utilizam discord sempre atualizados nas notícias de seu campus. Envia novas notícias do site do IFPE para os canais de anuncio dos servidores para sempre mantê-los atualizados ⏫. 

## Dependências

Para utilizar o bot você precisa das bibliotecas:
<ul>
	<li><a href="https://github.com/Rapptz/discord.py">Discord.py</a></li>
	<li><a href="https://pypi.org/project/beautifulsoup4/">BeautifulSoap4</a></li>
	
</ul>

## Tutorial de instalação

O bot foi criado como um repl do site [Replit](https://replit.com) e utiliza a feature de Banco de Dados do site, portanto o ideal é que o mesmo seja feito para testes locais. Apesar que você está livre para implementar um banco de dados em forma de arquivo.

<ol>
	<li>Crie um fork para o repositório</li>
	<li>Faça login no site [Replit](https://replit.com)</li>
	<li>Crie um Repl para o bot importando do Github</li>
	<li>Selecione a linguagem como <img src="https://www.python.org/favicon.ico" width="15px"/>Python e o comando como <code>python main.py</code></li>
	<li>Na aba de Secrets adicione o token de bot com a key:<code>DISCORD-BOT-TOKEN</code></li>
</ol>

##### Adquirindo token e link para bot do discord
<ul>
	<li>Vá até o site de [desenvolvedores do discord](https://discord.com/developers/applications)</li>
	<li>Clique no botão <code>New Application</code> e dê um nome para o seu aplicativo</li>
	<li>Siga para a aba de <code>Bot</code> e então clique em <code>Add Bot</code></li>
	<li>Ative os seletores para "Presence Intent" e "Server Member Intents"</li>
	<li>Na seção de token clique para copiar e pegue o seu token</li>
	<li>Vá então para a aba <code>OAuth2</code></li>
	<li>Marque os escopos de <code>bot,applications.commands</code></li>
	<li>Marque as seguintes permissões:
	<ul>
		<li>View Channels</li>
		<li>Send Messages</li>
		<li>Manage Messages</li>
		<li>Embed Links</li>
		<li>Attach Files</li>
		<li>Read Message History</li>
	</ul>
	<li>Por fim, clique no botão <code>Copy</code> para pegar o link para adicionar o bot ao seu servidor</li>
	</li>
</ul>

## Time

Este projeto é mantido pelas seguintes pessoas e por esses [incríveis contribuidores](https://github.com/ifpe-open-source/if-notifier/graphs/contributors).

| <a href="https://github.com/gvinfinity"><img src="https://avatars.githubusercontent.com/u/49999449?v=3&s=70" width="100px"/></a>        |
|-----------------------------------------------------------------------------------------------------|
| [Gvinfinity](https://github.com/gvinfinity)                                                                | 

## 🤝 Contribuir
Contribuições, issues e pedidos de features são bem-vindos!<br />Sinta-se livre para checar a [página de issues](https://github.com/ifpe-open-source/modelo/issues). 
- Crie um fork;
- Crie um branch com a sua feature: `git checkout -b my-feature`;
- Faça um commit com as mudanças: `git commit -m 'feat: My new feature'`;
- Faça um push para o seu branch: `git push origin my-feature`.

Após a sua pull request ser aceita, você pode excluir o seu branch.

## Demonstre o seu apoio

Dê uma ⭐️ se este projeto lhe ajudou!

## 📝 Licença

Este projeto está sob a licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.

***
Feito com ♥ por Gabriel Soares :wave: [Entre em contato!](mailto:gvss3@discente.ifpe.edu.com) no [<img src="https://avatars.githubusercontent.com/u/73182418?v=4" width="15px"/> IFPE Open Source](https://ifpeopensource.com.br)
