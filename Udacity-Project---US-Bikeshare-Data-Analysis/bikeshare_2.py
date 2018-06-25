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
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while 1==1:
        city = input('\nHello! Let\'s explore some US bikeshare data!\n'
                     'Would you like to see data for Chicago, New York, or'
                     ' Washington?\n').lower()
        if city in ['chicago', 'new york city', 'washington']:
            break
        else:
            print('Sorry, I do not understand your input. Please input either '
                  'Chicago, New York City, or Washington.')

    # get user input for month (all, january, february, ... , june)
    while 1==1:
        month = input('\nWhich month? January, February, March, April,'
                            ' May, or June?\n').lower()
        if month in ['january', 'february', 'march', 'april', 'may', 'june', 'all' ]:
            break
        else:
            print('Sorry, I do not understand your input. Please type in a '
                  'month between January and June')
        
    # get user input for day of week (all, monday, tuesday, ... sunday)
    while 1==1:
        day = input('\nWhich day? Monday, Tuesday, Wednesday, Thursday,'
                            ' Thursday, Friday, Saturday, or Sunday?\n').lower()
        if day in ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday', 'all']:
            break
        else:
            print('Sorry, I do not understand your input. Please type in a '
                  'month between January and June')

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

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    
    # Creat a journey column for the journey between station 
    df['Journey'] = df['Start Station'].str.cat(df['End Station'], sep=' to ')
    
    # extract hour from the Start Time column to create an hour column
    df['hour'] = df['Start Time'].dt.hour

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

    # display the most common month
    popular_month = df['month'].mode()[0]
    print("Most common Month:", popular_month)

    # display the most common day of week
    popular_day = df['day_of_week'].mode()[0]
    print("Most common Day of the Week:", popular_day)
    
    # display the most common start hour
    popular_hour = df['hour'].mode()[0]
    print("Most common Hour:", popular_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    pop_start = df['Start Station'].mode().to_string(index = False)
    print('The most popular start station is {}.'.format(pop_start))

    # display most commonly used end station
    pop_end = df['End Station'].mode().to_string(index = False)
    print('The most popular end station is {}.'.format(pop_end))
    
    # display most frequent combination of start station and end station trip
    pop_journey = df['Journey'].mode().to_string(index = False)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    total_travel_time = df['Trip Duration'].sum()
    
    minute, second = divmod(total_travel_time, 60)
    hour, minute = divmod(minute, 60)
    print('The total trip duration is {} hours, {} minutes and {}'
          ' seconds.'.format(hour, minute, second))

    # display mean travel time
    mean_travel_time = round(df['Trip Duration'].mean())
    m, s = divmod(mean_travel_time, 60)
    if m > 60:
        h, m = divmod(m, 60)
        print('The average trip duration is {} hours, {} minutes and {}'
              ' seconds.'.format(h, m, s))
    else:
        print('The average trip duration is {} minutes and {} seconds.'.format(m, s))
        

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    user_types = df['User Type'].value_counts()
    print(user_types)
    # Display counts of gender
    gender_types = df['Gender'].value_counts()
    print(gender_types)
    # Display earliest, most recent, and most common year of birth
    earliest = int(df['Birth Year'].min())
    latest = int(df['Birth Year'].max())
    mode = int(df['Birth Year'].mode())
    print('The oldest users are born in {}.\nThe youngest users are born in {}.'
          '\nThe most popular birth year is {}.'.format(earliest, latest, mode))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
