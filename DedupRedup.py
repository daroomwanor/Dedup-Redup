
"""
Author: Daro Omwanor 
Date: July 30 2019

    Algorithm:
    1.Read chunk-by-chunk the input file
    2.Calculate total chunk size using a pre-determined chunk size value of 43
    3.Return map relation: chunk - {position} ('<generator object <genexpr> at 0x106318c80>', 129, 86, 43, 0)
    4.Write MAP to Output file and write chunk data and positions 
    5.Redup retrieve and Recreate the original file
     
    Output format for the deduped file:
        
        Output: ('<generator object <genexpr> at 0x106318c80>', 129, 86, 43, 0)
        File Size: Original Size 215 (bytes) -> Deduped Size 61 (bytes)
        Hash Map: ('2880742edde73dc297cc52c716044a9a', '2880742edde73dc297cc52c716044a9a')
----------------------------------------------------------------------
Ran 2 tests in 0.005s

OK

"""

import unittest
import tempfile
import hashlib
import os
import random
import binascii





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
    print(str(data).strip('[]'))
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


class TestDedupRedup(unittest.TestCase):
	
	hmd5 = None
	hashbyte = None
	originSize = None
	inSize = None
	outSize = None

	def getChunkData(self):
		
		return bytes(x >= 254 for x in range(1024))

	def getFileSum(self, inFile):
		
		return os.path.getsize(inFile)
	
	def checkData(self, outFile):
		
		md5 = hashlib.md5()
		with open(outFile, "rb") as oFile:
			data =(oFile.read()).split(",")
			for x in data:
				md5.update(x)
		return md5.hexdigest()

	def process(self):
		
		chunkData = self.getChunkData()
		Data = [chunkData,chunkData, chunkData,chunkData, chunkData]
		hash_md5 = hashlib.md5()
		
		inFile = tempfile.NamedTemporaryFile()
		
		with open(inFile.name, "wb") as inFile:
			pass		
		outFile = tempfile.NamedTemporaryFile()
		
		with open(outFile.name, "wb") as outFile:
			pass
		
		originFile = tempfile.NamedTemporaryFile()
		
		with open(originFile.name, "wb") as oFile:
			for x in Data:
				oFile.write(chunkData)
				hash_md5.update(chunkData)
		
		
		dedup(oFile.name,inFile.name)
		redup(inFile.name,outFile.name)

		self.hmd5 = hash_md5.hexdigest()
		self.hashbyte = self.checkData(outFile.name)
		self.originSize =self.getFileSum(oFile.name)
		self.inSize =self.getFileSum(inFile.name)
		self.outSize =self.getFileSum(outFile.name)
		
		print("Original File Size: {} ----------->>> Deduped File Size: {}".format(self.originSize, self.inSize))
		print(self.hashbyte,self.hmd5)
	
	def test_size(self):
		
		self.process()
		self.assertTrue(self.originSize > self.inSize)

	def test_hash(self):
		
		self.assertEqual(self.hashbyte,self.hmd5)
 
if __name__ == '__main__':
    
    unittest.main()





