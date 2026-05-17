f = np.load('fig1.npz')
lon = f['lon']
trend = f['trend']* 1e05
trend_p = f['trend_p']* 1e05
curvature_b2000 = f['curvature_b2000']* 1e05
curvature_a2000 = f['curvature_a2000']* 1e05
curvature_mean = f['curvature_mean']* 1e05
curvature_we = f['curvature_we']* 1e05
curvature_abs_we = f['curvature_abs_we']* 1e05
curvature_ee = f['curvature_ee']* 1e05
curvature_abs_ee = f['curvature_abs_ee']* 1e05
curvature_ca = f['curvature_ca']* 1e05
curvature_abs_ca = f['curvature_abs_ca']* 1e05
curvature_ea = f['curvature_ea']* 1e05
curvature_abs_ea = f['curvature_abs_ea']* 1e05
curvature_pa = f['curvature_pa']* 1e05
curvature_abs_pa = f['curvature_abs_pa']* 1e05
curvature_wn = f['curvature_wn']* 1e05
curvature_abs_wn = f['curvature_abs_wn']* 1e05
curvature_cn = f['curvature_cn']* 1e05
curvature_abs_cn = f['curvature_abs_cn']* 1e05
curvature_en = f['curvature_en']* 1e05
curvature_abs_en = f['curvature_abs_en']* 1e05
region_trend = f['region_trend']* 1e05
region_trend_p  = f['region_trend_p']* 1e05
diff = curvature_b2000 - curvature_a2000
indices = np.where(np.diff(np.sign(diff)) != 0)[0]

fig3 = plt.figure(figsize=(12,8))
leftlon, rightlon, lowerlat, upperlat = (0,360,0,90)
img_extent = [leftlon, rightlon, lowerlat, upperlat]
f3_ax1 = fig3.add_axes([0.1, 0.8, 1.4, 0.6],projection = ccrs.PlateCarree(central_longitude=180))
f3_ax1.set_extent(img_extent, crs=ccrs.PlateCarree())
f3_ax1.add_feature(cfeature.COASTLINE.with_scale('50m'),alpha=0.5,ec='gray') 
for spine in f3_ax1.spines.values():
    spine.set_visible(False)
    
f3_ax2 = fig3.add_axes([0.1, 0.84, 1.4, 0.5])
f3_ax2.set_facecolor('none')
f3_ax2.fill_between(lon, trend, 0, where=(trend > 0), color='lightcoral', alpha=0.5, label='Positive Trend')
f3_ax2.fill_between(lon, trend, 0, where=(trend < 0), color='lightblue', alpha=0.5, label='Negative Trend')

pos = trend > 0
f3_ax2.fill_between(lon, trend_p , 0, where=pos,
                    facecolor='none', edgecolor='k', hatch='///',
                    linewidth=0.0, alpha=1.0)
neg = trend < 0
f3_ax2.fill_between(lon, trend_p , 0, where=neg,
                    facecolor='none', edgecolor='k', hatch='\\\\\\',
                    linewidth=0.0, alpha=1.0)

f3_ax2.plot(
    lon, 
    curvature_mean, 
    label='Mean Curvature', 
    color='k', 
    linewidth=2)

f3_ax2.legend(loc='upper right', fontsize=22)
f3_ax2.set_xlim(0,360)
f3_ax2.set_ylim(-10,10)
f3_ax2.set_title("a. Mean Curvature of the Westerlies", fontsize=25,loc='left')
f3_ax2.axhline(0,c='k',lw=1)

lon_formatter = cticker.LongitudeFormatter()
f3_ax2.xaxis.set_major_formatter(lon_formatter)
f3_ax2.tick_params(axis='x', labelsize=20)
f3_ax2.tick_params(axis='y', labelsize=20)

f3_ax1 = fig3.add_axes([0.1, 0.1, 1.4, 0.6],projection = ccrs.PlateCarree(central_longitude=180))
f3_ax1.set_extent(img_extent, crs=ccrs.PlateCarree())
f3_ax1.add_feature(cfeature.COASTLINE.with_scale('50m'),alpha=0.5,ec='gray') 
for spine in f3_ax1.spines.values():
    spine.set_visible(False)
    
f3_ax2 = fig3.add_axes([0.1, 0.14, 1.4, 0.5])
f3_ax2.set_facecolor('none')

f3_ax2.plot(
    lon, 
    curvature_b2000, 
    label='Before 1999', 
    color='lightblue', 
    linewidth=5)

f3_ax2.plot(
    lon, 
    curvature_a2000, 
    label='After 2000', 
    color='lightcoral', 
    linewidth=5)
f3_ax2.add_patch(patches.Rectangle((0, -30), lon[indices][0]-0, 60, linewidth=0, color='lightgray', alpha=0.3))
f3_ax2.add_patch(patches.Rectangle((lon[indices][1], -30), lon[indices][2]-lon[indices][1], 60, linewidth=0, color='lightgray', alpha=0.3))
f3_ax2.add_patch(patches.Rectangle((lon[indices][3], -30), lon[indices][4]-lon[indices][3], 60, linewidth=0, color='lightgray', alpha=0.3))
f3_ax2.add_patch(patches.Rectangle((lon[indices][5], -30), lon[indices][6]-lon[indices][5], 60, linewidth=0, color='lightgray', alpha=0.3))
f3_ax2.add_patch(patches.Rectangle((lon[indices][7], -30), 360-lon[indices][7], 60, linewidth=0, color='lightgray', alpha=0.3))

f3_ax2.text((lon[indices][0]+0)/2-6,-13,'WE',fontsize=22)
f3_ax2.text((lon[indices][1]+lon[indices][0])/2-6,-13,'EE',fontsize=22)
f3_ax2.text((lon[indices][2]+lon[indices][1])/2-6,-13,'CA',fontsize=22)
f3_ax2.text((lon[indices][3]+lon[indices][2])/2-6,-13,'EA',fontsize=22)
f3_ax2.text((lon[indices][4]+lon[indices][3])/2-6,-13,'PA',fontsize=22)
f3_ax2.text((lon[indices][5]+lon[indices][4])/2-6,-13,'WN',fontsize=22)
f3_ax2.text((lon[indices][6]+lon[indices][5])/2-6,-13,'CN',fontsize=22)
f3_ax2.text((lon[indices][7]+lon[indices][6])/2-6,-13,'EN',fontsize=22)
f3_ax2.legend(loc='upper right', fontsize=22)
f3_ax2.set_xlim(0,360)
f3_ax2.set_ylim(-15,15)
f3_ax2.set_title("b. Curvature anomalies of the Westerlies", fontsize=25,loc='left')
f3_ax2.axhline(0,c='k',lw=1)

lon_formatter = cticker.LongitudeFormatter()
f3_ax2.xaxis.set_major_formatter(lon_formatter)
f3_ax2.tick_params(axis='x', labelsize=20)
f3_ax2.tick_params(axis='y', labelsize=20)

years = np.arange(1979, 2024)  
fig3 = plt.figure(figsize=(12,8))

f3_ax1 = fig3.add_axes([0.1, 0.5, 0.2, 0.3])
colors = ['lightcoral' if value > 0 else 'lightblue' for value in curvature_we]
f3_ax1.bar(years, curvature_we , color=colors,ec='k',label='mean curvature')
f3_ax1.plot(np.arange(1979,2024),curvature_abs_we ,c='k',label='abs. mean curvature')
f3_ax1.set_title('c. WE',fontsize=18,loc='left')
f3_ax1.legend(fontsize=11)
f3_ax1.tick_params(axis='y', labelsize=13)
f3_ax1.tick_params(axis='x', labelsize=13)

f3_ax1 = fig3.add_axes([0.38, 0.5, 0.2, 0.3])
colors = ['lightcoral' if value > 0 else 'lightblue' for value in curvature_ee]
f3_ax1.bar(years, curvature_ee , color=colors,ec='k')
f3_ax1.plot(np.arange(1979,2024),curvature_abs_ee ,c='k')
f3_ax1.set_title('d. EE',fontsize=18,loc='left')
f3_ax1.tick_params(axis='y', labelsize=13)
f3_ax1.tick_params(axis='x', labelsize=13)

f3_ax1 = fig3.add_axes([0.66, 0.5, 0.2, 0.3])
colors = ['lightcoral' if value > 0 else 'lightblue' for value in curvature_ca]
f3_ax1.bar(years, curvature_ca , color=colors,ec='k')
f3_ax1.plot(np.arange(1979,2024),curvature_abs_ca ,c='k')
f3_ax1.set_title('e. CA',fontsize=18,loc='left')
f3_ax1.tick_params(axis='y', labelsize=13)
f3_ax1.tick_params(axis='x', labelsize=13)

f3_ax1 = fig3.add_axes([0.94, 0.5, 0.2, 0.3])
colors = ['lightcoral' if value > 0 else 'lightblue' for value in curvature_ea]
f3_ax1.bar(years, curvature_ea , color=colors,ec='k')
f3_ax1.plot(np.arange(1979,2024),curvature_abs_ea ,c='k')
f3_ax1.set_title('f. EA',fontsize=18,loc='left')
f3_ax1.tick_params(axis='y', labelsize=13)
f3_ax1.tick_params(axis='x', labelsize=13)

f3_ax1 = fig3.add_axes([0.1, 0.1, 0.2, 0.3])
colors = ['lightcoral' if value > 0 else 'lightblue' for value in curvature_pa]
f3_ax1.bar(years, curvature_pa , color=colors,ec='k')
f3_ax1.plot(np.arange(1979,2024),curvature_abs_pa ,c='k')
f3_ax1.set_title('g. PA',fontsize=18,loc='left')
f3_ax1.tick_params(axis='y', labelsize=13)
f3_ax1.tick_params(axis='x', labelsize=13)

f3_ax1 = fig3.add_axes([0.38, 0.1, 0.2, 0.3])
colors = ['lightcoral' if value > 0 else 'lightblue' for value in curvature_wn]
f3_ax1.bar(years, curvature_wn , color=colors,ec='k')
f3_ax1.plot(np.arange(1979,2024),curvature_abs_wn ,c='k')
f3_ax1.set_title('h. WN',fontsize=18,loc='left')
f3_ax1.tick_params(axis='y', labelsize=13)
f3_ax1.tick_params(axis='x', labelsize=13)

f3_ax1 = fig3.add_axes([0.66, 0.1, 0.2, 0.3])
colors = ['lightcoral' if value > 0 else 'lightblue' for value in curvature_cn]
f3_ax1.bar(years, curvature_cn , color=colors,ec='k')
f3_ax1.plot(np.arange(1979,2024),curvature_abs_cn ,c='k')
f3_ax1.set_title('i. CN',fontsize=18,loc='left')
f3_ax1.tick_params(axis='y', labelsize=13)
f3_ax1.tick_params(axis='x', labelsize=13)

f3_ax1 = fig3.add_axes([0.94, 0.1, 0.2, 0.3])
colors = ['lightcoral' if value > 0 else 'lightblue' for value in curvature_en]
f3_ax1.bar(years, curvature_en , color=colors,ec='k')
f3_ax1.plot(np.arange(1979,2024),curvature_abs_en,c='k')
f3_ax1.set_title('j. EN',fontsize=18,loc='left')
f3_ax1.tick_params(axis='y', labelsize=13)
f3_ax1.tick_params(axis='x', labelsize=13)


data_df = pd.DataFrame(
    region_trend,
    index=['mean curvature', 'mean abs. curvature'],
    columns=['WE','EE','CA','EA','PA','WN','CN','EN']
)

sig_flat = region_trend_p.flatten()

fig3 = plt.figure(figsize=(12,8))
f3_ax1 = fig3.add_axes([0.1, -0.3, 1.04, 0.3])

index = data_df.index.tolist()     
regions = data_df.columns.tolist() 
bar_width = 0.35                   
x = np.arange(len(regions))         

colors = ['lightcoral', 'lightblue']  

for i, idx in enumerate(index):
    f3_ax1.bar(
        x + (i - 0.5) * bar_width,    
        data_df.loc[idx],
        width=bar_width,
        label=idx,
        color=colors[i],
        edgecolor='black',
        linewidth=1.5
    )

flat_values = region_trend.flatten()
for i in range(2):  
    for j in range(len(regions)):  
        value = region_trend[i, j]
        sig = region_trend_p[i, j]
        
        xpos = x[j] + (i - 0.5) * bar_width  
        ypos = value                        
        
        if ypos >= 0:
            ytext = ypos + 0.5
            va = 'bottom'
        else:
            ytext = ypos - 0.5
            va = 'top'
        
        text = f"{value:.2f}"
        if sig:
            if j >=1:
                text += "*"
        f3_ax1.text(
            xpos,
            ytext,
            text,
            ha='center', va=va,
            fontsize=14, weight='bold', color='black'
        )
f3_ax1.set_title('k. Trend', fontsize=18, loc='left')
f3_ax1.set_xticks(x)
f3_ax1.set_xticklabels(regions, fontsize=13)
f3_ax1.tick_params(axis='y', labelsize=13)
f3_ax1.set_xlabel("")
f3_ax1.set_ylabel("")
f3_ax1.legend(title="", fontsize=12)
f3_ax1.set_ylim(-8, 8)
f3_ax1.axhline(0, ls='-', c='k')
