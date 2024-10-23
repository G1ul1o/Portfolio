import streamlit as st
import pandas as pd
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import seaborn as sns
import folium
from streamlit_folium import st_folium
from st_clickable_images import clickable_images
from streamlit_option_menu import option_menu
import io
import missingno as msno
import plotly.express as px
from streamlit_pdf_viewer import pdf_viewer
