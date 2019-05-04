from noaa_sdk import noaa
n = noaa.NOAA()
observations = n.get_observations('11365', 'US', start='2017-01-01', end='2018-02-02')
for observation in observations:
    print(observation)
    break
