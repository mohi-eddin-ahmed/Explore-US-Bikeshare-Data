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
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city = input('\nPlease, Enter a city from (chicago - new york city - washington): ').lower()
    while city not in CITY_DATA.keys():
        print('Please, Enter a valid City!')
        city = input('\nPlease, Enter a city from (chicago - new york city - washington): ').lower()

    # get user input for month (all, january, february, ... , june)
    months = ['all', 'january', 'february', 'march', 'april', 'may', 'june']
    month = input('\nPlease, Enter a month from (january - february - march - april - may - june - all): ').lower()
    while month not in months:
        print('Please Enter a valid Month!')
        month = input('\nPlease, Enter a month from (january - february - march - april - may - june - all): ').lower()

    # get user input for day of week (all, monday, tuesday, ... sunday)
    days = ['saturday', 'sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'all']
    day = input('\nPlease, Enter a day from (saturday - sunday - monday - tuesday - wednesday - thursday - friday - all): ').lower()
    while day not in days:
        print('Please Enter a valid day!')
        day = input('\nPlease, Enter a day from (saturday - sunday - monday - tuesday - wednesday - thursday - friday - all): ').lower()

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
    df = pd.read_csv(CITY_DATA[city])

    #to covert Start Time from string to datetime format
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    df['start hour'] = df['Start Time'].dt.hour

    #filter by month if applicable
    if month != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        df = df[df['month'] == month]

    #filters by day if applicable
    if day != 'all':
        df = df[df['day_of_week'] == day.title()]


    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    print('The Most Common Month is: {}'.format(df['month'].mode()[0]))

    # display the most common day of week
    print('The Most Common Day of Week is: {}'.format(df['day_of_week'].mode()[0]))

    # display the most common start hour
    print('The Most Common Start Hour is: {}'.format(df['start hour'].mode()[0]))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    print('The Most Commonly Used Start Station is: {}'.format(df['Start Station'].mode()[0]))

    # display most commonly used end station
    print('The Most Commonly Used End Station is: {}'.format(df['End Station'].mode()[0]))

    # display most frequent combination of start station and end station trip
    df['start_to_end'] = df['Start Station'] + ' >>>>> ' + df['End Station']
    print('The Most Frequent Combination from Start to End is: {}'.format(df['start_to_end'].mode()[0]))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    print('The Total Travel Time is: {} seconds'.format(df['Trip Duration'].sum()))

    # display mean travel time
    print('The Mean Travel Time is: {} seconds'.format(df['Trip Duration'].mean()))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df, city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    user_types = df['User Type'].value_counts().to_frame()
    print(user_types, '\n')

    # Display counts of gender
    if city != 'washigton':
        print(df['Gender'].value_counts().to_frame(), '\n')

    # Display earliest, most recent, and most common year of birth
    print('The Earliest Common Year of Birth is: ', int(df['Birth Year'].min()))
    print('The Most Recent Common Year of Birth is: ', int(df['Birth Year'].max()))
    print('The Most Common Year of Birth is: ', int(df['Birth Year'].mode()[0]))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def show_data(df):

    """prompt the user if they want to see 5 lines of raw data, Display that data if the answer is 'yes."""
    #asking user if needing to view some data
    index = 1
    while True:
        view = input('Would you like to view individual trip 5 line of raw data? Type \'yes\' or \'no\'.')
        if view.lower() == 'yes':
            print(df[index : index + 5])
            print('-'*40)
            index = index + 5
        else:
            break

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df, city)
        show_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
