"""Collection of regular expressions to catch spectrum XML-tags."""
import re
import regex

SPECTRUM_INDEX_PATTERN = re.compile(
    b'(?P<type>(scan=|nativeID="))(?P<nativeID>[0-9]*)">"'
    b"(?P<offset>[0-9]*)</offset>"
)

SPECTRUM_INDEX_PATTERN_SCIEX = re.compile(
    b'(?P<type>(cycle=))(?P<nativeID>[0-9]*) experiment=[0-9]*">(?P<offset>[0-9]*)</offset>'
)

"""
Regex pattern for spectrum index
works for obo format 1.1.0 until <last version checked>

Catches:
    #. demo 1
    #. demo 2
"""


SIM_INDEX_PATTERN = re.compile(
    b'(?P<type>idRef=")(?P<nativeID>.*)">(?P<offset>[0-9]*)</offset>'
)

SIM_INDEX_PATTERN_SCIEX = re.compile(
    b'(?P<type>(idRef=))"sample=[0-9]* period=[0-9]* cycle=(?P<nativeID>[0-9]*) experiment=[0-9]*">(?P<offset>[0-9]*)</offset>'
)
"""
Regex pattern for SIM index
"""
SPECTRUM_PATTERN3 = regex.compile(r"((\w+)=(\w+\s*))+")
SPECTRUM_ID_PATTERN = re.compile(r'="{0,1}([0-9]*)"{0,1}>{0,1}$')
SPECTRUM_ID_PATTERN2 = re.compile(r"(scan|scanId)=(\d+)")
"""
Simplified spectrum id regex. Greedly catches ints at the end of line
"""

FILE_ENCODING_PATTERN = re.compile(b'encoding="(?P<encoding>[A-Za-z0-9-]*)"')
"""
Regex to catch xml file encoding
"""

MOBY_DICK_CHAPTER_PATTERN = re.compile(r"CHAPTER ([0-9]+).*")
"""
Regex to catch moby dick chapter number used in the index gezip writer example.
"""
SPECTRUM_OPEN_PATTERN = re.compile(
    b'<*spectrum[^>]*(index|id)="(.*?)".*(index|id)="(.*?)"'
)
"""
Regex to catch specturm open xml tag with encoded array length
"""

SPECTRUM_OPEN_PATTERN_SIMPLE = re.compile(rb"<spectrum ")
SPECTRUM_ID_PATTERN_SIMPLE = re.compile(rb"<*spectrum[^>]*id=\"(?P<id>[^\"]+)\"")
SPECTRUM_DEFAULTARRY_PATTERN_SIMPLE = re.compile(
    rb"<*spectrum[^>]*defaultArrayLength=\"[0-9]+\">"
)

CHROMO_OPEN_PATTERN = re.compile(b'<chromatogram\\s.*?id="(.*?)"')

SPECTRUM_CLOSE_PATTERN = re.compile(b"</spectrum>")
"""Regex to catch spectrum xml close tags"""

CHROMATOGRAM_CLOSE_PATTERN = re.compile(b"</chromatogram>")
"""Regex to catch spectrum xml close tags"""

SPECTRUM_TAG_PATTERN = re.compile(r'<spectrum.*?id="(?P<index>[^"]+)".*?>')
"""Regex to catch spectrum tag pattern"""

CHROMATOGRAM_ID_PATTERN = re.compile(r'<chromatogram.*id="(.*?)".*?>')
"""Regex to catch chromatogram id patterns"""

CHROMATOGRAM_PATTERN = re.compile(r'<chromatogram.*id="(.*?)".*?>')
"""Regex to catch chromatogram id pattern (again ?)"""

CHROMATOGRAM_AND_SPECTRUM_PATTERN_WITH_ID = re.compile(
    r"<\s*(chromatogram|spectrum)\s*(id=(\".*?\")|index=\".*?\")\s(id=(\".*?\"))*\s*.*\sdefaultArrayLength=\"[0-9]+\">"
)
"""Regex to catch combined chromatogram and spectrum patterns"""

INDEX_LIST_OFFSET_PATTERN = re.compile(
    b"<indexListOffset>(?P<indexListOffset>[0-9]*)</indexListOffset>"
)

CHROMATOGRAM_OFFSET_PATTERN = re.compile(
    b'(?P<WTF>[nativeID|idRef])="TIC">(?P<offset>[0-9]*)</offset'
)
