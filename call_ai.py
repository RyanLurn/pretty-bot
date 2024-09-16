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
