import pandas as pd
import seaborn as sb
import matplotlib.pyplot as plt
df=pd.read_csv("dataset/Coffe_sales.csv")
print(df.head(10))
"""
   hour_of_day cash_type  money          coffee_name Time_of_Day Weekday Month_name  Weekdaysort  Monthsort        Date             Time
0           10      card   38.7                Latte     Morning     Fri        Mar            5          3  2024-03-01  10:15:50.520000
1           12      card   38.7        Hot Chocolate   Afternoon     Fri        Mar            5          3  2024-03-01  12:19:22.539000
2           12      card   38.7        Hot Chocolate   Afternoon     Fri        Mar            5          3  2024-03-01  12:20:18.089000
3           13      card   28.9            Americano   Afternoon     Fri        Mar            5          3  2024-03-01  13:46:33.006000
4           13      card   38.7                Latte   Afternoon     Fri        Mar            5          3  2024-03-01  13:48:14.626000
5           15      card   33.8  Americano with Milk   Afternoon     Fri        Mar            5          3  2024-03-01  15:39:47.726000
6           16      card   38.7        Hot Chocolate   Afternoon     Fri        Mar            5          3  2024-03-01  16:19:02.756000
7           18      card   33.8  Americano with Milk       Night     Fri        Mar            5          3  2024-03-01  18:39:03.580000
8           19      card   38.7                Cocoa       Night     Fri        Mar            5          3  2024-03-01  19:22:01.762000
9           19      card   33.8  Americano with Milk       Night     Fri        Mar            5          3  2024-03-01  19:23:15.887000"""

print(df.describe())
"""
       hour_of_day        money  Weekdaysort    Monthsort
count  3547.000000  3547.000000  3547.000000  3547.000000
mean     14.185791    31.645216     3.845785     6.453905
std       4.234010     4.877754     1.971501     3.500754
min       6.000000    18.120000     1.000000     1.000000
25%      10.000000    27.920000     2.000000     3.000000
50%      14.000000    32.820000     4.000000     7.000000
75%      18.000000    35.760000     6.000000    10.000000
max      22.000000    38.700000     7.000000    12.000000"""
print(df.describe(include="all"))
"""
        hour_of_day cash_type        money          coffee_name Time_of_Day Weekday Month_name  Weekdaysort    Monthsort        Date             Time
count   3547.000000      3547  3547.000000                 3547        3547    3547       3547  3547.000000  3547.000000        3547             3547
unique          NaN         1          NaN                    8           3       7         12          NaN          NaN         381             3547
top             NaN      card          NaN  Americano with Milk   Afternoon     Tue        Mar          NaN          NaN  2024-10-11  10:15:50.520000
freq            NaN      3547          NaN                  809        1205     572        494          NaN          NaN          26                1
mean      14.185791       NaN    31.645216                  NaN         NaN     NaN        NaN     3.845785     6.453905         NaN              NaN
std        4.234010       NaN     4.877754                  NaN         NaN     NaN        NaN     1.971501     3.500754         NaN              NaN
min        6.000000       NaN    18.120000                  NaN         NaN     NaN        NaN     1.000000     1.000000         NaN              NaN
25%       10.000000       NaN    27.920000                  NaN         NaN     NaN        NaN     2.000000     3.000000         NaN              NaN
50%       14.000000       NaN    32.820000                  NaN         NaN     NaN        NaN     4.000000     7.000000         NaN              NaN
75%       18.000000       NaN    35.760000                  NaN         NaN     NaN        NaN     6.000000    10.000000         NaN              NaN
max       22.000000       NaN    38.700000                  NaN         NaN     NaN        NaN     7.000000    12.000000         NaN              NaN"""
print(df.columns)
"""
Index(['hour_of_day', 'cash_type', 'money', 'coffee_name', 'Time_of_Day',
       'Weekday', 'Month_name', 'Weekdaysort', 'Monthsort', 'Date', 'Time'],
      dtype='str')"""
print(df.isnull().sum())
"""
hour_of_day    0
cash_type      0
money          0
coffee_name    0
Time_of_Day    0
Weekday        0
Month_name     0
Weekdaysort    0
Monthsort      0
Date           0
Time           0
dtype: int64
THERE IS NO NULL VALUE"""
print(df.duplicated().sum())
# no repeated row
maindf=df.drop(columns=["Month_name"])

maindf["Date"]=pd.to_datetime(maindf["Date"],format="mixed")
maindf["coffee_name"] = maindf["coffee_name"].str.strip().str.lower()
print(maindf.head(10))
print("--------------")
print(maindf["cash_type"].value_counts())
"""
cash_type
card    3547
Name: count, dtype: int64

there is no cash, so we can drop this column"""
maindf=df.drop(columns=["cash_type"])
print(maindf["coffee_name"].value_counts())
"""
coffee_name
Americano with Milk    809
Latte                  757
Americano              564
Cappuccino             486
Cortado                287
Hot Chocolate          276
Cocoa                  239
Espresso               129
Name: count, dtype: int64

mostly ordered: americano with milk
least ordered: espresso"""

print(maindf.groupby("coffee_name")["money"].sum())
"""
coffee_name
Americano              14650.26
Americano with Milk    24751.12
Cappuccino             17439.14
Cocoa                   8521.16
Cortado                 7384.86
Espresso                2690.28
Hot Chocolate           9933.46
Latte                  26875.30
Name: money, dtype: float64

the most profitable coffee: Latte
the least profitable coffee: Espresso
"""
print(maindf.head(10))
#print(maindf.groupby("Weekdaysort").value_counts())
print(maindf.groupby("Time_of_Day")["money"].sum())
"""
Time_of_Day
Afternoon    38130.04
Morning      35929.20
Night        38186.34
Name: money, dtype: float64

the most profitable time of the day: Night
the least profitable time of day: Morning"""

print(maindf.groupby("Weekdaysort")["money"].sum().sort_values())
"""
Weekdaysort
7    13336.06
6    14733.52
3    15750.46
4    16091.40
5    16802.66
1    17363.10
2    18168.38
Name: money, dtype: float64
the most profitable day of the week: Tuesday
the least profitable day of the week: Sunday
"""

print(maindf.groupby(["coffee_name","Time_of_Day"])["money"].sum())
"""
coffee_name          Time_of_Day
Americano            Afternoon       6133.94
                     Morning         5643.10
                     Night           2873.22
Americano with Milk  Afternoon       7384.36
                     Morning        10025.52
                     Night           7341.24
Cappuccino           Afternoon       5910.70
                     Morning         4327.44
                     Night           7201.00
Cocoa                Afternoon       2685.92
                     Morning         2059.38
                     Night           3775.86
Cortado              Afternoon       2315.84
                     Morning         3605.46
                     Night           1463.56
Espresso             Afternoon       1189.16
                     Morning          873.72
                     Night            627.40
Hot Chocolate        Afternoon       2899.02
                     Morning         1744.40
                     Night           5290.04
Latte                Afternoon       9611.10
                     Morning         7650.18
                     Night           9614.02
Name: money, dtype: float64
"""
print(maindf.groupby(["Monthsort","coffee_name"])["money"].sum().to_string())
"""
Monthsort  coffee_name        
1          Americano               649.00 
           Americano with Milk    1604.72 
           Cappuccino              965.52
           Cocoa                   500.64
           Cortado                 571.12
           Espresso                105.30
           Hot Chocolate           536.40
           Latte                  1466.16
2          Americano              3037.32 
           Americano with Milk    2623.10
           Cappuccino             1859.52
           Cocoa                  2002.56
           Cortado                 259.60
           Espresso                358.02
           Hot Chocolate          1144.32
           Latte                  1931.04
3          Americano              3572.72 
           Americano with Milk    2618.72
           Cappuccino             2118.18
           Cocoa                  1305.00
           Cortado                 861.12
           Espresso                426.60
           Hot Chocolate          1596.48
           Latte                  3392.82
4          Americano               941.94
           Americano with Milk    1267.74
           Cappuccino             1381.44 
           Cocoa                   153.82
           Cortado                 458.48
           Espresso                 96.00
           Hot Chocolate           386.02
           Latte                  1034.12
5          Americano              1116.80
           Americano with Milk    1772.28
           Cappuccino             1961.44 
           Cocoa                   301.76
           Cortado                 474.64
           Espresso                161.14
           Hot Chocolate           490.36
           Latte                  1886.00 
6          Americano               390.88
           Americano with Milk    2166.12
           Cappuccino             1735.12
           Cocoa                   150.88
           Cortado                 530.48
           Espresso                230.20
           Hot Chocolate           528.08
           Latte                  1886.00
7          Americano               858.12
           Americano with Milk    1863.80 
           Cappuccino             1079.64
           Cocoa                   300.28
           Cortado                 322.28
           Espresso                273.28
           Hot Chocolate           361.02
           Latte                  1857.52
8          Americano               851.74
           Americano with Milk    2010.24 
           Cappuccino             1115.88
           Cocoa                   361.02
           Cortado                 920.80
           Espresso                253.68
           Hot Chocolate           196.92
           Latte                  1903.56
9          Americano               739.58
           Americano with Milk    2930.14
           Cappuccino             1360.32
           Cocoa                   298.32
           Cortado                 961.46
           Espresso                217.44
           Hot Chocolate           366.90
           Latte                  3114.48
10         Americano              1142.24
           Americano with Milk    2530.52
           Cappuccino             1573.44
           Cocoa                  1144.32
           Cortado                 882.64
           Espresso                252.72
           Hot Chocolate          2074.08
           Latte                  4291.20
11         Americano               649.00
           Americano with Milk    1604.72
           Cappuccino              929.76
           Cocoa                  1251.60
           Cortado                 337.48
           Espresso                 63.18
           Hot Chocolate          1323.12
           Latte                  2431.68
12         Americano               700.92
           Americano with Milk    1759.02
           Cappuccino             1358.88
           Cocoa                   750.96
           Cortado                 804.76
           Espresso                252.72
           Hot Chocolate           929.76
           Latte                  1680.72
           """
print(maindf.groupby(["coffee_name","Weekday"])["money"].sum())
"""
coffee_name          Weekday
Americano            Fri        2736.58
                     Mon        2422.12
                     Sat        1789.28
                     Sun        1188.28
                     Thu        2123.82
                     Tue        2109.62
                     Wed        2280.56
Americano with Milk  Fri        3162.90
                     Mon        3915.78
                     Sat        3719.86
                     Sun        3018.88
                     Thu        3156.04
                     Tue        4333.60
                     Wed        3444.06
Cappuccino           Fri        2223.00
                     Mon        2557.58
                     Sat        2492.92
                     Sun        2488.50
                     Thu        2748.62
                     Tue        2256.80
                     Wed        2671.72
Cocoa                Fri        1865.40
                     Mon        1205.06
                     Sat         816.60
                     Sun         849.42
                     Thu         819.54
                     Tue        2035.38
                     Wed         929.76
Cortado              Fri         966.40
                     Mon         918.40
                     Sat        1418.48
                     Sun        1074.64
                     Thu        1069.74
                     Tue        1132.44
                     Wed         804.76
Espresso             Fri         440.30
                     Mon         209.62
                     Sat         270.34
                     Sun         341.86
                     Thu         563.72
                     Tue         327.16
                     Wed         537.28
Hot Chocolate        Fri        1612.14
                     Mon        1246.70
                     Sat         869.02
                     Sun        1445.10
                     Thu        1727.26
                     Tue        1765.96
                     Wed        1267.28
Latte                Fri        3795.94
                     Mon        4887.84
                     Sat        3357.02
                     Sun        2929.38
                     Thu        3882.66
                     Tue        4207.42
                     Wed        3815.04
Name: money, dtype: float64
"""

coffee_sales = maindf.groupby("coffee_name")["money"].sum().sort_values(ascending=False)

plt.figure(figsize=(10,5))
sb.barplot(x=coffee_sales.index, y=coffee_sales.values)

plt.title("Total Revenue by Coffee Type")
plt.xlabel("Coffee Type")
plt.ylabel("Total Revenue")
plt.savefig("images/coffee_revenue.png")
plt.show()

hourly = maindf.groupby("hour_of_day")["money"].sum()

sb.lineplot(x=hourly.index, y=hourly.values)

plt.title("Total Revenue by Hour")
plt.xlabel("Hour of Day")
plt.ylabel("Total Revenue")
plt.savefig("images/hourly_revenue.png")
plt.show()

monthly = maindf.groupby("Monthsort")["money"].sum()

sb.barplot(x=monthly.index, y=monthly.values)

plt.title("Total Revenue by Month")
plt.xlabel("Months")
plt.ylabel("Total Revenue")
plt.savefig("images/monthly_revenue.png")
plt.show()

