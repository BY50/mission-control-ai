import os
from ollama import Client
from dotenv import load_dotenv
load_dotenv()
# Identificação da trilha — ALTEREM conforme a escolha do grupo
TRILHA = "envirosat" # "agrosat" | "envirosat" | "connectsat" | "mobilitysat"
# Configuração Ollama Cloud (mesma do Checkpoint 02 e 03)
client = Client(
  host="https: /ollama.com",
  headers={'Authorization': 'Bearer ' + os.environ.get('OLLAMA_API_KEY')}
)
api = os.environ.get('OLLAMA_API_KEY')
print("API KEY carregada: ", "OK" if api else "FALTANDO")
def llm(prompt, system=None, max_tokens=800, temperature=0.3):
  """Envia prompt ao gpt-oss:120b via Ollama Cloud."""
  messages = []
  if system:
    messages.append({"role": "system", "content": system})
    messages.append({"role": "user", "content": prompt})
  try:
    return client.chat(
      model="gpt-oss:120b", messages=messages,
      options={"num_predict": max_tokens, "temperature": temperature},
      stream=False
    )['message']['content'].strip()
  except Exception as e:
    return f"⚠️ Erro ao consultar IA: {e}"
def load_system_prompt():
  """Lê o system prompt do arquivo prompts/system_prompt.md"""
  path = Path("prompts/system_prompt.md")
  if path.exists():
    return path.read_text(encoding="utf-8")
  return "Você é um assistente." # fallback genérico
class MissionEngine:
  """Motor de análise — vocês completam os métodos abaixo."""
  def _init _(self):
    self.trilha = TRILHA
    self.system_prompt = load_system_prompt()
  def is_ready(self):
    # Troquem para True quando analyze() estiver implementado
    return False
  def status_snapshot(self):
    """Retorna texto resumindo o estado atual da telemetria."""
    # TODO: chamar telemetria.coletar() e formatar legivelmente
    d = telemetria.coletar()
    status = f"A temperatura monitorada é {d[0]}°C, A quantidade de hectares destruidos é {d[1]} hectares 
        e a energia restante é {d[2]}%."
    return status
  def analyze(self, pergunta_usuario):
    """Analisa a pergunta com base na telemetria + alertas + IA."""
    # TODO (foco do trabalho):
    # 1. Coletar dados via src.telemetria.coletar()
    # 2. Avaliar alertas via src.alertas.avaliar(dados)
    # 3. Montar prompt com dados + alertas + pergunta
    # 4. Chamar llm(prompt, system=self.system_prompt)
    # 5. Retornar a resposta
    return (
      "🛠️ Implementação pendente.\n\n"
      "Olá! A interface CLI está funcionando, mas a lógica\n"
      "de análise ainda não foi conectada. O grupo precisa:\n\n"    
      " 1. Completar src/telemetria.py\n"
      " 2. Completar src/alertas.py\n"
      " 3. Escrever o system prompt em prompts/system_prompt.md\n"
      " 4. Sobrescrever analyze() em src/engine.py"
    )
