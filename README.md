# create-gh-repo

Bash script to interact with the [Github API](https://developer.github.com/v3/) to create a [repo](https://developer.github.com/v3/repos/).

## Parameter Descriptions

### Personal access token

A [personal access token](https://help.github.com/en/articles/creating-a-personal-access-token-for-the-command-line) must be created to interact with the Github API.

**Any OS:**
The personal access token can be passed in on the command line via the `--pat` switch.

**macOS Only:**
The personal access token may be fetched from the [macOS keychain](https://support.apple.com/en-gb/guide/keychain-access/kyca1083/mac). Note that this is accomplished with the command below.

```
sudo security find-internet-password -gws github.com
```

### Licenses

Licenses are represented by an abbreviation [utilized by Github](https://help.github.com/en/articles/licensing-a-repository#searching-github-by-license-type).

For convenience, the licenses available are listed below.

| License Abbreviation | License Text                                    |
| -------------------- | ----------------------------------------------- |
| afl-3.0              | Academic Free License v3.0                      |
| apache-2.0           | Apache license 2.0                              |
| artistic-2.0         | Artistic license 2.0                            |
| bsl-1.0              | Boost Software License 1.0                      |
| bsd-2-clause         | BSD 2-clause 'Simplified' license               |
| bsd-3-clause         | BSD 3-clause 'New' or 'Revised' license         |
| bsd-3-clause-clear   | BSD 3-clause Clear license                      |
| cc                   | Creative Commons license family                 |
| cc0-1.0              | Creative Commons Zero v1.0 Universal            |
| cc-by-4.0            | Creative Commons Attribution 4.0                |
| cc-by-sa-4.0         | Creative Commons Attribution Share Alike 4.0    |
| wtfpl                | Do What The F\*ck You Want To Public License    |
| ecl-2.0              | Educational Community License v2.0              |
| epl-1.0              | Eclipse Public License 1.0                      |
| eupl-1.1             | European Union Public License 1.1               |
| agpl-3.0             | GNU Affero General Public License v3.0          |
| gpl                  | GNU General Public License family               |
| gpl-2.0              | GNU General Public License v2.0                 |
| gpl-3.0              | GNU General Public License v3.0                 |
| lgpl                 | GNU Lesser General Public License family        |
| lgpl-2.1             | GNU Lesser General Public License v2.1          |
| lgpl-3.0             | GNU Lesser General Public License v3.0          |
| isc                  | ISC                                             |
| lppl-1.3c            | LaTeX Project Public License v1.3c              |
| ms-pl                | Microsoft Public License                        |
| mit                  | MIT                                             |
| mpl-2.0              | Mozilla Public License 2.0                      |
| osl-3.0              | Open Software License 3.0                       |
| postgresql           | PostgreSQL License                              |
| ofl-1.1              | SIL Open Font License 1.1                       |
| ncsa                 | University of Illinois/NCSA Open Source License |
| unlicense            | The Unlicense                                   |
| zlib                 | zLib License                                    |

## Use

To display the help text.

```
create-gh-repo --help
```

<br/>

The resulting help text (and usage) is below.

```
create-gh-repo: Create a Github repo

Usage: ./create-gh-repo [option...]

  -h, --help          display help
  -r, --repo          name of repository
  -p, --private       private repository
  -l, --license       license
  -t, --pat           personal access token

  Defaults
    - private: false (set to public)
    - license: mit
    - pat: accessed via macOS keychain

  Personal access token
    Personal access token may be passed in on the command line or it may be fetched from macOS keychain (default).

  Licenses
    License abbreviations may be found at https://help.github.com/en/articles/licensing-a-repository#searching-github-by-license-type

Examples:
  ./create-gh-repo --repo test                                   # create a repository named 'test', set it to be public (default), with mit license (default)
  ./create-gh-repo --repo test --private --license bsd-2-clause  # create a repository named 'test', set it to be private, with bsd license
  ./create-gh-repo --repo test --private --pat 123abc            # create a repository named 'test', set it to be private, and pass the personal access token on the command line
```

## Other

The repo also includes a script, [`process-gh-license-table.py`](https://github.com/curtisalexander/create-gh-repo/blob/master/utility/process-gh-license-table.py) which simply transforms the [Github license table](https://help.github.com/en/articles/licensing-a-repository#searching-github-by-license-type) into a few different forms to include in the script. This was done in lieu of hand writing everything.
