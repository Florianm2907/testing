import bz2

file_name = "F:/FESTPLATTE H/test1/test.txt"
with open(file_name, "rb") as file:
    compressed_data = file.read()
decompressed_data = bz2.decompress(compressed_data)

print(decompressed_data.decode("utf-8"))
