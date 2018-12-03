# My Production

Trabalho de Engenharia de Software 2, My Production:
  - Um Script com intuito de calcular o índice geral e o índice restrito de um Pesquisador ou grupo de pesquisadores cadastrados na plataforma Lattes.

  - Fizemos uso de uma ferramenta de webscraping desenvolvida para extração de dados da plataforma lattes, o ScriptLattes, por falta de disponibilidade de serviços de extração de dados oficiais disponibilizados pelo CNPq. A aplicação desenvolvida faz uma chamada direta ao ScriptLattes, que foi alterado para cumprir nossos propósitos.

## REQUIREMENTS

É necessário ter python 2 e python 3 instalados no sistema (inicialmente seria necessário somente o python3 mas por causa de algumas dependencias python2 também é necessário). Instale os pacotes necessários com os seguintes comandos:

``` 
sudo apt-get install python-all python-setuptools python-utidylib python-matplotlib python-levenshtein python-pygraphviz
sudo apt-get install python-numpy tidy python-scipy python-imaging python-mechanize python-pandas
sudo easy_install pytidylib
sudo apt-get install python-scipy
sudo apt-get install python-lxml
```

## EXECUÇÃO

Para executar o programa basta usar o comando `python3 script_extender.py`.


## CREDITOS

ScriptLattes não foi desenvolvido por nós e está disponível neste [link](http://scriptlattes.sourceforge.net/code.html), é um projeto open source em desenvolvimento desde 2005 para extração de dados da plataforma lattes e foi desenvolvido independentemente.

script_extender.py funciona em conjunto com o scriptLattes para calcular o índice geral e o índice restrito dos pesquisadores a partir dos dados extraídos com a ferramenta.



