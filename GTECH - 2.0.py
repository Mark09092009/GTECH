# Marcos Vinicius de Sousa
# Luis Gustavo
# Pedro Lucas
# Gabriel

# Listas para armazenar os dados dos usuários
nomes = []  # Armazena os nomes completos
cpfs = []   # Armazena os CPFs
telefones = []  # Armazena os telefones
emails = []  # Armazena os emails
enderecos = []  # Armazena os endereços
cidades = []  # Armazena as cidades

# Função para capturar o nome completo do usuário
def inputNome():
    while (True):
        while (True):
            # Captura o primeiro nome
            nome_p = str(input('|> Digite o primeiro nome: ')).strip().title()
            if (nome_p.count(' ') != 0 ):  # Verifica se há espaços no nome
                print('\n=- Somente o primeiro nome!')
                print('=- Sem espaços!!\n')
                continue
            elif (nome_p.isalpha()):  # Verifica se o nome contém apenas letras
                print('')
                break
            else:
                print('\n=- Somente letras!!\n')
                continue
        while (True):
            # Captura o sobrenome
            nome_s = str(input('|> Digite o ultimo sobrenome: ')).strip().title()
            if (nome_s.count(' ') != 0 ):  # Verifica se há espaços no sobrenome
                print('\n=- Somente o ultimo sobrenome!')
                print('=- Sem espaços!!\n')
                continue
            elif (nome_s.isalpha()):  # Verifica se o sobrenome contém apenas letras
                print('')
                nome_completo = (nome_p +' '+ nome_s)  # Concatena nome e sobrenome
                break
            else:
                print('\n=- Somente letras!!\n')
                continue
        return nome_completo  # Retorna o nome completo

# Função para capturar o CPF do usuário
def inputCpf(vetor):
    while (True):
        try:
            cpf_aux = str(input('|> Digite o cpf: ')).strip()
            cpf = int(cpf_aux)  # Tenta converter o CPF para inteiro
            if (((len(cpf_aux)) == 11) and (cpf_aux.isdigit())):  # Verifica se o CPF tem 11 dígitos
                print('')
                if (cpf_aux in vetor):  # Verifica se o CPF já foi cadastrado
                    print('CPF ja cadastrado!!')
                    print('Tente novamente!!\n')
                    continue
                else:
                    return cpf_aux  # Retorna o CPF válido
            else:
                print('\n=- CPF so pode haver 11 caracteres!!')
                print('=- Caracteres essas devem ser numeros!!\n')
                continue
        except ValueError:
            print('\n=- Os caracteres do CPF devem ser numeros!!\n')
            continue

# Função para capturar o telefone do usuário
def inputTelefone(vetor):
    while (True):
        try:
            telefone_aux = str(input('|> Digite o telefone: ')).strip()
            telefone = int(telefone_aux)  # Tenta converter o telefone para inteiro
            if (((len(telefone_aux)) == 11) and (telefone_aux.isdigit())):  # Verifica se o telefone tem 11 dígitos
                print('')
                if (telefone_aux in vetor):  # Verifica se o telefone já foi cadastrado
                    print('Telefone ja cadastrado!!')
                    print('Tente novamente!!\n')
                    continue
                else:
                    return telefone_aux  # Retorna o telefone válido
            else:
                print('\n=- Telefone so pode haver 11 caracteres!!')
                print('=- Caracteres essas devem ser numeros!!\n')
                continue
        except ValueError:
            print('\n=- Os caracteres do telefone devem ser numeros!!\n')
            continue

# Função para capturar o email do usuário
def inputEmail():
    while (True):
        email = str(input('|>Digite o Email (@gmail.com): ')).strip()
        print('')
        if (validarEmail(email)):  # Valida o email
            return email  # Retorna o email válido

# Função para validar o email
def validarEmail(email):
    while (True):
        if (email.count('@') != 1 ):  # Verifica se há exatamente um "@"
            print('=- Email invalido!!')
            print('=- Tente novamente!\n')
            return False
        
        usuario, dominio = email.split('@')  # Divide o email em usuário e domínio

        if (dominio != 'gmail.com'):  # Verifica se o domínio é "gmail.com"
            print('=- dominio invalido!!')
            print('=- Tente novamente!\n')
            return False
        
        if ((usuario.startswith('.')) or (usuario.endswith('.'))):  # Verifica se o usuário começa ou termina com "."
            print('=- O email não pode começar / terminar com "." !!')
            print('=- Tente novamente!\n')
            return False
        
        if ('..' in usuario):  # Verifica se há ".." no usuário
            print('=- Não pode haver ".." no email!')
            print('=- Tente novamente!\n')
            return False
        
        if not(usuario):
            print('=- Email deve ter algo antes do "@" !!!')
            print('=- Tente novamente!\n')
            return False

        for caractere in usuario:
            if not (caractere.isalnum() or caractere in ['.', '_', '-', '+']):  # Verifica caracteres válidos
                print('=- Caracteres invalidos!!')
                print('=- Tente novamente!\n')
                return False
    
        return True  # Retorna True se o email for válido

# Função para capturar o endereço do usuário
def inputEndereco():
    while (True):
        endereco = str(input('|> Digite o endereco: ')).strip().title()
        if (endereco.replace(' ','').isalnum()):  # Verifica se o endereço contém apenas letras e números
            print('')
            return endereco  # Retorna o endereço válido
        else:
            print('\n=- Tente novamente!\n')
            continue

# Função para capturar a cidade do usuário
def inputCidade():
    while (True):
        cidade = str(input('|> Digite o cidade: ')).strip().title()
        if (cidade.replace(' ','').isalnum()):  # Verifica se a cidade contém apenas letras e números
            print('')
            return cidade  # Retorna a cidade válida
        else:
            print('\n=- Tente novamente!\n')
            continue

# Função para editar os dados de um cadastro existente
def editar(vetor1, vetor2, vetor3, vetor4, vetor5, vetor6):
    if (vetor1.__len__() == 0):  # Verifica se há cadastros para editar
            print('=- Não há nada para editar\n')
    else:
        for i in range(0, vetor1.__len__()):  # Lista os cadastros existentes
            print(f'=- Cadastro de indice: {i} - {vetor1[i]}')
        print('')
        while (True):
            try:
                indice = int(input('=- Digite o indice do cadastro que dedeja editar: '))
                if (indice >= vetor1.__len__()):  # Verifica se o índice é válido
                    print('\n=- Indice não ocupado!')
                    print('=- Tente novamente!\n')
                    continue
                elif (indice < 0):  # Verifica se o índice é negativo
                    print('\n=- Indice invalido!')
                    print('=- Tente novamente!\n')
                    continue
                else: 
                    break
            except ValueError:
                print('\n=- Valor invalido\n')
                continue                
        while (True):
                try:
                    # Exibe os dados do cadastro selecionado
                    print(f'|> Cadastro {indice} --->')
                    print(f'|=- Nome - {vetor1[indice]}')
                    print(f'|=- CPF - {vetor2[indice]}')
                    print(f'|=- Telefone - {vetor3[indice]}')
                    print(f'|=- Email - {vetor4[indice]}')
                    print(f'|=- Endereço - {vetor5[indice]}')
                    print(f'|=- Cidade - {vetor6[indice]}')
                    print('')
                    # Menu de edição
                    print('|> ----menu editar---- <|')
                    print('|                       |')
                    print('|>- 1. Nome             |')
                    print('|>- 2. CPF              |')
                    print('|>- 3. Telefone         |')
                    print('|>- 4. Email            |')
                    print('|>- 5. Endereço         |')
                    print('|>- 6. Cidade           |')
                    print('|>- 0. Sair             |')
                    print('|>- ------------------ <|')
                    print('')
                    opc_3 = int(input('|> - Digite o numero da opção desejada: '))
                    if ((opc_3 == 1) or (opc_3 == 2) or (opc_3 == 3) or (opc_3 == 4) or (opc_3 == 5) or (opc_3 == 6) or (opc_3 == 0)):
                        if (opc_3 == 1):
                            nomes[indice] = (inputNome())  # Edita o nome
                        elif (opc_3 == 2):
                            cpfs[indice] = (inputCpf(cpfs))  # Edita o CPF
                        elif (opc_3 == 3):
                            telefones[indice] = (inputTelefone(telefones))  # Edita o telefone
                        elif (opc_3 == 4):
                            emails[indice] = (inputEmail())  # Edita o email
                        elif (opc_3 == 5):
                            enderecos[indice] = (inputEndereco())  # Edita o endereço
                        elif (opc_3 == 6):
                            cidades[indice] = (inputCidade())  # Edita a cidade
                        else:
                            print('')
                            break
                    else:
                        print('\n=- Opção não listada')
                        print('=- Tente novamente!\n')
                        continue
                except ValueError:
                    print('\n=- Valor invalido\n')
                    continue

# Função para listar todos os cadastros
def listar(vetor1, vetor2, vetor3, vetor4, vetor5, vetor6):
    if (vetor1.__len__() == 0):  # Verifica se há cadastros para listar
            print('=- Não há nada para listar\n')
    for i in range(0, vetor1.__len__()):  # Lista todos os cadastros
        print(f'|> Cadastro de indice: {i} --->')
        print(f'|=- Nome - {vetor1[i]}')
        print(f'|=- CPF - {vetor2[i]}')
        print(f'|=- Telefone - {vetor3[i]}')
        print(f'|=- Email - {vetor4[i]}')
        print(f'|=- Endereço - {vetor5[i]}')
        print(f'|=- Cidade - {vetor6[i]}')
        print('')

# Função para excluir um cadastro
def excluir(vetor1, vetor2, vetor3, vetor4, vetor5, vetor6):
    if (vetor1.__len__() == 0):  # Verifica se há cadastros para excluir
            print('=- Não há nada para Excluir\n')
    if not(vetor1.__len__() == 0):
        for i in range(0, vetor1.__len__()):  # Lista os cadastros existentes
            print(f'=- Cadastro de indice: {i} - {vetor1[i]}')
        print('')
        while (True):
            try:
                indice = int(input('=- Digite o indice do cadastro que deseja apagar: '))
                if (indice >= vetor1.__len__()):  # Verifica se o índice é válido
                    print('\n=- Indice não ocupado!')
                    print('=- Tente novamente!\n')
                    continue
                elif (indice < 0):  # Verifica se o índice é negativo
                    print('\n=- Indice invalido!')
                    print('=- Tente novamente!\n')
                    continue
                else: 
                    break
            except ValueError:
                print('\n=- Valor invalido\n')
                continue                
        vetor1.pop(indice)  # Remove o nome
        vetor2.pop(indice)  # Remove o CPF
        vetor3.pop(indice)  # Remove o telefone
        vetor4.pop(indice)  # Remove o email
        vetor5.pop(indice)  # Remove o endereço
        vetor6.pop(indice)  # Remove a cidade
        print(f'\n=- Cadastro do {indice}, excluido com sucesso!!!\n')

# Menu principal
while (True):
    try:
        while (True):
            # Exibe o menu principal
            print('|> ----- menu ----- <|')
            print('|                    |')
            print('|>- 1. Cadastrar     |')
            print('|>- 2. Editar        |')
            print('|>- 3. Listar        |')
            print('|>- 4. Excluir       |')
            print('|>- 0. Sair          |')
            print('|> ---------------- <|')
            print('')
            opc = int(input('|> - Digites o numero da opção desejada: '))
            print('')
            break
    except ValueError:
        print('\n=- Valor invalido\n')
        continue

    # Opc 1. - Cadastro
    if (opc == 1):
        nomes.append(inputNome())  # Adiciona o nome
        cpfs.append(inputCpf(cpfs))  # Adiciona o CPF
        telefones.append(inputTelefone(telefones))  # Adiciona o telefone
        emails.append(inputEmail())  # Adiciona o email
        enderecos.append(inputEndereco())  # Adiciona o endereço
        cidades.append(inputCidade())  # Adiciona a cidade
        print('=- Cadastro realizado com sucesso!!\n')

    # Opc 2. - Editar
    elif (opc == 2):
        editar(nomes, cpfs, telefones, emails, enderecos, cidades)  # Chama a função de edição

    # Opc 3. - Listar
    elif (opc == 3):
        listar(nomes, cpfs, telefones, emails, enderecos, cidades)  # Chama a função de listagem
    
    # Opc 4. - Excluir                                             
    elif (opc == 4):
        excluir(nomes, cpfs, telefones, emails, enderecos, cidades)  # Chama a função de exclusão

    # Opc 0. - Sair
    elif (opc == 0):
        print('=- Sobrevivi!! 0-o ')
        exit()  # Sai do programa
    # Opc ?. - Error
    else:
        print('\n=- Valor invalido\n')
        continue