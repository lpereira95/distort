
## Installation

Install with

```bash
pip install git+https://github.com/lpereira95/distort.git@master
```



## Design

By design, the `mesh` object send to `distortor.apply_distortion` is modified, meaning you should copy your `mesh` object before any distortion if you want to keep access to the initial mesh.




