import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york': 'new_york_city.csv',
              'washington': 'washington.csv' }

cities = ['chicago', 'new york', 'washington']
months = ['january', 'february', 'march', 'april', 'may', 'june','july','august','all']
days = ['monday','tuesday','wednesday', 'thursday', 'friday','saturday','sunday','all']
filters = ['month', 'day', 'both', 'none']


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
    try:
        city = input("Would you like to see data for Chicago, New York, or Washington? \n> ").lower()
        while city not in cities:
            print("Invalid input")
            city = input('Choose a city out of Chicago, New York or Washington? \n> ').lower()
            print("You select ",city,". Thank you for the correct input.")
    except e:
        print("error occurred")

    try:
        filter1 = input("Would you like to filter the data by month, day, both or not at all? Please type none for not at all. \n> ").lower()
        while filter1 not in filters:
            print("Invalid input")
            filter1 = input("Would you like to filter the data by month, day, both or not at all? Please type none for not at all. \n> ").lower()
            print("You select",filter1,". Thank you for the correct input.")
    except e:
        print("error occurred")

    # TO DO: get user input for month (all, january, february, ... , june)
    while filter1 == 'month':
        month = input("Which month - January, February, March, April, May, or June? or ALL\n> ").lower()
        day = 'all'
        break
        while month not in months:
            print('You have to choose one month until june or all')
            month = input('Wich month would you like to explore? january, february,...,june? or ALL?\n> ').lower()
            print("You select ",month,". Thank you for the correct input.")
            break

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while filter1 == 'day':
        day = input("Which day - Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, or Sunday? or ALL?\n> ").lower()
        month = 'all'
        break
        while day not in days:
            print("Invalid input")
            day = input("Which day - Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, or Sunday? or ALL?\n> ").lower()
            print("You select ",day,". Thank you for the correct input.")
            break

    # TO DO: get user input for a specific month and a specific day
    while filter1 == 'both':
        try:
            month = input("Which month - January, February, March, April, May, or June? or ALL? \n> ").lower()
            while month not in months:
                print('You have to choose one month until june or all')
                month = input('Which month would you like to explore? january, february,...,june? or ALL? \n> ').lower()
                print("You select ",month,". Thank you for the correct input.")
        except e:
            print("error occurred")

        try:
            day = input("Which day - Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, or Sunday? or ALL?\n> ").lower()
            while day not in days:
                print("Invalid input")
                day = input("Which day - Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, or Sunday? or ALL?\n> ").lower()
                print("You select ",day," thank you for correct input.")
            break
        except e:
            print("error occurred")


    # TO DO: get user input for all months and days
    while filter1 == 'none':
        month = 'all'
        day = 'all'
        break


    print("Data is filtered by", filter1)
    print('-'*40)
    return city, month, day, filter1


def load_data(city, month, day, filter1):
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
    df['day_of_week'] = df['Start Time'].dt.day_name()


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
    most_common_month = df['month'].mode()[0]
    most_common_month = int(most_common_month)
    c = df['month'].value_counts().loc[most_common_month]
    print('the most common month is', months[most_common_month - 1], '; count:', c)

    # TO DO: display the most common day of week
    most_common_day = df['day_of_week'].mode()[0]
    c1 = df['day_of_week'].value_counts().loc[most_common_day]
    print('Most common day is ', most_common_day, '; count:', c1)

    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    most_common_hour = df['hour'].mode()[0]
    c2 = df['hour'].value_counts().loc[most_common_hour]

    print('the most common hour is', most_common_hour, '; count:', c2)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def station_stats(df):
    """Displays statistics on the most popular stations and trip."""
    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    most_common_start_st = df['Start Station'].mode()[0]
    print('Most common start station is ' , most_common_start_st)

    # TO DO: display most commonly used end station
    most_common_end_st = df['End Station'].mode()[0]
    print('Most common end station is ' , most_common_end_st)

    # TO DO: display most frequent combination of start station and end station trip
    most_common_combo = ('from' + ' ' + df['Start Station'] + ' to ' + df['End Station']).mode()[0]
    print('Most common combo is ' , most_common_combo)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def trip_duration_stats(df):
    """Calculates statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print('Total travel time: ' , total_travel_time)

    # TO DO: display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    print('Average travel time: ' , mean_travel_time)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def user_stats(df):
    """Calculates statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    print(df['User Type'].value_counts())
    print("\n")
    # TO DO: Display counts of gender

    if "Gender" in df.columns:
        print(df['Gender'].value_counts())
    else:
        print("Gender column not found")

    print("\n")
    # TO DO: Display earliest, most recent, and most common year of birth
    if "Birth Year" in df.columns:
        min_birth = df['Birth Year'].min()
        max_birth = df['Birth Year'].max()
        mode_birth = df['Birth Year'].mode()[0]

        print('The oldest customer was born in ' , int(min_birth))
        print('The youngest customer was born in ' , int(max_birth))
        print('Most common birth year is: ' , int(mode_birth))
    else:
        print("Birth Year column not found")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

raw_data_filters = ['yes', 'no']

def display_data(df):
    """Displays raw data"""
    print('\nDisplaying data...\n')
    start_time = time.time()

    try:
        raw_data = input("Would you like to see the raw data? Enter yes or no. \n> ").lower()
        while raw_data not in raw_data_filters:
            print("Invalid input")
            raw_data = input("Would you like to see the raw data? Enter yes or no. \n> ").lower()
            print("You select",raw_data,". Thank you for the correct input.")
    except e:
        print("error occurred")

    i = 5

    while raw_data == 'yes':
        print(df.head(i))
        see_more = input('\nWould you like to see more? Enter yes or no.\n').lower()

        while see_more == 'yes':
            print(df.head(i))
            i += 5
            break
        if see_more == 'no':
            break
        else:
            print("Please type correct input. Enter yes or no.")

    while raw_data == 'no':
        break

def main():
    while True:
        city, month, day, filter1 = get_filters()
        df = load_data(city, month, day, filter1)

        print(time_stats(df))
        print(station_stats(df))
        print(trip_duration_stats(df))
        print(user_stats(df))
        print(display_data(df))

        restart = input('\nWould you like to restart? Enter yes or no.\n').lower()
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
