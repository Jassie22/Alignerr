# Professional Dark Business Dashboard

A modern, professional dark-themed business dashboard built with Python using only **pandas**, **numpy**, and **plotly** libraries.

## Features

- **Dark Professional Theme**: Clean, modern design with enhanced color palette
- **Interactive Visualizations**: 6 key performance indicators with interactive charts
- **Geographic User Distribution**: Map showing active users across the USA with intelligent clustering
- **Real-time Data**: Dynamic metrics for sales, social media, website analytics, and customer feedback
- **Responsive Layout**: Grid-based layout that adapts to different screen sizes

## Dashboard Components

### Left Panel
- **Sales Metrics**: Monthly sales ($297k), daily performance ($9.6k today, $20.6k yesterday)
- **NPS Score**: Interactive gauge showing Net Promoter Score (61)

### Right Panel
- **Biggest Deals**: Top sales representatives and their deal amounts
- **Social Followers**: LinkedIn (19.5k) and Twitter (10.5k) with growth indicators
- **Website Analytics**: 7-day user metrics (27.2k users, 126 enquiries)
- **Active Users Map**: Geographic distribution of users across the US with clustering
- **Recent Feedback**: Customer feedback with timestamps

## Technical Stack

- **Python 3.x**
- **pandas**: Data manipulation and analysis
- **numpy**: Numerical computing
- **plotly**: Interactive visualizations and charts

## File Structure

```
├── data/
│   ├── sales_data.csv          # Sales performance data
│   ├── deals_data.csv          # Individual deal records
│   ├── social_media_data.csv   # Social media metrics
│   ├── website_analytics.csv   # Website traffic data
│   ├── nps_data.csv           # Net Promoter Score data
│   ├── feedback_data.csv      # Customer feedback
│   ├── geographic_data.csv    # Geographic user distribution
│   └── *.npy                  # Numpy arrays for faster processing
├── scripts/
│   ├── data_gen.py            # Data generation script
│   └── viz.py                 # Dashboard visualization script
├── outputs/
│   └── dashboard.html         # Generated dashboard
└── README.md
```

## Installation & Usage

1. **Clone the repository**:
   ```bash
   git clone https://github.com/Jassie22/Alignerr.git
   cd Alignerr
   ```

2. **Install dependencies**:
   ```bash
   pip install pandas numpy plotly
   ```

3. **Generate sample data** (optional):
   ```bash
   python scripts/data_gen.py
   ```

4. **Create dashboard**:
   ```bash
   python scripts/viz.py
   ```

5. **View dashboard**:
   Open `outputs/dashboard.html` in your web browser

## Data Generation

The `data_gen.py` script creates realistic sample data including:
- **Sales Data**: Monthly sales figures with seasonal patterns
- **Deal Records**: Individual transactions with sales representatives
- **Social Media**: Growth patterns for LinkedIn and Twitter
- **Website Analytics**: Daily user engagement metrics
- **Geographic Data**: User distribution across US states and cities
- **Customer Feedback**: Timestamped feedback entries

## Visualization Features

- **Interactive Charts**: Hover effects and tooltips
- **Geographic Clustering**: User points intelligently group based on proximity
- **Real-time Updates**: Dashboard refreshes with current time
- **Professional Design**: Dark theme with consistent color scheme
- **Responsive Layout**: Adapts to different screen sizes

## Customization

The dashboard can be easily customized by:
- Updating color constants in `viz.py`
- Modifying data sources in the `data/` folder
- Adjusting chart parameters and layouts
- Adding new visualization components

## Dependencies

- **pandas**: Data manipulation and CSV handling
- **numpy**: Numerical operations and array processing
- **plotly**: Interactive charts and geographic visualizations

## Output

The dashboard generates a single HTML file (`outputs/dashboard.html`) that can be:
- Opened in any modern web browser
- Shared via email or file sharing
- Embedded in web applications
- Printed or exported as PDF

## Author

Built with attention to professional design and data visualization best practices. 