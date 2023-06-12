# PythonImageConverters
A module that runs the image data converters bfconvert and bioformats2raw from python using the subprocess module.

## Example

```
from DataConverter import get_bf2raw_cmd, bioformats2raw, bfconvert

res = bioformats2raw('/path/to/input',
                     '/path/to/output.źarr',
                     resolutions = 5,
                     chunk_w = 64,
                     chunk_h = 64,
                     compression = 'zlib',
                     drop_series = True,
                     no_nested = True
                     )

```
