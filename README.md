# newdir
A friendly tmp-program script

## Installation
1. Clone the repository
2. `cargo install --path .`
3. Put `source /path/to/repostiory/checkout/newdir.sh` in one of your init files, e.g. `.zshrc`.

OR

1. `cargo install newdir`
2. Put `alias newdir='eval $(~/.cargo/bin/newdir)'` in one of your init files, e.g. `.zshrc`.

## Usage Example
```console
$ echo $PWD
/home/tronje
$ newdir
cd /tmp/tronje/jolly_weasel
$ echo $PWD
/tmp/tronje/jolly_weasel
```
