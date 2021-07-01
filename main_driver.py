from reader.atp_reader import readAtpData

from client.httpclient import postAtp
import time


def main():
    while True:
        temperature, pressure, altitude, timestamp = readAtpData()
        postAtp(temperature, pressure, altitude, timestamp)
        print("Post completed!")
        time.sleep(10)


if __name__ == "__main__":
    main()
