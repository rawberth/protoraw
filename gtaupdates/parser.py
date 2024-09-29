


from pathlib import Path



samples = (
    Path(__file__).parent
    / 'samples')



def parse(
    content: str,
) -> dict:
    print(content)



for file in samples.iterdir():
    content = file.read_text()
    print(parse(content))
