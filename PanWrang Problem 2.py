import pandas as pd

data = {'Box': ['Box1','Box1','Box1','Box2','Box2','Box2'], 
        'Dimensions': ['Length','Width','Height','Length','Width','Height'], 
        'Value': [6,4,2,5,3,4]}

frame = pd.DataFrame(data, columns=['Box','Dimensions','Value'])
tidy = frame.pivot_table(index=['Box'], columns='Dimensions', values='Value').reset_index()

volume = [48,60] 
tidy['Volume'] =  volume