import time
import pandas as pd
import numpy as np
import calendar

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')   
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        city = input('choose a name city from (chicago ,new york city , or washington:)').lower()
        if city not in CITY_DATA:
            print('\n please choose a correct city name \n')
        else:
            break          
    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
      month = input("\nEnter a month from( January, February, March, April, May, June ,all)\n")
      if month not in ('January', 'February', 'March', 'April', 'May', 'June', 'all'):
        print("\n please choose a correct month name \n")
      else:
        break

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
      day = input("\nEnter a month from(Sunday, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday ,all \n")
      if day not in ('Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'all'):
        print("\n please choose a correct day name \n'.")
      else:
        break
        print('-'*40)

    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
   # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month, day of week and Hour from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name()
    

    # filter by month if applicable
    if month != 'all':
   	 	# use the index of the months list to get the corresponding int
        months = ['January', 'February', 'March', 'April', 'May', 'June']
        month = months.index(month) + 1
        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]
        
    return df

 #view raw data to user     
        
def time_stats(df):   
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    common_month = df['month'].mode()[0]
    print('Most common month:',common_month)
    
    # TO DO: display the most common day of week
    common_day = df['day_of_week'].mode()[0]
    print('Most Common day:', common_day)
     
    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    common_hour = df['hour'].mode()[0]
    print('Most Common start Hour:', common_hour) 
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    
    
def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start statio
    common_start = df['Start Station'].mode()[0]
    print('Most Commonly used start station:', common_start)

    # TO DO: display most commonly used end station
    common_end = df['End Station'].mode()[0]
    print('\nMost Commonly used end station:', common_end)

    # TO DO: display most frequent combination of start station and end station trip
    Common_start_end = (df['Start Station']+'_'+df['End Station']).mode()[0]
    print('\nMost Frequent Combination of start and end station:',Common_start_end)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    
    
def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    Total_Time = df['Trip Duration'].sum()
    print('Total travel time:', Total_Time)
    # TO DO: display mean travel time
    Mean_Time = df['Trip Duration'].mean()
    print('Mean travel time:', Mean_Time)
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    
    
def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()

    #print(user_types)
    print('User Types:\n', user_types)

    # TO DO: Display counts of gender
    if 'Gender' in df:
       print('\n Counts of Gender :\n',df['Gender'].value_counts())
    # TO DO: Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df:
      Earliest_Year =int( df['Birth Year'].min())
      print('\nEarliest Year:', Earliest_Year)
      Recent_Year = int(df['Birth Year'].max())
      print('\nMost Recent Year:', Recent_Year)
      common_year =int(df['Birth Year'].mode()[0])
      print('\ncommon year Year :\n ', common_year)
    
      print("\nThis took %s seconds." % (time.time() - start_time)) 
      print('-'*40)
    
def display_row_data(df):
        row=0
        while True:
         view_row = input("Would you like to display the first 5 rows of data? yes/no :").lower()
       
         if view_row == "yes":
            print(df.iloc[row : row + 6])    
            row+=6        
         elif view_row =='no':
            break
        else:
            answer = input("Would you like to display next the first 5 rows of data? yes/no :").lower()  
            
def main():
    while True:
        city,month,day = get_filters()      
        df = load_data(city,month,day)
        
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_row_data(df)
 
        restart = input('\nWould you like to restart? Enter yes or no.\n').lower()
        if restart.lower() != 'yes':
            break
            
if __name__ == "__main__":
	 main()