# quick.py

Copy this file for boilerplate Python 3 scripts, which I write far too often.

```
usage: quick.py [-h] [-c [CONFIG]] [-s CONFIG_SECTION] [-v]

optional arguments:
  -h, --help            show this help message and exit
  -c [CONFIG], --config [CONFIG]
                        Config path
  -s CONFIG_SECTION, --config-section CONFIG_SECTION
                        Config section
  -v, --verbose         Verbose logging
```

## Vim

If you're a fellow vimmer, add this to your .vimrc:

```
" Copy Python script
function! QuickPy(filename)
    execute "e " . a:filename
    execute "0r ~/path/to/quick-python/quick.py"
endfunction
command! -nargs=? QuickPy call QuickPy(<q-args>)
```

Whenever you need to create a new file, execute the following Vim command:

```
:QuickPy <filename.py>
```
