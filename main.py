from fastapi import FastAPI
from fastapi.responses import FileResponse
from pathlib import Path
from save_avatar import save_avatar
from save_avatar import name_file

app = FastAPI()


@app.get("/mc-moji/{playername}")
async def get_image(
    playername: str, shadows: bool = True, overlay: bool = True, size: int = 30
):
    if not 256 > size > 0:
        return {"error": f"Size should be between 1 and 255, size chosen was {size}"}

    filename = name_file(playername, shadows, overlay, size)

    save_avatar(playername, shadows, overlay, size, filename)

    image_path = Path("images", f"{filename}.png")
    print(image_path)
    if not image_path.is_file():
        return {"error": "Image not found on the server"}
    return FileResponse(image_path)
