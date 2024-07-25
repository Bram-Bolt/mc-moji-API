from fastapi import FastAPI
from fastapi.responses import FileResponse
from pathlib import Path
from save_avatar import save_avatar

app = FastAPI()


@app.get("/get_image/{playername}")
async def get_image(playername):
    save_avatar(playername)
    image_path = Path("images", f"{playername}.png")
    if not image_path.is_file():
        return {"error": "Image not found on the server"}
    return FileResponse(image_path)
