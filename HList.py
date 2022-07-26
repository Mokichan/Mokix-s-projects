hl = [548, 549, 550, 551, 552, 553, 554, 555]

hc = hl.index(min(hl))
hb = hl.index(max(hl))

hl[hb],hl[hc] = hl[hc],hl[hb]

print(hl)

