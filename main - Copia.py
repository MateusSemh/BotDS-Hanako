import discord
from discord.ext import commands
import random

id_do_servidor = 1234

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)


@bot.event
async def on_ready():
    print(f'Bot conectado como {bot.user.name}')


@bot.event
async def on_message(message):
    if message.author == bot.user:
        return  # Ignora as mensagens enviadas pelo próprio bot

    mensagens_boa_noite = [
        'Boa noite {user}, tudo bem com você hoje?',
        'Boa noite {user}, e aí, como está a vida?',
        'Boa noite {user} meu lindo(a), tudo bem contigo?',
        'Boa noite, {user}! Durma bem e sonhe com o adm!',
        'Boa noite {user}, aproveita pra me ligar aqui rapidinho, bot tambem ama',
        'Boa noite, {user}! Você é o meu jogo favorito. Não tem como jogar outro quando o seu coração é o meu console.',
        'Boa noite, {user}! Vamos jogar uma partida de conquista? Eu te dou meu coração como prêmio se você vencer o meu amor.',
        'Boa noite, {user}! Se você fosse um sonho, eu passaria a vida inteira dormindo só pra te encontrar todas as noites 💭.',
        'Boa noite {user}, sabia que da pra convidar o bot pra jantar tbm? fica dica rsrsrs',
        'Boa noite, {user}! Seu sorriso é o meu emoji favorito. 😘💕',
        'Boa noite, {user}! Sou especialista em causar insônia... porque fico pensando em você a noite toda. 😜💤'
    ]

    mensagens_bom_dia = [
        'Bom dia {user}, cuidado pra nao jogar gacha hoje em... Vai perde no 50/50 kkkk',
        'Bom dia {user}, hoje o dia ta bom pra você jogar na mega e vai ganhar e dividir metade com o chat em !',
        'Bom dia {user}}, nada de bom dia hoje pra voce kkkkk',
        'Bom dia, {user}! Agora vá trabaia.',
        'Bom dia {user}! Sabe aquela sensação de acordar e se sentir uma celebridade? Pois é, nem eu',
        'Bom dia {user}, cafe da manha ta pronto abre o jogo e vem tomar um cafe comigo rsrs',
        'Bom dia, {user}! Acredite nas suas capacidades e saiba que você é capaz de alcançar grandes coisas.',
        '{user}, Bom dia! Hoje acordei mais desanimado do que futebol sem gol. ',
        'Ô, {user}, bom dia, mermão! Cola aqui pra gente trocar uma ideia e começar o dia com aquele sorriso maroto no rosto.',
        '{user}, acorde com a certeza de que coisas maravilhosas estão por vir, euzinha. Tenha um bom dia!',
        'Bom dia, {user}! Hoje o adm tá mais fácil do que ganhar na loteria, aproveita',
        'Ô, {user}! Bom dia, meu consagrado! Vamos acordar que dormir não da XP'
    ]

    if 'boa noite' in message.content.lower():
        response = random.choice(mensagens_boa_noite).format(
            user=message.author.mention)
        await message.channel.send(response)

    elif 'bom dia' in message.content.lower():
        response = random.choice(mensagens_bom_dia).format(
            user=message.author.mention)
        await message.channel.send(response)

    await bot.process_commands(message)


bot.run(
    'token do bot')
