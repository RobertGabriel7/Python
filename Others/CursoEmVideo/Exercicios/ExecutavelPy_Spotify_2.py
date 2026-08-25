import os.path

from telethon.sync import TelegramClient

# Substitua essas variáveis com suas próprias credenciais
api_id = '22307423'
api_hash = '88da25447ed3c8fe085d124d436b2184'
phone_number = '55+11981155590'

# Crie um cliente Telegram
client = TelegramClient('session_name', 22307423, "88da25447ed3c8fe085d124d436b2184")


async def download_files_from_channel():
    await client.start(55+11981155590)

    # Substitua 'nome_do_canal' pelo nome de usuário do canal que você deseja baixar arquivos

    channel = await client.get_entity('https://t.me/+IKLRRiWaALRiN2M0')

    async for message in client.iter_messages(channel):
        if message.media:
            # Baixe o arquivo da mensagem
                await client.download_media(message, file=os.path.join('media', 'https://t.me/+IKLRRiWaALRiN2M0'))

    await client.disconnect()


# Execute a função para baixar os arquivos do canal
with client:
    client.loop.run_until_complete(download_files_from_channel())