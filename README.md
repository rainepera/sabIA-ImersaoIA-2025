# sabIA-ImersaoIA-2025
🧠 sabIA: App educacional com Google Gemini para simplificar textos complexos, gerar exercícios e dar feedback. Foco em alfabetização e compreensão leitora. Projeto da Imersão IA 2025 Alura + Google.

# 🧠 sabIA — Alfabetização com Inteligência e Simplicidade

![Mascote SabIA](https://raw.githubusercontent.com/rainepera2025/main/assets/mascote_sabia.png)
*(Substitua "SEU_USUARIO_GITHUB" pelo seu nome de usuário no GitHub e crie a pasta 'assets' para colocar a imagem do seu mascote Sabiá aqui!)*

---

## 🎯 Resumo do Projeto

O **sabIA** é um aplicativo educacional inovador, com foco em pais, educadores e professores do ensino fundamental. Ele foi criado para auxiliar crianças e adolescentes que enfrentam desafios como o analfabetismo funcional ou dificuldades de compreensão leitora. Minha missão é transformar textos complexos em conteúdos simples, claros e didáticos, promovendo inclusão, entendimento e aprendizado real.

---

## 🌱 Propósito: Combatendo o Analfabetismo Funcional na Era Digital

Em um cenário de avanço tecnológico sem precedentes, é paradoxal e preocupante observar as altas taxas de analfabetismo funcional entre crianças e adolescentes no Brasil. A educação, em vez de acompanhar a evolução digital, tem enfrentado desafios crescentes, resultando em barreiras significativas para o pleno desenvolvimento e inclusão social. O **sabIA** nasce deste cenário: meu propósito é utilizar a Inteligência Artificial para suprir essa lacuna, oferecendo uma ferramenta acessível que realmente ajude a **descomplicar o conhecimento** e a **fortalecer a base educacional**, garantindo que a tecnologia seja uma aliada na construção de um futuro mais letrado e consciente para todos.

---

## 💡 Próximos Passos e Visão Futura

Este projeto representa a **estrutura fundamental e a formulação da ideia** do **sabIA** como um aplicativo educacional. Meu objetivo é, com mais tempo e dedicação, transformar esta base em um **aplicativo de verdade** (com uma interface gráfica ou web) para colocar o **sabIA** em prática e alcançar ainda mais educadores e crianças. Esta é apenas a semente de um grande projeto!

---

## 🐦 O Nome e o Mascote

O nome **sabIA** é uma fusão criativa entre:
* **"sabiá"**: O pássaro símbolo da nossa fauna e da liberdade do conhecimento.
* **"sabedoria"**: Que remete ao aprendizado e à iluminação.
* **"IA" (Inteligência Artificial)**: A tecnologia que impulsiona a solução.

O mascote do aplicativo é um passarinho sabiá voando, com asas em formato de livro, representando o voo da leitura e do conhecimento acessível.

---

## ✨ Funcionalidade Principal

O **sabIA** possui uma interface de Linha de Comando (CLI) simples e intuitiva, com funcionalidades centrais movidas pela Inteligência Artificial do Google Gemini:

* **Simplificação de Textos:** O usuário insere um trecho de texto complexo (de livros, provas, notícias etc.), e o sabIA o reescreve com linguagem adaptada ao nível de compreensão do aluno.
* **Geração de Perguntas Didáticas:** Para reforçar a compreensão do texto simplificado e promover a reflexão, o sabIA gera perguntas contextualizadas.
* **Respostas e Feedback:** O sabIA pode responder a perguntas e oferecer feedback amigável e construtivo sobre as respostas dos alunos, agindo como um professor gentil.
* **Criação de Exercícios:** Gera pequenos exercícios sobre tópicos específicos para fixação do aprendizado.

---

## 🤖 O Papel da Inteligência Artificial (Google Gemini)

O coração do **sabIA** é a IA do Google Gemini, que atua como o próprio agente educativo, capaz de:
* Compreender o texto original.
* Reescrever com clareza e linguagem acessível.
* Sugerir perguntas e exercícios contextualizados para reforço de leitura.
* Fornecer feedback pedagógico de forma natural e amigável.

---

## 🌟 Diferenciais do sabIA

* **Inclusivo:** Desenvolvido pensando na realidade de alunos com dificuldades reais de leitura.
* **Visual Amigável:** (Embora seja uma CLI, o conceito visual é lúdico e inspirador, como o mascote Sabiá).
* **IA de Ponta:** Uso ético e educativo da inteligência artificial.
* **Impacto Social:** Foco principal em transformar vidas através da alfabetização, não apenas em tecnologia.

---

## 🚀 Como Executar o Projeto (Localmente)

Para rodar o sabIA em seu ambiente local, siga os passos:

1.  **Clone o Repositório:**
    ```bash
    git clone [https://github.com/SEU_USUARIO_GITHUB/sabIA-ImersaoIA-2025.git](https://github.com/SEU_USUARIO_GITHUB/sabIA-ImersaoIA-2025.git)
    cd sabIA-ImersaoIA-2025
    ```
    *(Não se esqueça de substituir "SEU_USUARIO_GITHUB" pelo seu nome de usuário no GitHub!)*

2.  **Crie e Ative um Ambiente Virtual (Recomendado):**
    ```bash
    python -m venv venv
    # No Windows:
    .\venv\Scripts\activate
    # No macOS/Linux:
    source venv/bin/activate
    ```

3.  **Instale as Dependências:**
    ```bash
    pip install -r requirements.txt
    ```
    *(Ainda vamos criar o arquivo `requirements.txt` no próximo passo!)*

4.  **Configure sua Chave API:**
    * Obtenha sua Google API Key no [Google AI Studio](https://aistudio.google.com/app/apikey).
    * Crie um arquivo chamado **`.env`** na raiz do projeto (na mesma pasta do `app.py`).
    * Dentro do arquivo `.env`, adicione a sua chave no seguinte formato:
        ```
        GOOGLE_API_KEY=SUA_CHAVE_API_AQUI
        ```
        **Importante:** Este arquivo `.env` está no `.gitignore` e não será enviado para o GitHub por segurança.

5.  **Execute o SabIA:**
    ```bash
    python app.py
    ```
    O aplicativo iniciará no seu terminal, exibindo um menu interativo.

---

## 🔗 Notebook Google Colab (Prova de Conceito)

Para ver uma demonstração funcional deste projeto e protótipos de desenvolvimento, acesse o notebook original no Google Colab:

[Link para o seu Notebook Google Colab](https://colab.research.google.com/drive/1wNgwVeSGDQQgj20Bt7UuJB_3ntsqSWKE?usp=sharing)

---

## 📝 Licença

Este projeto está licenciado sob a Licença MIT. Veja o arquivo `LICENSE` para mais detalhes.

---

## ✨ Imersão IA 2025 Alura + Google

Este projeto foi desenvolvido como parte da Imersão IA 2025, uma iniciativa da Alura em parceria com o Google para explorar o potencial da Inteligência Artificial generativa.

---
