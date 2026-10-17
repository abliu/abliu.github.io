#!/usr/bin/env python3
"""Reproduce the annotated Boston bicycle-commuter chart.

Install: python -m pip install matplotlib
Run:     python boston_bike_commuters.py
Or:      python boston_bike_commuters.py --output my-chart.png

The data are embedded; no network requests or additional data files are needed.
Population: Boston city, Massachusetts (16000US2507000), resident workers
age 16+ reporting bicycle as their usual means of transportation to work.
These are estimated people, not trips, Bluebikes users, or inbound commuters.

DATA verified against original Census downloads, October 19, 2026:
2002-03: annual pre-full-implementation ACS base tables P047 (total row1,
  bicycle row13). 2004-05: B08006 (total row1, bicycle row18).
2006-09: ACS 1-year B08006 (total row1, bicycle row14).
2010-19 and 2021-24: ACS 1-year B08301 (total row1, bicycle row18).
Percent = 100 * bicycle workers / all resident workers age 16+, including
those who worked at home. This is standard commuting mode share, not a
percentage of trips or of the entire city population (which includes children).
2020 has no standard ACS 1-year estimate; missing data are not interpolated.
Pre-2005 estimates come from the earlier, smaller ACS program. ACS added
group quarters in 2006; this is a population-coverage change in the series.
Counts and percentages are sample-based estimates, not full enumerations.
Uncertainty intervals are omitted from the figure, not assumed to be zero.
Annotations indicate timing and do not demonstrate causation.

Source files (Boston city GEOID 16000US2507000, or 1600000US2507000):
2002-04: https://www2.census.gov/acs/downloads/Core_Tables/{YEAR}/BaseTables160{YEAR}.csv
2005: https://www2.census.gov/acs2005/summaryfile/Massachusetts/ma0000022.2005-1yr.zip
2006: https://www2.census.gov/acs2006/summaryfile/Massachusetts/20061ma0029000.zip
2007-08: https://www2.census.gov/acs{YEAR}_1yr/summaryfile/Massachusetts/{YEAR}1ma0033000.zip
2009: https://www2.census.gov/acs2009_1yr/summaryfile/Seq_By_ST/MA/20091ma0033000.zip
2010-12: https://www2.census.gov/acs{YEAR}_1yr/summaryfile/{YEAR}_ACSSF_By_State_By_Sequence_Table_Subset/Massachusetts/
2013-19: https://www2.census.gov/programs-surveys/acs/summary_file/{YEAR}/data/1_year_seq_by_state/Massachusetts/
2021-24: https://www2.census.gov/programs-surveys/acs/summary_file/{YEAR}/table-based-SF/data/1YRData/acsdt1y{YEAR}-b08301.dat
For sequence files, select the geography's LOGRECNO. B08301 starts at CSV
column124 (1-based): sequence0042 in2010, 0041 in2011-12, 0040 in2013,
0037 in2014-18, and0036 in2019. Use each year's geographic file to resolve
LOGRECNO; it changes across years. Table-based files include GEO_ID directly.
Milestones:
https://bikeleague.org/in-time-for-bike-month-new-bicycle-friendly-communities/
https://bluebikes.com/about
https://www.census.gov/newsroom/press-releases/2022/people-working-from-home.html
https://www.boston.gov/departments/transportation/project/berkeley-street-better-bike-lane
https://www.boston.gov/departments/transportation/bluebikes
https://bluebikes.com/blog/the-ebike-boom-has-arrived-in-metro-boston
Recent milestones: pandemic commuting disruption began in March 2020;
Wu announced 9.4 miles of bike lanes and a 100-station Bluebikes expansion
in September 2022 (an announcement, not a completion date); Bluebikes began
rolling out ebikes on December 20, 2023. The 2021 ACS estimate is lower than
2019; the chart does not isolate COVID's causal effect or measure all cycling.
Latest release status:
https://www.census.gov/programs-surveys/acs/news/data-releases/2025/release-schedule.html
"""

import argparse
from datetime import date
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator, StrMethodFormatter, PercentFormatter

# (year, estimated bicycle commuters, all resident workers age 16+).
# Total workers includes people working at home; None denotes missing data.
DATA = [
    (2002, 2541, 263199),
    (2003, 2707, 268345),
    (2004, 2360, 265223),
    (2005, 2377, 253201),
    (2006, 3495, 286969),
    (2007, 2900, 304214),
    (2008, 4946, 318133),
    (2009, 7156, 338393),
    (2010, 4369, 309620),
    (2011, 5399, 311164),
    (2012, 6536, 326427),
    (2013, 6662, 341777),
    (2014, 8141, 337826),
    (2015, 5596, 360257),
    (2016, 8873, 362198),
    (2017, 7990, 371220),
    (2018, 8623, 376159),
    (2019, 9852, 400910),
    (2020, None, None),
    (2021, 5616, 349759),
    (2022, 9616, 363511),
    (2023, 9576, 380182),
    (2024, 10655, 378248),
]


def make_chart(output: Path) -> None:
    plt.rcParams.update({
        "font.family": "DejaVu Sans", "font.size": 11,
        "axes.labelsize": 11, "axes.spines.top": False,
        "axes.spines.right": False, "savefig.facecolor": "white",
    })
    fig, ax = plt.subplots(figsize=(14, 8.6), facecolor="white")
    fig.subplots_adjust(left=0.08, right=0.90, top=0.76, bottom=0.25)
    fig.text(0.09, 0.935, "Boston residents commuting by bicycle",
             fontsize=22, weight="bold", color="#152C3D")
    fig.text(0.09, 0.887, "2002–2024 · Annual counts and commuting mode share · Boston city proper",
             fontsize=12, color="#4C5D6A")

    ax.set_xlim(2001.5, 2024.7)
    ax.set_ylim(0, 13000)
    ax.yaxis.set_major_locator(MultipleLocator(2000))
    ax.yaxis.set_major_formatter(StrMethodFormatter("{x:,.0f}"))
    ax.set_xticks(list(range(2002, 2025, 2)))
    ax.xaxis.set_minor_locator(MultipleLocator(1))
    ax.set_xlabel("Year", labelpad=12)
    ax.set_ylabel("Estimated bike commuters", labelpad=12, color="#087E8B")
    ax.grid(axis="y", color="#E3E8EB", linewidth=0.8)
    ax.set_axisbelow(True)
    ax.tick_params(axis="both", colors="#4C5D6A", length=0, pad=9)
    ax.tick_params(axis="x", which="minor", length=3, color="#A4AFB6")
    for edge in ["bottom", "left"]:
        ax.spines[edge].set_color("#BBC4CB")

    # Original milestones retain annual positions. Recent dated events use
    # decimal years; March 1 is a month-level marker, not a lockdown date.
    for year, label, y in [
        (2007, "2007\nBoston Bikes\nprogram begins", 11300),
        (2011, "2011\nHubway launches\n(now Bluebikes)", 12400),
    ]:
        ax.axvline(year, color="#A46D2A", linewidth=1.4,
                   linestyle=(0, (4, 4)), zorder=1)
        ax.text(year + 0.22, y, label, ha="left", va="top",
                fontsize=10.5, linespacing=1.35, color="#80531D",
                bbox={"facecolor": "white", "edgecolor": "none", "pad": 3})

    def decimal_year(d: date) -> float:
        start, end = date(d.year, 1, 1), date(d.year + 1, 1, 1)
        return d.year + (d - start).days / (end - start).days

    covid = decimal_year(date(2020, 3, 1))
    wu = decimal_year(date(2022, 9, 6))
    ebikes = decimal_year(date(2023, 12, 20))
    for year, color in [(covid, "#A25454"), (wu, "#A46D2A"), (ebikes, "#A46D2A")]:
        ax.axvline(year, color=color, linewidth=1.4,
                   linestyle=(0, (4, 4)), zorder=1)
    ax.text(covid - 0.22, 12400,
            "Mar 2020\nCOVID-19 disrupts commuting\nLower estimate in 2021",
            ha="right", va="top", fontsize=10.5, linespacing=1.35,
            color="#914545",
            bbox={"facecolor": "white", "edgecolor": "none", "pad": 3})
    # A label above the plot separates the two closely spaced recent policies.
    ax.plot([wu, wu], [1, 1.035], transform=ax.get_xaxis_transform(),
            color="#A46D2A", linestyle=(0, (4, 4)), linewidth=1.4, clip_on=False)
    ax.text(wu + 0.2, 1.055,
            "Sep 2022 · Mayor Wu announces\n9.4 miles of bike lanes + 100 Bluebikes stations",
            transform=ax.get_xaxis_transform(), ha="right", va="bottom",
            fontsize=10.5, linespacing=1.35, color="#80531D", clip_on=False)
    ax.text(ebikes - 0.22, 4500,
            "Dec 2023\nBluebikes e-bike\nrollout begins",
            ha="right", va="top", fontsize=10.5, linespacing=1.35,
            color="#80531D",
            bbox={"facecolor": "white", "edgecolor": "none", "pad": 3})

    years = [year for year, count, total in DATA]
    counts = [float("nan") if count is None else count for year, count, total in DATA]
    count_line, = ax.plot(years, counts, label="Bike commuters · left axis", color="#087E8B", linewidth=2.5,
            marker="o", markersize=5.5, markeredgecolor="white",
            markeredgewidth=0.8, zorder=3)
    # Both axes start at zero; their different units are shown explicitly.
    pct = [float("nan") if count is None else 100 * count / total
           for year, count, total in DATA]
    ax2 = ax.twinx()
    ax2.set_ylim(0, 4)
    ax2.yaxis.set_major_locator(MultipleLocator(0.5))
    ax2.yaxis.set_major_formatter(PercentFormatter(xmax=100, decimals=1))
    ax2.set_ylabel("Bike commuters as % of all workers age 16+", labelpad=13,
                   color="#8876A8")
    ax2.tick_params(axis="y", colors="#8876A8", length=0, pad=9)
    ax2.spines["right"].set_visible(True)
    ax2.spines["right"].set_color("#C8BED8")
    ax2.spines["left"].set_visible(False)
    ax2.spines["bottom"].set_visible(False)
    pct_line, = ax2.plot(years, pct, color="#9985BB", alpha=0.55,
                        linewidth=2, linestyle="--", marker="o", markersize=4,
                        label="Share of workers · right axis", zorder=2)
    ax2.annotate(f"{pct[-1]:.2f}%", (years[-1], pct[-1]), xytext=(-4, -18),
                 textcoords="offset points", ha="right", color="#8876A8",
                 bbox={"facecolor": "white", "edgecolor": "none", "pad": 2})
    fig.legend(handles=[count_line, pct_line], loc="upper left",
               bbox_to_anchor=(0.08, 0.855), ncol=2, frameon=False, fontsize=10)
    ax.annotate("2,541", (2002, 2541), xytext=(0, -18),
                textcoords="offset points", ha="center", color="#155965")
    ax.annotate("10,655", (2024, 10655), xytext=(-4, 13),
                textcoords="offset points", ha="right", color="#155965",
                weight="bold", bbox={"facecolor": "white", "edgecolor": "none", "pad": 2})
    for year, text in [(2020, "2020\nno standard estimate")]:
        ax.text(year, 400, text, ha="center", va="bottom", fontsize=9,
                color="#687984", linespacing=1.25,
                bbox={"facecolor": "white", "edgecolor": "none", "pad": 2})

    fig.text(0.09, 0.145,
             "Percent = bike commuters ÷ all Boston resident workers age 16+ (including work from home) × 100.",
             fontsize=9, color="#465763")
    fig.text(0.09, 0.115,
             "ACS measures usual commute mode for people, not trips. Sample-based estimates; uncertainty intervals are not shown.",
             fontsize=9, color="#465763")
    fig.text(0.09, 0.085,
             "2020 gap is not zero. Pre-2005 coverage differs; group quarters added in 2006. Event lines do not establish causation.",
             fontsize=9, color="#465763")
    fig.text(0.09, 0.045,
             "Source: U.S. Census Bureau ACS annual estimates. Full data and source-file references in the companion Python script.",
             fontsize=8.5, color="#687984")
    output.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(output, dpi=240, facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__,
                                     formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--output", type=Path,
                        default=Path("boston_bike_commuters.png"))
    args = parser.parse_args()
    make_chart(args.output)
    print(f"Saved {args.output.resolve()}")
