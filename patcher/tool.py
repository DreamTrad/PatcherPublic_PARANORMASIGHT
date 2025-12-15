"""
File        : tool.py
Author      : Silous
Created on  : 2025-10-08
Description : call tool to repack the game.
"""

# == Imports ==================================================================

from logging import Logger
from pathlib import Path
import shutil
import subprocess

# -------------------- Import Lib User -------------------

from patcher import config
from patcher.utils import xdelta
from patcher.utils.logger import get_logger


# == Global Variables =========================================================

_logger: Logger = get_logger(__name__)


# == Functions ================================================================

def repack() -> None:
    """whole patching process."""
    _call_repack()


def _call_repack() -> None:
    game_folder: Path = Path(config.GAME_FOLDER)
    patch_folder: Path = config.PATCH_FOLDER

    asset_folder = game_folder / "PARANORMASIGHT_Data" / "StreamingAssets"
    data_folder = game_folder / "PARANORMASIGHT_Data"
    shared_asset = patch_folder / "PARANORMASIGHT_Data" / "sharedassets0.assets"
    zip_file = patch_folder / "StreamingAssets.zip"

    try:
        shutil.unpack_archive(str(zip_file), str(asset_folder))
    except Exception as exc:
        _logger.error("Failed to unzip patch %s: %s", zip_file, exc)

    try:
        shutil.copy2(shared_asset, data_folder)
    except Exception as exc:
        _logger.error(
            "Failed to copy sharedassets file from %s to %s: %s",
            shared_asset,
            data_folder,
            exc,
        )