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
    # prevent files from becomming to big
    if not 0 < size < 256:
        return {"error": f"Size should be between 1 and 255, size chosen was {size}"}

    # generate file name with image specs
    filename = name_file(playername, shadows, overlay, size)

    # save and load avatar file
    try:
        save_avatar(playername, shadows, overlay, size, filename)
    except:
        return {
            "error": "error in generating image, please ensure you put in a valid username.",
        }

    image_path = Path("images", f"{filename}.png")
    # check if image is available
    if not image_path.is_file():
        return {"error": "Image not found on the server"}

    # return image
    return FileResponse(image_path)
