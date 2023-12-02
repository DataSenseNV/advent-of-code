
# Day 2 - Advent of Code 2023
# https://adventofcode.com/2023/day/2

def part1():
     with open('input.txt') as file :
        lines = file.readlines()
        sum_ids = 0
        for line in lines:
            line = line.replace('\n', '')
            parts = line.split(':')
            game_part = parts[1]
            game_id = parts[0].split(' ')[1]
            done_game = False


            for single_game in game_part.split(';'):
                #print('single_game: ', single_game)
                mapped = {'blue': 0, 'green': 0, 'red': 0}

                for part in single_game.split(','):
                    ps = part.split(' ')
                    amount = ps[1]
                    color = ps[2]
                    #print(color, amount, ps)
                    mapped[color] = int(amount)
                

                if mapped['red'] > 12 or mapped['green'] > 13 or mapped['blue'] > 14:
                    done_game = True
                    break

            
            if not done_game:
                sum_ids += int(game_id)

                
                

            
        print(sum_ids)

def part2():
     with open('input.txt') as file :
        lines = file.readlines()
        sum_prods = 0
        for line in lines:
            line = line.replace('\n', '')
            parts = line.split(':')
            game_part = parts[1]
            minimal_map = {'blue': 1, 'green': 1, 'red': 1}

            for single_game in game_part.split(';'):
                #print('single_game: ', single_game)
                mapped = {'blue': 1, 'green': 1, 'red': 1}

                for part in single_game.split(','):
                    ps = part.split(' ')
                    amount = ps[1]
                    color = ps[2]
                    #print(color, amount, ps)
                    mapped[color] = int(amount)
                
                for key in mapped.keys():
                    if mapped[key] > minimal_map[key]:
                        minimal_map[key] = mapped[key]

            prod = 1
            for key in minimal_map.keys():                
                prod *= minimal_map[key] 
            
            sum_prods += prod
    
        print(sum_prods)
        
            

if __name__ == "__main__":
   part2()