import os
from pathlib import Path, PosixPath
from codemagic.tools import AppStoreConnect
from codemagic.tools import Keychain
from codemagic.tools.xcode_project import XcodeProject

# keychain_path = './keychains'
# keychain_password = '123456'
# certificate_password = '123456'

with open('AuthKey.p8', 'rb') as key_file:
    private_key = key_file.read()

keychain = Keychain(Path("/tmp/new.keychain"))

keychain.delete()
keychain.initialize()

# keychain.create(password=keychain_password)

PosixPath('/tmp/new.keychain')

keychain.make_default()

Keychain().get_default()

PosixPath('/private/tmp/new.keychain')


# keychain.unlock(password=keychain_password)

# print(Keychain().get_default())
# # keychain.add_certificates(certificate_password=certificate_password)

app_store_connect = AppStoreConnect(
    key_identifier=os.environ['KEY_ID'],
    issuer_id=os.environ['ISSUER_ID'],
    private_key=private_key,
    log_requests=True,
    unauthorized_request_retries=3,
    server_error_retries=3,
    json_output=True,
)

# project = XcodeProject(
#     verbose=True
# )

# project.use_profiles()

# for certificate in app_store_connect.list_profiles():
#     print(certificate.dict())
# # print(app_store_connect.list_certificates())

# Carregar o projeto Xcode
project = XcodeProject(
    verbose=True
)

# Listar os targets do projeto
# print("Targets do projeto:", targets)

# Definir a versão de marketing e o número de build
# project.set_build_setting('MARKETING_VERSION', '1.0.0')
# project.set_build_setting('CURRENT_PROJECT_VERSION', '42')

project.use_profiles()
# project.build_ipa(
#     xcode_workspace_path=Path('./apps/todo_list/ios/Runner.xcworkspace').expanduser(),
#     configuration_name='Release',# Defina a configuração (Release/Debug)
#     export_options_plist=Path('./apps/todo_list/ios/ExportOptions.plist').expanduser(),
#     ipa_directory='build/Runner.ipa',  # Caminho de saída para o IPA gerado
#     scheme_name='Runner'
# )

# Salvar as alterações no projeto
# project.save()
