import  struct

st=struct.Struct("i5sif")

data=st.pack(1,b'lili',170,99.5)
print(data)

data=st.unpack(data)
print(data)
print(data[1].decode().strip("\x00"))