import os

ans = int(input("""Press 1 to PASS the code
Press 0 to FAIL the code : """))

if ans == 1:
    print("This code has passed the QA test")
    os.system('curl --user "admin:docker" http://localhost:8080/job/auto-merge/build?token=auto-merge')
else:
    print("This code has failed the QA test")
