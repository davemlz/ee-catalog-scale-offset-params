# List of Scale and Offset parameters of the GEE Catalog

A list of all the scale and offset parameters for each raster dataset in Google Earth Engine.

## Scale and Offset Parameters

The list of scale and offset parameters for each raster dataset ([check the list here](https://github.com/davemlz/ee-catalog-scale-offset-params/blob/main/ee-catalog-scale-offset-parameters.json)) is presented in the `ee-catalog-scale-offset-parameters.json` file. This list will be be used by the [eemont Python package](https://github.com/davemlz/eemont) for the `.scale()` method in `ee.Image` and `ee.ImageCollection` extensions.

## Structure

The structure of the list follows this standard:

```python
{
    ...,
    'dataset_id': {
        'band1_name': {
            'scale': 'scale_value',
            'offset': 'offset_value'
        },
        'band2_name': {
            'scale': 'scale_value',
            'offset': 'offset_value'
        },
        ...
    },
    ...
}
```

The `scale` and `offset` parameters for each band are the `gee:scale` and `gee:offset` keys for each one of the bands in the `eo:bands` key of the raster datasets in the [Google Earth Engine STAC](https://earthengine-stac.storage.googleapis.com/catalog/catalog.json).

If a specific band doesn't have the `gee:scale` attribute, the `scale` attribute is set as `1.0`, while the `offset` attribute is set to `0.0` if the `gee:offset` attribute doesn't exist.

If a raster dataset doesn't have bands in the `eo:bands` attribute, the dataset is not included in this list.

## List

Check the full list of scale and offset parameters [here](https://github.com/davemlz/ee-catalog-scale-offset-params/blob/main/ee-catalog-scale-offset-parameters.json).

## Download Raw Files

You can download or clone the repository:

```
git clone https://github.com/davemlz/ee-catalog-scale-offset-params.git
```

Or you can download the single file here (right-click > Save link as...):

- json file: [Raw list](https://raw.githubusercontent.com/davemlz/ee-catalog-scale-offset-params/main/ee-catalog-scale-offset-parameters.json).

## Updates

The list is updated every day from the [Google Earth Engine STAC](https://earthengine-stac.storage.googleapis.com/catalog/catalog.json) by using GitHub Actions.