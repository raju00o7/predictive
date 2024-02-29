from helpers import *
from autots.autots import Dashboard

df = load_df('Data\Truck_sales.csv','%Y-%m')
app = Dashboard(df = df, image='assets/auto-ts-logo.png', title="Air Passengers", m=12, test_size=.20)
app.preprocess()
app.main()
