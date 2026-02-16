from time import monotonic

from textual.app import App, ComposeResult
from textual.widgets import Footer,Header,Button,Digits
from textual.containers import HorizontalGroup,VerticalScroll
from textual.reactive import reactive

class TimeDisplay(Digits):
    start_time=reactive(monotonic)
    time=reactive(0.0)

    def on_mount(self)-> None:
        self.set_interval(1/60,self.update_time)
    
    def update_time(self) ->None:
        self.time = monotonic() - self.start_time

class Stopwatch(HorizontalGroup):
    def compose(self) -> ComposeResult:
        yield Button("Start",id="start",variant="success")
        yield Button("Stop", id="stop",variant="error")
        yield Button("Reset",id="reset")
        yield TimeDisplay("00:00:00.00")


class StopwatchApp(App):
    BINDINGS = [("d","toggle_dark","Toggle dark mode")]

    def compose(self) -> ComposeResult:
        yield Header()
        yield Footer()
        yield VerticalScroll(Stopwatch())

    def action_toggle_dark(self):
        self.theme = (
            "textual-dark" if self.theme=="textual-light" else "textual-light"
        )

if __name__ == "__main__":
    app = StopwatchApp()
    app.run