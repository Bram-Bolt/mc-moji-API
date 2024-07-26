import sys
import os
import importlib

# execution path for avatar generator
project_root = os.path.dirname(os.path.abspath(__file__))
mc_moji_path = os.path.join(project_root, "mc-moji")
sys.path.insert(0, mc_moji_path)


# use mc_moji package
mc_moji = importlib.import_module("mc-moji.app")


# name image
def name_file(playername: str, shadows: bool, overlay: bool, size: int) -> str:
    name = playername
    if shadows:
        name += "_s"  # shadow tag
    if overlay:
        name += "_o"  # overlay tag
    name += f"_z{size}"  # size tag
    return name


# save image
def save_avatar(
    playername: str, shadows: bool, overlay: bool, size: int, filename: str
) -> None:
    img = mc_moji.avatar_generator.generate_avatar(playername, shadows, overlay, size)
    mc_moji.image_utils.save_image(img, filename, "images")
