data = np.load('fig5.npz')
ghg_gpp = data['ghg_gpp']
ghg_gpp_p95 = data['ghg_gpp_p95']
nghg_gpp = data['nghg_gpp']
nghg_gpp_p95 = data['nghg_gpp_p95']
dif = data['dif']
dif_p95 = data['dif_p95']
lon = data['lon']
lat = data['lat']

fig3 = plt.figure(figsize=(12,8))
leftlon, rightlon, lowerlat, upperlat = (0,360,0,80)
img_extent = [leftlon, rightlon, lowerlat, upperlat]

f3_ax1 = fig3.add_axes([0.05, 0.85, 1.4, 0.6],projection = ccrs.PlateCarree(central_longitude=180))
contour_map(f3_ax1,img_extent,30,30)
c7 = f3_ax1.contourf(lon,lat,ghg_gpp,levels=np.arange(-2,2.2,0.2),extend='both',
                   cmap=cmaps.GMT_panoply,transform=ccrs.PlateCarree())
f3_ax1.contourf(lon, lat, ghg_gpp_p95,levels=[0.5, 1.5],hatches=['///'], colors='none',transform=ccrs.PlateCarree(), zorder=3)

f3_ax1.add_patch(patches.Rectangle((10, 60),40,10,linewidth=3,linestyle='-',zorder=4,
                                   edgecolor='k',facecolor='none', transform=ccrs.PlateCarree()))
f3_ax1.text(38,72,'R1',fontsize=24, transform=ccrs.PlateCarree(),fontweight='bold',zorder=4)

f3_ax1.add_patch(patches.Rectangle((10, 45),40,15,linewidth=3,linestyle='-',zorder=4,
                                   edgecolor='k',facecolor='none', transform=ccrs.PlateCarree()))
f3_ax1.text(38,38,'R2',fontsize=24, transform=ccrs.PlateCarree(),fontweight='bold',zorder=4)

f3_ax1.add_patch(patches.Rectangle((90, 50),40,25,linewidth=3,linestyle='-',zorder=4,
                                   edgecolor='k',facecolor='none', transform=ccrs.PlateCarree()))
f3_ax1.text(118,52,'R3',fontsize=24, transform=ccrs.PlateCarree(),fontweight='bold',zorder=4)

f3_ax1.add_patch(patches.Rectangle((195, 50),45,20,linewidth=3,linestyle='-',zorder=4,
                                   edgecolor='k',facecolor='none', transform=ccrs.PlateCarree()))
f3_ax1.text(228,52,'R4',fontsize=24, transform=ccrs.PlateCarree(),fontweight='bold',zorder=4)

f3_ax1.add_patch(patches.Rectangle((245, 40),30,15,linewidth=3,linestyle='-',zorder=4,
                                   edgecolor='k',facecolor='none', transform=ccrs.PlateCarree()))
f3_ax1.text(263,42,'R5',fontsize=24, transform=ccrs.PlateCarree(),fontweight='bold',zorder=4)
f3_ax1.tick_params(axis='x', labelsize=16)
f3_ax1.tick_params(axis='y', labelsize=16)
f3_ax1.set_aspect(1.5)
f3_ax1.set_title("a. GHG induced GPP trend", fontsize=24,loc='left')

f3_ax1 = fig3.add_axes([0.05, 0.1, 1.4, 0.6],projection = ccrs.PlateCarree(central_longitude=180))
contour_map(f3_ax1,img_extent,30,30)
c7 = f3_ax1.contourf(lon,lat,nghg_gpp,levels=np.arange(-2,2.2,0.2),extend='both',
                   cmap=cmaps.GMT_panoply,transform=ccrs.PlateCarree())
f3_ax1.contourf(lon, lat, nghg_gpp_p95,levels=[0.5, 1.5],hatches=['///'], colors='none',transform=ccrs.PlateCarree(), zorder=3)

f3_ax1.add_patch(patches.Rectangle((10, 60),40,10,linewidth=3,linestyle='-',zorder=4,
                                   edgecolor='k',facecolor='none', transform=ccrs.PlateCarree()))
f3_ax1.text(38,72,'R1',fontsize=24, transform=ccrs.PlateCarree(),fontweight='bold',zorder=4)

f3_ax1.add_patch(patches.Rectangle((10, 45),40,15,linewidth=3,linestyle='-',zorder=4,
                                   edgecolor='k',facecolor='none', transform=ccrs.PlateCarree()))
f3_ax1.text(38,38,'R2',fontsize=24, transform=ccrs.PlateCarree(),fontweight='bold',zorder=4)

f3_ax1.add_patch(patches.Rectangle((90, 50),40,25,linewidth=3,linestyle='-',zorder=4,
                                   edgecolor='k',facecolor='none', transform=ccrs.PlateCarree()))
f3_ax1.text(118,52,'R3',fontsize=24, transform=ccrs.PlateCarree(),fontweight='bold',zorder=4)

f3_ax1.add_patch(patches.Rectangle((195, 50),45,20,linewidth=3,linestyle='-',zorder=4,
                                   edgecolor='k',facecolor='none', transform=ccrs.PlateCarree()))
f3_ax1.text(228,52,'R4',fontsize=24, transform=ccrs.PlateCarree(),fontweight='bold',zorder=4)

f3_ax1.add_patch(patches.Rectangle((245, 40),30,15,linewidth=3,linestyle='-',zorder=4,
                                   edgecolor='k',facecolor='none', transform=ccrs.PlateCarree()))
f3_ax1.text(263,42,'R5',fontsize=24, transform=ccrs.PlateCarree(),fontweight='bold',zorder=4)
f3_ax1.tick_params(axis='x', labelsize=16)
f3_ax1.tick_params(axis='y', labelsize=16)
f3_ax1.set_aspect(1.5)
f3_ax1.set_title("b. Non-GHG induced GPP trend", fontsize=24,loc='left')

f3_ax1 = fig3.add_axes([0.05, 0.1-0.75, 1.4, 0.6],projection = ccrs.PlateCarree(central_longitude=180))
contour_map(f3_ax1,img_extent,30,30)
c7 = f3_ax1.contourf(lon,lat,dif,levels=np.arange(-2,2.2,0.2),extend='both',
                   cmap=cmaps.GMT_panoply,transform=ccrs.PlateCarree())
f3_ax1.contourf(lon, lat, dif_p95,levels=[0.5, 1.5],hatches=['///'], colors='none',transform=ccrs.PlateCarree(), zorder=3)

f3_ax1.add_patch(patches.Rectangle((10, 60),40,10,linewidth=3,linestyle='-',zorder=4,
                                   edgecolor='k',facecolor='none', transform=ccrs.PlateCarree()))
f3_ax1.text(38,72,'R1',fontsize=24, transform=ccrs.PlateCarree(),fontweight='bold',zorder=4)

f3_ax1.add_patch(patches.Rectangle((10, 45),40,15,linewidth=3,linestyle='-',zorder=4,
                                   edgecolor='k',facecolor='none', transform=ccrs.PlateCarree()))
f3_ax1.text(38,38,'R2',fontsize=24, transform=ccrs.PlateCarree(),fontweight='bold',zorder=4)

f3_ax1.add_patch(patches.Rectangle((90, 50),40,25,linewidth=3,linestyle='-',zorder=4,
                                   edgecolor='k',facecolor='none', transform=ccrs.PlateCarree()))
f3_ax1.text(118,52,'R3',fontsize=24, transform=ccrs.PlateCarree(),fontweight='bold',zorder=4)

f3_ax1.add_patch(patches.Rectangle((195, 50),45,20,linewidth=3,linestyle='-',zorder=4,
                                   edgecolor='k',facecolor='none', transform=ccrs.PlateCarree()))
f3_ax1.text(228,52,'R4',fontsize=24, transform=ccrs.PlateCarree(),fontweight='bold',zorder=4)

f3_ax1.add_patch(patches.Rectangle((245, 40),30,15,linewidth=3,linestyle='-',zorder=4,
                                   edgecolor='k',facecolor='none', transform=ccrs.PlateCarree()))
f3_ax1.text(263,42,'R5',fontsize=24, transform=ccrs.PlateCarree(),fontweight='bold',zorder=4)
f3_ax1.tick_params(axis='x', labelsize=16)
f3_ax1.tick_params(axis='y', labelsize=16)
f3_ax1.set_aspect(1.5)
f3_ax1.set_title("c. Difference between a. and b.", fontsize=24,loc='left')

cax = fig3.add_axes([0.4, -0.8, 0.6, 0.035])  # [left, bottom, width, height]
cb = fig3.colorbar(c7, cax=cax, orientation='horizontal')
cb.set_label("gC m⁻² yr⁻¹", fontsize=16)
cb.ax.tick_params(labelsize=14)