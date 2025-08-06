from aula226_229_log import LogFileMixin

class Eletronico:
    def __init__(self, nome):
        self._nome = nome
        self._ligado = False

    def ligar(self):
        if not self._ligado:
            self._ligado = True

    def desligar(self):
        if self._ligado:
            self._ligado = False

class Smartphone(Eletronico, LogFileMixin):
    def ligar(self):
        super().ligar()

        if self._ligado:
            self.log_success(f'{self._nome} ligado com sucesso.')

    def desligar(self):
        super().desligar()

        if not self._ligado:
            self.log_error(f'{self._nome} desligado com sucesso.')