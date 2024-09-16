# Import for the AI APIs
import os
from openai import OpenAI
from dotenv import load_dotenv
from call_ai import call_openai
# Import for the text UI
from rich.console import Console
from rich.panel import Panel
from rich.markdown import Markdown
# Import utility functions
from utils import handle_user_input, delete_last_lines

# Create clients for AI providers
load_dotenv()
openai_client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# Initialize the UI console
console = Console()


def main():
    delete_last_lines()
    # Welcome message
    console.print(Panel(Markdown(
        '# Welcome to Pretty Bot\n- Type your message, then press Enter to chat.\n- Type ```/exit```, then press Enter to close the app.'), border_style="cyan"))
    print()

    # Initialize the chat history
    chat_history = list()

    # The app loop
    while True:
        # Get user's input
        user_input = console.input("[bold yellow]You: [/bold yellow]")
        # Check to see if they want to exit
        handle_user_input(user_input)
        # Save the user's input to the chat history
        chat_history.append({"role": "user", "content": user_input})
        # Replace the ask-for-input line with a panel
        delete_last_lines()
        console.print(Panel(
            Markdown(user_input, code_theme="github-dark"),
            title="[bold yellow]You[/bold yellow]",
            title_align="left",
            border_style="yellow"
        ))
        print()

        # Get AI's response
        console.print(Panel(
            "[italic]Thinking...[italic]",
            title="[bold green]AI[/bold green]",
            title_align="left",
            border_style="green"
        ))
        # Call the OpenAI API
        ai_response = call_openai(
            openai_client=openai_client,
            chat_history=chat_history,
            model="gpt-4o-mini",
            temperature=1,
            max_completion_tokens=1024
        )
        # Display the AI's response to the terminal
        delete_last_lines(3)
        console.print(Panel(
            Markdown(ai_response, code_theme="github-dark"),
            title="[bold green]AI[/bold green]",
            title_align="left",
            border_style="green"
        ))
        print()

        # Save the AI's response to the chat history
        chat_history.append({"role": "assistant", "content": ai_response})


if __name__ == "__main__":
    main()
