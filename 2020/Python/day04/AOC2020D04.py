with open('day4_input.txt', 'r') as reader:
    passports = [passport for passport in [{key: value for key, value in [field.split(':') for field in line.strip().replace('\n', ' ').split(' ')]} for line in reader.read().split('\n\n')]]

# Part 1 :
valid_passports = [passport for passport in passports if len(passport) == 8 or (len(passport) == 7 and not 'cid' in passport)]

print('Valid passport (part 1):', len(valid_passports))

# Part 2 :
import re
regex_hcl = re.compile(r'#[a-f0-9]{6}\Z')
regex_pid = re.compile(r'[0-9]{9}\Z')

valid_passports = [passport for passport in valid_passports if int(passport['byr']) >= 1920 and int(passport['byr']) <= 2002 and int(passport['iyr']) >= 2010 and int(passport['iyr']) <= 2020 and int(passport['eyr']) >= 2020 and int(passport['eyr']) <= 2030 and ((passport['hgt'][-2:] == 'cm' and int(passport['hgt'][:-2]) >= 150 and int(passport['hgt'][:-2]) <= 193) or (passport['hgt'][-2:] == 'in' and int(passport['hgt'][:-2]) >= 59 and int(passport['hgt'][:-2]) <= 76)) and regex_hcl.match(passport['hcl']) and passport['ecl'] in ['amb','blu','brn','gry','grn','hzl','oth'] and regex_pid.match(passport['pid'])]

print('Valid passport (part 2):', len(valid_passports))
