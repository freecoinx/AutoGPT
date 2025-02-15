from typing import Type

import pytest

from backend.data.block import Block, get_blocks
from backend.util.test import execute_block_test


def test_available_blocks(block: str):
    block_list = get_blocks().values()
    for block_class in block_list:
        if block_class.__name__ == block:
            execute_block_test(block_class())

