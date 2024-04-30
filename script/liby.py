import time


def coutdown(second):
    while second>0:
        print(second)
        time.sleep(1)
        second-=1
def shoutdown():
    second = 3
    coutdown(second)


if __name__ == "__main__":
    shoutdown()