from pathlib import Path
from rich.console import Console
from rich.panel import Panel
from rich.prompt import Prompt
from rich.text import Text
from rich.align import Align
from rich import box
import os

from Build.batch_processor import BatchProcessor


class RetroTerminalApp:
    def __init__(self):
        self.console = Console()
        self.processor = BatchProcessor()
        self.current_path = Path.home()

    def show_banner(self):
        title = Text("RetroTv Converter", style="bold cyan")
        subtitle = Text("⚡ Futuristic Video Tool ⚡", style="magenta")

        panel = Panel(
            Align.center(title + "\n" + subtitle),
            border_style="bright_blue",
            box=box.DOUBLE,
            padding=(1, 4),
        )

        self.console.print(panel)

    def show_path(self):
        self.console.print(
            f"[bold green]Current Directory:[/bold green] [yellow]{self.current_path}[/yellow]\n"
        )

    def navigate(self):
        while True:
            self.show_path()

            self.console.print("[cyan]Commands:[/cyan]")
            self.console.print("  [bold]cd <folder>[/bold] → enter folder")
            self.console.print("  [bold]back[/bold] → go up one directory")
            self.console.print("  [bold]list[/bold] → show files")
            self.console.print("  [bold]convert[/bold] → start conversion")
            self.console.print("  [bold]exit[/bold] → quit\n")

            cmd = Prompt.ask("[bold blue]>>>[/bold blue]").strip()

            if cmd.startswith("cd "):
                folder = cmd[3:].strip()
                new_path = self.current_path / folder

                if new_path.exists() and new_path.is_dir():
                    self.current_path = new_path
                else:
                    self.console.print("[red]Folder not found![/red]")

            elif cmd == "back":
                self.current_path = self.current_path.parent

            elif cmd == "list":
                files = os.listdir(self.current_path)
                for f in files:
                    self.console.print(f"[white]- {f}[/white]")

            elif cmd == "convert":
                self.console.print("\n[bold magenta]Starting conversion...[/bold magenta]\n")
                self.processor.batch_convert(str(self.current_path))

            elif cmd == "exit":
                self.console.print("[bold red]Exiting... Goodbye![/bold red]")
                break

            else:
                self.console.print("[red]Unknown command[/red]")

    def run(self):
        self.console.clear()
        self.show_banner()
        self.navigate()


if __name__ == "__main__":
    app = RetroTerminalApp()
    app.run()