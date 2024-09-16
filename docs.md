# Pretty Bot Code Walkthrough

This document provides a detailed explanation of the Pretty Bot application's code structure and functionality.

## Table of Contents

1. [Project Structure](#project-structure)
2. [Main Application (main.py)](#main-application-mainpy)
3. [AI API Call (call_ai.py)](#ai-api-call-call_aipy)
4. [Utility Functions (utils.py)](#utility-functions-utilspy)
5. [Dependencies (requirements.txt)](#dependencies-requirementstxt)

## Project Structure

The Pretty Bot application consists of four main files:

- `main.py`: The core application logic
- `call_ai.py`: Handles API calls to OpenAI
- `utils.py`: Contains utility functions
- `requirements.txt`: Lists the project dependencies

## Main Application (main.py)

The `main.py` file is the heart of the Pretty Bot application. Let's break it down:

### Imports

```python
import os
from openai import OpenAI
from dotenv import load_dotenv
from call_ai import call_openai
from rich.console import Console
from rich.panel import Panel
from rich.markdown import Markdown
from utils import handle_user_input, delete_last_lines
```

These imports bring in necessary modules for API interaction, environment variable management, UI rendering, and utility functions.

### Initialization

```python
load_dotenv()
openai_client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
console = Console()
```

This section loads environment variables, initializes the OpenAI client, and creates a Rich console for enhanced terminal output.

### Main Function

Let's break down the `main()` function step by step:

```python
def main():
    # Welcome message
    console.print(Panel(Markdown(
        '# Welcome to Pretty Bot\n- Type your message, then hit enter to chat.\n- Type ```/exit```, then hit enter to close the app.'), border_style="cyan"))
    print()
```

The function starts by displaying a welcome message using Rich's `Panel` and `Markdown` classes. This creates a visually appealing introduction with a cyan border.

```python
    # Initialize the chat history
    chat_history = list()
```

An empty list is created to store the chat history. This will be used to maintain context for the AI responses.

```python
    # The app loop
    while True:
        # Get user's input
        user_input = console.input("[bold yellow]You: [/bold yellow]")
        # Check to see if they want to exit
        handle_user_input(user_input)
```

The main loop begins. It first prompts the user for input using Rich's colored input. The `handle_user_input()` function is called to check if the user wants to exit the application.

```python
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
```

The user's input is added to the chat history. The `delete_last_lines()` function is called to remove the input prompt, and then the user's message is displayed in a yellow-bordered panel with Markdown formatting.

```python
        # Get AI's response
        console.print(Panel(
            "[italic]Think...[italic]",
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
```

A "thinking" message is displayed to indicate that the AI is processing. The `call_openai()` function is then called with the current chat history and specified parameters to get the AI's response.

```python
        # Display the AI's response to the terminal
        delete_last_lines(3)
        console.print(Panel(
            Markdown(ai_response, code_theme="github-dark"),
            title="[bold green]AI[/bold green]",
            title_align="left",
            border_style="green"
        ))
        print()
```

The "thinking" message is removed using `delete_last_lines(3)`, and the AI's response is displayed in a green-bordered panel with Markdown formatting.

```python
        # Save the AI's response to the chat history
        chat_history.append({"role": "assistant", "content": ai_response})
```

Finally, the AI's response is added to the chat history, maintaining the conversation context for future interactions.

This loop continues indefinitely until the user types `/exit`, which is caught by the `handle_user_input()` function, terminating the application.

## AI API Call (call_ai.py)

The `call_ai.py` file contains a single function, `call_openai()`, which handles the interaction with the OpenAI API:

```python
def call_openai(
    openai_client,
    chat_history,
    model="gpt-4o-mini",
    temperature=0,
    max_completion_tokens=512
):
    completion = openai_client.chat.completions.create(
        model=model,
        messages=chat_history,
        temperature=temperature,
        max_completion_tokens=max_completion_tokens
    )
    response = completion.choices[0].message.content
    return response
```

This function takes the OpenAI client, chat history, and optional parameters for the model, temperature, and token limit. It sends a request to the OpenAI API and returns the generated response.

## Utility Functions (utils.py)

The `utils.py` file contains two utility functions:

1. `handle_user_input(user_input)`: Checks if the user wants to exit the application.
2. `delete_last_lines(number_of_lines=1)`: Deletes the specified number of lines from the terminal output, used for updating the display.

## Dependencies (requirements.txt)

The `requirements.txt` file lists the external Python packages required for the project:

```
openai
rich
```

These can be installed using pip with the command `pip install -r requirements.txt`.