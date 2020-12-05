import pytest
from Day_4_add import birth_year_4_2, issue_year_4_2, expiration_year_4_2, height_4_2, hair_4_2, eyes_4_2
from Day_4_add import passport_4_2, check_validation_4_2
from Advent_of_Code import txt_to_array

@pytest.mark.parametrize("byr, valid",[("byr:1950",1),("byr:2005",0)])
def test_birth_year(byr, valid):
    assert (birth_year_4_2(byr)==valid)

@pytest.mark.parametrize("iyr, valid",[("iyr:2020",1),("iyr:2005",0)])
def test_issue_year(iyr, valid):
    assert (issue_year_4_2(iyr)==valid)

@pytest.mark.parametrize("eyr, valid",[("eyr:2020",1),("eyr:150",0)])
def test_expiration_year(eyr, valid):
    assert(expiration_year_4_2(eyr) == valid)

@pytest.mark.parametrize("hgt, valid",[("hgt:170cm",1),("hgt:170",0), ("hgt:60in",1), ("hgt:160in",0)])
def test_height(hgt, valid):
    assert(height_4_2(hgt)==valid)

@pytest.mark.parametrize("hcl,valid",[("hcl:123abc",0),("hcl:#123abc", 1),("hcl:#a97842",1),("hcl:#md34",0)])
def test_hair(hcl, valid):
    assert(hair_4_2(hcl)==valid)

@pytest.mark.parametrize("ecl,valid",[("ecl:amb",1),("ecl:anb",0),("ecl:brngry",0)])
def test_eyes(ecl,valid):
    assert(eyes_4_2(ecl)==valid)

@pytest.mark.parametrize("pid, valid",[("pid:000099999",1),("pid:0000012345",0),("pid:2930",0)])
def test_passport(pid, valid):
    assert(passport_4_2(pid)==valid)

