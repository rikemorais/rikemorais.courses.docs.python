from datetime import datetime, timedelta

class DatasBr:
    def __init__(self):
        self.momento_cadastro = datetime.today()
        
    def mes_cadastro(self):
        meses_do_ano = ['Janeiro', 
                        'Fevereiro', 
                        'Março', 
                        'Abril', 
                        'Maio', 
                        'Junho', 
                        'Julho', 
                        'Agosto', 
                        'Setembro', 
                        'Outubro', 
                        'Novembro', 
                        'Dezembro']
    
        mes = self.momento_cadastro.month
        return meses_do_ano[mes-1]
    
    def dia_semana(self):
        dias_semana_lista = ['Segunda-feira', 
                       'Terça-feira', 
                       'Quarta-feira', 
                       'Quinta-feira', 
                       'Sexta-feira', 
                       'Sábado', 
                       'Domingo'
        ]
        dia_semana = self.momento_cadastro.weekday()
        return dias_semana_lista[dia_semana]
    
    def format_data(self):
        data_formatada = self.momento_cadastro.strftime('%d/%m/%Y %H:%M:%S')
        return data_formatada
    
    def tempo_cadastro(self):
        tempo_cadastro = (datetime.today() + timedelta(days=30)) - self.momento_cadastro
        return tempo_cadastro