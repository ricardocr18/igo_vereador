# -*- coding: utf-8 -*-
from odoo import models, fields, api,tools,exceptions, _, SUPERUSER_ID

class RelatorioSolicitacao(models.TransientModel):
    _name = 'report_solicitacao'
    #Campos para o usuario selecionar
    status = fields.Selection([('andamento', 'Em andamento'),
                               ('pendente', 'Pendente'),
                               ('concluido', 'Concluído')], string="Status")

    cpf = fields.Char("CPF")


    def get_report(self):
        #Funcao que retorna o campo solucionado
        data = {
            'ids': self.ids,
            'model': self._name,
            'form': {
                'status': self.status,
                'cpf': self.cpf,

            },
        }
        #Retorno para a view pdf_report com o ID recap_report
        return self.env.ref('igo_vereador.recap_report').report_action(self, data=data)

class ReportRelatorioSolicitacao(models.AbstractModel):
    #Model de construcao do relatorio o nome da model deve sempre começar com report
    _name = 'report.igo_vereador.solicitacao_report_view'

    @api.model
    def _get_report_values(self, docids, data=None):
        status = data['form']['status']
        cpf = data['form']['cpf']
        docs = []
        print (status,cpf)

        if status != False and cpf == False:
            solicitacoes = self.env['cadastro.cidadao'].search([('status', '=', status),], order='data_solicitacao asc')

        if cpf != False and status == False:
            solicitacoes = self.env['cadastro.cidadao'].search([('cpf', '=', cpf), ], order='data_solicitacao asc')

        if cpf != False and status != False:
            solicitacoes = self.env['cadastro.cidadao'].search([('status', '=', status),('cpf', '=', cpf), ], order='data_solicitacao asc')

        for solicitacao in solicitacoes:
            docs.append({
                'name': solicitacao.name,
                'cpf': solicitacao.cpf,
                'email': solicitacao.email,
                'telefone': solicitacao.telefone,
                'celular': solicitacao.celular,
                'descricao_pedido': solicitacao.descricao_pedido,
                'categoria': solicitacao.categoria,
                'data_solicitacao': solicitacao.data_solicitacao,
                'data_entrega': solicitacao.data_entrega,
                'status': solicitacao.status,
            })

        return {
            'doc_ids': data['ids'],
            'doc_model': data['model'],
            'status': status,
            'docs': docs,
        }

