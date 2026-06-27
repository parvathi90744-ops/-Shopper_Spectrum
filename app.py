import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(page_title="Shopper Spectrum", layout="wide")

st.title("🛒 Shopper Spectrum")
st.markdown("### Customer Segmentation using K-Means Clustering")
st.markdown("---")

# Load customer segments
rfm = pd.read_csv("Data/customer_segments.csv")
st.write("### Dataset Information")

col1, col2 = st.columns(2)

with col1:
    st.metric("Total Customers", len(rfm))

with col2:
    st.metric("Number of Segments", rfm["Cluster"].nunique())
    st.write("### Customer Distribution by Cluster")

cluster_count = rfm["Cluster"].value_counts().sort_index()

st.bar_chart(cluster_count)
fig, ax = plt.subplots()

cluster_count.plot(
    kind="pie",
    autopct="%1.1f%%",
    ax=ax
)

ax.set_ylabel("")

st.pyplot(fig)

st.write("### Filter Customers by Cluster")

selected_cluster = st.selectbox(
    "Choose a Cluster",
    sorted(rfm["Cluster"].unique())
)

filtered_data = rfm[rfm["Cluster"] == selected_cluster]

st.dataframe(filtered_data)

st.download_button(
    label="📥 Download Filtered Data",
    data=filtered_data.to_csv(index=False),
    file_name="customer_segments.csv",
    mime="text/csv"
)   
st.write("### Cluster Description")

cluster_info = {
    0: "🏆 High Value Customers - Frequent buyers who spend the most.",
    1: "😊 Regular Customers - Purchase regularly with moderate spending.",
    2: "⚠️ At Risk Customers - Haven't purchased recently and may leave.",
    3: "🌱 New / Low Value Customers - New or infrequent buyers."
}

st.info(cluster_info[selected_cluster])
# Scatter Plot
st.write("### Customer Segments Visualization")

fig, ax = plt.subplots(figsize=(8,6))

scatter = ax.scatter(
    rfm["Frequency"],
    rfm["Monetary"],
    c=rfm["Cluster"],
    cmap="viridis",
    s=60,
    alpha=0.7
)

ax.set_xlabel("Frequency")
ax.set_ylabel("Monetary")
ax.set_title("Customer Segments")

plt.colorbar(scatter)

st.pyplot(fig)