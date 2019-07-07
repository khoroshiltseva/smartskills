def SynchronizingTables(N, ids, salary):
    ids_sorted = sorted(ids)

    salary_sorted = sorted(salary)

    salary_new = []

    for i in range(N):
        j = ids_sorted.index(ids[i])
        salary_new.append(salary_sorted[j])

    return salary_new
