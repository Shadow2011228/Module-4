dataset = [-868, 934, 661, 541, 709, -277, 142, 493, 286, 733, -229, 79]

def choice_sort(dataset):
    N = len(dataset)
    for a in range(N - 1):
        m = dataset[a]
        p = a
        for b in range(a + 1, N):
            if m > dataset[b]:
                m = dataset[b]
                p = b
        if p != a:
            t = dataset[a]
            dataset[a] = dataset[p]
            dataset[p] = t
    return dataset

print(choice_sort(dataset))