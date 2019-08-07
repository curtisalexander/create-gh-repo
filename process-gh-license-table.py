# copied from html at https://help.github.com/en/articles/licensing-a-repository#searching-github-by-license-type
license_text = """\
Academic Free License v3.0	afl-3.0
Apache license 2.0	apache-2.0
Artistic license 2.0	artistic-2.0
Boost Software License 1.0	bsl-1.0
BSD 2-clause "Simplified" license	bsd-2-clause
BSD 3-clause "New" or "Revised" license	bsd-3-clause
BSD 3-clause Clear license	bsd-3-clause-clear
Creative Commons license family	cc
Creative Commons Zero v1.0 Universal	cc0-1.0
Creative Commons Attribution 4.0	cc-by-4.0
Creative Commons Attribution Share Alike 4.0	cc-by-sa-4.0
Do What The F*ck You Want To Public License	wtfpl
Educational Community License v2.0	ecl-2.0
Eclipse Public License 1.0	epl-1.0
European Union Public License 1.1	eupl-1.1
GNU Affero General Public License v3.0	agpl-3.0
GNU General Public License family	gpl
GNU General Public License v2.0	gpl-2.0
GNU General Public License v3.0	gpl-3.0
GNU Lesser General Public License family	lgpl
GNU Lesser General Public License v2.1	lgpl-2.1
GNU Lesser General Public License v3.0	lgpl-3.0
ISC	isc
LaTeX Project Public License v1.3c	lppl-1.3c
Microsoft Public License	ms-pl
MIT	mit
Mozilla Public License 2.0	mpl-2.0
Open Software License 3.0	osl-3.0
PostgreSQL License	postgresql
SIL Open Font License 1.1	ofl-1.1
University of Illinois/NCSA Open Source License	ncsa
The Unlicense	unlicense
zLib License	zlib
"""

# Replace tabs with custom separator
license_text_no_tab = license_text.replace("\t", "||")

# Split into list based on newlines
license_list = license_text_no_tab.splitlines()

# Split each line again based on custom separator
result = []
for l in license_list:
    result.append(l.split("||"))

# Print to standard out case statement needed for script
print("case $LICENSE in")
for r in result:
    license_abbrev = r[1]
    license_txt = r[0].replace('"', "'")
    print(f'    "{license_abbrev}")')
    print(f'        LICENSETEXT="{license_txt}"')
    print("        ;;")
print("    *)")
print("        display_license_help")
print("        exit 0")
print("        ;;")
print("esac")

# Print out matching for use in license help
print("\n")
license_abbrev_header = "License Abbreviation".ljust(20)
license_txt_header = "License Text".ljust(50)
print(f'    echo "| {license_abbrev_header} | {license_txt_header} |"')
line_abbrev = "-" * 20
line_txt = "-" * 50
print(f'    echo "| {line_abbrev} | {line_txt} |"')
for r in result:
    license_abbrev = r[1].ljust(20)
    license_txt = r[0].replace('"', "'").ljust(50)
    print(f'    echo "| {license_abbrev} | {license_txt} |"')
