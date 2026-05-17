data = np.load('fig3_part1.npz', allow_pickle=True)
z200_ee   = data['z200_ee']
z200_ee_p = data['z200_ee_p']
u200_ee   = data['u200_ee']
v200_ee   = data['v200_ee']

z200_ca   = data['z200_ca']
z200_ca_p = data['z200_ca_p']
u200_ca   = data['u200_ca']
v200_ca   = data['v200_ca']

z200_ea   = data['z200_ea']
z200_ea_p = data['z200_ea_p']
u200_ea   = data['u200_ea']
v200_ea   = data['v200_ea']

z200_wn   = data['z200_wn']
z200_wn_p = data['z200_wn_p']
u200_wn   = data['u200_wn']
v200_wn   = data['v200_wn']

z200_cn   = data['z200_cn']
z200_cn_p = data['z200_cn_p']
u200_cn   = data['u200_cn']
v200_cn   = data['v200_cn']

lon = data['lon']
lat = data['lat']

fig3 = plt.figure(figsize=(12,8))

f3_ax1 = fig3.add_axes([0.1, 0.1, 0.6, 0.6],projection = ccrs.PlateCarree(central_longitude=180))
leftlon, rightlon, lowerlat, upperlat = (0,60,20,80)
img_extent = [leftlon, rightlon, lowerlat, upperlat]
contour_map(f3_ax1,img_extent,20,20)
c7 = f3_ax1.contourf(lon,lat,z200_ee,levels=np.arange(-0.8,0.88,0.08),extend='both',
                   cmap=cmaps.cmp_b2r,transform=ccrs.PlateCarree())
c1b = f3_ax1.contourf(lon,lat,z200_ee_p, [0,0.05,1], zorder=1,
                      hatches=['//', None],colors="none", transform=ccrs.PlateCarree())
c1c = f3_ax1.quiver(lon[::10],lat[::10],
                    u200_ee[::10,::10],v200_ee[::10,::10],
                    color='k',width=0.005, transform=ccrs.PlateCarree(),scale=8)
f3_ax1.tick_params(axis='x', labelsize=28)
f3_ax1.tick_params(axis='y', labelsize=28)
f3_ax1.set_title('a. EE', loc='left', fontsize=32)

f3_ax1 = fig3.add_axes([0.1+0.52*1, 0.1, 0.6, 0.6],projection = ccrs.PlateCarree(central_longitude=180))
leftlon, rightlon, lowerlat, upperlat = (30,90,20,80)
img_extent = [leftlon, rightlon, lowerlat, upperlat]
contour_map(f3_ax1,img_extent,20,20)
c7 = f3_ax1.contourf(lon,lat,z200_ca,levels=np.arange(-0.8,0.88,0.08),extend='both',
                   cmap=cmaps.cmp_b2r,transform=ccrs.PlateCarree())
c1b = f3_ax1.contourf(lon,lat,z200_ca_p, [0,0.05,1], zorder=1,
                      hatches=['//', None],colors="none", transform=ccrs.PlateCarree())
c1c = f3_ax1.quiver(lon[::10],lat[::10],
                    u200_ca[::10,::10],v200_ca[::10,::10],
                    color='k',width=0.005, transform=ccrs.PlateCarree(),scale=8)

f3_ax1.tick_params(axis='x', labelsize=28)
f3_ax1.tick_params(axis='y', labelsize=0)
f3_ax1.set_title('b. CA', loc='left', fontsize=32)

f3_ax1 = fig3.add_axes([0.1+0.52*2, 0.1, 0.6, 0.6],projection = ccrs.PlateCarree(central_longitude=180))
leftlon, rightlon, lowerlat, upperlat = (70,130,20,80)
img_extent = [leftlon, rightlon, lowerlat, upperlat]
contour_map(f3_ax1,img_extent,20,20)
c7 = f3_ax1.contourf(lon,lat,z200_ea,levels=np.arange(-0.8,0.88,0.08),extend='both',
                   cmap=cmaps.cmp_b2r,transform=ccrs.PlateCarree())
c1b = f3_ax1.contourf(lon,lat,z200_ea_p, [0,0.05,1], zorder=1,
                      hatches=['//', None],colors="none", transform=ccrs.PlateCarree())
c1c = f3_ax1.quiver(lon[::10],lat[::10],
                    u200_ea[::10,::10],v200_ea[::10,::10],
                    color='k',width=0.005, transform=ccrs.PlateCarree(),scale=8)

f3_ax1.tick_params(axis='x', labelsize=28)
f3_ax1.tick_params(axis='y', labelsize=0)
f3_ax1.set_title('c. EA', loc='left', fontsize=32)

f3_ax1 = fig3.add_axes([0.1+0.52*3, 0.1, 0.6, 0.6],projection = ccrs.PlateCarree(central_longitude=180))
leftlon, rightlon, lowerlat, upperlat = (190,250,20,80)
img_extent = [leftlon, rightlon, lowerlat, upperlat]
contour_map(f3_ax1,img_extent,20,20)
c7 = f3_ax1.contourf(lon,lat,z200_wn,levels=np.arange(-0.8,0.88,0.08),extend='both',
                   cmap=cmaps.cmp_b2r,transform=ccrs.PlateCarree())
c1b = f3_ax1.contourf(lon,lat,z200_wn_p, [0,0.05,1], zorder=1,
                      hatches=['//', None],colors="none", transform=ccrs.PlateCarree())
c1c = f3_ax1.quiver(lon[::10],lat[::10],
                    u200_wn[::10,::10],v200_wn[::10,::10],
                    color='k',width=0.005, transform=ccrs.PlateCarree(),scale=8)

f3_ax1.tick_params(axis='x', labelsize=28)
f3_ax1.tick_params(axis='y', labelsize=0)
f3_ax1.set_title('d. WN', loc='left', fontsize=32)


f3_ax1 = fig3.add_axes([0.1+0.52*4, 0.1, 0.6, 0.6],projection = ccrs.PlateCarree(central_longitude=180))
leftlon, rightlon, lowerlat, upperlat = (220,280,20,80)
img_extent = [leftlon, rightlon, lowerlat, upperlat]
contour_map(f3_ax1,img_extent,20,20)
c7 = f3_ax1.contourf(lon,lat,z200_cn,levels=np.arange(-0.8,0.88,0.08),extend='both',
                   cmap=cmaps.cmp_b2r,transform=ccrs.PlateCarree())
c1b = f3_ax1.contourf(lon,lat,z200_cn_p, [0,0.05,1], zorder=1,
                      hatches=['//', None],colors="none", transform=ccrs.PlateCarree())
c1c = f3_ax1.quiver(lon[::10],lat[::10],
                    u200_cn[::10,::10],v200_cn[::10,::10],
                    color='k',width=0.005, transform=ccrs.PlateCarree(),scale=8)

f3_ax1.tick_params(axis='x', labelsize=28)
f3_ax1.tick_params(axis='y', labelsize=0)
f3_ax1.set_title('e. CN', loc='left', fontsize=32)


data = np.load('fig3_part2.npz', allow_pickle=True)
z500_ee = data['z500_ee']
z500_ee_p = data['z500_ee_p']
u200_ee = data['u200_ee']
v200_ee = data['v200_ee']

z500_ca = data['z500_ca']
z500_ca_p = data['z500_ca_p']
u200_ca = data['u200_ca']
v200_ca = data['v200_ca']

z500_ea = data['z500_ea']
z500_ea_p = data['z500_ea_p']
u200_ea = data['u200_ea']
v200_ea = data['v200_ea']

z500_wn = data['z500_wn']
z500_wn_p = data['z500_wn_p']
u200_wn = data['u200_wn']
v200_wn = data['v200_wn']

z500_cn = data['z500_cn']
z500_cn_p = data['z500_cn_p']
u200_cn = data['u200_cn']
v200_cn = data['v200_cn']

lon_cesm = data['lon']
lat_cesm = data['lat']

fig3 = plt.figure(figsize=(12,8))

f3_ax1 = fig3.add_axes([0.1, 0.1, 0.6, 0.6],projection = ccrs.PlateCarree(central_longitude=180))
leftlon, rightlon, lowerlat, upperlat = (0,60,20,80)
img_extent = [leftlon, rightlon, lowerlat, upperlat]
contour_map(f3_ax1,img_extent,20,20)
c7 = f3_ax1.contourf(lon_cesm,lat_cesm,z500_ee,levels=np.arange(-0.8,0.88,0.08),extend='both',
                   cmap=cmaps.cmp_b2r,transform=ccrs.PlateCarree())
c1b = f3_ax1.contourf(lon_cesm,lat_cesm,z500_ee_p, [0,0.05,1], zorder=1,
                      hatches=['//', None],colors="none", transform=ccrs.PlateCarree())
c1c = f3_ax1.quiver(lon_cesm[::2],lat_cesm[::2],
                    u200_ee[::2,::2],v200_ee[::2,::2],
                    color='k',width=0.005, transform=ccrs.PlateCarree(),scale=8)

f3_ax1.tick_params(axis='x', labelsize=28)
f3_ax1.tick_params(axis='y', labelsize=28)
f3_ax1.set_title('f. EE', loc='left', fontsize=32)

f3_ax1 = fig3.add_axes([0.1+0.52*1, 0.1, 0.6, 0.6],projection = ccrs.PlateCarree(central_longitude=180))
leftlon, rightlon, lowerlat, upperlat = (30,90,20,80)
img_extent = [leftlon, rightlon, lowerlat, upperlat]
contour_map(f3_ax1,img_extent,20,20)
c7 = f3_ax1.contourf(lon_cesm,lat_cesm,z500_ca,levels=np.arange(-0.8,0.88,0.08),extend='both',
                   cmap=cmaps.cmp_b2r,transform=ccrs.PlateCarree())
c1b = f3_ax1.contourf(lon_cesm,lat_cesm,z500_ca_p, [0,0.05,1], zorder=1,
                      hatches=['//', None],colors="none", transform=ccrs.PlateCarree())
c1c = f3_ax1.quiver(lon_cesm[::2],lat_cesm[::2],
                    u200_ca[::2,::2],v200_ca[::2,::2],
                    color='k',width=0.005, transform=ccrs.PlateCarree(),scale=8)

f3_ax1.tick_params(axis='x', labelsize=28)
f3_ax1.tick_params(axis='y', labelsize=0)
f3_ax1.set_title('g. CA', loc='left', fontsize=32)

f3_ax1 = fig3.add_axes([0.1+0.52*2, 0.1, 0.6, 0.6],projection = ccrs.PlateCarree(central_longitude=180))
leftlon, rightlon, lowerlat, upperlat = (70,130,20,80)
img_extent = [leftlon, rightlon, lowerlat, upperlat]
contour_map(f3_ax1,img_extent,20,20)
c7 = f3_ax1.contourf(lon_cesm,lat_cesm,z500_ea,levels=np.arange(-0.8,0.88,0.08),extend='both',
                   cmap=cmaps.cmp_b2r,transform=ccrs.PlateCarree())
c1b = f3_ax1.contourf(lon_cesm,lat_cesm,z500_ea_p, [0,0.05,1], zorder=1,
                      hatches=['//', None],colors="none", transform=ccrs.PlateCarree())
c1c = f3_ax1.quiver(lon_cesm[::2],lat_cesm[::2],
                    u200_ea[::2,::2],v200_ea[::2,::2],
                    color='k',width=0.005, transform=ccrs.PlateCarree(),scale=8)

f3_ax1.tick_params(axis='x', labelsize=28)
f3_ax1.tick_params(axis='y', labelsize=0)
f3_ax1.set_title('h. EA', loc='left', fontsize=32)

f3_ax1 = fig3.add_axes([0.1+0.52*3, 0.1, 0.6, 0.6],projection = ccrs.PlateCarree(central_longitude=180))
leftlon, rightlon, lowerlat, upperlat = (190,250,20,80)
img_extent = [leftlon, rightlon, lowerlat, upperlat]
contour_map(f3_ax1,img_extent,20,20)
c7 = f3_ax1.contourf(lon_cesm,lat_cesm,z500_wn,levels=np.arange(-0.8,0.88,0.08),extend='both',
                   cmap=cmaps.cmp_b2r,transform=ccrs.PlateCarree())
c1b = f3_ax1.contourf(lon_cesm,lat_cesm,z500_wn_p, [0,0.05,1], zorder=1,
                      hatches=['//', None],colors="none", transform=ccrs.PlateCarree())
c1c = f3_ax1.quiver(lon_cesm[::2],lat_cesm[::2],
                    u200_wn[::2,::2],v200_wn[::2,::2],
                    color='k',width=0.005, transform=ccrs.PlateCarree(),scale=8)

f3_ax1.tick_params(axis='x', labelsize=28)
f3_ax1.tick_params(axis='y', labelsize=0)
f3_ax1.set_title('i. WN', loc='left', fontsize=32)


f3_ax1 = fig3.add_axes([0.1+0.52*4, 0.1, 0.6, 0.6],projection = ccrs.PlateCarree(central_longitude=180))
leftlon, rightlon, lowerlat, upperlat = (220,280,20,80)
img_extent = [leftlon, rightlon, lowerlat, upperlat]
contour_map(f3_ax1,img_extent,20,20)
c7 = f3_ax1.contourf(lon_cesm,lat_cesm,z500_cn,levels=np.arange(-0.8,0.88,0.08),extend='both',
                   cmap=cmaps.cmp_b2r,transform=ccrs.PlateCarree())
c1b = f3_ax1.contourf(lon_cesm,lat_cesm,z500_cn_p, [0,0.05,1], zorder=1,
                      hatches=['//', None],colors="none", transform=ccrs.PlateCarree())
c1c = f3_ax1.quiver(lon_cesm[::2],lat_cesm[::2],
                    u200_cn[::2,::2],v200_cn[::2,::2],
                    color='k',width=0.005, transform=ccrs.PlateCarree(),scale=8)

f3_ax1.tick_params(axis='x', labelsize=28)
f3_ax1.tick_params(axis='y', labelsize=0)
f3_ax1.set_title('j. CN', loc='left', fontsize=32)

cax = fig3.add_axes([0.96, -0.05, 0.8, 0.055])  # [left, bottom, width, height]
cb = fig3.colorbar(c7, cax=cax, orientation='horizontal')
cb.set_label("gpm", fontsize=28)
cb.ax.tick_params(labelsize=28)

qk = f3_ax1.quiverkey(c1c, X=0.65, Y=-0.15, U=2, label=r'2m s$^{-1}$', labelpos='E', fontproperties={'size':30},zorder=8)