#!/usr/bin/env python
import sys
import time
import binaryninja as binja

handled_target_value_types = [
    binja.RegisterValueType.ConstantPointerValue,
    binja.RegisterValueType.ConstantValue,
    binja.RegisterValueType.ImportedAddressValue,
]

def find_mlil_calls_to_targets(mlil_ssa_func, interesting_targets):
    for bb in mlil_ssa_func:
        for insn in bb:
            if insn.operation != binja.MediumLevelILOperation.MLIL_CALL_SSA:
                continue
            target = insn.dest.value
            if target.type not in handled_target_value_types:
                continue
            if target.value not in interesting_targets:
                continue
            yield insn
    return