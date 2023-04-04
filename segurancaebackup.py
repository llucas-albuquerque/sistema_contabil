# segurancaebackup
import os
import shutil
from cryptography.fernet import Fernet


class Security:
    def __init__(self):
        self.key = None
        self.file_ext = '.encrypted'
        self.encryptor = None
        self.decryptor = None

    def generate_key(self):
        self.key = Fernet.generate_key()
        self.encryptor = Fernet(self.key)
        self.decryptor = Fernet(self.key)
        with open('key.key', 'wb') as key_file:
            key_file.write(self.key)

    def load_key(self):
        if not os.path.exists('key.key'):
            self.generate_key()
        with open('key.key', 'rb') as key_file:
            self.key = key_file.read()
            self.encryptor = Fernet(self.key)
            self.decryptor = Fernet(self.key)

    def encrypt_file(self, filename):
        with open(filename, 'rb') as file:
            file_data = file.read()
            encrypted_data = self.encryptor.encrypt(file_data)
        with open(filename + self.file_ext, 'wb') as encrypted_file:
            encrypted_file.write(encrypted_data)
        os.remove(filename)

    def decrypt_file(self, filename):
        with open(filename + self.file_ext, 'rb') as encrypted_file:
            encrypted_data = encrypted_file.read()
            decrypted_data = self.decryptor.decrypt(encrypted_data)
        with open(filename, 'wb') as file:
            file.write(decrypted_data)
        os.remove(filename + self.file_ext)

    def backup_files(self, folder):
        backup_folder = folder + '_backup'
        if not os.path.exists(backup_folder):
            os.makedirs(backup_folder)
        for filename in os.listdir(folder):
            self.encrypt_file(os.path.join(folder, filename))
            shutil.move(os.path.join(folder, filename) + self.file_ext,
                        os.path.join(backup_folder, filename) + self.file_ext)

    def restore_files(self, backup_folder):
        for filename in os.listdir(backup_folder):
            self.decrypt_file(os.path.join(backup_folder, filename))
            shutil.move(os.path.join(backup_folder, filename),
                        os.path.join(os.path.dirname(backup_folder), filename))

# Neste exemplo, o sistema de segurança utiliza a biblioteca cryptography para criar uma chave de criptografia para proteger os dados do escritório. O método generate_key é responsável por gerar uma nova chave de criptografia e salvá-la em um arquivo key.key. O método load_key verifica se a chave já foi gerada e carrega a chave existente a partir do arquivo key.key.
# O método encrypt_file utiliza a chave de criptografia para criptografar um arquivo e o salva com uma extensão .encrypted. O método decrypt_file utiliza a chave de criptografia para descriptografar um arquivo criptografado e o salva com o nome original do arquivo.
# O método backup_files faz backup de todos os arquivos em uma pasta específica, criptografando cada arquivo e movendo-o para uma pasta de backup. O método restore_files restaura todos os arquivos na pasta original, descriptografando cada arquivo e movendo-o de volta para a pasta original.
# Além da criptografia de dados, outras medidas de segurança devem ser implementadas, como a utilização de senhas fortes e complexas para o acesso ao sistema, autenticação em dois fatores, restrição de acesso a dados sensíveis apenas para usuários autorizados, entre outras.
# Também é importante implementar um sistema de backup que permita a recuperação dos dados em caso de perda ou corrupção de informações. O sistema deve realizar backups regulares em locais seguros e confiáveis, de preferência fora do local de trabalho, como em nuvens ou dispositivos externos. É importante realizar testes periódicos de recuperação de dados para garantir que o backup esteja funcionando corretamente.
# Outra medida importante é manter o sistema atualizado com as últimas atualizações de segurança e correções de bugs. Isso ajuda a evitar vulnerabilidades que possam ser exploradas por hackers.
# Por fim, é necessário que a empresa siga as normas da Lei Geral de Proteção de Dados (LGPD), que estabelece diretrizes para a proteção de dados pessoais. É importante que o sistema contábil em Python esteja em conformidade com a LGPD, garantindo a privacidade e proteção das informações dos clientes e do escritório contábil.
