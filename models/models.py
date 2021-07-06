# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import UserError
import requests
import json

# TABELA DO CADASTRO PRINCIPAL
class CadastroCidadao(models.Model):
    _name = 'cadastro.cidadao'
    _description = 'Cadastro do Cidadao'

    name = fields.Char("Nome Completo")
    cpf = fields.Char("CPF")
    # ("cpf").inputmask("999.999.999-99")
    email = fields.Char("E-mail")
    telefone = fields.Char("Telefone")
    celular = fields.Char("Celular")
    endereco = fields.Char("Endereço")
    cep = fields.Char("Digite o Cep")
    bairro = fields.Char("Bairro")
<<<<<<< HEAD
    municipio = fields.Char("Município")
=======
    #localidade = fields.Char("Município")
>>>>>>> 4d76488576a2f03bc14103c0512e5de96c7eb43d
    estado = fields.Char("Estado")
    datadenascimento = fields.Datetime ("Data de Nascimento")
    muni = fields.Char("muni")

    descricao_pedido = fields.Selection([('acao_social','Ação Social'),('ass_juridica','Assistência Jurídica'),
    ('ass_social','Assitência Social'), ('aterro','Aterro'),('aux_desemprogo','Auxílio Desemprego'),
    ('aux_emergencial','Auxílio Emergencial'),('bolsa_emergencial','Bolsa Emergencial'),('bola_familia','Bolsa Família'),
    ('bolsa_familia_agendamento','Bolsa Família Agendamento'),('cadastro_unico','Cadastro Único'),('cartão_sus_primeira','Cartão do SUS 1ª Via'),
    ('cartão_sus_segunda','Cartão do SUS 2ª Via'), ('cartao_idoso','Cartão Idoso'),('carteira_trabalho_primeira','Carteira de Trabalho 1ª Via'),
    ('carteira_trabalho_segunda', 'Carteira de Trabalho 2ª Via'),('cirurgira','Cirurgia'),('conservação','Conservação'),('consulta','Consulta')])

    categoria = fields.Selection([('ass_social','Ass. Social'),('conservação','Conservação'),
                                  ('documentacao','Documentação'), ('educacao','Educação'),
                                  ('lazer','Lazer'), ('limpeza','Limpeza'),('moradia','Moradia'),
                                  ('saude', 'Saúde'), ('serv_publico','Serviço Público'),
                                  ('trabalho','Trabalho')])
    data_solicitacao = fields.Datetime("Data Solicitacao")
    data_entrega = fields.Datetime("Data Entrega")
    status = fields.Selection([('andamento','Em andamento'),
                             ('pendente','Pendente'),
                             ('concluido','Concluído')],string="Status")

    observacao = fields.Text("Observação")
    acao = fields.Char("Ação")
    responsavel = fields.Many2one("res.users","Responsável")

    def consulta_cep_api(self):
        cep = self.cep.replace('-', '')
        cep = cep[:8]
        url = "https://viacep.com.br/ws/%s/json/" % cep

        payload = {}
        headers = {}
        """
        Modelo de Retorno
        {'cep': '09750-730', 
        'logradouro': 'Rua José Versolato', 
        'complemento': '', 
        'bairro': 
        'Centro', 
        'localidade': 'São Bernardo do Campo', 
        'uf': 'SP', 
        'ibge': '3548708', 
        'gia': '630', 
        'ddd': '11', 
        'siafi': '7075'}
        """
        response = requests.request("GET", url, headers=headers, data=payload)

        resultado = response.json()
        print(resultado)
        if resultado.get('erro') == True:
            raise UserError('Nenhum CEP encontrado')
        else:
            self.cep = resultado.get('cep')
            self.endereco = resultado.get('logradouro')
            self.bairro = resultado.get('bairro')
<<<<<<< HEAD
            self.municipio = resultado.get('localidade')
=======
            self.muni = resultado.get('localidade')
>>>>>>> 4d76488576a2f03bc14103c0512e5de96c7eb43d
            self.estado = resultado.get('uf')



# TABELA DOS CADASTROS DOS DADOS PARA O PROCON
class SolicitacaoProcon(models.Model):
    _name = 'solicitacao.procon'
    _description = 'Solicitação Procon'

    #Cadastro referente aos dados do reclamante
    atendente = fields.Char("Nome da Atendente")
    name = fields.Char("Nome Completo")
    cpf = fields.Char("CPF")
    rg = fields.Char("RG")
    telefone = fields.Char("Telefone")
    celular = fields.Char("Celular")
    email = fields.Char("E-mail")
    cep = fields.Char("CEP")
    endereco = fields.Char("Endereço")
    bairro = fields.Char("Bairro")
    municipio = fields.Char("Município")
    estado = fields.Char("Estado")

    def consulta_cepreclamante_api(self):
        cep = self.cep.replace('-', '')
        cep = cep[:8]
        url = "https://viacep.com.br/ws/%s/json/" % cep

        payload = {}
        headers = {}

        response = requests.request("GET", url, headers=headers, data=payload)

        resultado = response.json()
        print(resultado)
        if resultado.get('erro') == True:
            raise UserError('Nenhum CEP encontrado')
        else:
            self.cep = resultado.get('cep')
            self.endereco = resultado.get('logradouro')
            self.bairro = resultado.get('bairro')
            self.municipio = resultado.get('localidade')
            self.estado = resultado.get('uf')


    #Cadastro do Pessoa Física
    nomedaempresa = fields.Char("Nome da Empresa")
    cnpj = fields.Char("CNPJ")
    email_empresa = fields.Char("E-mail")
    telefone_empresa = fields.Char("Telefone")
    celular_empresa = fields.Char("Celular")
    cep_empresa = fields.Char("CEP")
    endereco_empresa = fields.Char("Endereço")
    bairro_empresa = fields.Char("Bairro")
    municipio_empresa = fields.Char("Município")
    estado_empresa = fields.Char("Estado")
    data_cadastro = fields.Datetime("Data do Cadastro")
    relato = fields.Text("Relato")

    def consulta_cepempresa_api(self):
        cep = self.cep_empresa.replace('-', '')
        cep = cep [:8]
        url = "https://viacep.com.br/ws/%s/json/" % cep

        payload = {}
        headers = {}

        response = requests.request("GET", url, headers=headers, data=payload)

        resultado = response.json()
        print(resultado)
        if resultado.get('erro') == True:
            raise UserError('Nenhum CEP encontrado')
        else:
            self.cep_empresa = resultado.get('cep')
            self.endereco_empresa = resultado.get('logradouro')
            self.bairro_empresa = resultado.get('bairro')
            self.municipio_empresa = resultado.get('localidade')
            self.estado_empresa = resultado.get('uf')



#AQUI SERÁ A TABELA DE CATEGORIA E SUAS DESCRIÇÕES
class CadastroCategoria(models.Model):
    _name = 'cadastro.categoria'
    _description = 'Cadastro Categoria'

    name = fields.Char("Categorias")
    descricao = fields.Char("Descriçãos")


"""AQUI SERÁ A TABELA DE DESCRIÇÃO QUE TEM REFERENCIA A CATEGORIA
class CadastroDescricao(models.Model):
    _name = 'cadastro.descricao'
    _description = 'Cadastro Descrição' """

