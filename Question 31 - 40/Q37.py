dictionary = {
    'Student': ['S1','S2','S3','S4'],
    'Physics': [78,45,56,32],
    'Chemistry': [45,12,56,98],
    'Mathematics':[88,98,100,45]
}

m_total = 0

for values in list(dictionary.values())[1:]:
    if max(values)>m_total:
        m_total = max(values)

print(m_total)