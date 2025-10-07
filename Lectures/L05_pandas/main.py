import pandas as pd

data_url = 'https://blog.kakaocdn.net/dna/bBaIM3/btsGBsBNUDl/AAAAAAAAAAAAAAAAAAAAAGUZdUlo0x_MIQi75zRxx8g-pz67fyJevwp_pnYLA1kp/boston.csv?credential=yqXZFxpELC7KVnFOS48ylbz2pIh7yKj8&expires=1759244399&allow_ip=&allow_referer=&signature=YTGYti%2BLCXY1dqlMwxqVuus35H0%3D&attach=1&knm=tfile.csv'

df = pd.read_csv(
    data_url,
    skiprows=0,
    header=0,
    sep='.'
)

print(df)
