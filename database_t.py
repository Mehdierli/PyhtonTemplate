# -*- coding: utf-8 -*-

import dbm
db = dbm.open('captions', 'c')

db['he.jpg'] = "photo of a model"
db['flame.jpg'] = "Flame Soul Goddess"
db['fate.jpg'] = "Young Goddess Of Fate"
db['fates.jpg'] = "Young Goddess Of Fate"

"""
db['he.jpg'] = "photo of a model, beautiful?"

If you make another assignment to an existing key, 
dbm replaces the old value:
"""

for key in db:
    print(key, db[key])  
    
db.close()