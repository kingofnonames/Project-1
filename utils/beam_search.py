from collections import defaultdict
from tqdm import tqdm
import re
import string
def beam_search(obs, states, start_prob, trans_prob, emit_prob, beam_width = 5):
  T = len(obs)
  dp = [{} for _ in range(T)]
  path = {}

  for state in states.get(obs[0], [obs[0]]):
    dp[0][state] = start_prob.get(state, 1e-6) * emit_prob.get(state, {}).get(obs[0], 1e-6)
    path[state] = [state]

  for t in range(1, T):
    new_path = {}

    candidates = []
    for current_state in states.get(obs[t], [obs[t]]):
      for prev_state in dp[t - 1]:
        prob = dp[t - 1][prev_state] * trans_prob.get(prev_state, {}).get(current_state, 1e-6) * emit_prob.get(current_state, {}).get(obs[t], 1e-6)
        candidates.append((prob, prev_state, current_state))

    candidates.sort(reverse=True, key=lambda x: x[0])
    candidates = candidates[:beam_width]
    for prob, prev_state, current_state in candidates:
      dp[t][current_state] = prob
      if current_state not in new_path:
        new_path[current_state] = path[prev_state] + [current_state]
    path = new_path
  (prob, best_final_state) = max((dp[T - 1][state], state) for state in dp[T - 1])
  return path[best_final_state]