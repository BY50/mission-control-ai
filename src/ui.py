"""Interface CLI estilo Claude Code — usa Rich + prompt-toolkit."""
from rich.console import Console
from rich.panel import Panel
from rich.text import Text
from prompt_toolkit import PromptSession
from prompt_toolkit.styles import Style
import pyfiglet
from datetime import datetime
console = Console()
session = PromptSession(style=Style.from_dict({"prompt": "#06B6D4 bold"}))
def show_banner():
  """Exibe banner ASCII colorido no início."""
  banner = pyfiglet.figlet_format("Mission Control", font="ansi_shadow")
  console.print(Text(banner, style="bold #06B6D4"))
  console.print(Panel.fit(
    "Sistema de monitoramento e análise por IA generativa.\n"
    "Use /help para ver os comandos · /exit para sair.\n"
    "Modelo: gpt-oss:120b via Ollama Cloud",
    title="◆ MISSION CONTROL", border_style="#06B6D4"
  ))

