# Marcos Vinicius de Sousa
# luiz Gustavo
# Pedro Lucas
# Gabriel

nomes = []
cpfs = []
telefones = []
emails = []
enderecos = []
cidades = []

def inputNome(vetor):
    while (True):
        while (True):
                nome_p = str(input('|> Digite o primeiro nome: ')).strip().title()
                if (nome_p.isalpha()):
                    print('')
                    break
                else:
                    print('\n=- Nome invalido!\n')
                    continue
        while (True):
            nome_s = str(input('|> Digite o sobrenome: ')).strip().title()
            if (nome_s.isalpha()):
                print('')
                nome_completo = (nome_p +' '+ nome_s)
                break
            else:
                print('\n=- Nome invalido!\n')
                continue
        if (nome_completo in vetor):
            print('Nome ja cadastrado!!')
            print('Tente novamente!!\n')
            continue
        else:
            return nome_completo

def inputCpf(vetor):
    while (True):
        try:
            cpf_aux = str(input('|> Digite o cpf: ')).strip()
            cpf = int(cpf_aux)
            if (((len(cpf_aux)) == 11) and (cpf_aux.isdigit())):
                print('')
                if (cpf_aux in vetor):
                    print('CPF ja cadastrado!!')
                    print('Tente novamente!!\n')
                    continue
                else:
                    return cpf_aux
            else:
                print('\n=- CPF invalido!')
                print('=- Tente novamente!\n')
                continue
        except ValueError:
            print('\n=- CPF invalido!')
            print('=- Tente novamente!\n')
            continue

def inputTelefone(vetor):
    while (True):
        try:
            telefone_aux = str(input('|> Digite o telefone: ')).strip()
            telefone = int(telefone_aux)
            if (((len(telefone_aux)) == 11) and (telefone_aux.isdigit())):
                print('')
                if (telefone_aux in vetor):
                    print('Telefone ja cadastrado!!')
                    print('Tente novamente!!\n')
                    continue
                else:
                    return telefone_aux
            else:
                print('\n=- telefone invalido!')
                print('=- Tente novamente!\n')
                continue
        except ValueError:
            print('\n=- telefone invalido!')
            print('=- Tente novamente!\n')
            continue

def inputEmail(vetor):
    while (True):
        email = str(input('|>Digite o Email: ')).strip()
        print('')
        if (email in vetor):
            print('Email ja cadastrado!!')
            print('Tente novamente!!\n')
            continue
        else:
            return email

def inputEndereco():
    while (True):
        endereco = str(input('|> Digite o endereco: ')).strip().title()
        if (endereco.replace(' ','').isalnum()):
            print('')
            return endereco
        else:
            print('\n=- Tente novamente!\n')
            continue

def inputCidade():
    while (True):
        cidade = str(input('|> Digite o cidade: ')).strip().title()
        if (cidade.replace(' ','').isalnum()):
            print('')
            return cidade
        else:
            print('\n=- Tente novamente!\n')
            continue

def editar(vetor1, vetor2, vetor3, vetor4, vetor5, vetor6):
    if (vetor1.__len__() == 0):
            print('=- Não há nada para listar\n')
    else:
        for i in range(0, vetor1.__len__()):
            print(f'=- Cadastro {i} - {vetor1[i]}')
        print('')
        while (True):
            try:
                print('|> ----menu editar---- <|')
                print('|                       |')
                print('|>- 1. Pelo Indice      |')
                print('|>- 2. Pelo Nome        |')
                print('|>- ------------------ <|')
                print('')
                opc_2 = int(input('|> - Digite o numero da opção desejada: '))
                if ((opc_2 == 1) or (opc_2 == 2)):
                    break
                else:
                    print('\n=- Opção não listada')
                    print('=- Tente novamente!\n')
                    continue
            except ValueError:
                print('\n=- Valor invalido\n')
                continue
        if (opc_2 == 1):
            while (True):
                try:
                    indice = int(input('=- Digite o indice do cadastro que dedeja editar: '))
                    if (indice > vetor1.__len__()):
                        print('\n=- Indice não ocupado!')
                        print('=- Tente novamente!\n')
                        continue
                    else: 
                        break
                except ValueError:
                    print('\n=- Valor invalido\n')
                    continue                
        if (opc_2 == 2):
            while (True):
                nome = str(input('=- Digite o nome do cadastro que dedeja editar: ')).strip().title()
                for i in range (0, vetor1.__len__()):
                    if (nome == vetor1[i]):
                        indice = i
                        break
                else: 
                    print('\n=- Nome não existente!')
                    print('=- Tente novamente!\n')
                    continue
                break
        while (True):
                try:
                    print(f'|> Cadastro {indice} --->')
                    print(f'|=- Nome - {vetor1[indice]}')
                    print(f'|=- CPF - {vetor2[indice]}')
                    print(f'|=- Telefone - {vetor3[indice]}')
                    print(f'|=- Email - {vetor4[indice]}')
                    print(f'|=- Endereço - {vetor5[indice]}')
                    print(f'|=- Cidade - {vetor6[indice]}')
                    print('')
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
                            nomes[indice] = (inputNome(nomes))
                        elif (opc_3 == 2):
                            cpfs[indice] = (inputCpf())
                        elif (opc_3 == 3):
                            telefones[indice] = (inputTelefone())
                        elif (opc_3 == 4):
                            emails[indice] = (inputEmail())
                        elif (opc_3 == 5):
                            enderecos[indice] = (inputEndereco())
                        elif (opc_3 == 6):
                            cidades[indice] = (inputCidade())
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

def listar(vetor1, vetor2, vetor3, vetor4, vetor5, vetor6):
    if (vetor1.__len__() == 0):
            print('=- Não há nada para listar\n')
    for i in range(0, vetor1.__len__()):
        print(f'|> Cadastro {i} --->')
        print(f'|=- Nome - {vetor1[i]}')
        print(f'|=- CPF - {vetor2[i]}')
        print(f'|=- Telefone - {vetor3[i]}')
        print(f'|=- Email - {vetor4[i]}')
        print(f'|=- Endereço - {vetor5[i]}')
        print(f'|=- Cidade - {vetor6[i]}')
        print('')

def excluir(vetor1, vetor2, vetor3, vetor4, vetor5, vetor6):
    listar(vetor1, vetor2, vetor3, vetor4, vetor5, vetor6)
    if not(vetor1.__len__() == 0):
        while (True):
            try:
                print('|> ----menu editar---- <|')
                print('|                       |')
                print('|>- 1. Pelo Indice      |')
                print('|>- 2. Pelo Nome        |')
                print('|>- ------------------ <|')
                print('')
                opc_2 = int(input('|> - Digite a opção desejada: '))
                if ((opc_2 == 1) or (opc_2 == 2)):
                    break
                else:
                    print('\n=- Opção não listada')
                    print('=- Tente novamente!\n')
                    continue
            except ValueError:
                print('\n=- Valor invalido\n')
                continue
        if (opc_2 == 1):
            while (True):
                try:
                    indice = int(input('=- Digite o indice do cadastro que dedeja editar: '))
                    if (indice > vetor1.__len__()):
                        print('\n=- Indice não ocupado!')
                        print('=- Tente novamente!\n')
                        continue
                    else: 
                        break
                except ValueError:
                    print('\n=- Valor invalido\n')
                    continue                
        if (opc_2 == 2):
            while (True):
                nome = str(input('=- Digite o nome do cadastro que dedeja editar: ')).strip().title()
                for i in range (0, vetor1.__len__()):
                    if (nome == vetor1[i]):
                        indice = i
                        break
                else: 
                    print('\n=- Nome não existente!')
                    print('=- Tente novamente!\n')
                    continue
                break
        vetor1.pop(indice)
        vetor2.pop(indice)
        vetor3.pop(indice)
        vetor4.pop(indice)
        vetor5.pop(indice)
        vetor6.pop(indice)


#! Menu --->
while (True):
    try:
        while (True):
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
        nomes.append(inputNome(nomes))
        cpfs.append(inputCpf(cpfs))
        telefones.append(inputTelefone(telefones))
        emails.append(inputEmail(emails))
        enderecos.append(inputEndereco())
        cidades.append(inputCidade())
        print('=- Cadastro realizado com sucesso!!\n')

    # Opc 2. - Editar
    elif (opc == 2):
        editar(nomes, cpfs, telefones, emails, enderecos, cidades)

    # Opc 3. - Listar
    elif (opc == 3):
        listar(nomes, cpfs, telefones, emails, enderecos, cidades)
    
    # Opc 4. - Excluir
    elif (opc == 4):
        excluir(nomes, cpfs, telefones, emails, enderecos, cidades)

    # Opc 0. - Sair
    elif (opc == 0):
        print('FOI TARDE!!')
        exit()

    # Opc ?. - Error
    else:
        print('\n=- Valor invalido\n')
        continue