# encoding:utf-8
# !/bin/python

import sqlite3

conn = sqlite3.connect('db.sqlite3')
print "Opened database successfully";

conn.execute('''CREATE TABLE ENV
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
conn.commit()
print "ENV Table created successfully";


conn.close()
