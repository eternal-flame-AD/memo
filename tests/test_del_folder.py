import os


def test_del_folder():
    os.mkdir('./testdir')
    from del_folder import delete_file_folder
    f = open('./testdir/1.txt', mode='w')
    f.write('something')
    f.close()
    os.mkdir('./testdir/testsubfolder')
    delete_file_folder('./testdir')
    assert not os.path.exists('./testdir')
