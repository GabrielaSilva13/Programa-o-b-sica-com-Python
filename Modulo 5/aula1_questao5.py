import emoji

# Dicionário de emojis e seus códigos
emojis_disponiveis = {
    "❤️": ":red_heart:",
    "👍": ":thumbs_up:",
    "🤔": ":thinking_face:",
    "🥳": ":partying_face:"
}

# Exibe a lista de emojis disponíveis
print("Emojis disponíveis:")
for emoji_char, emoji_code in emojis_disponiveis.items():
    print(f"{emoji_char} - {emoji_code}")

# Solicita a frase ao usuário
frase = input("\nDigite uma frase e ela será emojizada: ")

# Emojiza a frase
frase_emojizada = emoji.emojize(frase, use_aliases=True)

# Exibe a frase emojizada
print("\nFrase emojizada:")
print(frase_emojizada)