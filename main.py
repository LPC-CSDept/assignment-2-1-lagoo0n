def main():
    """
    ##################################################
    Comlete your code here
    Use m_perc and f_perc for your results
    ##################################################
    """

    """
    ########################################
    # Do not delete the return statement
    ########################################
    """
    males = int(input("How many males are there: "))
    females = int(input("How many females are there: "))
    total_people = males + females
    m_perc = str((males/total_people)*100)+"%"
    f_perc = str((females/total_people)*100)+"%"

    print(f'total number of students: {total_people}')
    print(f'number of males: {males}')
    print(f'number of females: {females}')
    print(f'percentatge of males: {m_perc}')
    print(f'percentatge of females: {f_perc}')

    return m_perc, f_perc


if __name__ == '__main__':
    main()
