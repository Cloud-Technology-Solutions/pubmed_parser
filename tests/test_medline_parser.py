import os
import pytest

import pubmed_parser as pp


def test_parse_medline_xml():
    """
    Test parsing MEDLINE XML
    """
    expected_title = "Monitoring of bacteriological contamination and as"
    expected_abstract = "Two hundred and sixty nine beef, 230 sheep and 165"

    parsed_medline = pp.parse_medline_xml(os.path.join("data", "pubmed20n0014.xml.gz"))
    assert isinstance(parsed_medline, list)
    assert len(parsed_medline) == 30000, "Expect to have 30000 records"
    assert (
        len([p for p in parsed_medline if len(p["title"]) > 0]) == 30000
    ), "Expect every records to have title"
    assert parsed_medline[0]["title"][0:50] == expected_title
    assert parsed_medline[0]["abstract"][0:50] == expected_abstract
    assert parsed_medline[0]["pmid"] == "399296"
    assert parsed_medline[0]["language"] == ["eng"]
    assert parsed_medline[965]["language"] == ["fre", "ger"]


def test_parse_medline_xml_abcam():
    """
    Test parsing MEDLINE XML - Abcam version
    """

    expected_title = "Monitoring of bacteriological contamination and as"
    expected_abstract = "Two hundred and sixty nine beef, 230 sheep and 165"

    parsed_medline = pp.parse_medline_xml_abcam(os.path.join("data", "pubmed20n0014.xml.gz"))

    assert isinstance(parsed_medline, list)
    assert len(parsed_medline) == 30000, "Expect to have 30000 records"
    assert (len([p for p in parsed_medline if len(p["Title"]) > 0]) == 30000), "Expect every records to have title"
    assert [len(elem.keys()) for elem in parsed_medline] == [14] * len(parsed_medline), "Every record should have 14 keys"

    assert parsed_medline[0]["Title"][0:50] == expected_title
    assert parsed_medline[0]["Abstract"][0:50] == expected_abstract
    assert parsed_medline[0]["PMID"] == "399296"
    assert parsed_medline[0]["Language"] == ["eng"]
    assert parsed_medline[965]["Language"] == ["fre", "ger"]
    assert parsed_medline[23]['Year'] == '1979'
    assert parsed_medline[31]['DOI'] == '10.1038/281646a0'
    assert parsed_medline[33]['Journal'] == 'Nature'
    assert parsed_medline[33]['JournalAbv'] == 'Nature'
    assert parsed_medline[45]['IngestedFrom'] == 'pubmed20n0014.xml.gz'


def test_parse_medline_grant_id():
    """
    Test parsing grants from MEDLINE XML
    """
    grants = pp.parse_medline_grant_id(os.path.join("data", "pubmed20n0014.xml.gz"))
    assert isinstance(grants, list)
    assert isinstance(grants[0], dict)
    assert grants[0]["pmid"] == "399300"
    assert grants[0]["grant_id"] == "HL17731"
    assert len(grants) == 484, "Expect number of grants in a given file to be 484"
