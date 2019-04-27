#!/usr/bin/env python
import sys
import binaryninja as binja
# while main.medium_level_il.basic_blocks[i].end


for bb in main:
    for insn in bb:
        if insn.operation != binja.MediumLevelILOperation.MLIL_CALL:
            bv.navigate(bv.file.view, callAddress)


# 1
for instruction in main.basic_blocks:
    if instruction.operation == binja.MediumLevelILOperation.MLIL_CALL:
        callAddress = instruction.address
        print(callAddress)
        # Take me there
        bv.navigate(bv.file.view, callAddress)
        time.sleep(1)
# 2
for instruction in main.medium_level_il.basic_blocks[i]:
    if instruction.operation == binaryninja.MediumLevelILOperation.MLIL_CALL:
        callAddress = instruction.address
        print(callAddress)
        # Take me there
        bv.navigate(bv.file.view, callAddress)
        time.sleep(1)
    if main.medium_level_il.basic_blocks[i] == main.medium_level_il.basic_blocks[i].end:
        i += 1
