data = np.load('fig4.npz')
# ------------------- curv EE -------------------
curv_ee_all = data['curv_ee_all']*1e05
curv_ee_ghg = data['curv_ee_ghg']*1e05
curv_ee_aer = data['curv_ee_aer']*1e05
curv_ee_bmb = data['curv_ee_bmb']*1e05

curv_ee_all_p95 = data['curv_ee_all_p95']*1e05
curv_ee_ghg_p95 = data['curv_ee_ghg_p95']*1e05
curv_ee_aer_p95 = data['curv_ee_aer_p95']*1e05
curv_ee_bmb_p95 = data['curv_ee_bmb_p95']*1e05

# ------------------- curv CA -------------------
curv_ca_all = data['curv_ca_all']*1e05
curv_ca_ghg = data['curv_ca_ghg']*1e05
curv_ca_aer = data['curv_ca_aer']*1e05
curv_ca_bmb = data['curv_ca_bmb']*1e05

curv_ca_all_p95 = data['curv_ca_all_p95']*1e05
curv_ca_ghg_p95 = data['curv_ca_ghg_p95']*1e05
curv_ca_aer_p95 = data['curv_ca_aer_p95']*1e05
curv_ca_bmb_p95 = data['curv_ca_bmb_p95']*1e05

# ------------------- curv EA -------------------
curv_ea_all = data['curv_ea_all']*1e05
curv_ea_ghg = data['curv_ea_ghg']*1e05
curv_ea_aer = data['curv_ea_aer']*1e05
curv_ea_bmb = data['curv_ea_bmb']*1e05

curv_ea_all_p95 = data['curv_ea_all_p95']*1e05
curv_ea_ghg_p95 = data['curv_ea_ghg_p95']*1e05
curv_ea_aer_p95 = data['curv_ea_aer_p95']*1e05
curv_ea_bmb_p95 = data['curv_ea_bmb_p95']*1e05

# ------------------- curv WN -------------------
curv_wn_all = data['curv_wn_all']*1e05
curv_wn_ghg = data['curv_wn_ghg']*1e05
curv_wn_aer = data['curv_wn_aer']*1e05
curv_wn_bmb = data['curv_wn_bmb']*1e05

curv_wn_all_p95 = data['curv_wn_all_p95']*1e05
curv_wn_ghg_p95 = data['curv_wn_ghg_p95']*1e05
curv_wn_aer_p95 = data['curv_wn_aer_p95']*1e05
curv_wn_bmb_p95 = data['curv_wn_bmb_p95']*1e05

# ------------------- curv CN -------------------
curv_cn_all = data['curv_cn_all']*1e05
curv_cn_ghg = data['curv_cn_ghg']*1e05
curv_cn_aer = data['curv_cn_aer']*1e05
curv_cn_bmb = data['curv_cn_bmb']*1e05

curv_cn_all_p95 = data['curv_cn_all_p95']*1e05
curv_cn_ghg_p95 = data['curv_cn_ghg_p95']*1e05
curv_cn_aer_p95 = data['curv_cn_aer_p95']*1e05
curv_cn_bmb_p95 = data['curv_cn_bmb_p95']*1e05

# ------------------- RMS NH -------------------
rms_nh_all = data['rms_nh_all']*1e05
rms_nh_ghg = data['rms_nh_ghg']*1e05
rms_nh_aer = data['rms_nh_aer']*1e05
rms_nh_bmb = data['rms_nh_bmb']*1e05

rms_nh_all_p95 = data['rms_nh_all_p95']*1e05
rms_nh_ghg_p95 = data['rms_nh_ghg_p95']*1e05
rms_nh_aer_p95 = data['rms_nh_aer_p95']*1e05
rms_nh_bmb_p95 = data['rms_nh_bmb_p95']*1e05

import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

sns.set_theme(style="white", font_scale=1.2, rc={"lines.linewidth": 2.5})

regions = {
    "EE": (curv_ee_all, curv_ee_ghg, curv_ee_aer, curv_ee_bmb),
    "CA": (curv_ca_all, curv_ca_ghg, curv_ca_aer, curv_ca_bmb),
    "EA": (curv_ea_all, curv_ea_ghg, curv_ea_aer, curv_ea_bmb),
    "WN": (curv_wn_all, curv_wn_ghg, curv_wn_aer, curv_wn_bmb),
    "CN": (curv_cn_all, curv_cn_ghg, curv_cn_aer, curv_cn_bmb),
    "NH": (rms_nh_all, rms_nh_ghg, rms_nh_aer, rms_nh_bmb)
}
regions_p95 = {
    "EE": (curv_ee_all_p95, curv_ee_ghg_p95, curv_ee_aer_p95, curv_ee_bmb_p95),
    "CA": (curv_ca_all_p95, curv_ca_ghg_p95, curv_ca_aer_p95, curv_ca_bmb_p95),
    "EA": (curv_ea_all_p95, curv_ea_ghg_p95, curv_ea_aer_p95, curv_ea_bmb_p95),
    "WN": (curv_wn_all_p95, curv_wn_ghg_p95, curv_wn_aer_p95, curv_wn_bmb_p95),
    "CN": (curv_cn_all_p95, curv_cn_ghg_p95, curv_cn_aer_p95, curv_cn_bmb_p95),
    "NH": (rms_nh_all_p95, rms_nh_ghg_p95, rms_nh_aer_p95, rms_nh_bmb_p95)
}

years_all = np.arange(1920, 2081)
years_bmb = np.arange(1920, 2030)

fig, axes = plt.subplots(2, 3, figsize=(18, 8), sharex=True)
axes = axes.flatten()

region_order = ["EE", "CA", "EA", "WN", "CN", "NH"]

colors = {
    "all": "gray",
    "ghg": "lightcoral",
    "aer": "#72ddf7",
    "bmb": "#8CB369"
}

title_prefix = ['a.', 'b.', 'c.', 'd.', 'e.', 'f.']

for i, region in enumerate(region_order):
    ax = axes[i]
    all_, ghg, aer, bmb = regions[region]
    all_p95, ghg_p95, aer_p95, bmb_p95 = regions_p95[region]
    ax.plot(years_all, all_, color=colors["all"], label="All Forcing")
    ax.fill_between(years_all, all_ - all_p95, all_ + all_p95, alpha=0.3, color=colors["all"])

    ax.plot(years_all, ghg, color=colors["ghg"], label="XGHG")
    ax.fill_between(years_all, ghg - ghg_p95, ghg + ghg_p95, alpha=0.3, color=colors["ghg"])

    ax.plot(years_all, aer, color=colors["aer"], label="XAER")
    ax.fill_between(years_all, aer - aer_p95, aer + aer_p95, alpha=0.3, color=colors["aer"])

    ax.plot(years_bmb, bmb, color=colors["bmb"], label="XBMB")
    ax.fill_between(years_bmb, bmb - bmb_p95, bmb + bmb_p95, alpha=0.3, color=colors["bmb"])
    if region != "NH":
        ax.axhline(0, c='k', ls='--')
    ax.set_xlim(1920, 2080)
    title_text = f"{title_prefix[i]} {region}" if region != "NH" else f"{title_prefix[i]} Overall Curvature"
    ax.set_title(title_text, loc='left', fontsize=22)

    ax.spines['right'].set_visible(False)
    ax.spines['top'].set_visible(False)
    if i == 0:
        ax.legend(frameon=True, loc='upper left', fontsize=16)

    ax.axvline(1979, c='gray', ls='-', lw=0.5, zorder=8)
    ax.axvline(2023, c='gray', ls='-', lw=0.5, zorder=8)
    ax.tick_params(axis='y', labelsize=16)
    ax.tick_params(axis='x', labelsize=16)
    

plt.tight_layout()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

data = np.load("fig4_part2.npz", allow_pickle=True)

df_plot = pd.DataFrame({
    "Region": data["Region"],
    "Forcing": data["Forcing"],
    "Mean": data["Mean"],
    "CI": data["CI"]
})

region_order = ['EE','CA','EA','WN','CN','Overall Curvature']
forcing_order = ['XGHG','XAER']

df_plot["Region"] = pd.Categorical(df_plot["Region"], categories=region_order, ordered=True)
df_plot["Forcing"] = pd.Categorical(df_plot["Forcing"], categories=forcing_order, ordered=True)
df_plot = df_plot.sort_values(["Region", "Forcing"])

fig, ax = plt.subplots(figsize=(10,6))
palette = ["lightcoral", "#72ddf7"]

x = np.arange(len(region_order))
dodge_width = 0.25  

for i, forcing in enumerate(forcing_order):
    sub = df_plot[df_plot["Forcing"]==forcing].reset_index(drop=True)
    xpos = x - dodge_width*(len(forcing_order)-1)/2 + i*dodge_width  
    ax.scatter(xpos, sub["Mean"], color=palette[i], s=50, label=forcing)
    ax.errorbar(xpos, sub["Mean"], yerr=sub["CI"], fmt='none', color=palette[i],
                elinewidth=1.5, capsize=3)

ax.axhline(0, ls='--', c='k', lw=1)
xticks = np.arange(len(region_order))
ax.set_xticks(xticks)
ax.set_xticklabels(region_order, fontsize=12)

for i in range(len(xticks)-1):
    x_pos = (xticks[i]+xticks[i+1])/2
    ax.axvline(x=x_pos, ls='--', c='gray', lw=1)

ax.set_ylabel("Contribution (%)", fontsize=14)
ax.set_xlabel("Region", fontsize=14)
ax.set_ylim(-60, 150)
ax.set_title("g. Contribution of Individual Forcings", fontsize=16, loc='left')
ax.legend(title="Forcing", fontsize=14, title_fontsize=14)

plt.show()