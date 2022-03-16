#!/usr/bin/env python3
import os
import datetime
import reports
import emails


def get_summary(file):
        # print(files)
    with open(file) as f:
            lines = f.read().strip().splitlines()
    name_field = "name: {}".format(lines[0])
    weight_field = "weight: {}".format(lines[1])
    return "{}<br/>{}<br/><br/>".format(name_field, weight_field)

def main():
    txt_dir = "supplier-data/descriptions/"
    txt_files = [txt_dir + f for f in os.listdir(txt_dir) if f.endswith(".txt")]
    #report body
    report_body = ""
    for file in txt_files:
        report_body += get_summary(file)
    
    #report date and report title
    today = datetime.datetime.today()
    
    report_title = "Processed update on {} {}, {}".format (today.strftime("%B"), today.day, today.year)
    # print(report_title)

    #generate pdf
    attachment = "/tmp/processed.pdf"
    reports.generate_report(attachment, report_title, report_body)

    #send email
    sender = "automation@example.com"
    receiver = "{}@example.com".format("student-02-37474229022a")
    subject = "Upload Completed - Online Fruit Store"
    body = "All fruits are uploaded to our website successfully. A detailed list is attached to this email."

    message = emails.generate_email(sender, receiver, subject, body, attachment)
    emails.send_email(message)


if __name__ == "__main__":
    main()