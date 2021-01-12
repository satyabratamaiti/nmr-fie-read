#! /usr/bin/env python
model_number = 1
fp=open("1g03.pdb",'r')
info=fp.readlines
#PDB_text = """
# 
#"""
new_file_text = ""
for line in fp:
    line = line.strip () #for better control of ends of lines
    if line == "ENDMDL":
        # save file with file number in name
        output_file = open("model_" + str(model_number) + ".pdb", "w")
        output_file.write(new_file_text.rstrip('\r\n'))
        output_file.close()
        # reset everything for next model
        model_number += 1
        new_file_text = ""
    elif not line.startswith("MODEL"):
        new_file_text += line + '\n'
