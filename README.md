Android Library Detection
====

This repo contains some infrastructure for Android Library Detection.

## Get started

First, `cd tools/`.

Put APKs inside `examples/`, and then run `make run` in both `libd` and `libradar` directories,
which will build the container and run the corresponding tool on APKs, and store them in
their `output/` sub-directory.

Compute statistics back in `tools/`:

```
$ python compare_libd_libradar.py libd/output libradar/output
Finding the overlapping libraries on c577b7e730f955a5f99642e5a8898f64a5b5080d1bf2096804f9992a895ac956.apk.txt
The intersections are: 
['Lcom/android/vending', 'Lcom/openfeint', 'Lcom/prime31', 'Lorg/fmod', 'Lcom/google/ads']
The libraries that are not in the intersection for libd are: 
Lcom/unity3d/Plugin, the frequency is 1
Lcom/unity3d/player, the frequency is 1
Lorg/apache/commons, the frequency is 1
Lorg/codehaus/jackson, the frequency is 1
Lcom/google/api, the frequency is 1


The libraries that are not in the intersection for libradar are: 
Lcom/unity3d, the frequency is 1
```
