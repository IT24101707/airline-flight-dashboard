✈️ Airline Flight Operations Dashboard

🚀 A real-time flight-schedule analysis project built to practice an end-to-end Business Analyst workflow — sourcing live data from an external API, processing it, documenting business requirements, and presenting insights through two different dashboard formats.

📌 What this project does
🌐 Pulls live flight data from the AviationStack API using Python
🧹 Cleans and analyzes the data with pandas (top airlines, busiest departure airports, flight status breakdown)
📊 Visualizes the findings two ways:
📈 Power BI dashboard
🌍 Custom-coded HTML/CSS dashboard
📝 Documents the business context in a full Business Requirements Document (BRD), including objectives, scope, methodology, key findings, and — importantly — the data's limitations
🎯 Why I built it this way

Real-world data is rarely perfect. ⚠️
The free-tier API used here returned only "scheduled" flights with almost no delay data, which meant a reliable on-time-performance metric wasn't possible from this snapshot.

Instead of estimating or fabricating results ❌, I clearly documented the data limitation in the BRD (BRD_Airline_Flight_Dashboard.docx).

👉 Being transparent about what the data can and cannot support is a core Business Analysis skill.

📊 Key findings
📌 Metric	📈 Value
✈️ Total flights captured	100
🏢 Distinct airlines	42
🛫 Distinct departure airports	18
🔥 Busiest departure airport	Tianjin Binhai International (32%)
📁 Files in this repo
📄 File	🧾 Description
flight_data.py	Pulls real-time flight data from the AviationStack API and saves it to CSV
analyze.py	Loads the CSV and prints summary statistics (top airlines, busiest airports, status breakdown)
flight_data.csv	The raw dataset captured during this run
flight_operations_dashboard.html	Custom-coded dashboard (open in any browser)
BRD_Airline_Flight_Dashboard.docx	Full Business Requirements Document
🛠 Tools used

🐍 Python (requests, pandas) · 🌐 AviationStack API · 📊 Power BI · 🎨 HTML/CSS

⚠️ Notes
🔐 API credentials are excluded from this repo (.env file, not uploaded) — you'll need your own free AviationStack API key to re-run flight_data.py.
⛔ This project uses the free API tier, which limits requests to 100/month and does not include historical flight data — see the BRD for full details.
