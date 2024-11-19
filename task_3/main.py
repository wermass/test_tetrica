def get_intersection(interval1, interval2):
    """Возвращает пересечение двух интервалов"""
    start = max(interval1[0], interval2[0])
    end = min(interval1[1], interval2[1])
    return (start, end) if start < end else None


def merge_intervals(intervals):
    """Объединяет пересекающиеся интервалы"""
    if not intervals:
        return []

    intervals.sort()
    merged = [intervals[0]]

    for current in intervals[1:]:
        last = merged[-1]
        if current[0] <= last[1]:
            merged[-1] = (last[0], max(last[1], current[1]))
        else:
            merged.append(current)

    return merged


def calculate_overlap(intervals1, intervals2):
    """Вычисляет общее время пересечения двух списков интервалов"""
    result = []
    for interval1 in intervals1:
        for interval2 in intervals2:
            intersection = get_intersection(interval1, interval2)
            if intersection:
                result.append(intersection)
    return merge_intervals(result)


def appearance(intervals: dict[str, list[int]]) -> int:
    lesson_interval = [(intervals['lesson'][0], intervals['lesson'][1])]

    pupil_intervals = [(intervals['pupil'][i], intervals['pupil'][i + 1])
                       for i in range(0, len(intervals['pupil']), 2)]
    tutor_intervals = [(intervals['tutor'][i], intervals['tutor'][i + 1])
                       for i in range(0, len(intervals['tutor']), 2)]

    pupil_with_lesson = calculate_overlap(pupil_intervals, lesson_interval)
    tutor_with_lesson = calculate_overlap(tutor_intervals, lesson_interval)

    common_intervals = calculate_overlap(pupil_with_lesson, tutor_with_lesson)

    return sum(end - start for start, end in common_intervals)


tests = [
    {'intervals': {'lesson': [1594663200, 1594666800],
                   'pupil': [1594663340, 1594663389, 1594663390, 1594663395, 1594663396, 1594666472],
                   'tutor': [1594663290, 1594663430, 1594663443, 1594666473]},
     'answer': 3117
     },
    {'intervals': {'lesson': [1594702800, 1594706400],
                   'pupil': [1594702789, 1594704500, 1594702807, 1594704542, 1594704512, 1594704513, 1594704564,
                             1594705150, 1594704581, 1594704582, 1594704734, 1594705009, 1594705095, 1594705096,
                             1594705106, 1594706480, 1594705158, 1594705773, 1594705849, 1594706480, 1594706500,
                             1594706875, 1594706502, 1594706503, 1594706524, 1594706524, 1594706579, 1594706641],
                   'tutor': [1594700035, 1594700364, 1594702749, 1594705148, 1594705149, 1594706463]},
     'answer': 3577
     },
    {'intervals': {'lesson': [1594692000, 1594695600],
                   'pupil': [1594692033, 1594696347],
                   'tutor': [1594692017, 1594692066, 1594692068, 1594696341]},
     'answer': 3565
     },
]

if __name__ == '__main__':
    for i, test in enumerate(tests):
        test_answer = appearance(test['intervals'])
        assert test_answer == test['answer'], f'Ошибка в тесте {i}: получено {test_answer}, ожидалось {test["answer"]}'
    print("Все тесты успешно пройдены!")
