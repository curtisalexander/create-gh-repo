# create-gh-repo

Bash script to interact with the [Github API](https://developer.github.com/v3/) to create a [repo](https://developer.github.com/v3/repos/).

## Use

To display the help text.

```bash
create-gh-repo --help
```

The resulting help text (and usage) is below.

```bash
create-gh-repo: Create a Github repo

Usage: ./create-gh-repo [option...]

  -h, --help          display help
  -r, --repo          name of repository
  -p, --private       private repository
  -l, --license       license

  By default sets repo to public and license to MIT.

  License abbreviations may be found at https://help.github.com/en/articles/licensing-a-repository#searching-github-by-license-type

Examples:
  ./create-gh-repo --repo test                                      # create a repository named 'test', set it to be public (default), with mit license (default)
  ./create-gh-repo --repo test --private --license bsd-2-clause     # create a repository named 'test', set it to be private, with bsd license
```

## Other

The repo also includes a script, [`process-gh-license-table.py`](https://github.com/curtisalexander/create-gh-repo/blob/master/utility/process-gh-license-table.py) which simply transforms the [Github license table](https://help.github.com/en/articles/licensing-a-repository#searching-github-by-license-type) into a few different forms to include in the script. This was done in lieu of hand writing everything.
