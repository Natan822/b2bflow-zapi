import requests
import logging

logging.basicConfig(level=logging.INFO)

class ZAPIClient:

    API_URL = "https://api.z-api.io"

    def __init__(self, instance_id: str, instance_token: str, account_token: str = ""):
        self.instance_id = instance_id
        self.instance_token = instance_token
        self.account_token = account_token

        logging.debug(f"Cliente Z-API criado. URL base: {self._get_base_url()}")

    """
    Envia uma mensagem a um número
    params:
        receiver_phone: número do destinatário
        message: texto da mensagem a ser enviada
    returns:
        string do JSON retornado na resposta do request
    """
    def send_message(self, receiver_phone: str, message: str) -> str:
        url = f"{self._get_base_url()}/send-text"
        headers = self._get_request_headers()
        payload = self._get_send_message_payload(receiver_phone, message)

        response = requests.post(url, headers=headers, json=payload)
        if response.status_code == 200:
            logging.info(f"Mensagem enviada com sucesso. Destinatário: {receiver_phone}, Mensagem: {message}")
        else:
            logging.error(f"Falha ao enviar mensagem. Erro: {response.status_code}, {response.json()}, Destinatário: {receiver_phone}, Mensagem: {message}")

        return response.json()

    
    def _get_base_url(self) -> str:
        return f"{self.API_URL}/instances/{self.instance_id}/token/{self.instance_token}"
    
    def _get_request_headers(self) -> dict:
        return {
            "Client-Token" : self.account_token,
            "Content-Type" : "application/json"
        }
    
    def _get_send_message_payload(self, phone, message) -> dict:
        return {
            "phone": phone,
            "message": message
        }