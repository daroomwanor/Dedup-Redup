# Dedup-Redup
Author: Daro Omwanor
Date: July 30 2019




    Generic Algorithm:
    1.Read chunk-by-chunk the input file
    2.Calculate total chunk size using a pre-determined chunk size value of 43
    3.Map relation: chunk - {position} 
    4.Export MAP to Output file and write chunk data and positions 

    Output format for the deduped file:
        ('<generator object <genexpr> at 0x106318c80>', 43, 0)
        Original Size 129 (bytes) -> Deduped Size 52 (bytes)
        ('<generator object <genexpr> at 0x106318c80>', 129, 86, 43, 0)
        Original Size 215 (bytes) -> Deduped Size 61 (bytes)
----------------------------------------------------------------------
Ran 2 tests in 0.005s

OK
