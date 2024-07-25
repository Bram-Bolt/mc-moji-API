import sys
import os
import importlib

# execution path for avatar generator
project_root = os.path.dirname(os.path.abspath(__file__))
mc_moji_path = os.path.join(project_root, "mc-moji")
sys.path.insert(0, mc_moji_path)


# use mc_moji package
mc_moji = importlib.import_module("mc-moji.app")


# save image
def save_avatar(playername: str):
    img = mc_moji.avatar_generator.generate_avatar(playername, True, True, 30)
    mc_moji.image_utils.save_image(img, playername)
