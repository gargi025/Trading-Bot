import typer

from rich.console import Console
from rich.panel import Panel
from rich.prompt import Prompt, FloatPrompt, Confirm
from rich.progress import Progress, SpinnerColumn, TextColumn
from rich.table import Table

from bot.constants import Side, OrderType
from bot.models import OrderRequest
from bot.orders import OrderService

app = typer.Typer()

console = Console()


def show_banner():
    console.print(
        Panel.fit(
            "[bold cyan]Binance Futures Trading Bot[/bold cyan]\n"
            "[green]USDT-M Futures Testnet[/green]",
            title="Trading Bot",
            border_style="cyan",
        )
    )


@app.callback(invoke_without_command=True)
def main():
    """
    Binance Futures Trading Bot
    """

    show_banner()

    symbol = Prompt.ask(
        "[cyan]Enter Symbol[/cyan]",
        default="BTCUSDT",
    ).upper()

    side = Prompt.ask(
        "[cyan]Side[/cyan]",
        choices=["BUY", "SELL"],
        default="BUY",
    )

    order_type = Prompt.ask(
        "[cyan]Order Type[/cyan]",
        choices=["MARKET", "LIMIT", "STOP"],
        default="MARKET",
    )

    quantity = FloatPrompt.ask("[cyan]Quantity[/cyan]")

    price = None
    if order_type in ["LIMIT", "STOP"]:
        price = FloatPrompt.ask("[cyan]Limit Price[/cyan]")

    stop_price = None
    if order_type == "STOP":
        stop_price = FloatPrompt.ask("[cyan]Stop Price[/cyan]")

    try:
        order = OrderRequest(
            symbol=symbol,
            side=Side(side),
            order_type=OrderType(order_type),
            quantity=quantity,
            price=price,
            stop_price=stop_price,
        )

    except Exception as e:
        console.print(f"[bold red]Validation Error:[/bold red] {e}")
        raise typer.Exit()

    summary = Table(title="📋 Order Request Summary")

    summary.add_column("Field", style="cyan")
    summary.add_column("Value", style="green")

    summary.add_row("Symbol", order.symbol)
    summary.add_row("Side", order.side.value)
    summary.add_row("Order Type", order.order_type.value)
    summary.add_row("Quantity", str(order.quantity))

    if order.price is not None:
        summary.add_row("Price", str(order.price))

    if order.stop_price is not None:
        summary.add_row("Stop Price", str(order.stop_price))

    console.print()
    console.print(summary)
    console.print()

    if not Confirm.ask("[yellow]Submit this order?[/yellow]"):
        console.print("[bold red]Order cancelled.[/bold red]")
        raise typer.Exit()

    service = OrderService()

    with Progress(
        SpinnerColumn(), TextColumn("[progress.description]{task.description}")
    ) as progress:

        progress.add_task(
            description="Submitting order...",
            total=None,
        )

        response = service.place_order(order)

    console.print()

    table = Table(title="📄 Order Response")

    table.add_column("Field", style="cyan")
    table.add_column("Value", style="green")

    if "code" in response:
        table.add_row("Error Code", str(response["code"]))
        table.add_row("Message", response["msg"])
    else:
        table.add_row("Order ID", str(response.get("orderId", "-")))
        table.add_row("Status", response.get("status", "-"))
        table.add_row("Executed Qty", str(response.get("executedQty", "-")))
        table.add_row("Average Price", str(response.get("avgPrice", "-")))

    console.print(table)
    console.print()

    if "code" in response:
        console.print(f"[bold red]❌ Order Failed[/bold red]\n{response['msg']}")
    else:
        console.print("[bold green]✅ Order placed successfully![/bold green]")


if __name__ == "__main__":
    app()
