f = open("12.gfx",'rb').read()

for i in range(5):
    open('12_%d.jpg' %i, 'wb').write(f[i::5])
