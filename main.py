def solve(pairs):
    day_beginning = min(pairs)[0]
    day_ending = max([i[1] for i in pairs])

    timeline = dict().fromkeys(range(day_beginning, day_ending+1), 0)

    for pair in pairs:
        meeting_start = pair[0]
        meeting_end = pair[1]

        timeline[meeting_start] += 1

        timeline[meeting_end] -= 1

    sessions_in_progress = 0
    sessions_schedule = []
    start = end = 0
    in_progress = False

    for (key, value) in timeline.items():

        sessions_in_progress += value

        if sessions_in_progress and not in_progress:
            start = key
            in_progress = True

        if not sessions_in_progress and in_progress:
            end = key
            in_progress = False
            session = (start, end)
            sessions_schedule.append(session)

    return sessions_schedule


if __name__ == "__main__":
    k = int(input())
    pairs = []
    for i in range(k):
        pair = [int(i) for i in input().split(" ")]
        pairs.append(pair)

    print(solve(pairs))