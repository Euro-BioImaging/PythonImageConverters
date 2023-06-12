# PythonImageConverters
A module that wraps the image data converters `bfconvert` and `bioformats2raw` as `python` functions using the `subprocess` module.

## Requirements
`bfconvert` and `bioformats2raw` must be available. The recommended approach is to install the relevant conda packages [bftools](https://anaconda.org/bioconda/bftools) and [bioformats2raw](https://anaconda.org/ome/bioformats2raw) to a (preferably new) conda environment. Then the module can be used by simply activating this environment.

## Example use

```
from DataConverter import bioformats2raw

_ = bioformats2raw('/path/to/input',
                   '/path/to/output.źarr',
                   resolutions = 5,
                   chunk_w = 64,
                   chunk_h = 64,
                   compression = 'blosc',
                   drop_series = True,
                   )

```
