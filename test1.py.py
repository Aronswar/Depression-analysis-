
def main():
        print("""Basic test for depression:
                Enter the numbers as how you really feel:
                1.Never
                2.Rarely
                3.Sometimes
                4.Often
                5.Most of the Time""")
        action=input('1. Have you cried this week?:')
        fft=input("2.Do you feel that you are good at doing things?")
        nxt=input('2. Have your been energy deprived for the past the past 7 days?:')
        thrd=input("3.How was your sleep: ")
        fur=input("4. How often have you felt sad in the past 7 days:")

        tot=action+fft+nxt+thrd+fur
        print tot
        
                
                
main()
