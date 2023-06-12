#!/usr/bin/env python

"""Wrappers for bfconvert and bioformats2raw to be run from python environment. """

import subprocess, re, shlex

intlist = lambda s: [int(x) for x in re.findall(r'\b\d+\b', s)]

def get_bfconvert_cmd(*args, **kwargs):
    cmd = []
    cmd += ["bfconvert"]
    keys = kwargs.keys()
    if "noflat" in keys:
        cmd += [" -noflat"]
    if "series" in keys:
        cmd += [" -series", ' %s' % kwargs['series']]
    if "timepoint" in keys:
        cmd += [" -timepoint", ' %s' % kwargs['timepoint']]
    if "channel" in keys:
        cmd += [" -channel", ' %s' % kwargs['channel']]
    if "z_slice" in keys:
        cmd += [" -z", ' %s' % kwargs['z_slice']]
    if "range" in keys:
        _range = intlist(kwargs['range'])
        if len(_range) != 2:
            raise TypeError('Range must have two integers specifying first and last indices of images.')
        else:
            cmd += [" -range"]
            for i in _range:
                cmd += [' %s' % i]
    if "autoscale" in keys:
        cmd += [" -autoscale"]
    if "crop" in keys:
        _crop = ''.join(kwargs['crop'][1:-1].split(' '))
        cmd += [" -crop", ' %s' % _crop]
    if "compression" in keys:
        cmd += [" -compression", ' %s' % kwargs['compression']]
    if "resolution_scale" in keys:
        cmd += [" -pyramid-scale", ' %s' % kwargs['resolution_scale']]
    if "resolutions" in keys:
        cmd += [" -pyramid-resolutions", ' %s' % kwargs['resolutions']]
    # add here all params
    cmd.append(' %s' % args[0])
    cmd.append(' %s' % args[1])
    cmdstr = ''.join(cmd)
    return cmdstr

def bfconvert(*args, shell = False, **kwargs):
    cmd = get_bfconvert_cmd(*args, **kwargs)
    if not shell:
        cmd = shlex.split(cmd)
    subprocess.run(cmd, shell = shell)
    return cmd

def get_bf2raw_cmd(*args, **kwargs):
    cmd = []
    cmd += ["bioformats2raw"]
    keys = kwargs.keys()
    if "resolutions" in keys: # The number of sub-resolutions created
        cmd += [" --resolutions", ' %s' % kwargs['resolutions']]
    if "min_image_size" in keys: # Will create sub-resolutions until the minimum image size is reached
        cmd += [" --target-min-size", ' %s' % kwargs['min_image_size']]
    if "chunk_h" in keys:
        cmd += [" --tile_height", ' %s' % kwargs['chunk_h']]
    if "chunk_w" in keys:
        cmd += [" --tile_width", ' %s' % kwargs['chunk_w']]
    if "chunk_d" in keys:
        cmd += [" --chunk_depth", ' %s' % kwargs['chunk_d']]
    if "downsample_type" in keys:
        cmd += [" --downsample-type", ' %s' % kwargs['downsample_type']]
    if "compression" in keys:
        cmd += [" --compression", ' %s' % kwargs['compression']]
    if "max_workers" in keys:
        cmd += [" --max_workers", ' %s' % kwargs['max_workers']]
    if "no_nested" in keys:
        cmd += [" --no-nested"]
    if "drop_series" in keys:
        cmd += [" --scale-format-string", ' %s' % "'%2$d'"]
    if "overwrite" in keys:
        cmd += [" --overwrite"]
    cmd.append(' %s' % args[0])
    cmd.append(' %s' % args[1])
    cmdstr = ''.join(cmd)
    return cmdstr

def bioformats2raw(*args, shell = False, **kwargs):
    cmd = get_bf2raw_cmd(*args, **kwargs)
    if not shell:
        cmd = shlex.split(cmd)
    subprocess.run(cmd, shell = shell)
    return cmd

