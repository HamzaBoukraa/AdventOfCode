from aocd import get_data
import os

year = '2022'
day = '19'

input_directory_folder_path = '..\input'
input_file_path = '{0}\AOC{1}D{2}_input.txt'.format(input_directory_folder_path,year, day)

if not os.path.exists(input_directory_folder_path):
    os.makedirs(input_directory_folder_path)

if not os.path.exists(input_file_path):
    data = get_data(year=int(year),day=int(day))
    
    with open(input_file_path, 'w') as writer:
        writer.write(data)

# Get Puzzle Input
with open(input_file_path, 'r') as reader:
    puzzle_input =  [puzzle_line for puzzle_line in reader.read().split('\n')]

# Part 1 :
blueprints = []
for input_line in puzzle_input:
    line_components = input_line.split(' ')
    blueprint = [int(line_components[1].removesuffix(':')), int(line_components[6]), int(line_components[12]), int(line_components[18]), int(line_components[21]), int(line_components[27]), int(line_components[30])]
    blueprints += [blueprint]

for i in range(len(blueprints)):
    blueprint = blueprints[i]
    print("Blueprint", blueprint)
    minutes = 1
    ores = 0
    ore_robots = 1
    ore_robot_building = False
    clays = 0
    clay_robots = 0
    clay_robot_building = False
    obsidians = 0
    obsidian_robots = 0
    obsidian_robot_building = False
    geodes = 0
    geode_robots = 0
    geode_robot_building = False
    while minutes < 25:
        print("\nMinute", minutes)
        if ores >= blueprint[5] and obsidians >= blueprint[6]:
            ores -= blueprint[5]
            obsidians -= blueprint[6]
            print("Spend", blueprint[5], "ore and", blueprint[6], "obsidian to start building a geode-cracking robot.")
            geode_robot_building = True
        elif (ores >= (blueprint[5]-ore_robots)) and (obsidians >= (blueprint[6]-obsidian_robots)):
            pass
        elif ores >= blueprint[3] and clays >= blueprint[4]:
            ores -= blueprint[3]
            clays -= blueprint[4]
            print("Spend", blueprint[3], "ore and", blueprint[4], "clay to start building a obsidian-collecting robot.")
            obsidian_robot_building = True
        elif (ores >= (blueprint[3]-ore_robots)) and (clays >= (blueprint[4]-clay_robots)):
            pass
        elif ores >= blueprint[2]:
            ores -= blueprint[2]
            print("Spend", blueprint[2], "ore to start building a clay-collecting robot.")
            clay_robot_building = True
        elif ores >= blueprint[2]-ore_robots:
            pass
        elif ores >= blueprint[1]:
            ores -= blueprint[1]
            print("Spend", blueprint[1], "ore to start building a ore-collecting robot.")
            ore_robot_building = True
        
        if ore_robots > 0:
            ores += ore_robots
            print(ore_robots, "ore-collecting robot collects", ore_robots, "ore; you now have", ores, "ore.")
        if clay_robots > 0:
            clays += clay_robots
            print(clay_robots, "clay-collecting robot collects", clay_robots, "clay; you now have", clays, "clay.")
        if obsidian_robots > 0:
            obsidians += obsidian_robots
            print(obsidian_robots, "obsidian-collecting robot collects", obsidian_robots, "obsidian; you now have", obsidians, "obsidian.")
        if geode_robots > 0:
            geodes += geode_robots
            print(geode_robots, "geode-collecting robot collects", geode_robots, "geode; you now have", geodes, "open geode.")

        if ore_robot_building:
            ore_robot_building = False
            ore_robots += 1
            print("The new ore-collecting robot is ready; you now have", ore_robots, "of them.")
        if clay_robot_building:
            clay_robot_building = False
            clay_robots += 1
            print("The new clay-collecting robot is ready; you now have", clay_robots, "of them.")
        if obsidian_robot_building:
            obsidian_robot_building = False
            obsidian_robots += 1
            print("The new obsidian-collecting robot is ready; you now have", obsidian_robots, "of them.")
        if geode_robot_building:
            geode_robot_building = False
            geode_robots += 1
            print("The new geode-collecting robot is ready; you now have", geode_robots, "of them.")
        minutes += 1

print('{0}{1} - Part 1 answer : {2}'.format(year, day, 0))

# Part 2 :
print('{0}{1} - Part 2 answer : {2}'.format(year, day, 0))