class Solution:
  def mostPoints(self, questions: list[list[int]]) -> int:
    n = len(questions)
    
    dp = [0] * (n + 1)

    for i in reversed(range(n)):
      points, brainpower = questions[i]
      nextIndex = i + brainpower + 1
      nextPoints = dp[nextIndex] if nextIndex < n else 0
      dp[i] = max(points + nextPoints, dp[i + 1])

    return dp[0]
