# encoding:utf-8
# !/bin/python

import sqlite3

conn = sqlite3.connect('db.sqlite3')
print "Opened database successfully";

conn.execute('''CREATE TABLE IF NOT EXISTS ENV
       (ID INT PRIMARY KEY     NOT NULL,
       NAME            TEXT    NOT NULL,
       IP              TEXT    NOT NULL,
       USER            TEXT    NOT NULL,
       PASS            TEXT    NOT NULL,
       JOINTIME        TEXT    NOT NULL,
       LOCK            TEXT    NOT NULL,
       STATUS          TEXT    NOT NULL,
       IPMI            TEXT,
       IPMIUSER        TEXT,
       IPMIPASS        TEXT,
       JOBID           INT,
       JOBNAME         TEXT
       );''')
print "ENV Table created successfully";

conn.execute('''CREATE TABLE IF NOT EXISTS JOB
       (JOBID INT PRIMARY KEY     NOT NULL,
       JOBNAME            TEXT    NOT NULL,
       STARTTIME          TEXT,
       ENDTIME            TEXT,
       STATUS             TEXT
       );''')
print "JOB Table created successfully";
conn.commit()


conn.close()
