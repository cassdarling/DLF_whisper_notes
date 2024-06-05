#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import os.path as Path


# In[ ]:


if not Path.isfile('filelist.txt'):
    print('need to create a filelist.txt file')
else:
    inputfile = open('filelist.txt', 'r')
    for line in inputfile:
        whisperfile = line.rstrip()
        data = pd.read_csv(whisperfile,delimiter="\t")
        file_number = 0 #set parameters
        last_time = 0
        slice = 900000
        tape,b=whisperfile.split("_", 1) #create output file name
        outfile_base = 'output/output' + tape
        for time in range(slice, data.end.max() + slice, slice):
            outfile_name = outfile_base + "_" + str(round(time/slice)) + ".tsv" #creates filename with integer
            slice_file = data[(data['end'] < time) & (data['end'] > last_time)] #slices data
            slice_file.to_csv(outfile_name, index=False, header=True, sep='\t') #write out dataframe to file
            last_time = time
            
    inputfile.close()


# In[ ]:




