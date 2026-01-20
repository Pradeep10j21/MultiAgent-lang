async def fake_stream(text: str):
    for word in text.split():
        yield word + ' '
