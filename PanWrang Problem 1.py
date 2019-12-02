import pandas as pd

data1 = {'Student': ['Ice Bear','Panda','Grizzly'], 
         'Math': [80,95,79]}
frame1 = pd.DataFrame(data1, columns=['Student', 'Math']) 

data2 = {'Student': ['Ice Bear','Panda','Grizzly'], 
         'Electronics': [85,81,83]}
frame2 = pd.DataFrame(data2, columns=['Student', 'Electronics']) 

data3 = {'Student': ['Ice Bear','Panda','Grizzly'], 
         'GEAS': [90,79,93]}
frame3 = pd.DataFrame(data3, columns=['Student', 'GEAS']) 

data4 = {'Student': ['Ice Bear','Panda','Grizzly'], 
         'ESAT': [93,89,88]}
frame4 = pd.DataFrame(data4, columns=['Student', 'ESAT']) 

frame5 = pd.merge(frame1,frame2, on='Student')
frame6 = pd.merge(frame3,frame4, on='Student')
frame7 = pd.merge(frame5,frame6, on='Student')
frame8 = pd.melt(frame7, id_vars=['Student'], var_name='Subjects', value_name='Grades')