def text_repl(string_item):
    return (string_item.replace('PEAGE', 'PRTAGE').replace('PTERNHLY', 'PRERNHLY')
            .replace('PTERNWA', 'PRERNWA').replace('GEMETSTA', 'METSTA')
            .replace('GTMETSTA', 'METSTA').replace('PERACE', 'PRDTRACE')
            .replace('PTDTRACE', 'PRDTRACE').replace('PRORIGIN', 'PRDTHSP')
            .replace('HRHHID (partII)', 'HRHHID2').replace('PTERN2', 'PUERN2')
            .replace('PTIO1OCD', 'PEIO1OCD').replace('PUAFEVER', 'PEAFEVER')
            .replace('GECO', 'GTCO').replace('GEMSA', 'MSA').replace('GECMSA', 'CMSA')
            .replace('GTMSA', 'MSA').replace('GTCMSA', 'CMSA'))


VarList = ['PWORWGT', 'PWCMPWGT', 'PRERNWA',
           'PTERNWA', 'PWSSWGT', 'HRHHID (partII)', 
           'HRHHID2', 'HRYEAR', 'HRYEAR4', 'PRERNHLY',
           'PTERNHLY', 'HRMONTH', 'PESEX', 'PEMLR',
           'PENLFRET', 'PENLFACT', 'GESTFIPS',
           'HRMIS', 'PRFTLF', 'PEERNHRY', 'PWLGWGT',
           'PRSJMJ', 'PEEDUCA', 'PENATVTY', 'PUSLFPRX',
           'PRWKSTAT', 'PRMJOCC1', 'PRMJOCC2', 'PRMJIND1', 'PRMJIND2', 
           'GTMETSTA', 'GEMETSTA', 'GECO', 'GTCO', 'GEMSA', 'GECMSA',
           'PEDWWNTO', 'PRUNTYPE', 'GTCBSA', 'GTCMSA',
           'PERACE', 'PTDTRACE', 'PRDTRACE', 'PRORIGIN',
           'HUHHNUM', 'PRDTHSP', 'PRCHLD', 'PRTAGE',
           'PEAGE', 'PULINENO', 'PRWNTJOB', 'PEERNLAB',
           'PRUNEDUR', 'PEHRUSL1', 'PRMARSTA', 'PRCITSHP',
           'PRDTOCC1', 'PRDTOCC2', 'PRDTIND1', 'PRDTIND2', 
           'PEHRUSL2', 'PEHRUSLT',
           'PEIO1COW', 'PEIO1OCD', 'PEIO2OCD', 'PEIO1ICD', 'PEIO2ICD',
           'HRHHID', 'HRSAMPLE', 'HRSERSUF', 'PTIO1OCD',
           'PRDISFLG', 'PUAFEVER', 'PEAFEVER', 'PECERT1',
           'GTCSA', 'PEHRACTT', 'PEHRACT1', 'PEERNCOV',
           'PESCHENR', 'PRNMCHLD', 'PTERN2', 'PEHRACT2',
           'PUERN2', 'QSTNUM', 'OCCURNUM']
            # 'HRNUMHOU', 'HWHHWGT', '\x0cRNUMHOU', 'HRHTYPE' 

DataDict = {'January_2017_Record_Layout.txt':
            {'start': '2017-01-01', 'end': '2019-12-01',
             're': f'({"|".join(VarList)})\s+(\d+)\s+.*?\t+.*?(\d\d*).*?(\d\d+)'},
            'January_2015_Record_Layout.txt':
            {'start': '2015-01-01', 'end': '2016-12-31',
             're': f'({"|".join(VarList)})\s+(\d+)\s+.*?\t+.*?(\d\d*).*?(\d\d+)'},
            'January_2014_Record_Layout.txt':
            {'start': '2014-01-01', 'end': '2014-12-31',
             're': f'({"|".join(VarList)})\s+(\d+)\s+.*?\t+.*?(\d\d*).*?(\d\d+)'},
            'January_2013_Record_Layout.txt':
            {'start': '2013-01-01', 'end': '2013-12-31',
             're': f'({"|".join(VarList)})\s+(\d+)\s+.*?\t+.*?(\d\d*).*?(\d\d+)'},
            'may12dd.txt':
            {'start': '2012-05-01', 'end': '2012-12-31',
             're': f'({"|".join(VarList)})\s+(\d+)\s+.*?\t+.*?(\d\d*).*?(\d\d+)'},
            'jan10dd.txt':
            {'start': '2010-01-01', 'end': '2012-04-30',
             're': f'\n(?:\x0c)?({"|".join(VarList)})\s+(\d+)\s+.*? \s+.*?(\d\d*).*?(\d\d+)'},
            'jan09dd.txt':
            {'start': '2009-01-01', 'end': '2009-12-31',
             're': f'\n(?:\x0c)?({"|".join(VarList)})\s+(\d+)\s+.*? \s+.*?(\d\d*).*?(\d\d+)'},
            'jan07dd.txt':
            {'start': '2007-01-01', 'end': '2008-12-31',
             're': f'\n(?:\x0c)?({"|".join(VarList)})\s+(\d+)\s+.*? \s+.*?(\d\d*).*?(\d\d+)'},
            'augnov05dd.txt':
            {'start': '2005-08-01', 'end': '2006-12-31',
             're': f'\n(?:\x0c)?({"|".join(VarList)})\s+(\d+)\s+.*? \s+.*?(\d\d*).*?(\d\d+)'},
            'may04dd.txt':
            {'start': '2004-05-01', 'end': '2005-7-31',
             're': f'\n(?:\x0c)?({"|".join(VarList)})\s+(\d+)\s+.*? \s+.*?(\d\d*).*?(\d\d+)'},
            'jan03dd.txt':
            {'start': '2003-01-01', 'end': '2004-04-30',
             're': f'\n(?:\x0c)?({"|".join(VarList)})\s+(\d+)\s+.*? \s+.*?(\d\d*).*?(\d\d+)'},
            'jan98dd.asc':
            {'start': '1998-01-01', 'end': '1999-10-31',
             're': 'D (\w+)\s+(\d{1,2})\s+(\d+)\s+'},
            'jan98dd2.asc':
            {'start': '1999-11-01', 'end': '2002-12-31',
             're': 'D (\w+)\s+(\d{1,2})\s+(\d+)\s+'},
            'sep95_dec97_dd.txt':
            {'start': '1995-09-01', 'end': '1997-12-31',
             're': f'\n(?:\x0c)?({"|".join(VarList)})\s+(\d+)\s+.*? \s+.*?(\d\d*).*?(\d\d+)'},
            'jun95_aug95_dd.txt':
            {'start': '1995-06-01', 'end': '1995-08-31',
             're': f'\n(?:\x0c)?({"|".join(VarList)})\s+(\d+)\s+.*? \s+.*?(\d\d*).*?(\d\d+)'},
            'apr94_may95_dd.txt':
            {'start': '1994-04-01', 'end': '1995-05-31',
             're': f'\n(?:\x0c)?({"|".join(VarList)})\s+(\d+)\s+.*? \s+.*?(\d\d*).*?(\d\d+)'},
            'jan94_mar94_dd.txt':
            {'start': '1994-01-01', 'end': '1995-03-31',
             're': f'\n(?:\x0c)?({"|".join(VarList)})\s+(\d+)\s+.*? \s+.*?(\d\d*).*?(\d\d+)'},
#            'cps89.ddf':
#            {'start': '1989-01-01', 'end': '1991-12-31',
#             're': '(\w{1,2}[\$\-%]\w*|PADDING)\s*CHARACTER\*(\d{3})\s*\.{0,1}\s*\((\d*):(\d*)\).*'},
#            'cps92.ddf':
#            {'start': '1992-01-01', 'end': '1993-12-31',
#             're': '(\w{1,2}[\$\-%]\w*|PADDING)\s*CHARACTER\*(\d{3})\s*\.{0,1}\s*\((\d*):(\d*)\).*'}
            }
             
             
StatesMap = {1: 'AL',
             30: 'MT',
             2: 'AK',
             31: 'NE',
             4: 'AZ',
             32: 'NV',
             5: 'AR',
             33: 'NH',
             6: 'CA',
             34: 'NJ',
             8: 'CO',
             35: 'NM',
             9: 'CT',
             36: 'NY',
             10: 'DE',
             37: 'NC',
             11: 'DC',
             38: 'ND',
             12: 'FL',
             39: 'OH',
             13: 'GA',
             40: 'OK',
             15: 'HI',
             41: 'OR',
             16: 'ID',
             42: 'PA',
             17: 'IL',
             44: 'RI',
             18: 'IN',
             45: 'SC',
             19: 'IA',
             46: 'SD',
             20: 'KS',
             47: 'TN',
             21: 'KY',
             48: 'TX',
             22: 'LA',
             49: 'UT',
             23: 'ME',
             50: 'VT',
             24: 'MD',
             51: 'VA',
             25: 'MA',
             53: 'WA',
             26: 'MI',
             54: 'WV',
             27: 'MN',
             55: 'WI',
             28: 'MS',
             56: 'WY',
             29: 'MO'}

RegionsMap = {'AK': 'West',
              'HI': 'West',
              'WA': 'West',
              'OR': 'West',
              'CA': 'West',
              'NV': 'West',
              'ID': 'West',
              'MT': 'West',
              'UT': 'West',
              'AZ': 'West',
              'CO': 'West',
              'WY': 'West',
              'NM': 'West',
              'ND': 'Midwest',
              'SD': 'Midwest',
              'NE': 'Midwest',
              'KS': 'Midwest',
              'MN': 'Midwest',
              'IA': 'Midwest',
              'MO': 'Midwest',
              'WI': 'Midwest',
              'IL': 'Midwest',
              'IN': 'Midwest',
              'MI': 'Midwest',
              'OH': 'Midwest',
              'TX': 'South',
              'OK': 'South',
              'AR': 'South',
              'LA': 'South',
              'MS': 'South',
              'AL': 'South',
              'TN': 'South',
              'KY': 'South',
              'WV': 'South',
              'VA': 'South',
              'MD': 'South',
              'DE': 'South',
              'DC': 'South',
              'NC': 'South',
              'SC': 'South',
              'GA': 'South',
              'FL': 'South',
              'PA': 'Northeast',
              'NJ': 'Northeast',
              'NY': 'Northeast',
              'CT': 'Northeast',
              'RI': 'Northeast',
              'MA': 'Northeast',
              'NH': 'Northeast',
              'VT': 'Northeast',
              'ME': 'Northeast'}
          
COB1994Map = {57: 'United States',
              60: 'American Samoa',
              66: 'Guam',
              72: 'Puerto Rico',
              78: 'U.S. Virgin Islands',
              96: 'No coding available/US Outlying Area',
              102: 'Austria',
              103: 'Belgium',
              105: 'Czechoslovakia',
              106: 'Denmark',
              108: 'Finland',
              109: 'France',
              110: 'Germany',
              116: 'Greece',
              117: 'Hungary',
              119: 'Ireland/Eire',
              120: 'Italy',
              126: 'Holland/Netherlands',
              127: 'Norway',
              128: 'Poland',
              129: 'Portugal',
              130: 'Azores',
              132: 'Romania',
              134: 'Spain',
              136: 'Sweden',
              137: 'Switzerland',
              138: 'Great Britain',
              139: 'England',
              140: 'Scotland',
              142: 'Northern Ireland',
              147: 'Yugoslavia',
              148: 'Europe',
              155: 'Czech Republic',
              156: 'Slovakia/Slovak Republic',
              180: 'USSR',
              183: 'Latvia',
              184: 'Lithuania',
              185: 'Armenia',
              192: 'Russia',
              195: 'Ukraine',
              200: 'Afghanistan',
              202: 'Bangladesh',
              205: 'Burma',
              206: 'Cambodia',
              207: 'China',
              209: 'Hong Kong',
              210: 'India',
              211: 'Indonesia',
              212: 'Iran',
              213: 'Iraq',
              214: 'Israel',
              215: 'Japan',
              216: 'Jordan',
              217: 'Korea/South Korea',
              218: 'Korea/ South Korea',
              221: 'Laos',
              222: 'Lebanon',
              224: 'Malaysia',
              229: 'Pakistan',
              231: 'Philippines',
              233: 'Saudi Arabia',
              234: 'Singapore',
              237: 'Syria',
              238: 'Taiwan',
              239: 'Thailand',
              240: 'Turkey',
              242: 'Vietnam',
              245: 'Asia',
              252: 'Middle East',
              253: 'Palestine',
              300: 'Bermuda',
              301: 'Canada',
              304: 'North America',
              310: 'Belize',
              311: 'Costa Rica',
              312: 'El Salvador',
              313: 'Guatemala',
              314: 'Honduras',
              315: 'Mexico',
              316: 'Nicaragua',
              317: 'Panama',
              318: 'Central America',
              333: 'Bahamas',
              334: 'Barbados',
              337: 'Cuba',
              338: 'Dominica',
              339: 'Dominican Republic',
              340: 'Grenada',
              342: 'Haiti',
              343: 'Jamaica',
              351: 'Trinidad & Tobago',
              353: 'Caribbean',
              375: 'Argentina',
              376: 'Bolivia',
              377: 'Brazil',
              378: 'Chile',
              379: 'Colombia',
              380: 'Ecuador',
              383: 'Guyana',
              385: 'Peru',
              387: 'Uruguay',
              388: 'Venezuela',
              389: 'South America',
              415: 'Egypt',
              417: 'Ethiopia',
              421: 'Ghana',
              427: 'Kenya',
              436: 'Morocco',
              440: 'Nigeria',
              449: 'South Africa',
              462: 'Other Africa',
              468: 'North Africa',
              501: 'Australia',
              507: 'Fiji',
              514: 'New Zealand',
              527: 'Pacific Islands',
              555: 'Elsewhere'}
             
COB2007Map = {57: 'United States',
              60: 'American Samoa',
              66: 'Guam',
              69: 'Northern Marianas',
              73: 'Puerto Rico',
              78: 'U.S. Virgin Islands',
              96: 'Other US Island Areas',
              100: 'Albania',
              102: 'Austria',
              103: 'Belgium',
              104: 'Bulgaria',
              105: 'Czechoslovakia',
              106: 'Denmark',
              108: 'Finland',
              109: 'France',
              110: 'Germany',
              116: 'Greece',
              117: 'Hungary',
              118: 'Iceland',
              119: 'Ireland/Eire',
              120: 'Italy',
              126: 'Netherlands',
              127: 'Norway',
              128: 'Poland',
              129: 'Portugal',
              130: 'Azores',
              132: 'Romania',
              134: 'Spain',
              136: 'Sweden',
              137: 'Switzerland',
              138: 'United Kingdom',
              139: 'England',
              140: 'Scotland',
              141: 'Wales',
              142: 'Northern Ireland',
              147: 'Yugoslavia',
              148: 'Czech Republic',
              149: 'Slovakia',
              150: 'Bosnia & Herzegovina',
              151: 'Croatia',
              152: 'Macedonia',
              154: 'Serbia',
              155: 'Estonia',
              156: 'Latvia',
              157: 'Lithuania',
              158: 'Armenia',
              159: 'Azerbaijan',
              160: 'Belarus',
              161: 'Georgia',
              162: 'Moldova',
              163: 'Russia',
              164: 'Ukraine',
              165: 'USSR',
              166: 'Europe, n.s.',
              167: 'Kosovo',
              168: 'Montenegro',
              200: 'Afghanistan',
              202: 'Bangladesh',
              203: 'Bhutan',
              205: 'Myanmar (Burma)',
              206: 'Cambodia',
              207: 'China',
              208: 'Cyprus',
              209: 'Hong Kong',
              210: 'India',
              211: 'Indonesia',
              212: 'Iran',
              213: 'Iraq',
              214: 'Israel',
              215: 'Japan',
              216: 'Jordan',
              217: 'Korea',
              218: 'Kazakhstan',
              220: 'South Korea',
              222: 'Kuwait',
              223: 'Laos',
              224: 'Lebanon',
              226: 'Malaysia',
              228: 'Mongolia',
              229: 'Nepal',
              231: 'Pakistan',
              233: 'Philippines',
              235: 'Saudi Arabia',
              236: 'Singapore',
              238: 'Sri Lanka',
              239: 'Syria',
              240: 'Taiwan',
              242: 'Thailand',
              243: 'Turkey',
              245: 'United Arab Emirates',
              246: 'Uzbekistan',
              247: 'Vietnam',
              248: 'Yemen',
              249: 'Asia, n.s.',
              252: 'Middle East',
              300: 'Bermuda',
              301: 'Canada',
              303: 'Mexico',
              310: 'Belize',
              311: 'Costa Rica',
              312: 'El Salvador',
              313: 'Guatemala',
              314: 'Honduras',
              315: 'Nicaragua',
              316: 'Panama',
              321: 'Antigua and Barbuda',
              323: 'Bahamas',
              324: 'Barbados',
              327: 'Cuba',
              328: 'Dominica',
              329: 'Dominican Republic',
              330: 'Grenada',
              332: 'Haiti',
              333: 'Jamaica',
              338: 'St. Kitts--Nevis',
              339: 'St. Lucia',
              340: 'St. Vincent and the Grenadines',
              341: 'Trinidad & Tobago',
              343: 'West Indies, n.s.',
              360: 'Argentina',
              361: 'Bolivia',
              362: 'Brazil',
              363: 'Chile',
              364: 'Colombia',
              365: 'Ecuador',
              368: 'Guyana',
              369: 'Paraguay',
              370: 'Peru',
              372: 'Uruguay',
              373: 'Venezuela',
              374: 'South America, n.s.',
              399: 'Americas, n.s.',
              400: 'Algeria',
              407: 'Cameroon',
              408: 'Cape Verde',
              412: 'Congo',
              414: 'Egypt',
              416: 'Ethiopia',
              417: 'Eritrea',
              421: 'Ghana',
              423: 'Guinea',
              425: 'Ivory Coast',
              427: 'Kenya',
              429: 'Liberia',
              430: 'Libya',
              436: 'Morocco',
              440: 'Nigeria',
              444: 'Senegal',
              447: 'Sierra Leone',
              448: 'Somolia',
              449: 'South Africa',
              451: 'Sudan',
              453: 'Tanzania',
              454: 'Togo',
              457: 'Uganda',
              459: 'Zaire',
              460: 'Zambia',
              461: 'Zimbabwe',
              462: 'Africa, n.s.',
              501: 'Australia',
              508: 'Fiji',
              511: 'Marshall Islands',
              512: 'Micronesia',
              515: 'New Zealand',
              523: 'Tonga',
              527: 'Samoa',
              528: 'Oceania, n.s.',
              555: 'Elsewhere'}
              

CodebookNotes = {'MONTH': {'Notes': 'Survey reference month.', 
                           'Name': 'Month'},
                  'YEAR': {'Notes': 'Survey reference year.', 
                          'Name': 'Year'},
                  'MIS': {'Notes': 'Household month in sample.',
                          'Name': 'Month in sample'},
                  'HHID': {'Notes': 'First part of CPS household ID.',
                          'Name': 'Household ID 1'},
                  'PULINENO': {'Notes': 'Unique line number for person.',
                          'Name': 'Person line number'},
                  'AGE': {'Notes': 'Person age, topcode varies by year, based on the original CPS data.',
                          'Name': 'Age'},
                  'HRSACTT': {'Notes': 'Actual hours worked in reference week, all jobs total.',
                          'Name': 'Actual hours worked, total'},        
                  'UNEMPDUR': {'Notes': 'Number of weeks person has been unemployed',
                          'Name': 'Unemployment Duration'},
                  'HRSUSL1': {'Notes': 'Usual hours worked at main job, per week.',
                          'Name': 'Usual hours worked, main job'},
                  'EDUC': {'Notes': 'Highest level of education attained: Advanced degree, college degree, some college but no degree or associate degree, high school degree, less than high school degree. Some assumptions are made to create this variable for pre-1992 data, using highest grade completed and highest graded attended, since the highest degree completed information is unavailable.',
                          'Name': 'Education level'},
                  'PTECON': {'Notes': 'People who want to work full-time but are not able to because of economic reasons.',
                          'Name': 'Part-time for economic reasons'},
                  'COW1': {'Notes': 'Class of worker on main job.',
                          'Name': 'Class of worker 1'},
                  'LFS': {'Notes': 'Indicates whether someone is employed, unemployed, or not in the labor force (NILF).',
                          'Name': 'Labor force status'},
                  'EMP': {'Notes': 'Indicates if someone is employed, for any hours.',
                          'Name': 'Employed'},
                  'WBHAO': {'Notes': 'Time-consistent racial/ethnic group: white non-Hispanic, black non-Hispanic, Hispanic any race, Asian non-Hispanic, or other non-Hispanic (primarily native American).',
                          'Name': 'Race/Ethnic Group'},
                  'STATE': {'Notes': 'Two letter US state code.',
                          'Name': 'State'},
                  'REGION': {'Notes': 'Census regional grouping of states.',
                          'Name': 'Region'},
                  'FEMALE': {'Notes': 'Indicates if person is identified as female.',
                          'Name': 'Female'},
                  'VETERAN': {'Notes': 'Indicates if person is a veteran.',
                              'Name': 'Veteran'},
                  'SCHENR': {'Notes': 'Indicates if person was enrolled in school during prior week.',
                              'Name': 'School enrolled'},
                  'UNEMPTYPE': {'Notes': 'Type of unemployment: job loser/on layoff, job leaver, re-entrant, or new entrant.',
                              'Name': 'Unemployment type'},
                  'FORBORN': {'Notes': 'Indicates if person is born outside the US.',
                              'Name': 'Foreign born'},
                  'NILFREASON': {'Notes': 'Primary reason person is not in the labor force.',
                              'Name': 'NILF reason'},
                  'MINWAGE': {'Notes': 'Indicates if person is paid the federal minimum wage or less.',
                              'Name': 'Minimum wage worker'},
                  'CTYBIRTH': {'Notes': 'Country of birth.',
                              'Name': 'Birth country'},
                  'HHID2': {'Notes': 'Second piece of CPS unique household identifier.',
                              'Name': 'Household ID 2'},
                  'INDGRP': {'Notes': 'Major industry group', 'Name': 'Industry Group'},
                  'MARRIED': {'Notes': 'Indicates if person is currently married.',
                          'Name': 'Married'},
                  'QSTNUM': {'Notes': 'Household number within current month.',
                              'Name': 'Unique household number'},
                  'OCCURNUM': {'Notes': 'Person number within household and current month.',
                              'Name': 'Unique person number'},
                  'CPSID': {'Notes': 'Manually created unique household ID that includes household start month and household number for start month. Can be used to match houeseholds over time. ',
                              'Name': 'Unique household ID'},
                  'PRCHLD': {'Notes': 'Age group of own children, following original CPS coding for variable of the same name.',
                              'Name': 'Own children ages'},
                  'PRNMCHLD': {'Notes': 'Number of own children',
                              'Name': 'Number of own children'},
                  'WBHAOM': {'Notes': 'Racial/ethnic group with separate group for persons of more than one race.',
                              'Name': 'Race/ethnic group'},
                  'PRDTRACE': {'Notes': 'Original CPS definitions for race or combination of races', 'Name': 'Race/ethnicity'},
                  'HRSUSL2': {'Notes': 'Number of hours usually worked, per week, at second job', 'Name': 'Usual hours, job 2'},
                  'HRSUSLT': {'Notes': 'Number of hours usually worked, per week, total', 'Name': 'Usual hours, total'},
                  'HRSACT1': {'Notes': 'Number of hours actually worked last week, main job', 'Name': 'Actual hours, main job'},
                  'HRSACT2': {'Notes': 'Number of hours actually worked last week, second job', 'Name': 'Actual hours, job 2'},
                  'PEIO1ICD': {'Notes': 'Industry code for main job', 'Name': 'Industry, main job'},
                  'IND': {'Notes': 'Industry code for main job', 'Name': 'Industry, main job'},
                  'OCC': {'Notes': 'Occupation code for main job', 'Name': 'Occupation, main job'},
                  'PEIO1OCD': {'Notes': 'Occupation code for main job', 'Name': 'Occupation, main job'},
                  'PRDTIND1': {'Notes': 'Detailed industry recode, main job', 'Name': 'Industry, main job'},
                  'PRDTOCC1': {'Notes': 'Detailed occupation recode, main job', 'Name': 'Occupation, main job'},
                  'PRMJIND1': {'Notes': 'Major industry recode, main job', 'Name': 'Industry, main job'},
                  'PRMJOCC1': {'Notes': 'Major occupation recode, main job', 'Name': 'Occupation, main job'},
                  'IND': {'Notes': 'Industry code, main job', 'Name': 'Industry, main job'},
                  'IND2': {'Notes': 'Industry code, second job', 'Name': 'Industry, job 2'},
                  'INDD': {'Notes': 'Detailed industry recode, main job', 'Name': 'Detailed industry, main job'},
                  'IND2D': {'Notes': 'Detailed industry recode, second job', 'Name': 'Detailed industry, second job'},
                  'INDM': {'Notes': 'Major industry recode, main job', 'Name': 'Major industry, main job'},
                  'IND2M': {'Notes': 'Major industry recode, second job', 'Name': 'Major industry, second job'},
                  'OCC': {'Notes': 'Occupation code, main job', 'Name': 'Occupation, main job'},
                  'OCC2': {'Notes': 'Occupation code, second job', 'Name': 'Occupation, second job'},
                  'OCCD': {'Notes': 'Detailed occupation recode, main job', 'Name': 'Detailed occupation, main job'},
                  'OCC2D': {'Notes': 'Detailed occupation recode, second job', 'Name': 'Detailed occupation, job 2'},
                  'OCCM': {'Notes': 'Major occupation recode, main job', 'Name': 'Major occupation, main job'},
                  'OCC2M': {'Notes': 'Major occupation recode, second job', 'Name': 'Major occupation, job 2'},
                  'IND80': {'Notes': 'Industry code, main job, 1980 basis', 'Name': 'Industry, main job'},
                  'IND280': {'Notes': 'Industry code, second job, 1980 basis', 'Name': 'Industry, job 2'},
                  'IND80D': {'Notes': 'Detailed industry recode, main job, 1980 basis', 'Name': 'Detailed industry, main job'},
                  'IND280D': {'Notes': 'Detailed industry recode, second job, 1980 basis', 'Name': 'Detailed industry, second job'},
                  'IND80M': {'Notes': 'Major industry recode, main job, 1980 basis', 'Name': 'Major industry, main job'},
                  'IND280M': {'Notes': 'Major industry recode, second job, 1980 basis', 'Name': 'Major industry, second job'},
                  'OCC80': {'Notes': 'Occupation code, main job, 1980 basis', 'Name': 'Occupation, main job'},
                  'OCC280': {'Notes': 'Occupation code, second job, 1980 basis', 'Name': 'Occupation, second job'},
                  'OCC80D': {'Notes': 'Detailed occupation recode, main job, 1980 basis', 'Name': 'Detailed occupation, main job'},
                  'OCC280D': {'Notes': 'Detailed occupation recode, second job, 1980 basis', 'Name': 'Detailed occupation, job 2'},
                  'OCC80M': {'Notes': 'Major occupation recode, main job, 1980 basis', 'Name': 'Major occupation, main job'},
                  'OCC280M': {'Notes': 'Major occupation recode, second job, 1980 basis', 'Name': 'Major occupation, job 2'},
                  'PWLGWGT': {'Notes': 'Weights for matching month to month CPS observations', 'Name': 'Longitudinal weight'},
                  'PWSSWGT': {'Notes': 'Person weight, including children', 'Name': 'Person weight'},
                  'CBSA': {'Notes': 'Similar to metro area.',
                              'Name': 'Center-based statistical area'},
                  'CSA': {'Notes': 'Grouping of nearby metro areas.',
                              'Name': 'Consolidated statistical area'},
                  'COUNTY': {'Notes': 'U.S. county code, derived from GECO and GTCO', 'Name': 'County'},
                  'MSA': {'Notes': 'Metropolitan Statistical Area (MSA) code', 'Name': 'MSA code'},
                  'CMSA': {'Notes': 'Combined Metropolitan Statistical Area (MSA) code', 'Name': 'CMSA code'},
                  'DISABILITY': {'Notes': 'Indicates if person is has any of six disabilities: difficulty hearing, difficulty seeing even with glasses, difficulty remembering or making decisions, difficulty walking or climbing stairs, difficulty dressing or bathing, or difficulty doing errands alone.',
                              'Name': 'Disability'},
                  'CERT': {'Notes': 'Indicates if a person has a professional certification or license.',
                              'Name': 'Professional certification'},
                  'WORKFT': {'Notes': 'Indicates if person worked full-time (35 hours or more) in the reference week.',
                          'Name': 'Education level'},
                  'UNION': {'Notes': 'Indicates if person is covered by a union contract or similar collective bargaining agreement.',
                          'Name': 'Union'},
                  'UNIONMEM': {'Notes': 'Indicates if person is a member of a union or similar employee association.',
                          'Name': 'Union member'},
                  'PAIDHRLY': {'Notes': 'Indicates whether person is usually paid on a per-hour basis.',
                          'Name': 'Paid hourly'},
                  'WKWAGE': {'Notes': 'Nominal weekly earnings, in USD.',
                          'Name': 'Weekly wage'},
                  'HRWAGE': {'Notes': 'Nominal hourly earnings, in USD.',
                          'Name': 'Hourly wage'},
                  'RWKWAGE': {'Notes': 'Real weekly earnings, in USD, adjusted for inflation by regional CPI-U.',
                          'Name': 'Real weekly wage'},
                  'RHRWAGE': {'Notes': 'Real hourly earnings, in USD, adjusted for inflation by regional CPI-U.',
                          'Name': 'Real hourly wage'},
                  'BASICWGT': {'Notes': 'Basic person weight, equal to the composite weight where available.',
                          'Name': 'Basic weight'},
                  'PWORWGT': {'Notes': 'Person weight for outgoing rotation group variables, such as wage or hours or union membership.',
                          'Name': 'Female'},
                  'PROXY': {'Notes': 'Identifies whether labor force information was collected by self or by proxy response.', 'Name': 'Proxy response'},
                  'MJH': {'Notes': 'Indicates if person has more than one job.',
                          'Name': 'Multiple jobholder'}}
                        
