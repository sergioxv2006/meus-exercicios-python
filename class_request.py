from abc import ABC, abstractmethod
import requests # Fazer requisição
import datetime # Manipular datas

class IVerificador(ABC):
    @abstractmethod
    def verificar(self) -> bool:
        pass

class IAlerta(ABC):
    @abstractmethod
    def enviar_alerta(self, mensagem: str):
        pass

# Classes Concretas

class VerificarAPI(IVerificador):
    def __init__(self, url: str):
        self.__url = url # privado

    def verificar(self) -> bool:
        try:
            response = requests.get(self.__url, timeout=5)
            if response.status_code == 200:
                print(f"--> Status: OK (200)")
                return True
            else:
                print("--> Status: ERRO")
        except requests.exceptions.RequestException as e:
            print(f"--> ERRO DE CONEXÃO: {e}")
            return False
        
class AlertaSlack(IAlerta):
    def __init__(self, webhook_url: str):
        self.__webhook_url = webhook_url

    def enviar_alerta(self, mensagem: str):

        payload = {"text:" f"ALERTA URGENTE \n{mensagem}"}

        try:
            print("(ALERTA) Enviando para o slack...")
            requests.post(self.__webhook_url, json=payload, timeout=5).raise_for_status()
            print("Alerta enviado com sucesso!")
        except requests.exceptions.RequestException as e:
            print(f"--> ERRO ao enviar alerta ao Slack: {e}")

class AlertaEmail(IAlerta):
    def __init__(self, destinatario: str):
        self._destinatario = destinatario

    def enviar_alerta(self, mensagem: str):
        print(f"(ALERTA) Gerando e-mail para {self._destinatario}...")

class Monitor:
    def __init__(self, verificador: IVerificador, alerta: IAlerta):
        self._verificador = verificador
        self._alerta = alerta

    def rodar_ciclo(self):

        print("Iniciando novo ciclo...")
        if not self._verificador.verificar():
            self._alerta.enviar_alerta("O serviço está offline ou retornando erro.")
        else:
            print("Serviço funcionando normalmente.")

url_webhook = 'https://webhook.site/9450e813-dea7-423c-9fdc-9f84db595df5'
url_real = 'https://ufpa.br/'
url_fake = 'https://url-inexistente-12345.com/'

alerta_para_slack = AlertaSlack(url_webhook)
alerta_para_email = AlertaEmail("9450e813-dea7-423c-9fdc-9f84db595df5@emailhook.site")

verificar_ok = VerificarAPI(url=url_real)
verificador_falha = VerificarAPI(url=url_fake)

# 1 cenário: tudo ok
monitor_principal = Monitor(verificar_ok, alerta_para_slack)
monitor_principal.rodar_ciclo()

# 2 cenário: falha na verificação
monitor_secundario = Monitor(verificador_falha, alerta_para_email)
monitor_secundario.rodar_ciclo()
