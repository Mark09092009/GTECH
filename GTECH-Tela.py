# Marcos Vinicius de Sousa
# luiz Gustavo
# Pedro Lucas
# Gabriel

import sys
from PyQt5.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QMessageBox, QListWidget, QInputDialog
)

# Listas para armazenar os dados
cadastros = []

class CadastroApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    # responsável por configurar a interface gráfica da janela
    def initUI(self):

        # Janela, Tamanho e Titulo
        self.setGeometry(100, 100, 400, 300)
        self.setWindowTitle('GTECH')

        layout = QVBoxLayout()

        self.btn_cadastrar = QPushButton('1. Cadastrar', self)
        self.btn_cadastrar.clicked.connect(self.cadastrar)
        layout.addWidget(self.btn_cadastrar)

        self.btn_editar = QPushButton('2. Editar', self)
        self.btn_editar.clicked.connect(self.opc_editar)
        layout.addWidget(self.btn_editar)

        self.btn_listar = QPushButton('3. Listar', self)
        self.btn_listar.clicked.connect(self.listar)
        layout.addWidget(self.btn_listar)

        self.btn_excluir = QPushButton('4. Excluir', self)
        self.btn_excluir.clicked.connect(self.excluir)
        layout.addWidget(self.btn_excluir)

        self.btn_sair = QPushButton('0. Sair', self)
        self.btn_sair.clicked.connect(self.sair)
        layout.addWidget(self.btn_sair)

        self.setLayout(layout)

    def cadastrar(self):
        while (True):
            nome_p, ok = QInputDialog.getText(self, 'Cadastrar', 'Digite seu primeiro nome: ')
            if not(ok):
                break
            if (nome_p.isalpha() and ok):
                break
            elif not(nome_p.isalpha()):
                QMessageBox.warning(self, 'Erro', 'Somente letra e sem espaços entre elas!!')
                continue

        while (ok):
            nome_s, ok = QInputDialog.getText(self, 'Cadastrar', 'Digite seu sobrenome: ')
            if not(ok):
                break
            if (nome_s.isalpha() and ok):
                break
            elif not(nome_s.isalpha()):
                QMessageBox.warning(self, 'Erro', 'Somente letra e sem espaços entre elas!!')
                continue

        while (ok):
            cpf, ok = QInputDialog.getText(self, 'Cadastrar', 'Digite seu CPF: ')
            if not(ok):
                break
            if (cpf.isnumeric() and ok and (len(cpf) == 11 )):
                break
            elif not(cpf.isnumeric()):
                QMessageBox.warning(self, 'Erro', 'Somente numeros!!')
                continue
            elif not(len(cpf) == 11 ):
                QMessageBox.warning(self, 'Erro', 'CPF necessita ser composto por 11 numeros!!')
                continue
        
        while (ok):
            telefone, ok = QInputDialog.getText(self, 'Cadastrar', 'Digite seu telefone: ')
            if not(ok):
                break
            if (telefone.isnumeric() and ok and (len(telefone) == 11)):
                break
            elif not(telefone.isnumeric()):
                QMessageBox.warning(self, 'Erro', 'Somente numeros!!')
                continue
            elif not(len(telefone) == 11):
                QMessageBox.warning(self, 'Erro', 'Telefone necessita ser composto por 11 numeros!!')
                continue
        
        while (ok):
            email, ok = QInputDialog.getText(self, 'Cadastrar', 'Digite seu E-mail: ')
            if not(ok):
                break
            if (email and ok):
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

                nome = nome_p + ' ' + nome_s
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
        self.editar_window.setGeometry(100, 400, 300, 300)
        self.editar_window.setWindowTitle('Editar')

        # Sobrescreve o método closeEvent da janela de edição
        self.editar_window.closeEvent = self.fechar_janela_edicao

        layout = QVBoxLayout()

        self.btn_nome = QPushButton('1. Nome', self)
        self.btn_nome.clicked.connect(self.editar)
        layout.addWidget(self.btn_nome)

        self.btn_cpf = QPushButton('2. CPF', self)
        self.btn_cpf.clicked.connect(self.editar)
        layout.addWidget(self.btn_cpf)

        self.btn_telefone = QPushButton('3. Telefone', self)
        self.btn_telefone.clicked.connect(self.editar)
        layout.addWidget(self.btn_telefone)

        self.btn_email = QPushButton('4. E-mail', self)
        self.btn_email.clicked.connect(self.editar)
        layout.addWidget(self.btn_email)

        self.btn_endereco = QPushButton('5. Endereço', self)
        self.btn_endereco.clicked.connect(self.editar)
        layout.addWidget(self.btn_endereco)

        self.btn_cidade = QPushButton('6. Cidade', self)
        self.btn_cidade.clicked.connect(self.editar)
        layout.addWidget(self.btn_cidade)

        # Define o layout da janela de edição
        self.editar_window.setLayout(layout)

        # Exibe a janela de edição
        self.editar_window.show()

    def fechar_janela_edicao(self, event):
        # Função chamada quando a janela de edição é fechada
        if (self.ok):
            QMessageBox.information(self, 'Edição', 'Edição concluída')
            self.editar_window = None  # Remove a referência à janela de edição
            event.accept()  # Aceita o evento de fechamento
        else:
            self.editar_window = None  # Remove a referência à janela de edição
            event.accept()  # Aceita o evento de fechamento

    def editar(self):
        # Identifica qual botão foi clicado

        sender = self.sender()

        if (sender == self.btn_nome):
            while (True):
                nome_p, self.ok = QInputDialog.getText(self, 'Editar', 'Digite seu primeiro nome: ')
                if not(self.ok):
                    break
                if (nome_p.isalpha() and self.ok):
                    break
                elif not(nome_p.isalpha()):
                    QMessageBox.warning(self, 'Erro', 'Somente letra e sem espaços entre elas!!')
                    continue

            while (self.ok):
                nome_s, self.ok = QInputDialog.getText(self, 'Editar', 'Digite seu sobrenome: ')
                if not(self.ok):
                    break
                if (nome_s.isalpha() and self.ok):
                    break
                elif not(nome_s.isalpha()):
                    QMessageBox.warning(self, 'Erro', 'Somente letra e sem espaços entre elas!!')
                    continue

            if (self.ok):
                nome = nome_p + ' ' + nome_s
                self.dicionario['nome'] = nome
                cadastros[self.editar_indice] = self.dicionario

        elif (sender == self.btn_cpf):
            while (True):
                cpf, self.ok = QInputDialog.getText(self, 'Editar', 'Digite seu CPF: ')
                if not(self.ok):
                    break
                if (cpf.isnumeric() and self.ok and (len(cpf) == 11 )):
                    self.dicionario['cpf'] = cpf
                    cadastros[self.editar_indice] = self.dicionario
                    break
                elif not(cpf.isnumeric()):
                    QMessageBox.warning(self, 'Erro', 'Somente numeros!!')
                    continue
                elif not(len(cpf) == 11 ):
                    QMessageBox.warning(self, 'Erro', 'CPF necessita ser composto por 11 numeros!!')
                    continue

        elif (sender == self.btn_telefone):
            while (True):
                telefone, self.ok = QInputDialog.getText(self, 'Editar', 'Digite seu telefone: ')
                if not(self.ok):
                    break
                if (telefone.isnumeric() and self.ok and (len(telefone) == 11)):
                    self.dicionario['telefone'] = telefone
                    cadastros[self.editar_indice] = self.dicionario
                    break
                elif not(telefone.isnumeric()):
                    QMessageBox.warning(self, 'Erro', 'Somente numeros!!')
                    continue
                elif not(len(telefone) == 11):
                    QMessageBox.warning(self, 'Erro', 'Telefone necessita ser composto por 11 numeros!!')
                    continue
                
        elif (sender == self.btn_email):
            while (True):
                email, self.ok = QInputDialog.getText(self, 'Editar', 'Digite seu E-mail: ')
                if not(self.ok):
                    break
                if (email and self.ok):
                    self.dicionario['email'] = email
                    cadastros[self.editar_indice] = self.dicionario
                    break

        elif (sender == self.btn_endereco):
            while (True):  
                endereco, self.ok = QInputDialog.getText(self, 'Editar', 'Digite seu endereco: ')
                if not(self.ok):
                    break
                if (endereco and self.ok):
                    self.dicionario['endereco'] = endereco
                    cadastros[self.editar_indice] = self.dicionario
                    break

        elif (sender == self.btn_cidade):
            while (True):
                cidade, self.ok = QInputDialog.getText(self, 'Editar', 'Digite o nome de sua cidade: ')
                if not(self.ok):
                    break
                if (cidade and self.ok):
                    self.dicionario['cidade'] = cidade
                    cadastros[self.editar_indice] = self.dicionario
                    break
                    
        
        self.editar_window.close()

        # Chama a função de listar para exibir os cadastros
        self.listar()

    def excluir(self):
        print('Botao clicado')
        
    def listar(self):
        if len(cadastros) == 0:  # Verifica se a lista de cadastros está vazia
            QMessageBox.warning(self, 'Erro', 'Nenhum cadastro encontrado!')
            return

        # Se a janela de listagem já existir, apenas atualize a lista
        if hasattr(self, 'lista_window') and self.lista_window is not None:
            self.atualizar_lista()
            return

        # Cria uma nova janela de listagem
        self.lista_window = QWidget()
        self.lista_window.setGeometry(500, 100, 400, 300)
        self.lista_window.setWindowTitle('Lista de Cadastros')

        layout = QVBoxLayout()
        self.lista_widget = QListWidget()  # Armazena o QListWidget como atributo

        # Preenche a lista com os cadastros
        self.atualizar_lista()

        layout.addWidget(self.lista_widget)
        self.lista_window.setLayout(layout)

        # Exibe a nova janela de listagem
        self.lista_window.show()

    def atualizar_lista(self):
        # Atualiza o conteúdo do QListWidget com os dados mais recentes
        self.lista_widget.clear()  # Limpa a lista atual

        for i, cadastro in enumerate(cadastros):
            item_text = (
                f"Cadastro  {i}  ---> \n"
                f"Nome: {cadastro['nome']} \n"
                f"CPF: {cadastro['cpf']} \n"
                f"Telefone: {cadastro['telefone']} \n"
                f"E-mail: {cadastro['email']} \n"
                f"Endereço: {cadastro['endereco']} \n"
                f"Cidade: {cadastro['cidade']}\n\n"
            )
            self.lista_widget.addItem(item_text)  # Adiciona o item ao QListWidget

    
    def sair(self):
        print('Botao clicado')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    janela = CadastroApp()
    janela.show()
    sys.exit(app.exec_())
