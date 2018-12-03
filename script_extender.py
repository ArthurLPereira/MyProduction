from subprocess import run
import os

def definirPesquisadores():
    listaPesquisadores = open("pesquisadores.list", 'w+')
    
    print ('\n\nInsira o id dos pesquisadores, separados por espaço, o id pode ser encontrado na página lattes do pesquisador embaixo do nome na url, seguindo o padrão: \nhttp://lattes.cnpq.br/<id>:')
    persquisadores = [p for p in input().split()]
    for i in persquisadores:
        listaPesquisadores.write(i)
        listaPesquisadores.write('\n')
        
def definirData():
    print('\n\n Deseja pesquisar os índices baseados em um período de tempo específico? (s) para sim, (n) para não.\t')
    resp = input("Sim(s) ou Não(n): ")
    arquivo = open('trabalho/configuracao.config', 'w+')
    
    
    arquivo.write('# ---------------------------------------------------------------------------- #\n# scriptLattes                                                                 #\n# ---------------------------------------------------------------------------- #\n')
    arquivo.write('global-nome_do_grupo                      = pesquisadores\n')
    arquivo.write('global-arquivo_de_entrada                 = ./trabalho/pesquisadores.list\n')
    arquivo.write('global-diretorio_de_saida                 = ./trabalho/resultados/\n')
    arquivo.write('global-email_do_admin                     = admin@email.com\n')
    arquivo.write('global-idioma                             = PT    # ainda não implementada na versão Python\n')
    arquivo.write('global-itens_desde_o_ano                  = ')
    
    
    if resp == 's':
        print('\n\n Digite a partir de que data deseja pesquisar:\t')
        datainicial = input("Data inicial: ")
        
        arquivo.write(datainicial)
        arquivo.write(' # se não for indicado o ano então serão consideradas as publicações\n')
        
        print('\n\n Agora digite até qual data deve ser verificado:\t')
        datafinal = input("Data final: ")
        
        arquivo.write('global-itens_ate_o_ano                    = ')
        arquivo.write(datafinal)
        
    else:
        arquivo.write(' # se não for indicado o ano então serão consideradas as publicações\n')
        arquivo.write('global-itens_ate_o_ano                    = 2018')
        
    with open('trabalho/configuracao_complementar.config', 'r+') as f:
        with arquivo as f1:
            for line in f:
                f1.write(line)
                
def getIndices():
    with open(os.devnull, 'w') as devnull:
        run(['python', 'scriptLattes/scriptlattes.py', './trabalho.config'], stdout=devnull, stderr=devnull)
    # os.system("python scriptLattes/scriptla")
    arquivo = open("trabalho/qualis.txt", 'r+')
    qualis = [int(line) for line in arquivo]
    qualis_restrito = [q for q in qualis if q >= 50]
    indices = (sum(qualis), sum(qualis_restrito))
    os.remove("./trabalho/qualis.txt")
    return indices

def mostrarIndices():
  indices = getIndices()
  print('\n')
  print('Índice geral: ', indices[0])
  print("Índice Restrito", indices[1])
   
    
    
if __name__ == "__main__":
    
   definirPesquisadores()
   definirData()
   mostrarIndices()

# 4935788335854516 6331835838649652