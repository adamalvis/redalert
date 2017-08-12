
priority_triggers = [
    'red',
    'hot',
    'urgent',
]


def is_high_priority(subject):
    priority = False
    for trigger in priority_triggers:
        if trigger in subject.lower():
            priority = True
    return priority
