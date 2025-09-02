
# Ground_Water_Network

## Description
This project analyzes groundwater monitoring points in Queensland, with a focus on Brisbane, using Python, pandas, seaborn, and folium for interactive geospatial visualization. The goal is to transform complex governmental data into an accessible and inclusive tool, benefiting both professionals and the general public by simplifying the understanding of groundwater networks.

## Key Features
- **Cluster Visualization**: Utilizes MarkerCluster in Folium to group nearby monitoring points, enhancing readability and reducing visual clutter on the map.
- **Inclusivity**: Designed to make data from the Queensland Government (available at data.qld.gov.au) accessible to non-experts through an interactive dashboard, moving away from traditional tables with thousands of rows.

## Structure
- `data/raw/groundwater.csv`: Raw dataset.
- `data/processed/groundwaterclean.csv`: Cleaned and processed dataset.
- `notebooks/groundwater.ipynb`: Exploratory data analysis notebook.
- `maps/ground_water_map.html`: Interactive map generated with Folium.
- `streamlit/dashboard.py`: Streamlit dashboard application.

## Dataset Official URL
- Site: https://www.data.qld.gov.au/dataset/hydrology-archive-data/resource/677ab124-9626-4099-b376-2c75d632783f?inner_span=True

## How to Run
1. Install the dependencies: `pip install -r streamlit/requirements.txt`.
2. Run the dashboard: `streamlit run streamlit/dashboard.py`.

## Contact
Wagner Luiz Apel - wagnerapel@gmail.com | https://www.linkedin.com/in/wagner-luiz-apel/ | https://github.com/wagnerluizapel

## Version
Version 1.0 - 01/09/2025