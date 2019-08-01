
"""
Author: Daro Omwanor 
Date: July 30 2019

    Algorithm:
    1.Read chunk-by-chunk the input file
    2.Calculate total chunk size using a pre-determined chunk size value of 43
    3.Return map relation: chunk - {position} ('<generator object <genexpr> at 0x106318c80>', 129, 86, 43, 0)
    4.Write MAP to Output file and write chunk data and positions 
    5.Redup and Recreate the original file
     
    Output format for the deduped file:
        ('<generator object <genexpr> at 0x106318c80>', 43, 0)
        Original Size 129 (bytes) -> Deduped Size 52 (bytes)
        ('<generator object <genexpr> at 0x106318c80>', 129, 86, 43, 0)
        Original Size 215 (bytes) -> Deduped Size 61 (bytes)
----------------------------------------------------------------------
Ran 2 tests in 0.005s

OK

"""

import unittest
import tempfile
import hashlib
import os
import random


def dedup(inFile=None,outFile=None):
    """
       Read chunk-by-chunk the input file 
       Save the actual file data and byte positions in array 
    """
    data =[]
    chunk_size = 43

    iFile_size= os.path.getsize(inFile)
    total_chunk = iFile_size/43 # inputfile/n-byte: where n=43
    if iFile_size%43 != 0: # Round up to the nearest whole Number to determine total chunk size
        total_chunk=total_chunk+1

    with open(inFile,"rb") as iFile:
        chunk_pos = 0;
        for x in range(total_chunk+1):
            if x == 0:
                pass
            elif x == 1:
                chunk_pos=chunk_pos+chunk_size
                iLine =iFile.read(chunk_pos)
                data.append(iLine[:chunk_pos]) # Append the actual data of the first n bytes  
            else:                           
                pos = iFile_size-x*chunk_size # Save position of unique successive chunks
                data.append(pos)
                chunk_pos=chunk_pos+chunk_size
    # write to output file string value of data as a comma separated value (Plaform agnostic)
    with open(outFile, "wb") as oFile:
            oFile.write(str(data).strip('[]'))
    pass

def redup(inFile=None,outFile=None):
    """
        Export MAP to Output file and write chunk data and positions 
    """
    data = None
    with open(inFile, "rb") as iFile:
        data=iFile.read()
        with open(outFile, "wb") as oFile:
            bData = data.split(",")
            for x in range(len(bData)):
                oFile.write(bData[0].strip("''"))
    return True

