def test_csv_read():
    import csv_read
    expectedResult = {'Hello': '你好', 'Welcome': '欢迎'}
    data = csv_read.readcsv('test_csv.csv')
    for row in data:
        assert expectedResult[row['English']] == row['中文']
