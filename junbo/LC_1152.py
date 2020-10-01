class Solution:
  def mostVisitedPattern(self, username: List[str], timestamp: List[int], website: List[str]) -> List[str]:
      d = collections.defaultdict(list)
      for n, t, w in zip(username, timestamp, website):
          d[n].append((t, w))
      d = {k:list(zip(*sorted(v,key=lambda x:x[0])))[1] for k,v in d.items()}
      
      count = collections.defaultdict(set)
      for k, v in d.items():
          for webs in itertools.combinations(v, 3):
              count['-'.join(webs)].add(k)

      return min(count.items(), key=lambda x :(-len(x[1]), x[0]))[0].split('-')
      
      
      '''
      more convice version:
      1) python can sort list of list by compare each element from left to right of element list
      2) Counter() + Counter()
      3) tuple is hashable
      '''
      d = collections.defaultdict(list)
      for t, w, n in sorted(zip(timestamp, website, username)):
          d[n].append(w)
      count = sum([collections.Counter(set(itertools.combinations(d[n], 3))) for n in d], collections.Counter())
      return list(min(count, key=lambda k: (-count[k], k)))

