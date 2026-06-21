import requests
import logging

from requests.exceptions import RequestException

class ZAPIClient:

    API_URL = "https://api.z-api.io"

    def __init__(self, instance_id: str, instance_token: str, account_token: str = ""):
        self.instance_id = instance_id
        self.instance_token = instance_token
        self.account_token = account_token

        logging.debug(f"Cliente Z-API criado. URL base: {self._get_base_url()}")

    @staticmethod
    def get_default_message(name: str) -> str:
        return f"Olá, {name}! Tudo bem com você?"

    """
    Envia uma mensagem a um número
    params:
        receiver_phone: número do destinatário
        message: texto da mensagem a ser enviada
    returns:
        dict do JSON retornado na resposta do request ou None em caso de falha
    """
    def send_message(self, receiver_phone: str, message: str) -> dict | None:
        url = f"{self._get_base_url()}/send-text"
        headers = self._get_request_headers()
        payload = self._get_send_message_payload(receiver_phone, message)

        try:
            response = requests.post(url, headers=headers, json=payload, timeout=8)
            if response.status_code == 200:
                logging.info(f"Mensagem enviada com sucesso. Destinatário: {receiver_phone}, Mensagem: {message}")
            else:
                logging.error(f"Falha ao enviar mensagem. Erro: {response.status_code}, {response.json()}, Destinatário: {receiver_phone}, Mensagem: {message}")

            return response.json()
        except RequestException as e:
            logging.error(f"POST Request to URL {url} has failed: {e}")
            return None

    def _get_base_url(self) -> str:
        return f"{self.API_URL}/instances/{self.instance_id}/token/{self.instance_token}"
    
    def _get_request_headers(self) -> dict:
        return {
            "Client-Token" : self.account_token,
            "Content-Type" : "application/json"
        }
    
    def _get_send_message_payload(self, phone: str, message: str) -> dict:
        return {
            "phone": phone,
            "message": message
        }