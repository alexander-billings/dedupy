# dedupy
File deduplication using Python

Given two paths, dedupy should iterate over files in those paths and identify duplicates for removal.

## Rough planned outline:
* Take two paths as arguments
* Iterate over the files in each path and hash them
* Compare file list for duplicates
* Output list for removal
* Prompt for removal
* If user approves the list, remove files