# Lista vazia para guardar as doses checadas pelo usuarios
dose_total = []
# lista vazia para guardar os inputs feitos pelo usuario no menu
resumo = []
# dicionario com os dados de conversão das medidas usadas no código
medidas = {'g': 0.001,
             'kg':0.000001}

# função com o calculo de tempo sobre a dosagem de remédio
def tempo(t):
    # a função matemática que realiza o calculo
    funcao = - t ** 2 + 6 * t + 20
    
    # setando uma clausula se para testar se pessoa já pode ou não tomar o remédio de novo
    if funcao <= 10:
        return "Pode tomar mais uma Dose!"
    else:
        return 'O remédio ainda esta fazendo efeito'

# função para calcular a dose maxima que a pessoa pode tomar baseada no seu peso
def dose(peso, dosagem):
    # função matemática que calcula a dose
    dose_mx = peso / 4 * dosagem
    
    # linha de código que guarda a dose checada pelo usuario na lista vazia criada no começo do código
    dose_total.append(dose_mx)
    
    # Linha de código que retorna uma string manipulada para informar o usuario a dose máxima adeuqada a se tomar
    return f'a dose máxima adequada seria: {dose_mx}'

# Função de checagem de dose e tempo  
def checar():
    # input servindo de menu para o usuario escolher qual checagem realizará
    usuario = int(input('Deseja realizar qual checagem sobre seu remédio? [1] Dose máxima, [2] Se já deu tempo suficiente para proxima dose ou [3] voltar'))
    
    # loop que realizara o codigo até o usuario pedir para voltar ao menu principal
    while usuario != 'Voltar':
        
        # condição se que levara o usuario ao conjunto de codigo correto baseado na resposta do input inicial
        if usuario == 1:
            
            # dois inputs pedindo o peso e a dosagem que consta na caixinha do remedio
            peso = float(input('Qual o seu peso (kg)? '))
            dosagem = float(input('Qual a dosagem descrita na caixa de remédio (mg)?'))
            
            # variavel que chama a função dose
            calulo = dose(peso, dosagem)
            
            # um print para imprimir o resultado do calculo da função
            print(calulo)
            
            # um input para verificar se o usuario deseja realizar outra checagem ou se deseja voltar ao menu principal
            cnt = str(input('Deseja realizar outra checagem? S ou N')).title()
            
            # Condição se que vai definir se o usuario continua nessa função ou volta para o menu
            if cnt == 'S':
                # se sim o usuario reebera a mesma pergunta do começo da função para que o código possa rodar de novo
                usuario = int(input('Deseja realizar qual checagem sobre seu remédio? [1] Dose máxima, [2] Se já deu tempo suficiente para proxima dose ou [3] voltar'))
                
                # Essa linha vai dar um append no termo 'Checar' dentro da lista que resume as ações do usuario, pois assim constara neala essa segunda checagem feita internamente na função checar
                resumo.append('Checar')
            else:
                # se não a variavel usuario recebera o valor 'Voltar' o que fara com que o loop pare
                usuario = 'Voltar'
        
        elif usuario == 2:
            
            # Input pedindo que o usuario forneca a quanto tempo foi que ele tomou a ultima dose de seu remedio
            hora = float(input('Quanto tempo faz que você tomou a última dose? Ou escreva volte para voltar'))
            
            # variavel para chamar a função tempo
            periodo = tempo(hora)
            
            # imprimimos o resultado da função tempo
            print(periodo)
            
            # um input para verificar se o usuario deseja realizar outra checagem ou se deseja voltar ao menu principal
            cnt = str(input('Deseja realizar outra checagem? S ou N')).title()
            
            # Condição se que vai definir se o usuario continua nessa função ou volta para o menu
            if cnt == 'S':
                # se sim o usuario reebera a mesma pergunta do começo da função para que o código possa rodar de novo
                usuario = int(input('Deseja realizar qual checagem sobre seu remédio? [1] Dose máxima, [2] Se já deu tempo suficiente para proxima dose ou [3] voltar'))
                
                # Essa linha vai dar um append no termo 'Checar' dentro da lista que resume as ações do usuario, pois assim constara neala essa segunda checagem feita internamente na função checar
                resumo.append('Checar')
            else:
                # se não a variavel usuario recebera o valor 'Voltar' o que fara com que o loop pare
                usuario = 'Voltar'
        
        # No caso dessa ultima condição estamos setnado para que o usuario possa quebrar o loop e voltar para o menu
        elif usuario == 3:
            # a variavel usuario recebera o valor 'Voltar' o que fara com que o loop pare
            usuario = 'Voltar'
        
        # Caso o usuário digite um numero fora dos definidos para o menu usamos essa condição final para informar que não foi encontrada e para ele digitar uma nova
        else:
            usuario = int(input('Opção não encontrada! [1] Dose máxima, [2] Se já deu tempo suficiente para proxima dose ou [3] voltar'))

# função que converte os dados para a medida que o usuario requisitar
def converter():
    
    # input para confirmarmos qual entre as opções de medidas o usuario deseja realizar a conversão
    confirmacao = str(input('Você quer converter a dosagem de mg para: g ou kg? Ou deseja voltar para o menu?'))
    
    # input que pergunta de onde vira o dado que será convertido
    pergunta = int(input('Você quer: [1] Calcular a dose [2] Usar uma dose já calculada pelo programa  [3] Digitar a dose?'))
     
    # Criando o loop que só sera quebrado sé o usuario pedir para voltar ao menu
    while confirmacao != 'voltar':
        
        # Condição se que redireciona o usuario baseado na resposta de onde vem os dados
        if pergunta == 1:
            
            # condição se que relizara a conversão baseada na medida requisitada pelo usuario
            if confirmacao == 'g':
                
                # calculo de conversão puxando o valor do dicionario de medidas que criamos no começo do codigo
                conversao = dose() * medidas['g']
                
                # imprimindo o resultado da conversao
                print(f'O valor da sua conversão é: {conversao}g')
            
            # Condição se que redireciona o usuario baseado na respostta de onde vem os dados
            elif confirmacao == 'kg':
                
                # calculo de conversão puxando o valor do dicionario de medidas que criamos no começo do codigo
                conversao = dose() * medidas['kg']
                
                # imprimindo o resultado da conversao
                print(f'O valor da sua conversão é: {conversao}kg')
            
             
            else:
                
                # imprime uma notificação para o usuario que ele escolheu uma metrica que não está disponivel
                print('Selecione uma métrica disponível!')
            
            # input para o usuario informar se quer continuar nessa seção do codigo ou não
            cnt = str(input('Você quer converter mais algum valor? S ou N')).title()
             
            # condição se para redirecionar o usuario baseado na resposta de se ele que continuar na seção ou não   
            if cnt == 'S':
                # se sim refazemos a pergunta inicial do local onde vira os dados
                pergunta = int(input('Você quer: [1] Calcular a dose [2] Usar uma dose já calculada pelo programa  [3] Digitar a dose?'))
                
                # e refazemos a pergunta inicial das métricas
                confirmacao = str(input('Você quer converter a dosagem de mg para: g ou kg?'))
                
                # Essa linha faz com que essa nova conversão apareca no resumo de ações
                resumo.append('Converter')
            else:
                
                # se não ele seta a variavel confirmacao como voltar e termina o loop e retorna o usuario para o menu principal
                confirmacao = 'voltar'
        
        # Condição se que redireciona o usuario baseado na resposta de onde vem os dados   
        elif pergunta == 2:
            # variavel que servira de contador para o loop
            i = 0
            
            # loop que usaremos para olhar os dados da lista dose_total e podermos conveter eles para a medida resquisitada
            while i < len(dose_total):
                
                # Condição se que redireciona o usuario baseado na respostta de onde vem os dados
                if confirmacao == 'g':
                    
                    # calculo de conversão puxando o valor do dicionario de medidas que criamos no começo do codigo
                    conversao = dose_total[i] * medidas['g']
                    
                    # imprimindo o resultado da conversao
                    print(f'O valor da sua conversão é: {conversao}g')
                
                # Condição se que redireciona o usuario baseado na respostta de onde vem os dados    
                elif confirmacao == 'kg':
                    
                    # calculo de conversão puxando o valor do dicionario de medidas que criamos no começo do codigo
                    conversao = dose_total[i] * medidas['kg']
                    
                    # imprimindo o resultado da conversao
                    print(f'O valor da sua conversão é: {conversao}kg')
                
                else:
                    
                    # imprime uma notificação para o usuario que ele escolheu uma metrica que não está disponivel
                    print('Selecione uma métrica disponível!')
                
                #aumentando o contador para que o loop não fique infinito
                i+=1
                
                # input para o usuario informar se quer continuar nessa seção do codigo ou não
                cnt = str(input('Você quer converter mais algum valor? S ou N')).title()
                
                if cnt == 'S':
                    # se sim refazemos a pergunta inicial do local onde vira os dados
                    pergunta = int(input('Você quer: [1] Calcular a dose [2] Usar uma dose já calculada pelo programa  [3] Digitar a dose?'))
                
                    # e refazemos a pergunta inicial das métricas
                    confirmacao = str(input('Você quer converter a dosagem de mg para: g ou kg?'))
                
                    # Essa linha faz com que essa nova conversão apareca no resumo de ações
                    resumo.append('Converter')
                else:
                    # se não ele seta a variavel confirmacao como voltar e termina o loop e retorna o usuario para o menu principal
                    confirmacao = 'voltar'
        
        # Condição se que redireciona o usuario baseado na resposta de onde vem os dados         
        elif pergunta == 3:
            
            # Condição se que redireciona o usuario baseado na respostta de onde vem os dados
            if confirmacao == 'g':
                
                # input pedindo a dose desejada para a conversão
                dose = float(input('Digite a dose desejada: '))
                
                # calculo de conversão puxando o valor do dicionario de medidas que criamos no começo do codigo
                conversao = dose * medidas['g']
                
                # imprimindo o resultado da conversao
                print(f'O valor da sua conversão é: {conversao}g')
                
            # Condição se que redireciona o usuario baseado na respostta de onde vem os dados
            elif confirmacao == 'kg':
                
                # input pedindo a dose desejada para a conversão
                dose = float(input('Digite a dose desejada: '))
                
                # calculo de conversão puxando o valor do dicionario de medidas que criamos no começo do codigo
                conversao = dose * medidas['kg']
                
                # imprimindo o resultado da conversao
                print(f'O valor da sua conversão é: {conversao}kg')
            else:
                
                # imprime uma notificação para o usuario que ele escolheu uma metrica que não está disponivel
                print('Selecione uma métrica disponível!')
            
            # input para o usuario informar se quer continuar nessa seção do codigo ou não
            cnt = str(input('Você quer converter mais algum valor? S ou N')).title()
                
            if cnt == 'S':
                # se sim refazemos a pergunta inicial do local onde vira os dados
                pergunta = int(input('Você quer: [1] Calcular a dose [2] Usar uma dose já calculada pelo programa  [3] Digitar a dose?'))
                
                # e refazemos a pergunta inicial das métricas
                confirmacao = str(input('Você quer converter a dosagem de mg para: g ou kg?'))
                
                # Essa linha faz com que essa nova conversão apareca no resumo de ações
                resumo.append('Converter')
            else:
                # se não ele seta a variavel confirmacao como voltar e termina o loop e retorna o usuario para o menu principal
                confirmacao = 'voltar'
        
        else:
            
            # Caso o usuario coloque uma opção invalida usamos essa linha para informar eles
            print('Operação não suportada')

# função que cria o menu principal
def menu():
    
    # input inicial para sabermos qual funcionalidade o usuário deseja realizar ou se ele quer parar o código
    usuario = str(input('O que você quer fazer: Checar, Converter ou Parar?')).title()
    
    # loop que faz o código rodar até o usuário pedir que pare
    while usuario != 'Parar':
        
        # condição se que leva o usuario para a função que deseja
        if usuario == 'Checar':
            
            # linha que vai deixar registrado no resumo qual foi a função realizada pelo usuario
            resumo.append(usuario)
            
            # linha que chama a função que vai realizar a funcionalidade requisitada pelo usuario
            checar()
            
            # linha que apos o final do código da função irá perguntar se o usuario deseja realizar uma nova função ou parar o código
            usuario = str(input('O que você quer fazer: Checar, Converter ou Parar?')).title()
        elif usuario == 'Converter':
            
            # linha que vai deixar registrado no resumo qual foi a função realizada pelo usuario
            resumo.append(usuario)
            
            # linha que chama a função que vai realizar a funcionalidade requisitada pelo usuario
            converter()
            
            # linha que apos o final do código da função irá perguntar se o usuario deseja realizar uma nova função ou parar o código
            usuario = str(input('O que você quer fazer: Checar, Converter ou Parar?')).title()
        else:
            # Caso ele não coloque uma operação que temos, realizo a pergunta novamente
            usuario = str(input('O que você quer fazer: Checar, Converter ou Parar?')).title()
    
    # Contador para correr os itens de uma linha
    i = 0
    
    # loop para que o código rode até o final do tamanho da lista
    while i < len(resumo):
        
        # linha pedindo que o código imprima o iten da lista resumo que está no index i
        print(f'O usuario fez {i+1}º: {resumo[i]}')
        
        # aumentando o numero do nosso contador para que o loop não fique infinito
        i+=1

# linha de código chama a função menu e assim inicializando todo o programa
menu()