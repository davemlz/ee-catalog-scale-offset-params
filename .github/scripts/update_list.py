import requests
import json
# Request ee catalog
eeCatalog = requests.get('https://raw.githubusercontent.com/davemlz/ee-flatten/main/list/ee-catalog-flatten.json').json()
# Get the datasets
eeDict = dict()
for dataset in eeCatalog:
    if dataset['rel'] == 'child':
        response = requests.get(dataset['href'])
        if response.status_code == 200:
            dataset = requests.get(dataset['href']).json()
            if dataset['gee:type'] in ['image','image_collection']:
                if 'eo:bands' in list(dataset['summaries'].keys()):
                    bands = dataset['summaries']['eo:bands']
                    if len(bands) > 0:
                        bandsDict = dict()
                        for band in bands:
                            name = band['name']
                            if 'gee:scale' in list(band.keys()):
                                scale = band['gee:scale']
                            else:
                                scale = 1.0
                            if 'gee:offset' in list(band.keys()):
                                offset = band['gee:offset']
                            else:
                                offset = 0.0
                            bandsDict[name] = {'scale':scale, 'offset':offset}
                        eeDict[dataset['id']] = bandsDict
# Save the list as a json file
with open('./list/ee-catalog-scale-offset-parameters.json','w') as fp:
    json.dump(eeDict, fp, indent = 4, sort_keys = True)