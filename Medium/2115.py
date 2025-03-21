from collections import defaultdict, Counter, deque

class Solution:
    def findAllRecipes(self, recipes: list[str], ingredients: list[list[str]], supplies: list[str]) -> list[str]:
        result = []
        supplies = set(supplies)
        graph = defaultdict(list)
        indegree = Counter()
        queue = deque()

        for i, recipe in enumerate(recipes):
            for item in ingredients[i]:
                if item not in supplies:
                    graph[item].append(recipe)
                    indegree[recipe] += 1

        for recipe in recipes:
            if indegree[recipe] == 0:
                queue.append(recipe)

        while queue:
            current = queue.popleft()
            result.append(current)
            for next_recipe in graph[current]:
                indegree[next_recipe] -= 1
                if indegree[next_recipe] == 0:
                    queue.append(next_recipe)

        return result
