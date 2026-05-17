f = np.load('fig2.npz')
rms_curvature = f['rms_curvature']*1e05
curvature_reg = f['s_cur']*1e05
curvature_p = f['p_cur']
gpp_lon = f['gpp_lon']
gpp_lat = f['gpp_lat']
gpp_r = f['gpp_r']
gpptrend_lon = f['gpptrend_lon']
gpptrend_lat = f['gpptrend_lat']
gpp_trend = f['gpp_trend']

leftlon, rightlon, lowerlat, upperlat = (0, 360, 0, 80)
img_extent = [leftlon, rightlon, lowerlat, upperlat]
years = np.arange(1979, 2024)
colors = ['lightcoral' if val > 0 else 'lightblue' for val in rms_curvature]
fig3 = plt.figure(figsize=(10, 6))
f3_ax1 = fig3.add_axes([0.15, 0.15, 0.75, 0.7])
f3_ax1.bar(years, rms_curvature , color=colors, ec='k')  # 注意乘1000是为了单位统一
f3_ax1.set_title("a. Overall Curvature", fontsize=22,loc='left')
f3_ax1.tick_params(axis='x', labelsize=18)
f3_ax1.tick_params(axis='y', labelsize=18)
f3_ax1.axhline(0,c='k',lw=2)
f3_ax1.axhline(0.5,c='k',lw=2,ls='--')
f3_ax1.axhline(-0.5,c='k',lw=2,ls='--')
f3_ax1.set_ylabel(r"Curvature ($10^{-5}\ \mathrm{degree}$)", fontsize=22)
f3_ax1 = fig3.add_axes([1.05, 0.15, 0.75, 0.7],projection = ccrs.PlateCarree(central_longitude=180))
f3_ax1.set_extent(img_extent, crs=ccrs.PlateCarree())
f3_ax1.add_feature(cfeature.COASTLINE.with_scale('50m'),alpha=0.5,ec='gray') 
for spine in f3_ax1.spines.values():
    spine.set_visible(False)
f3_ax1.set_aspect(2.22)
f3_ax2 = fig3.add_axes([1.05, 0.15, 0.75, 0.7])
f3_ax2.set_facecolor('none')
f3_ax2.plot(lon,curvature_reg,c='k')
segments = []
for i in range(len(lon) - 1):
    if (curvature_p[i] < 0.05) and (curvature_p[i+1] < 0.05):
        x = [lon[i], lon[i+1]]
        y = [curvature_reg[i], curvature_reg[i+1]]
        segments.append(np.column_stack([x, y]))
if segments:
    line_segments = LineCollection(segments, colors='r', linewidths=5, label='p < 0.1')
    f3_ax2.add_collection(line_segments)
f3_ax2.set_xlim(0,360)
f3_ax2.set_ylim(-12,12)
f3_ax2.set_title("b. Reg. Local Curvature onto Overall Curvature", fontsize=22,loc='left')
f3_ax2.set_ylabel("Regression Coefficient", fontsize=22)
f3_ax2.axhline(0,c='k',lw=1)

lon_formatter = cticker.LongitudeFormatter()
f3_ax2.xaxis.set_major_formatter(lon_formatter)
f3_ax2.tick_params(axis='x', labelsize=18)
f3_ax2.tick_params(axis='y', labelsize=18)
f3_ax2.add_patch(patches.Rectangle((0, -30), lon[indices][0]-0, 60, linewidth=0, color='lightgray', alpha=0.3))
f3_ax2.add_patch(patches.Rectangle((lon[indices][1], -30), lon[indices][2]-lon[indices][1], 60, linewidth=0, color='lightgray', alpha=0.3))
f3_ax2.add_patch(patches.Rectangle((lon[indices][3], -30), lon[indices][4]-lon[indices][3], 60, linewidth=0, color='lightgray', alpha=0.3))
f3_ax2.add_patch(patches.Rectangle((lon[indices][5], -30), lon[indices][6]-lon[indices][5], 60, linewidth=0, color='lightgray', alpha=0.3))
f3_ax2.add_patch(patches.Rectangle((lon[indices][7], -30), 360-lon[indices][7], 60, linewidth=0, color='lightgray', alpha=0.3))

f3_ax2.text((lon[indices][0]+0)/2-6,-10,'WE',fontsize=22)
f3_ax2.text((lon[indices][1]+lon[indices][0])/2-6,-10,'EE',fontsize=22)
f3_ax2.text((lon[indices][2]+lon[indices][1])/2-6,-10,'CA',fontsize=22)
f3_ax2.text((lon[indices][3]+lon[indices][2])/2-6,-10,'EA',fontsize=22)
f3_ax2.text((lon[indices][4]+lon[indices][3])/2-6,-10,'PA',fontsize=22)
f3_ax2.text((lon[indices][5]+lon[indices][4])/2-6,-10,'WN',fontsize=22)
f3_ax2.text((lon[indices][6]+lon[indices][5])/2-6,-10,'CN',fontsize=22)
f3_ax2.text((lon[indices][7]+lon[indices][6])/2-6,-10,'EN',fontsize=22)

f3_ax1 = fig3.add_axes([0.15, -0.8, 2, 0.75], projection=ccrs.PlateCarree(central_longitude=180))
contour_map(f3_ax1,img_extent,30,30)
sc = f3_ax1.scatter(gpp_lon, gpp_lat,
                    s=8,
                    c=gpp_r,
                    cmap=cmaps.GMT_panoply,
                    marker='s',
                    vmin=-0.8, vmax=0.8,
                    transform=ccrs.PlateCarree(),
                    alpha=0.8)
f3_ax1.tick_params(axis='x', labelsize=18)
f3_ax1.tick_params(axis='y', labelsize=18)

f3_ax1.add_patch(patches.Rectangle((10, 60),40,10,linewidth=3,linestyle='-',zorder=4,
                                   edgecolor='k',facecolor='none', transform=ccrs.PlateCarree()))
f3_ax1.text(38,72,'R1',fontsize=24, transform=ccrs.PlateCarree(),fontweight='bold')

f3_ax1.add_patch(patches.Rectangle((10, 45),40,15,linewidth=3,linestyle='-',zorder=4,
                                   edgecolor='k',facecolor='none', transform=ccrs.PlateCarree()))
f3_ax1.text(38,38,'R2',fontsize=24, transform=ccrs.PlateCarree(),fontweight='bold')

f3_ax1.add_patch(patches.Rectangle((90, 50),40,25,linewidth=3,linestyle='-',zorder=4,
                                   edgecolor='k',facecolor='none', transform=ccrs.PlateCarree()))
f3_ax1.text(118,52,'R3',fontsize=24, transform=ccrs.PlateCarree(),fontweight='bold')

f3_ax1.add_patch(patches.Rectangle((195, 50),35,20,linewidth=3,linestyle='-',zorder=4,
                                   edgecolor='k',facecolor='none', transform=ccrs.PlateCarree()))
f3_ax1.text(208,52,'R4',fontsize=24, transform=ccrs.PlateCarree(),fontweight='bold')

f3_ax1.add_patch(patches.Rectangle((245, 35),35,20,linewidth=3,linestyle='-',zorder=4,
                                   edgecolor='k',facecolor='none', transform=ccrs.PlateCarree()))
f3_ax1.text(265,38,'R5',fontsize=24, transform=ccrs.PlateCarree(),fontweight='bold')


# 添加 colorbar
cb = plt.colorbar(sc, ax=f3_ax1, orientation='vertical', shrink=0.9, pad=0.02)
cb.set_label('Correlation Coefficient', fontsize=22)
cb.ax.tick_params(labelsize=18)
# 设置标题
f3_ax1.set_title("c. Relationship between GPP & Overall Curvature", 
                 fontsize=22, loc='left')

f3_ax1 = fig3.add_axes([0.15,-1.65, 2, 0.75], projection=ccrs.PlateCarree(central_longitude=180))
contour_map(f3_ax1,img_extent,30,30)
# 绘制散点图
sc = f3_ax1.scatter(gpptrend_lon, gpptrend_lat,
                    s=8,
                    c=gpp_trend,
                    cmap=cmaps.GMT_panoply,
                    marker='s',
                    vmin=-1, vmax=1,
                    transform=ccrs.PlateCarree(),
                    alpha=0.8)

f3_ax1.tick_params(axis='x', labelsize=18)
f3_ax1.tick_params(axis='y', labelsize=18)

f3_ax1.add_patch(patches.Rectangle((10, 60),40,10,linewidth=3,linestyle='-',zorder=4,
                                   edgecolor='k',facecolor='none', transform=ccrs.PlateCarree()))
f3_ax1.text(38,72,'R1',fontsize=24, transform=ccrs.PlateCarree(),fontweight='bold')

f3_ax1.add_patch(patches.Rectangle((10, 45),40,15,linewidth=3,linestyle='-',zorder=4,
                                   edgecolor='k',facecolor='none', transform=ccrs.PlateCarree()))
f3_ax1.text(38,38,'R2',fontsize=24, transform=ccrs.PlateCarree(),fontweight='bold')

f3_ax1.add_patch(patches.Rectangle((90, 50),40,25,linewidth=3,linestyle='-',zorder=4,
                                   edgecolor='k',facecolor='none', transform=ccrs.PlateCarree()))
f3_ax1.text(118,52,'R3',fontsize=24, transform=ccrs.PlateCarree(),fontweight='bold')
f3_ax1.add_patch(patches.Rectangle((195, 50),35,20,linewidth=3,linestyle='-',zorder=4,
                                   edgecolor='k',facecolor='none', transform=ccrs.PlateCarree()))
f3_ax1.text(208,52,'R4',fontsize=24, transform=ccrs.PlateCarree(),fontweight='bold')

f3_ax1.add_patch(patches.Rectangle((245, 35),35,20,linewidth=3,linestyle='-',zorder=4,
                                   edgecolor='k',facecolor='none', transform=ccrs.PlateCarree()))
f3_ax1.text(265,38,'R5',fontsize=24, transform=ccrs.PlateCarree(),fontweight='bold')

f3_ax1.set_title("d. Trend of GPP from 1982 to 2018", 
                 fontsize=22, loc='left')

cb = plt.colorbar(sc, ax=f3_ax1, orientation='vertical', shrink=0.9, pad=0.02)
cb.set_label('Trend', fontsize=22)
cb.ax.tick_params(labelsize=18)

plt.show()