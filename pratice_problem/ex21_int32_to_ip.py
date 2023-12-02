def int32_to_ip(int32):
    return "{}.{}.{}.{}".format(int32 >> 24,int32 >> 16 & 255,int32 >> 8 & 255,int32 & 255)

print(int32_to_ip(2154959208))