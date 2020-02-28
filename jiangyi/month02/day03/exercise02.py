def copy(file1, file2):
    f1 = open(file1, 'rb')
    f2 = open(file2, 'wb')

    while True:
        data = f1.read(1024)
        if not data:
            break
        f2.write(data)

    f1.close()
    f2.close()


copy('justin.jpg', 'j.jpg')
