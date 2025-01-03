# Spotify Power BI Dashboard

This project showcases a Spotify dashboard built using Power BI. It integrates advanced techniques, including data enrichment using ChatGPT, custom HTML visuals, and a glass morphism background design. The dashboard is polished and interactive, leveraging Python, PowerPoint, and Power BI.

## Dashboard Features

### 1. Key Performance Indicators
- Displays the most streamed songs, artist statistics, and various audio features like danceability and energy.
- Includes year-on-year performance comparison with visually distinct KPIs.

### 2. Visual Insights
- **Bar Chart**: Tracks by stream count.
- **Line Chart**: Track releases over time.
- **Heat Map**: Tracks released per day of the week and month.
- **Custom HTML Visuals**: Album covers with rounded corners for enhanced aesthetics.

### 3. Interactivity
- Slicers for filtering by artist, track, year, and date.
- Clear All Slicers button for resetting filters.
- Responsive design with dynamic formatting tied to Power BI themes.

### 4. Tools and Technologies
- **Power BI**: For creating and hosting the dashboard.
- **ChatGPT**: To enrich data with album cover URLs and HTML code generation.
- **Python**: Used to fetch album cover URLs via Spotify Web API.
- **Deneb**: Custom visuals for advanced charts like unit charts and heat maps.
- **PowerPoint**: Glass morphism background design.

### 5. Key Insights
- Top streamed songs outperform yearly averages by significant percentages.
- Release trends indicate popular release days and months.
- Audio feature distribution provides insights into track characteristics.

### 6. Dataset
- **Source**: [Kaggle](https://www.kaggle.com/): Most Streamed Spotify Songs of 2023.
- **Details**: CSV file with 24 columns including track name, artist, streams, and more.
- **Enhancements**: Added album cover URLs via Spotify Web API.

### Steps
1. **Data Preparation**:
   - Download the dataset from Kaggle.
   - Enrich the dataset using ChatGPT and Python to include album cover URLs.
   - Ensure proper formatting for CSV files and Python scripts.

2. **Background Design**:
   - Use PowerPoint to create a glass morphism background.
   - Export the design as an image and apply it as the Power BI canvas background.

3. **Dashboard Creation**:
   - Import the dataset into Power BI.
   - Create a date column and a calendar table using SQL BI's Bravo tool.
   - Add visuals (charts, KPIs, slicers) to the dashboard.

4. **Custom Visuals**:
   - Use HTML visuals for album covers and Deneb visuals for unit charts and heat maps.
   - Modify DAX measures to include KPIs and performance comparisons.

5. **Final Touches**:
   - Customize themes, colors, and fonts for a cohesive design.
   - Add interactivity with slicers, buttons, and dynamic filters.
