import zlib
with open('29.zlib', 'rb') as f_in:
    compressed_data = f_in.read()
decompressed_data = zlib.decompress(compressed_data)
with open('decompressed.data', 'wb') as f_out:
    f_out.write(decompressed_data)