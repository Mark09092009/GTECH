# Marcos Vinicius de Sousa
# luiz Gustavo
# Pedro Lucas
# Gabriel

import sys
from PyQt5.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QMessageBox, QListWidget, QInputDialog, QHBoxLayout, QTableWidget, QTableWidgetItem, QHeaderView
)

# Listas para armazenar os dados
cadastros = []

class CadastroApp(QWidget):
    
    #Responsável por fixar o display dos botões
    @staticmethod
    def add_centered_button(layout, button):
        hbox = QHBoxLayout()
        hbox.addStretch()  # Espaço antes do botão
        hbox.addWidget(button)
        hbox.addStretch()  # Espaço depois do botão
        layout.addLayout(hbox)

    def __init__(self):
        super().__init__()
        self.initUI()

    # responsável por configurar a interface gráfica da janela
    def initUI(self):

        # Janela, Tamanho e Titulo
        self.setGeometry(100, 50, 450, 450)
        self.setWindowTitle('GTECH')
        

        layout = QVBoxLayout()

        self.btn_cadastrar = QPushButton('1. Cadastrar', self)
        self.btn_cadastrar.clicked.connect(self.cadastrar)
        self.btn_cadastrar.setStyleSheet('''
                                    padding: 10px;
                                    font-size: 20px;
                                        ''')
        self.btn_cadastrar.setMinimumSize(200, 70)  # Tamanho mínimo
        self.btn_cadastrar.setMaximumSize(350, 130)  # Tamanho máximo

        self.btn_editar = QPushButton('2. Editar', self)
        self.btn_editar.clicked.connect(self.opc_editar)
        self.btn_editar.setStyleSheet('''
                                    padding: 10px;
                                    font-size: 20px;
                                        ''')
        self.btn_editar.setMinimumSize(200, 70)  # Tamanho mínimo
        self.btn_editar.setMaximumSize(350, 130)  # Tamanho máximo                                

        self.btn_listar = QPushButton('3. Listar', self)
        self.btn_listar.clicked.connect(self.listar)
        self.btn_listar.setStyleSheet('''
                                    padding: 10px;
                                    font-size: 20px;
                                        ''')
        self.btn_listar.setMinimumSize(200, 70)  # Tamanho mínimo
        self.btn_listar.setMaximumSize(350, 130)  # Tamanho máximo                                

        self.btn_excluir = QPushButton('4. Excluir', self)
        self.btn_excluir.clicked.connect(self.excluir)
        self.btn_excluir.setStyleSheet('''
                                    padding: 10px;
                                    font-size: 20px;
                                        ''')
        self.btn_excluir.setMinimumSize(200, 70)  # Tamanho mínimo
        self.btn_excluir.setMaximumSize(350, 130)  # Tamanho máximo

        self.btn_sair = QPushButton('0. Sair', self)
        self.btn_sair.clicked.connect(self.sair)
        self.btn_sair.setStyleSheet('''
                                    padding: 10px;
                                    font-size: 20px;
                                        ''')
        self.btn_sair.setMinimumSize(90, 40)  # Tamanho mínimo
        self.btn_sair.setMaximumSize(200, 50)  # Tamanho máximo

        CadastroApp.add_centered_button(layout, self.btn_cadastrar)
        CadastroApp.add_centered_button(layout, self.btn_editar)
        CadastroApp.add_centered_button(layout, self.btn_listar)
        CadastroApp.add_centered_button(layout, self.btn_excluir)
        CadastroApp.add_centered_button(layout, self.btn_sair)

        # Remove o espaçamento entre os widgets
        #layout.setSpacing(0)
        # Remove as margens do layout
        #layout.setContentsMargins(0, 0, 0, 0)

        self.setLayout(layout)
    def validarEmail(self, email):

        while (True):
            if (email.count('@') != 1 ):
                QMessageBox.warning(self, 'Erro', 'Email invalido!! \nTente novamente!!')
                return False
            usuario, dominio = email.split('@')
            if (dominio != 'gmail.com'):
                QMessageBox.warning(self, 'Erro', 'dominio invalido!! \nTente novamente!!')
                return False
            if ((usuario.startswith('.')) or (usuario.endswith('.'))):
                QMessageBox.warning(self, 'Erro', 'O email não pode começar / terminar com "." !! \nTente novamente!!')
                return False
            if ('..' in usuario):
                QMessageBox.warning(self, 'Erro', 'Não pode haver ".." no email! \nTente novamente!!')
                return False
            for caractere in usuario:
                if not (caractere.isalnum() or caractere in ['.', '_', '-', '+']):
                    QMessageBox.warning(self, 'Erro', 'Caracteres invalidos!! \nTente novamente!!')
                    return False
            return True

    def cadastrar(self):
        while (True):
            nome_p, ok = QInputDialog.getText(self, 'Cadastrar', 'Digite seu primeiro nome: ')
            if not(ok):
                break
            if (nome_p.isalpha() and ok):
                break
            elif not(nome_p.isalpha()):
                QMessageBox.warning(self, 'Erro', 'Somente o primeiro nome!! \nSomente letra e sem espaços entre elas!!')
                continue

        while (ok):
            nome_s, ok = QInputDialog.getText(self, 'Cadastrar', 'Digite seu ultimo sobrenome: ')
            if not(ok):
                break
            if (nome_s.isalpha() and ok):
                break
            elif not(nome_s.isalpha()):
                QMessageBox.warning(self, 'Erro', 'Somente o sobrenome!! \nSomente letra e sem espaços entre elas!!')
                continue

        while (ok):
            cpf, ok = QInputDialog.getText(self, 'Cadastrar', 'Digite seu CPF: ')
            if not(ok):
                break
            elif not(cpf.isnumeric()):
                QMessageBox.warning(self, 'Erro', 'Somente numeros!!')
                continue
            elif not(len(cpf) == 11 ):
                QMessageBox.warning(self, 'Erro', 'CPF necessita ser composto por 11 numeros!!')
                continue
            ja_cadastrado = False
            for i, cadastro in enumerate(cadastros):
                if (cadastro['cpf'] == cpf):
                    ja_cadastrado = True
            if (ja_cadastrado):
                QMessageBox.warning(self, 'Erro', 'CPF ja cadastrado!!')
                continue
            elif (cpf and ok):
                break

        while (ok):
            telefone, ok = QInputDialog.getText(self, 'Cadastrar', 'Digite seu telefone: ')
            if not(ok):
                break
            elif not(telefone.isnumeric()):
                QMessageBox.warning(self, 'Erro', 'Somente numeros!!')
                continue
            elif not(len(telefone) == 11):
                QMessageBox.warning(self, 'Erro', 'Telefone necessita ser composto por 11 numeros!!')
                continue
            ja_cadastrado = False
            for i, cadastro in enumerate(cadastros):
                if (cadastro['telefone'] == telefone):
                    ja_cadastrado = True
            if (ja_cadastrado):
                QMessageBox.warning(self, 'Erro', 'Telefone ja cadastrado!!')
                continue
            elif (telefone and ok):
                break

        while (ok):
            email, ok = QInputDialog.getText(self, 'Cadastrar', 'Digite seu E-mail (@gmail.com): ')
            if not(ok):
                break
            if (self.validarEmail(email) and ok):
                break

        while (ok):  
            endereco, ok = QInputDialog.getText(self, 'Cadastrar', 'Digite seu endereco: ')
            if not(ok):
                break
            if (endereco and ok):
                break

        while (ok):            
            cidade, ok = QInputDialog.getText(self, 'Cadastrar', 'Digite o nome de sua cidade: ')
            if (cidade and ok):

                nome = nome_p.strip().title() + ' ' + nome_s.strip().title()
                endereco = endereco.strip().title()
                cidade = cidade.strip().title()
                cadastro = (
                    {
                        'nome': nome,
                        'cpf': cpf,
                        'telefone': telefone,
                        'email': email,
                        'endereco': endereco,
                        'cidade': cidade
                    }
                )
                cadastros.append(cadastro)
                QMessageBox.information(self, 'Sucesso!', 'Cadastro realizado com sucesso!!')
                break
    
    def opc_editar(self):
        if len(cadastros) == 0:  # Verifica se a lista de cadastros está vazia
            QMessageBox.warning(self, 'Erro', 'Nenhum cadastro encontrado!')
            return

        # Chama a função de listar para exibir os cadastros
        self.listar()

        while True:
            self.editar_indice, ok = QInputDialog.getInt(self, 'Editar', 'Digite o índice do cadastro que deseja editar: ')
            if not ok:
                break  # Sai do loop se o usuário cancelar

            if self.editar_indice < 0 or self.editar_indice >= len(cadastros):
                QMessageBox.warning(self, 'Erro', 'Índice inválido!')
                continue  # Pede o índice novamente

            # Abre a janela de edição
            self.abrir_janela_edicao()
            self.dicionario = cadastros[self.editar_indice]
            break

    def abrir_janela_edicao(self):
        # Cria a janela de edição
        self.editar_window = QWidget()
        self.editar_window.setGeometry(100, 525, 520, 450)
        self.editar_window.setWindowTitle('Editar')

        # Sobrescreve o método closeEvent da janela de edição
        self.editar_window.closeEvent = self.fechar_janela_edicao

        layout = QVBoxLayout()

        self.btn_nome = QPushButton('1. Nome', self)
        self.btn_nome.clicked.connect(self.editar)
        self.btn_nome.setStyleSheet('''
                                    padding: 25px;
                                    font-size: 20px;
                                        ''')

        layout.addWidget(self.btn_nome)

        self.btn_cpf = QPushButton('2. CPF', self)
        self.btn_cpf.clicked.connect(self.editar)
        self.btn_cpf.setStyleSheet('''
                                    padding: 25px;
                                    font-size: 20px;
                                        ''')

        layout.addWidget(self.btn_cpf)

        self.btn_telefone = QPushButton('3. Telefone', self)
        self.btn_telefone.clicked.connect(self.editar)
        self.btn_telefone.setStyleSheet('''
                                    padding: 25px;
                                    font-size: 20px;
                                        ''')

        layout.addWidget(self.btn_telefone)

        self.btn_email = QPushButton('4. E-mail', self)
        self.btn_email.clicked.connect(self.editar)
        self.btn_email.setStyleSheet('''
                                    padding: 25px;
                                    font-size: 20px;
                                        ''')

        layout.addWidget(self.btn_email)

        self.btn_endereco = QPushButton('5. Endereço', self)
        self.btn_endereco.clicked.connect(self.editar)
        self.btn_endereco.setStyleSheet('''
                                    padding: 25px;
                                    font-size: 20px;
                                        ''')

        layout.addWidget(self.btn_endereco)

        self.btn_cidade = QPushButton('6. Cidade', self)
        self.btn_cidade.clicked.connect(self.editar)
        self.btn_cidade.setStyleSheet('''
                                    padding: 25px;
                                    font-size: 20px;
                                        ''')

        layout.addWidget(self.btn_cidade)

        # Define o layout da janela de edição
        self.editar_window.setLayout(layout)

        # Exibe a janela de edição
        self.editar_window.show()

    def fechar_janela_edicao(self, event):
        # Função chamada quando a janela de edição é fechada
        self.editar_window = None  # Remove a referência à janela de edição
        event.accept()  # Aceita o evento de fechamento

    def editar(self):
        # Identifica qual botão foi clicado
        sender = self.sender()

        if sender == self.btn_nome:
            nome_p, ok = QInputDialog.getText(self, 'Editar', 'Digite seu primeiro nome: ')
            if ok and nome_p.isalpha():
                nome_s, ok = QInputDialog.getText(self, 'Editar', 'Digite seu último sobrenome: ')
                if ok and nome_s.isalpha():
                    nome = nome_p.strip().title() + ' ' + nome_s.strip().title()
                    self.dicionario['nome'] = nome
                    cadastros[self.editar_indice] = self.dicionario
                    QMessageBox.information(self, 'Sucesso', 'Nome atualizado com sucesso!')
                    self.editar_window.close()  # Fecha a janela de edição após a conclusão

        elif sender == self.btn_cpf:
            cpf, ok = QInputDialog.getText(self, 'Editar', 'Digite seu CPF: ')
            if ok and cpf.isnumeric() and len(cpf) == 11:
                ja_cadastrado = any(cadastro['cpf'] == cpf for cadastro in cadastros)
                if not ja_cadastrado:
                    self.dicionario['cpf'] = cpf
                    cadastros[self.editar_indice] = self.dicionario
                    QMessageBox.information(self, 'Sucesso', 'CPF atualizado com sucesso!')
                    self.editar_window.close()  # Fecha a janela de edição após a conclusão
                else:
                    QMessageBox.warning(self, 'Erro', 'CPF já cadastrado!')

        elif sender == self.btn_telefone:
            telefone, ok = QInputDialog.getText(self, 'Editar', 'Digite seu telefone: ')
            if ok and telefone.isnumeric() and len(telefone) == 11:
                ja_cadastrado = any(cadastro['telefone'] == telefone for cadastro in cadastros)
                if not ja_cadastrado:
                    self.dicionario['telefone'] = telefone
                    cadastros[self.editar_indice] = self.dicionario
                    QMessageBox.information(self, 'Sucesso', 'Telefone atualizado com sucesso!')
                    self.editar_window.close()  # Fecha a janela de edição após a conclusão
                else:
                    QMessageBox.warning(self, 'Erro', 'Telefone já cadastrado!')

        elif sender == self.btn_email:
            email, ok = QInputDialog.getText(self, 'Editar', 'Digite seu E-mail (@gmail.com): ')
            if ok and self.validarEmail(email):
                self.dicionario['email'] = email
                cadastros[self.editar_indice] = self.dicionario
                QMessageBox.information(self, 'Sucesso', 'E-mail atualizado com sucesso!')
                self.editar_window.close()  # Fecha a janela de edição após a conclusão

        elif sender == self.btn_endereco:
            endereco, ok = QInputDialog.getText(self, 'Editar', 'Digite seu endereço: ')
            if ok and endereco.strip():
                self.dicionario['endereco'] = endereco.strip().title()
                cadastros[self.editar_indice] = self.dicionario
                QMessageBox.information(self, 'Sucesso', 'Endereço atualizado com sucesso!')
                self.editar_window.close()  # Fecha a janela de edição após a conclusão

        elif sender == self.btn_cidade:
            cidade, ok = QInputDialog.getText(self, 'Editar', 'Digite o nome de sua cidade: ')
            if ok and cidade.strip():
                self.dicionario['cidade'] = cidade.strip().title()
                cadastros[self.editar_indice] = self.dicionario
                QMessageBox.information(self, 'Sucesso', 'Cidade atualizada com sucesso!')
                self.editar_window.close()  # Fecha a janela de edição após a conclusão
        self.atualizar_tabela()

    def excluir(self):
        if len(cadastros) == 0:  # Verifica se a lista de cadastros está vazia
            QMessageBox.warning(self, 'Erro', 'Nenhum cadastro encontrado!')
            return

        # Chama a função de listar para exibir os cadastros
        self.listar()
        
        while True:
            excluir_indice, ok = QInputDialog.getInt(self, 'Excluir', 'Digite o índice do cadastro que deseja excluir: ')
            if not ok:
                break  # Sai do loop se o usuário cancelar

            if excluir_indice < 0 or excluir_indice >= len(cadastros):
                QMessageBox.warning(self, 'Erro', 'Índice inválido!')
                continue  # Pede o índice novamente

            else:
                cadastros.pop(excluir_indice)
                QMessageBox.information(self, 'Excluir', 'Cadastro excluído com sucesso!!')
                
                if len(cadastros) == 0:  # Verifica se a lista de cadastros está vazia após a exclusão
                    if hasattr(self, 'lista_window') and self.lista_window is not None:
                        self.lista_window.close()  # Fecha a janela de listagem
                        self.lista_window = None  # Remove a referência à janela de listagem
                else:
                    # Atualiza a lista de cadastros na janela de listagem
                    self.atualizar_tabela()

                break
    
    def listar(self):
        if len(cadastros) == 0:  # Verifica se a lista de cadastros está vazia
            QMessageBox.warning(self, 'Erro', 'Nenhum cadastro encontrado!')
            return

        # Se a janela de listagem já existir, apenas atualize a lista
        if hasattr(self, 'lista_window') and self.lista_window is not None:
            self.atualizar_tabela()
            return

        # Cria uma nova janela de listagem
        self.lista_window = QWidget()
        self.lista_window.setGeometry(550, 50, 950, 450)
        self.lista_window.setWindowTitle('Lista de Cadastros')

        # Sobrescreve o método closeEvent para limpar a referência à janela
        self.lista_window.closeEvent = self.fechar_janela_listagem

        layout = QVBoxLayout()
        self.table_widget = QTableWidget()  # Armazena o QTableWidget como atributo

        # Preenche a lista com os cadastros
        self.atualizar_tabela()

        layout.addWidget(self.table_widget)
        self.lista_window.setLayout(layout)

        # Exibe a nova janela de listagem
        self.lista_window.show()
    
    def fechar_janela_listagem(self, event):
        # Função chamada quando a janela de listagem é fechada
        self.lista_window = None  # Remove a referência à janela de listagem
        event.accept()  # Aceita o evento de fechamento

    def atualizar_tabela(self):
        # Atualiza o conteúdo do QTableWidget com os dados mais recentes
        self.table_widget.clear()  # Limpa a tabela atual
        self.table_widget.setRowCount(len(cadastros))  # Define o número de linhas

        # Define o número de colunas e os cabeçalhos horizontais
        self.table_widget.setColumnCount(6)
        self.table_widget.setHorizontalHeaderLabels(["Nome", "CPF", "Telefone", "E-mail", "Endereço", "Cidade"])
        self.table_widget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

        # Define os cabeçalhos verticais (índices das linhas) começando em 0
        self.table_widget.setVerticalHeaderLabels([str(i) for i in range(len(cadastros))])
        self.table_widget.verticalHeader().setMinimumWidth(50)  # Define um tamanho adequado para os índices

        # Preenche a tabela com os dados
        for row, cadastro in enumerate(cadastros):
            self.table_widget.setItem(row, 0, QTableWidgetItem(cadastro['nome']))
            self.table_widget.setItem(row, 1, QTableWidgetItem(cadastro['cpf']))
            self.table_widget.setItem(row, 2, QTableWidgetItem(cadastro['telefone']))
            self.table_widget.setItem(row, 3, QTableWidgetItem(cadastro['email']))
            self.table_widget.setItem(row, 4, QTableWidgetItem(cadastro['endereco']))
            self.table_widget.setItem(row, 5, QTableWidgetItem(cadastro['cidade']))

        # Aplica o estilo à tabela
        self.table_widget.setStyleSheet('''
                                    padding: 3px;
                                    font-size: 20px;
                                        ''')
        
    
    def sair(self):
        while True:
            sair, ok = QInputDialog.getInt(self, 'Sair', 'Deseja mesmo sair? \n0- Sim \n1- Não')
            if ((sair != 0) and (sair != 1) and ok):
                QMessageBox.warning(self, 'Erro', 'Opção não listada!!')
                continue
            if ((sair == 0) and ok):
                exit()
            elif (((sair == 1) and ok) or not(ok)):
                return
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    janela = CadastroApp()
    janela.show()
    sys.exit(app.exec_())