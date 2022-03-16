#!/usr/bin/env python
import shutil
import psutil
import socket
import emails

def check_cpu_usage():
    usage = psutil.cpu_percent(3)
    # return positive
    return usage < 80

def check_disk_usage(disk):
    du = psutil.disk_usage(disk).percent
    #return positive
    return du < 80

def check_memory_usage():
    one_mb = 2 ** 20
    minmem = one_mb * 500
    memava = psutil.virtual_memory().available
    #return positive
    return memava > minmem

def check_localhost():
    local_host_ip = socket.gethostbyname("localhost")
    #retun positive
    return local_host_ip == "127.0.0.1"

def sendAlert(alert):
    """output alert error and send email"""
    content = {
        "sender": "automation@example.com",
        "receiver": "student-02-37474229022a@example.com",
        "subject": alert,
        "body": "Please check your system and resolve the issue as soon as possible.",
        "attachment": None,
    }
    try:
        message = emails.generate_email(**content)
        emails.send_email(message)
    except:
        print("unable to send alert email notification!")
    finally:
        print(alert)
        exit(1)

def main():
    # check system resources:
    print("checking system resources")
    alert = None
    if not check_cpu_usage():
        alert = f"Error - CPU usage is over 80%"
    elif not check_disk_usage("/"):
        alert = f"Error - Available disk space is less than 20%"
    elif not check_memory_usage():
        alert = f"Error - Available memory is less than 500MB"
    elif not check_localhost():
        alert = f"Error - localhost cannot be resolved to 127.0.0.1"

    # alert if error raised:
    if alert:
        sendAlert(alert)
    else:
        print("system ok")


if __name__ == "__main__":
    main()