import google.generativeai as genai
from google.colab import userdata

# Configura a API Key do Google Gemini usando o segredo do Colab
api_key = userdata.get('GOOGLE_API_KEY')
genai.configure(api_key=api_key)

# Inicializa o modelo Gemini
model = genai.GenerativeModel('gemini-2.0-flash')

# --- FUNÇÕES DO SABIA (MANTIDAS) ---
def simplificar_texto(texto_complexo):
  prompt_simplificacao = f"""
  Por favor, simplifique o seguinte texto para que uma criança de 7 anos possa entendê-lo facilmente.
  Use linguagem simples, frases curtas e evite jargões técnicos.

  Texto a simplificar:
  {texto_complexo}

  Texto simplificado:
  """
  try:
    response = model.generate_content(prompt_simplificacao)
    return response.text
  except Exception as e:
    return f"O SabIA encontrou um problema ao simplificar: {e}"

def responder_pergunta(pergunta):
  prompt_pergunta = f"""
  Responda à seguinte pergunta de forma simples, clara e educativa para uma criança.
  Seja amigável e use exemplos se for útil.

  Pergunta: {pergunta}

  Resposta:
  """
  try:
    response = model.generate_content(prompt_pergunta)
    return response.text
  except Exception as e:
    return f"O SabIA encontrou um problema ao responder: {e}"

def gerar_exercicio(topico):
  prompt_exercicio = f"""
  Crie um pequeno e divertido exercício ou uma pergunta simples para uma criança de 7 anos sobre o seguinte tópico: {topico}.
  O objetivo é testar se ela entendeu o que aprendeu. Faça a pergunta de forma direta e clara.

  Exemplo de exercício:
  """
  try:
    response = model.generate_content(prompt_exercicio)
    return response.text
  except Exception as e:
    return f"O SabIA encontrou um problema ao gerar o exercício: {e}"

def dar_feedback(topico, resposta_aluno):
  prompt_feedback = f"""
  Um aluno respondeu sobre o tópico "{topico}".
  A resposta do aluno foi: "{resposta_aluno}"

  Por favor, avalie a resposta do aluno de forma amigável e encorajadora, como se fosse um professor gentil.
  Se a resposta estiver correta, elogie e talvez adicione algo interessante.
  Se estiver incompleta ou errada, ajude o aluno a pensar na resposta certa, dando dicas ou explicando de forma simples, sem dizer que está "errado".
  Fale para uma criança de 7 anos.

  Feedback do professor SabIA:
  """
  try:
    response = model.generate_content(prompt_feedback)
    return response.text
  except Exception as e:
    return f"O SabIA encontrou um problema ao dar feedback: {e}"

# --- MODO INTERATIVO DO SABIA ---
def iniciar_sabia_interativo():
  print("Olá! Eu sou o SabIA, seu amigo para aprender!")
  print("O que você gostaria de fazer hoje?")

  while True:
    print("\n--- Menu do SabIA ---")
    print("1. Simplificar um texto")
    print("2. Fazer uma pergunta")
    print("3. Gerar um exercício")
    print("4. Avaliar uma resposta (dar feedback)")
    print("5. Sair")
    print("---------------------")

    opcao = input("Escolha uma opção (1-5): ")

    if opcao == '1':
      texto = input("Qual texto você quer que eu simplifique? ")
      print("\nProcessando...")
      print(f"\n--- Texto Simplificado pelo SabIA ---")
      print(simplificar_texto(texto))
    elif opcao == '2':
      pergunta = input("Qual é a sua pergunta para o SabIA? ")
      print("\nProcessando...")
      print(f"\n--- Resposta do SabIA ---")
      print(responder_pergunta(pergunta))
    elif opcao == '3':
      topico = input("Sobre qual tópico você quer um exercício? ")
      print("\nProcessando...")
      print(f"\n--- Exercício do SabIA sobre {topico.capitalize()} ---")
      print(gerar_exercicio(topico))
    elif opcao == '4':
      topico_feedback = input("Sobre qual tópico é a resposta? ")
      resposta_aluno = input("Qual foi a resposta do aluno? ")
      print("\nProcessando...")
      print(f"\n--- Feedback do SabIA ---")
      print(dar_feedback(topico_feedback, resposta_aluno))
    elif opcao == '5':
      print("Até a próxima! O SabIA te espera para mais aprendizado!")
      break # Sai do loop
    else:
      print("Opção inválida. Por favor, escolha um número de 1 a 5.")

# --- INICIAR O SABIA INTERATIVO ---
iniciar_sabia_interativo()
