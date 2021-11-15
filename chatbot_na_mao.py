def processar_resposta(resposta, nome):
    if resposta == '1':
        print(f'''\n{nome}, na minha visão vale muito apena, isso porque Python é uma das linguagens que mais cresce no
mundo e possui salários mensais que vão desde R$2100,00 a até mais R$10000,00 no Brasil, além de contar 
com uma média anual de $85.000 dolares nos EUA.\n''')

    elif resposta == '2':
        print(f''' \n{nome}, isso varia muito com o nível de esforço, dedicação e busca diária por vagas de cada indivíduo.
Alguns conseguem com menos de 3 meses e outros com mais, tudo depende do quanto você já sabe ou está 
disposto a correr atrás para aprender.\n''')

    elif resposta == '3':
        print(f'''\n{nome}, primeiro entenda, ninguém vai te dizer ou chegar magicamente um dia e te dizer que você está
BOM o suficiente para conseguir um emprego ou fazer dinheiro com seu conhecimento de programação, seja em 
Python ou qualquer outra linguagem ou habilidade, você simplesmente tem que começar dar a sua cara a tapa 
e começar a aplicar para oportunidades ou até mesmo começar a criar elas, desde o dia que você já domina 
os fundamentos de uma linguagem(se estamos falando de Python, recomendo aprender no mínimo os 5 pilares
de programação.\n''')

    elif resposta == '4':
        print(f'''\n{nome}, você pode estudar através de vídeos gratúitos no YouTube, livros e sites de programação,
porém se buscar um lugar com suporte 1 a 1, estrutura sequencial, projetos novos todos os meses dos 
ano e um curso que vai te ensinar toda a base e habilidades mais lucrativas que precisa para criar
aplicações em python e estar pronto para o mercado, recomendo o cursodepython.net.\n''')

    elif resposta == '5':
        exit()

    else:
        print('Digite apenas 1, 2, 3 ou 4')


def start():
    # Apresentar o chatbot
    print('Olá! Bem-vindo ao ChatBot do Renan')
    # pedir o nome
    nome = str(input('Digite seu nome: ')).strip().title()
    # pedir o e-mail
    email = str(input('Digite seu e-mail: ')).strip().title()
    while True:
        # Oferer o menu de opções
        print('''
[1] - Vale a pena aprender Python?
[2] - Quanto tempo leva para conseguir um emprego com Python?
[3] - Quando vou saber que estou BOM o suficiente para conseguir um emprego?
[4] - Onde me recomenda estudar Python para conseguir um emprego hoje?
[5] - Encerrar a conversa com Bot''')
        resposta = str(input('O que Gostaria de saber hoje? ')).strip()
        # Processar a resposta enviada
        processar_resposta(resposta, nome)


if __name__ == '__main__':
    start()
