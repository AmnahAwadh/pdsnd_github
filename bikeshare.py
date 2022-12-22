'''
Amnah Alsulami
Programming for data scince nanodegree
'''
import time
import pandas as pd
import numpy as np

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
        CITY = input("Which city would you like to explore ?")
        if CITY.lower() in ['chicago', 'new york city', 'washington']:
            break
        else:
            print("invalid input. Please enter a valid input")

    # TO DO: get user input for month (all, january, february, ... , june)
    MONTH = input('Enter the month: ').lower()
    while MONTH not in ['all', 'january', 'february', 'march', 'april', 'may', 'june']:
        MONTH = input('Enter a correct month: january, february, ... , june ').lower()



    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    DAY = input('Enter the day : ').lower()
    while DAY not in ['all', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']:
        DAY = input('Enter a correct DAY: monday, tuesday, ... sunday ').lower()


    print('-'*40)
    return CITY, MONTH, DAY


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

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    common_month = df['month'].value_counts().idxmax()
    print("The most common month is: ", common_month)


    # TO DO: display the most common day of week
    common_day_of_week = df['day_of_week'].value_counts().idxmax()
    print("The most common day of week is: ", common_day_of_week)


    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    common_hour = df['hour'].value_counts().idxmax()
    print("The most common start hour is: ", common_hour)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    common_start_station = df ['Start Station'].value_counts().idxmax()
    print("The most common start station is: ", common_start_station)


    # TO DO: display most commonly used end station
    common_end_station = df['End Station'].value_counts().idxmax()
    print("The most common end station is: ", common_end_station)


    # TO DO: display most frequent combination of start station and end station trip
    common_start_and_end_stations = df.groupby(['Start Station', 'End Station']).size().nlargest(1)
    print("The most frequent combination of start station and end station trip", common_start_and_end_stations)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = df['Trip Duration'].sum() / 3600.0
    print("total travel time in hours is: ", total_travel_time)


    # TO DO: display mean travel time
    mean_travel_time = df['Trip Duration'].mean() / 3600.0
    print("mean travel time in hours is: ", mean_travel_time)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df, city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    types = df['User Type'].value_counts()
    print(types)
    
    if city != 'washington':
        # TO DO: Display counts of gender
        gender = df['Gender'].value_counts()
        print(gender)
        
        # TO DO: Display earliest, most recent, and most common year of birth
        earliest = int(df['Birth Year'].min())
        most_recent = int(df['Birth Year'].max())
        most_common = int(df['Birth Year'].value_counts().idxmax())
        print("The earliest year of birth is:",earliest,
              ", most recent is:",most_recent,
              "and the most common one is: ",most_common)
  

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def display(df):
    
    i =1
    while True:
        data = input('\nWould you like to see some raw data? Enter yes or no.\n')
        if data.lower() != 'yes':
            break   
        else:
            print(df[i:i+5])
            i = i+5


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df, city)
        display(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
