# Data dictionary

Source file: Student_attendance_dataset.xlsx
Rows: 225014

## `year`  (original column: "Calendar year")
- type: int64; blank values: 0; distinct values: 11
- values: 2014 (18286); 2015 (18332); 2016 (20741); 2017 (20806); 2018 (20929); 2019 (21080); 2021 (21041); 2022 (20822); 2023 (20934); 2024 (21027); 2025 (21016)

## `state`  (original column: "State/Territory")
- type: str; blank values: 0; distinct values: 9
- values: Australia (32170); Australian Capital Territory (12738); New South Wales (28549); Northern Territory (21298); Queensland (28754); South Australia (27313); Tasmania (21319); Victoria (23853); Western Australia (29020)

## `sector`  (original column: "School Sector")
- type: str; blank values: 0; distinct values: 5
- values: All (49613); All non-government (44023); Catholic (41880); Government (49180); Independent (40318)

## `sex`  (original column: "Sex/Gender")
- type: str; blank values: 0; distinct values: 3
- values: All (122284); Female (51018); Male (51712)

## `geo`  (original column: "Geolocation")
- type: str; blank values: 0; distinct values: 8
- values: All (82887); Inner Regional (25681); Major Cities (26469); Metropolitan (6620); Outer Regional (29291); Provincial (6614); Remote (26447); Very Remote (21005)

## `indigenous`  (original column: "Indigenous Status")
- type: str; blank values: 0; distinct values: 4
- values: Aboriginal and Torres Strait Islander (42645); All (95273); Gap (42123); Non-Indigenous (44973)

## `disaggregation`  (original column: "Disaggregation")
- type: str; blank values: 0; distinct values: 58
- values: 1st Quarter (296); 2nd Quarter (306); 3rd Quarter (312); 4th Quarter (314); Aboriginal and Torres Strait Islander (6702); Aboriginal and Torres Strait Islanders in Inner regional (4165); Aboriginal and Torres Strait Islanders in Major cities (4270); Aboriginal and Torres Strait Islanders in Metropolitan (1072); Aboriginal and Torres Strait Islanders in Outer regional (4761); Aboriginal and Torres Strait Islanders in Provincial (1086); Aboriginal and Torres Strait Islanders in Remote (3831); Aboriginal and Torres Strait Islanders in Very remote (3540); All (7019); Female (6896); Female Aboriginal and Torres Strait Islander (6578); Female Gap (6572); Female Non-Indigenous (6886); Females in Inner regional (4312); Females in Major cities (4457); Females in Metropolitan (1101); Females in Outer regional (4867); Females in Provincial (1090); Females in Remote (4650); Females in Very remote (3609); Gap (6695); Gap in Inner regional (4165); Gap in Major cities (4270); Gap in Metropolitan (1072); Gap in Outer regional (4758); Gap in Provincial (1074); Gap in Remote (3810); Gap in Very remote (3069); Inner regional (4347); Major cities (4492); Male (7013); Male Aboriginal and Torres Strait Islander (6640); Male Gap (6638); Male Non-Indigenous (7008); Males in Inner regional (4345); Males in Major cities (4488); Males in Metropolitan (1125); Males in Outer regional (4967); Males in Provincial (1122); Males in Remote (4678); Males in Very remote (3688); Metropolitan (1125); Non-Indigenous (7012); Non-Indigenous people in Inner regional (4347); Non-Indigenous people in Major cities (4492); Non-Indigenous people in Metropolitan (1125); Non-Indigenous people in Outer regional (4966); Non-Indigenous people in Provincial (1114); Non-Indigenous people in Remote (4727); Non-Indigenous people in Very remote (3296); Outer regional (4972); Provincial (1128); Remote (4751); Very remote (3803)

## `year_level`  (original column: "School Year Level")
- type: str; blank values: 0; distinct values: 15
- values: Primary Ungraded (5011); Secondary Ungraded (5850); Year 1 (16463); Year 10 (15911); Year 2 (16456); Year 3 (16469); Year 4 (16512); Year 5 (16489); Year 6 (16488); Year 7 (16130); Year 8 (16076); Year 9 (16052); Years 1-10 (18055); Years 1-6 (16771); Years 7-10 (16281)

## `rate`  (original column: "Attendance Rate")
- type: float64; blank values: 0; distinct values: 1038
- range: -12.2 to 100.0

## `level`  (original column: "Attendance Level")
- type: float64; blank values: 20543; distinct values: 1156
- range: -56.8 to 100.0

## `is_quarter_row`  (added by script)
- type: bool; blank values: 0; distinct values: 2
- values: False (223786); True (1228)
