#!/usr/bin/env python
# FindTraceCalls is a Binary Ninja Api Script to find & navigate to each function call within a block/function
import sys
import time
import binaryninja as binja

functionToFind = "Quicksort"
PauseTime = 1 #Seconds


#! Finds the address of a function named Quicksort and sets it as a function object
for function in binja.BinaryView.functions:
    if function.symbol.name == functionToFind:
        inSearchFunction = function

for basicBlock in inSearchFunction.medium_level_il.basic_blocks:
    for instruction in basicBlock:
        if instruction.operation == binja.MediumLevelILOperation.MLIL_CALL:
            callAddress = instruction.address
            print(callAddress)
            # Take me there
            binja.BinaryView.navigate(bv.file.view, callAddress)
            time.sleep(PauseTime)