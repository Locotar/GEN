# encoding:utf-8
# !/bin/python

import sqlite3

conn = sqlite3.connect('db.sqlite3')
print "Opened database successfully";

conn.execute('''CREATE TABLE JOB
       (JOBID INT PRIMARY KEY     NOT NULL,
       JOBNAME            TEXT    NOT NULL,
       STARTTIME          TEXT,
       ENDTIME            TEXT,
       STATUS             TEXT
       );''')
conn.commit()
print "JOB Table created successfully";


conn.close()
