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
        chunkfile = line.rstrip()
        data=pd.read_csv(chunkfile, delimiter='\t', converters={'text': str.strip})
        pd.set_option('display.max_colwidth', None)
        df = data['text']
        df_text=df.to_string(index=False, header=False)
        s = int(data.iloc[0]['start'])
        e = int(data.iloc[-1]['end'])
        s_time = pd.Timestamp(s, unit='ms')
        rounded_s_time = s_time.round('S')
        s_timeonly = pd.Timestamp.time(rounded_s_time)
        e_time=pd.Timestamp(e, unit='ms')
        rounded_e_time = e_time.round('S')
        e_timeonly = pd.Timestamp.time(rounded_e_time)
        timestamp = 'start: ' + str(s_timeonly) + " " + 'end: ' + str(e_timeonly)
        tape,extension = chunkfile.split(".", 1)
        outfile = 'ready_output/' + tape + 'ready' + '.txt'
        final_doc = timestamp + '\n' + '\n' + df_text
        with open(outfile,'a') as f:
            f.write(final_doc)
            f.close()

    inputfile.close()

