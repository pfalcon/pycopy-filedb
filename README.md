micropython-filedb
==================

`filedb` is a simple ORM-like module for storing database data in file
system using files and directories, primarily intended for MicroPython
(https://github.com/micropython/micropython).

`filedb` was a proof-of-concept style implementation of database-like
functionality, made before the builtin
[btree](http://docs.micropython.org/en/latest/library/btree.html) database
module was added to MicroPython. For the most purposes, `filedb` would
be superceded by `btree` now, but is still provided for special cases
when it may be useful.

For more information, refer to the source, and for usage example in
https://github.com/pfalcon/notes-pico/tree/master/notes_pico (this
web application support different backends, included `filedb`; note
that the default one is `btree`).
