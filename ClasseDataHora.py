from datetime import datetime

class DatasBR:
    def __init__(self):
        self.momento_cadastro = datetime.today()

    def mes_cadastro(self):
        meses_do_ano = ["Janeiro", "Fevereiro", "Março",
                        "Abril", "Maio", "Junho",
                        "Julho", "Agosto", "Setembro",
                        "Outubro", "Novembro", "Dezembro"]
        
        mes_cadastro = self.momento_cadastro.month-1
        return meses_do_ano[mes_cadastro]
    
    def dia_semana(self):
        dias_semana_lista = ["Domingo", "Segunda-Feira", "Terça-Feira", "Quarta-Feira", "Quinta-Feira", "Sexta-Feira", "Sábado"]
        cadastro_dia = self.momento_cadastro.weekday()+1
        return dias_semana_lista[cadastro_dia]
    
    def formata_data(self):
        data_formatada = self.momento_cadastro.strftime("%d/%m/%Y - %H:%M:%S")
        return data_formatada
    
    def tempo_cadastro(self):
        return datetime.today() - self.momento_cadastro


    def __str__(self):
        return self.formata_data()