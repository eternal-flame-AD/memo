import os,sys  


parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  
sys.path.insert(0,parentdir) 
def test_csv_read():
    import csv_read
    expectedResult = {'Hello': 'bonjour', 'Welcome': 'bienvenue'}
    data = csv_read.readcsv('tests/test_csv.csv')
    for row in data:
        assert expectedResult[row['English']] == row['French']
