class Solution:
def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
    '''
    Need to track what job is current running
    And know the next job when the current one finishes running
    Naturally would lead to stack
    '''
    def convert(x, y, z):
        return int(x), y, int(z)
    ret = [0] * n
    stack = []
    current = last = None
    for log in logs:
        current, last = convert(*log.split(":")), current
        if len(stack):
            ret[stack[-1]] += current[2] - last[2] - 1 + (0,1)[current[1] == 'end'] + (0,1)[last[1] == 'start']
        if current[1] == 'start':
            stack.append(current[0])
        else:
            stack.pop()
    return ret
    '''
    cleaner version
    '''
    ret = [0] * n
    stack = []
    prev_time = 0
    for log in logs:
        jobId, op, time = log.split(":")
        jobId, time = int(jobId), int(time)
        if len(stack):
            ret[stack[-1]] += time - prev_time - 1 + (0,1)[op == 'end']
        if op == 'start':
            stack.append(jobId)
            prev_time = time - 1
        else:
            stack.pop()
            prev_time = time
    return ret
