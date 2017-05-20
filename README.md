# mdwebsite

Static website generator with support for Markdown.

**Status:** Unavailable, currently under initial development.

## Summary

This is a Python tool for building a website that is easy to maintain once configured and templated. Add content to the website by adding files to source directory tree and running `mdwebsite`.

## The short-short version

There are two commands supported, `build` and `deploy`. By default both commands are run to perform a full site update.

### Build

Runs just the build step of the tool. Useful for ad hoc checks of the output and viewing the rendered website content locally.

```
/path/of/mdwebsite> python mdwebsite build
```

### Deploy

Creates an archive of the current version of the website, and replaces the website with the latest built version.

```
/path/of/mdwebsite> python mdwebsite deploy
```

## Setup

*Under development.*

## Configuration

*Under development.*

## Templates

*Under development.*

## Folder structure

*Under development.*

## Version history

Refer to [VERSION.md](VERSION.md) file.

## TODO

All the things!

1. Define source content, template, and resource structure
2. Configuration file
    1. source directories
    2. output directory
    3. archival options
    4. deployment options
3. Build step
4. Deploy step
5. Future: redeploy from archive
