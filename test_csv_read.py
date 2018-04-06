def test_csv_read():
    import csv_read
    expectedResult = {'Hello': 'bonjour', 'Welcome': 'bienvenue'}
    data = csv_read.readcsv('test_csv.csv')
    for row in data:
        assert expectedResult[row['English']] == row['French']
