import streamlit as st
import pandas as pd
import plotly.express as px
import altair as alt
H_data=pd.read_csv('delhi/vehicles.csv')
H_data.set_index('Year')
H_data= H_data.applymap(lambda val: str(val).replace(',', '').strip())
H_data= H_data.applymap(lambda val: str(val).replace('-', '0').replace(',', '').strip())
H_data = H_data.replace('-', '0')
H_data = H_data.replace(',', '', regex=True)
H_data = H_data.apply(pd.to_numeric, errors='coerce')
H_data = H_data.fillna(0)
H_data = H_data.astype(int)

st.set_page_config(layout='wide')
st.write("""
# Vehicle Stock and Emission

This dashboard predicts the **vehicle stock** of **Delhi**!
""")
petrol_df = pd.read_csv("delhi/petrol.csv")

vehicle_config = {
    ("2-Wheeler", "Petrol"): {
        "pos": "2w",
        'fuel_df':pd.read_csv('delhi/petrol.csv'),
        "bs_2_em": 0.0313,
        "bs_4_em": 0.0313,
        "bs_6_em": 0.0045,
        "mileage": 9900
    },
    ("2-Wheeler", "Electric"): {
        'pos':'2w',
        'fuel_df':pd.read_csv('delhi/electric.csv'),
        "bs_2_em": 0,
        "bs_4_em": 0,
        "bs_6_em": 0,
        "mileage": 9900
    },
    ("Car", "Petrol"): {
        "pos": "car",
        'fuel_df':pd.read_csv('delhi/petrol.csv'),
        "bs_2_em": 0.0367,
        "bs_4_em": 0.0367,
        "bs_6_em": 0.0045,
        "mileage": 11550
    },
    ("Car", "Diesel"): {
        "pos": "car",
        'fuel_df':pd.read_csv('delhi/diesel.csv'),
        "bs_2_em": 0.0741,
        "bs_4_em": 0.0741,
        "bs_6_em": 0.0045,
        "mileage": 11550
    },
    ('Car','CNG'):{
        "pos": "car",
        'fuel_df':pd.read_csv('delhi/CNG.csv'),
        "bs_2_em": 0.0126,
        "bs_4_em": 0.0126,
        "bs_6_em": 0.0045,
        "mileage": 11550  
    },
    ('Car','Electric'):{
        "pos": "car",
        'fuel_df':pd.read_csv('delhi/electric.csv'),
        "bs_2_em": 0,
        "bs_4_em": 0,
        "bs_6_em": 0,
        "mileage": 11550  
    },
    ("Bus", "Diesel"): {
        "pos": "bus",
        'fuel_df':pd.read_csv('delhi/diesel.csv'),
        "bs_2_em": 0.0520,
        "bs_4_em": 0.0520,
        "bs_6_em": 0.0172,
        "mileage": 74250
    },
    ("Bus", "CNG"): {
        "pos": "bus",
        'fuel_df':pd.read_csv('delhi/CNG.csv'),
        "bs_2_em": 0.0520,
        "bs_4_em": 0.0520,
        "bs_6_em": 0.0172,
        "mileage": 74250
    },
    ("Bus", "Electric"): {
        "pos": "bus",
        'fuel_df':pd.read_csv('delhi/electric.csv'),
        "bs_2_em": 0,
        "bs_4_em": 0,
        "bs_6_em": 0,
        "mileage": 74250
    },
    ("Taxi", "Diesel"): {
        "pos": "taxi",
        'fuel_df':pd.read_csv('delhi/diesel.csv'),
        "bs_2_em": 0.0367,
        "bs_4_em": 0.0367,
        "bs_6_em": 0.0045,
        "mileage": 66000
    },
    ("Taxi", "Petrol"): {
        "pos": "taxi",
        'fuel_df':pd.read_csv('delhi/petrol.csv'),
        "bs_2_em": 0.0367,
        "bs_4_em": 0.0367,
        "bs_6_em": 0.0045,
        "mileage": 66000
    },
    ("Taxi", "CNG"): {
        "pos": "taxi",
        'fuel_df':pd.read_csv('delhi/CNG.csv'),
        "bs_2_em": 0.0126,
        "bs_4_em": 0.0126,
        "bs_6_em": 0.0045,
        "mileage": 66000
    },
    ("Taxi", "Electric"): {
        "pos": "taxi",
        'fuel_df':pd.read_csv('delhi/electric.csv'),
        "bs_2_em": 0,
        "bs_4_em": 0,
        "bs_6_em": 0,
        "mileage": 66000
    },
    ("3-Wheeler-Passanger", "Petrol"): {
        "pos": "3wp",
        'fuel_df':pd.read_csv('delhi/petrol.csv'),
        "bs_2_em": 0.0590,
        "bs_4_em": 0.0590,
        "bs_6_em": 0.0250,
        "mileage": 33000
    },
    ("3-Wheeler-Passanger", "CNG"): {
        "pos": "3wp",
        'fuel_df':pd.read_csv('delhi/CNG.csv'),
        "bs_2_em": 0.0590,
        "bs_4_em": 0.0590,
        "bs_6_em": 0.0250,
        "mileage": 33000
    },
    ("3-Wheeler-Passanger", "Electric"): {
        "pos": "3wp",
        'fuel_df':pd.read_csv('delhi/electric.csv'),
        "bs_2_em": 0,
        "bs_4_em": 0,
        "bs_6_em": 0,
        "mileage": 33000
    },
    ("3-Wheeler-Goods", "Petrol"): {
        "pos": "3wg",
        'fuel_df':pd.read_csv('delhi/petrol.csv'),
        "bs_2_em": 0.0590,
        "bs_4_em": 0.0590,
        "bs_6_em": 0.0250,
        "mileage": 33000
    },
    ("3-Wheeler-Goods", "CNG"): {
        "pos": "3wg",
        'fuel_df':pd.read_csv('delhi/CNG.csv'),
        "bs_2_em": 0.0590,
        "bs_4_em": 0.0590,
        "bs_6_em": 0.0250,
        "mileage": 33000
    },
    ("3-Wheeler-Goods", "Electric"): {
        "pos": "3wg",
        'fuel_df':pd.read_csv('delhi/electric.csv'),
        "bs_2_em": 0,
        "bs_4_em": 0,
        "bs_6_em": 0,
        "mileage": 33000
    },
    ("LGV", "Petrol"): {
        "pos": "lgv",
        'fuel_df':pd.read_csv('delhi/petrol.csv'),
        "bs_2_em": 0.0367,
        "bs_4_em": 0.0367,
        "bs_6_em": 0.0045,
        "mileage": 16500
    },
    ("LGV", "Diesel"): {
        "pos": "lgv",
        'fuel_df':pd.read_csv('delhi/diesel.csv'),
        "bs_2_em": 0.0741,
        "bs_4_em": 0.0741,
        "bs_6_em": 0.0045,
        "mileage": 16500
    },
    ('LGV','CNG'):{
        "pos": "lgv",
        'fuel_df':pd.read_csv('delhi/CNG.csv'),
        "bs_2_em": 0.0126,
        "bs_4_em": 0.0126,
        "bs_6_em": 0.0045,
        "mileage": 16500  
    },
    ('LGV','Electric'):{
        "pos": "lgv",
        'fuel_df':pd.read_csv('delhi/electric.csv'),
        "bs_2_em": 0,
        "bs_4_em": 0,
        "bs_6_em": 0,
        "mileage": 16500  
    }
  }

#### USER INPUT MANAGEMENT ####

st.subheader('Filters', divider='gray')
col1,col2,col3=st.columns(3,gap='small',vertical_alignment='center')
with col1:
  type=st.selectbox('VEHICLE TYPE',('2-Wheeler','Car',"LGV",'3-Wheeler-Passanger',"3-Wheeler-Goods",'Bus','Taxi'))
with col2:
  fuel = st.selectbox('Fuel', ('Total stock','Petrol','Electric','CNG','Diesel'))
with col3:
  year1 = st.selectbox('year', (2000,2001,2002,2003,2004,2005,2006,2007,2008,2009,2010,2011,2012,2013,2014,2015,2016,2017,2018,2019,2020,2021,2022,2023,2024,2025,2026,2027,2028,2029,2030,2031,2032,2033,2034,2035,2036,2037,2038,2039,2040))

data = {'Fuel': fuel,'Year':year1,'Vehicle Type':type}
features = pd.DataFrame(data, index=[0])
#df = user_input_features()


#st.markdown('User Input parameters')
#st.write(features)



def total_stock(y,fuel_df,pos):
   survival_df=pd.read_csv('delhi/survival.csv')
   total=0
   s_index=(y-2000)

   for i in range(0,(y-2000)+1): 
      if y<2000:
        break
      else: 
        split=fuel_df.at[i,pos]
        survival=survival_df.at[s_index,pos]
        total+= H_data.at[i, pos]*split*survival
      y-=1
      s_index-=1
   return total

def emission(y,fuel_df,bs_2_em,bs_4_em,bs_6_em,mileage):
  survival_df=pd.read_csv('delhi/survival.csv')
  bs_2=0
  bs_4=0
  bs_6=0
  s_index=(y-2000)
  year=2000
  for i in range(0,(y-2000)+1):
    if y<2000:
      break 
    else:
      split=fuel_df.at[i,pos]
      survival=survival_df.at[s_index,pos]
      t=H_data.at[i, pos]*split*survival
      if year<2010:
        bs_2+=t
      elif year<2018:
        bs_4+=t
        print('bs4:',bs_4)
      else:
        bs_6+=t
    y-=1
    year+=1
    s_index-=1

  data={'BS-II & BS-III':int(bs_2),'BS-IV':int(bs_4),'BS-VI':int(bs_6)}
  data_emission={'BS-II & BS-III':(((bs_2)*bs_2_em*mileage)/(10**6)),'BS-IV':(((bs_4)*bs_4_em*mileage)/(10**6)),'BS-VI':(((bs_6)*bs_6_em*mileage)/(10**6))}
  emission_total=(((bs_2)*bs_2_em*mileage)/(10**6))+(((bs_4)*bs_4_em*mileage)/(10**6))+(((bs_6)*bs_6_em*mileage)/(10**6))
  data_emission={'BS-II & BS-III':(((bs_2)*bs_2_em*mileage)/(10**6)),'BS-IV':(((bs_4)*bs_4_em*mileage)/(10**6)),'BS-VI':(((bs_6)*bs_6_em*mileage)/(10**6))}
  full_data=pd.DataFrame([data,data_emission],index=['stock','emission'])
  return full_data,emission_total






def emission_total_fuel(y):
  survival_df=pd.read_csv('delhi/survival.csv')
  bs_2=0
  bs_4=0
  bs_6=0
  s_index=(y-2000)
  year=2000
  for i in range(0,(y-2000)+1):
    if y<2000:
      break 
    else:
      split=fuel_df.at[i,pos]
      survival=survival_df.at[s_index,pos]
      t=H_data.at[i, pos]*split*survival
      if year<2010:
        bs_2+=t
      elif year<2018:
        bs_4+=t
        print('bs4:',bs_4)
      else:
        bs_6+=t
    y-=1
    year+=1
    s_index-=1

####DATA MANAGEMENT####

key_filters=(type,fuel)


if fuel=='Electric':
  config=vehicle_config[key_filters]
  pos=config['pos']
  y=year1
  reg_data=H_data.at[year1-2000,pos]
  fuel_df=pd.read_csv('delhi/electric.csv')
  split=fuel_df.at[year1-2000,pos]
  reg_data=reg_data*split
  stock=total_stock(y,fuel_df,pos)
  stock=int(stock)
  stockd = pd.DataFrame({'Total registration':int(reg_data),'Total stock':int(stock)},index=[0])
  c1,c2=st.columns(2,gap='small',vertical_alignment='center')
  with c1:
    st.metric(label='Total Registration',value=int(reg_data))
  with c2:
    st.metric(label='Total Stock',value=int(stock))
  st.write('Emissions standards do not apply.')


elif key_filters in vehicle_config.keys():
  config=vehicle_config[key_filters]
  fuel_df=config['fuel_df']
  bs_2_em=config['bs_2_em']
  bs_4_em=config['bs_4_em']
  bs_6_em=config['bs_6_em']
  pos=config['pos']
  mileage=config['mileage']
  y=year1
  reg_data=H_data.at[year1-2000,pos]
  split=fuel_df.at[year1-2000,pos]
  reg_data=reg_data*split
  stock=total_stock(y,fuel_df,pos)
  stock=int(stock)
  a,p=emission(y,fuel_df,bs_2_em,bs_4_em,bs_6_em,mileage)
  stockd = pd.DataFrame({'Total registration':int(reg_data),'Total stock':stock},index=[0])
  #st.subheader('total stock in the given year')
  bs_2=a.at['stock','BS-II & BS-III']
  bs_4=a.at['stock','BS-IV']
  bs_6=a.at['stock','BS-VI']
  bs_2_emission=a.at['emission','BS-II & BS-III']
  bs_4_emission=a.at['emission','BS-IV']
  bs_6_emission=a.at['emission','BS-VI']
  c1,c2=st.columns(2,gap='small',vertical_alignment='center')
  with c1:
    st.metric(label='Total Registration',value=f"{int(reg_data):,}")
  with c2:
    st.metric(label='Total Stock',value=f'{int(stock):,}')
  
  st.write(a)


  source_stock = pd.DataFrame({"category": ['BS-II & BS-III','BS-IV','BS_VI'], "value": [bs_2,bs_4,bs_6]})
  source_emission = pd.DataFrame({"category": ['BS-II & BS-III','BS-IV','BS_VI'], "value": [bs_2_emission,bs_4_emission,bs_6_emission]})
  tab1, tab2 = st.tabs(["Norm wise stock", "Norm wise emissions"])
  with tab1:
    fig1= px.pie(source_stock, names='category', values='value',hole=0.5,color='category',color_discrete_map=
                {'BS-II & BS-III': '#e85724',
                  'BS-IV': '#7F7F7F',
                  'BS_VI':'#029bd6'})                                                                                                 
    fig1.update_traces(textinfo='percent + value')
    fig1.update_layout(title_text='Norm-wise Stock')
    fig1.update_layout(legend=dict(
      orientation="h",
      yanchor="bottom",
      y=-0.1,
      xanchor="center",
      x=0.5
  ))
    st.plotly_chart(fig1)
  with tab2:
    fig1= px.pie(source_emission, names='category', values='value',hole=0.5,color='category',color_discrete_map=
                {'BS-II & BS-III': '#029bd6',
                  'BS-IV': '#7F7F7F',
                  'BS_VI':'#e85724'})                                                                                                 
    fig1.update_traces(textinfo='percent + value')
    fig1.update_layout(title_text='Norm-wise emission in tons/yr')
    fig1.update_layout(legend=dict(
      orientation="h",
      yanchor="bottom",
      y=-0.1,
      xanchor="center",
      x=0.5
  ))
    st.plotly_chart(fig1)
  


elif fuel=='Total stock':
  y=year1
  bs_2=0
  bs_4=0
  bs_6=0
  bs_2_emission=0
  bs_4_emission=0
  bs_6_emission=0
  key_filters=(type,'Petrol')
  if key_filters in vehicle_config.keys():
    config=vehicle_config[key_filters]
    fuel_df=config['fuel_df']
    bs_2_em=config['bs_2_em']
    bs_4_em=config['bs_4_em']
    bs_6_em=config['bs_6_em']
    pos=config['pos']
    mileage=config['mileage']
    a,p=emission(y,fuel_df,bs_2_em,bs_4_em,bs_6_em,mileage)
    bs_2+=a.at['stock','BS-II & BS-III']
    bs_4+=a.at['stock','BS-IV']
    bs_6+=a.at['stock','BS-VI']
    bs_2_emission+=a.at['emission','BS-II & BS-III']
    bs_4_emission+=a.at['emission','BS-IV']
    bs_6_emission+=a.at['emission','BS-VI']
  key_filters=(type,'Diesel')
  if key_filters in vehicle_config.keys():
    config=vehicle_config[key_filters]
    fuel_df=config['fuel_df']
    bs_2_em=config['bs_2_em']
    bs_4_em=config['bs_4_em']
    bs_6_em=config['bs_6_em']
    pos=config['pos']
    mileage=config['mileage']
    a,p=emission(y,fuel_df,bs_2_em,bs_4_em,bs_6_em,mileage)
    bs_2+=a.at['stock','BS-II & BS-III']
    bs_4+=a.at['stock','BS-IV']
    bs_6+=a.at['stock','BS-VI']
    bs_2_emission+=a.at['emission','BS-II & BS-III']
    bs_4_emission+=a.at['emission','BS-IV']
    bs_6_emission+=a.at['emission','BS-VI']
  key_filters=(type,'CNG')
  if key_filters in vehicle_config.keys():
    config=vehicle_config[key_filters]
    fuel_df=config['fuel_df']
    bs_2_em=config['bs_2_em']
    bs_4_em=config['bs_4_em']
    bs_6_em=config['bs_6_em']
    pos=config['pos']
    mileage=config['mileage']
    a,p=emission(y,fuel_df,bs_2_em,bs_4_em,bs_6_em,mileage)
    bs_2+=a.at['stock','BS-II & BS-III']
    bs_4+=a.at['stock','BS-IV']
    bs_6+=a.at['stock','BS-VI']
    bs_2_emission+=a.at['emission','BS-II & BS-III']
    bs_4_emission+=a.at['emission','BS-IV']
    bs_6_emission+=a.at['emission','BS-VI']
  reg_data=H_data.at[year1-2000,pos]
  fuel_df=pd.read_csv('delhi/total.csv')
  stock=total_stock(y,fuel_df,pos)



  c1,c2=st.columns(2,gap='small',vertical_alignment='center')
  with c1:
    st.metric(label='Total Registration',value=f"{int(reg_data):,}")
  with c2:
    st.metric(label='Total Stock',value=f"{int(stock):,}")
  data={'BS-II & BS-III':int(bs_2),'BS-IV':int(bs_4),'BS_VI':(bs_6)}
  data_emission={'BS-II & BS-III':bs_2_emission,'BS-IV':bs_4_emission,'BS_VI':bs_6_emission}
  full_data=pd.DataFrame([data,data_emission],index=['stock','emission'])
  st.write(full_data)
  source_stock = pd.DataFrame({"category": ['BS-II & BS-III','BS-IV','BS_VI'], "value": [bs_2,bs_4,bs_6]})
  source_emission = pd.DataFrame({"category": ['BS-II & BS-III','BS-IV','BS_VI'], "value": [bs_2_emission,bs_4_emission,bs_6_emission]})
  tab1, tab2 = st.tabs(["Norm wise stock", "Norm wise emissions"])

  with tab1:
    fig1= px.pie(source_stock, names='category', values='value',hole=0.5,color='category',color_discrete_map=
                {'BS-II & BS-III':'#e85724' ,
                  'BS-IV': '#7F7F7F',
                  'BS_VI':'#029bd6'})
                                                                                                    
    fig1.update_traces(textinfo='percent')
    fig1.update_layout(title_text='Norm-wise Stock')
    fig1.update_layout(legend=dict(
      orientation="h",
      yanchor="bottom",
      y=-0.1,
      xanchor="center",
      x=0.5
  ))
    st.plotly_chart(fig1)
  with tab2:
    fig1= px.pie(source_emission, names='category', values='value',hole=0.5,color='category',color_discrete_map=
                {'BS-II & BS-III': '#e85724',
                  'BS-IV': '#7F7F7F',
                  'BS_VI':'#029bd6'})
                                                                                                    
    fig1.update_traces(textinfo='percent')
    fig1.update_layout(title_text='Norm-wise emission in tons/yr')
    fig1.update_layout(legend=dict(
      orientation="h",
      yanchor="bottom",
      y=-0.1,
      xanchor="center",
      x=0.5
  ))
    st.plotly_chart(fig1)
else:
  st.write('Data of the selected combination of vehicle type and fuel is not available')


























