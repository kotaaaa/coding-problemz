# N = int(input())
# A = list(map(int, input().split()))
# B = list(map(int, input().split()))


# class Game:
#     def __init__(self, enemies: list[int], heroes: list[int]):
#         self.enemies = enemies
#         self.heroes = heroes

#     def combat_in_town_i(self, town_id: int) -> int:
#         if self.heroes[town_id] <= self.enemies[town_id]:
#             self.enemies[town_id] -= self.heroes[town_id]
#             result = self.heroes[town_id]
#             self.heroes[town_id] = 0
#             next_result = 0
#         else:
#             # In town i
#             result = self.enemies[town_id]
#             self.heroes[town_id] -= result

#             # In town i + 1
#             if self.heroes[town_id] >= self.enemies[town_id + 1]:
#                 next_result = self.enemies[town_id + 1]
#                 self.enemies[town_id + 1] -= next_result
#                 self.heroes[town_id] -= next_result
#             else:
#                 next_result = self.heroes[town_id]
#                 self.enemies[town_id + 1] -= next_result
#                 self.heroes[town_id] -= next_result

#         result += next_result
#         return result


# def main():
#     combat_result = 0
#     game = Game(A, B)
#     for i, _ in enumerate(B):
#         combat_result += game.combat_in_town_i(i)
#     print(combat_result)



