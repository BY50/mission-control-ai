# 🚀 Mission Control AI — Monitoramento de florestas
# Integrantes
- Bruno Yudi Moritaka Kanashiro — RM: 571776 — Turma: 1CCPG
# O que o projeto faz
Esse projeto gera dados sobre potenciais ameaças a florestas e a energia do satélite e então os analisa para ambos os dados e a análise serem a base das respostas de uma IA. 
# Persona atendida
A persona usada é de um operador de satélite pois a IA responde com base nos dados de um satélite.
# Tecnologias utilizadas
- Python 3.10+
- Ollama Cloud API (modelo gpt-oss:120b)
- Bibliotecas: ollama, python-dotenv, prompt-toolkit, pyfiglet, rich
# Como executar
☐ README.md completo na raiz (estrutura detalhada na seção 9.2)
☐ Código Python funcional rodável após pip install -r requirements.txt
☐ requirements.txt com versões fixadas
☐ .env.example mostrando quais variáveis são necessárias (sem a chave real)
☐ .gitignore configurado para ignorar .env e _pycache _
☐ Pasta assets/ com no mínimo 2 prints reais do sistema funcionando
☐ Repositório público — sem isso, a entrega é considerada não realizada
1. Clone o repositório
2. Crie ambiente virtual: `python -m venv .venv & source .venv/bin/activate`
3. Instale dependências: `pip install -r requirements.txt`
4. Crie arquivo `.env` na raiz com:
`OLLAMA_API_KEY=sua_chave_aqui`
5. Execute: `python main.py
# System Prompt
Você é um operador de satélite que monitora a condição de florestas. Responda perguntas sobre o status das florestas baseado nos dados e alertas do seu satélite. Tom: profissional e amigável.
# Cenários de teste demonstrados
1. Operação normal — todos os parâmetros dentro do range.
2. Temperatura crítica — alerta que muda a resposta da IA.
3. Desmatamento excessivo — alerta que muda a resposta da IA.
# Limitações conhecidas
Eu não tive tempo para testar o código.
