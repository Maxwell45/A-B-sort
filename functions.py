def id_start_at_zero(n_customers):
    return id_start_at_n(n_customers, 0)


def id_start_at_n(n_customers, n_first_id):
    group_distribution = {}
    for i in range(n_first_id, n_first_id + n_customers):
        group = find_sum_of_digits(i)
        if not group_distribution.get(group):
            group_distribution[group] = 1
            continue
        group_distribution[find_sum_of_digits(i)] += 1
    return group_distribution


def find_sum_of_digits(number):
    digit_sum = 0
    while number > 0:
        digit_sum += number % 10
        number = int(number / 10)
    return digit_sum
