import os

import yaml

# with open('../extract.yaml','r',encoding='utf8') as f:
#     safe_file = yaml.safe_load(f)
#     print(safe_file,type(safe_file))
#     f.close()

with open('../extract.yaml','a+',encoding='utf8') as f:
    # f.truncate()
    new_f = [{"id": 12304,"data": {"school":"pingdain","student":"yao"}}]
    yaml.safe_dump(new_f,f)
    f.close()

