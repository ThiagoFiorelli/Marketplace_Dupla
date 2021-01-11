import sys
sys.path.append('.')

from datetime import datetime

log_txt = 'data/log.txt'

def generate_log(msg: str) -> None:
    data_hora_atual = datetime.now().strftime('%H:%M:%S - %d/%m/%Y')
    with open(log_txt, 'a', encoding='utf-8') as log_file:
        log_file.write(f'{data_hora_atual} - {msg}\n')


def read_logs() -> list:
    with open(log_txt, 'r', encoding='utf-8') as log_file:
        logs = []
        for log in log_file:
            hora, data, mensagem = log.split('-')
            logs.append({'hora': hora, 'data': data, 'mensagem': mensagem})
    return logs
