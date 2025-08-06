import sqlite3
import os

os.makedirs("database", exist_ok=True)
conn = sqlite3.connect('database/chatbot.db')
cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS info (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    topic TEXT UNIQUE,
    value TEXT
)
''')

data = [
    ("location", "HITAM is located in Medchal, Hyderabad, Telangana."),
    ("faculty", "Faculty includes PhD and M.Tech holders across CSE, ECE, EEE, and Mechanical branches."),
    ("departments", "CSE, CSD, CSM, CSC, CSO, ECE, EEE, Mechanical Engineering."),
    ("fees", "B.Tech: ₹90,000/year. Hostel: ₹60,000/year."),
    ("labs", "Labs include AI-ML Lab, IoT Lab, Mechanical Workshop, Electronics Lab, and Python Programming Lab."),
    ("sports", "HITAM offers cricket, football, basketball, volleyball, badminton, and table tennis."),
    ("hygiene", "The campus is sanitized regularly with excellent hygiene standards in hostels and mess."),
    ("blocks", "A Block - Admin, B Block - CSE & IT, C Block - ECE & EEE, D Block - Workshops & Labs."),
    ("transport", "Buses operate from Secunderabad, Kukatpally, Uppal, and other parts of Hyderabad."),
    ("placements", "In 2024, 400+ students were placed with TCS, Infosys, Amazon, Wipro, Capgemini."),
    ("education", "Focus on skill-based learning with Project-Based Learning (PBL) and COE programs."),
    ("hostel", "Separate hostels for boys and girls with WiFi, security, and mess facilities."),
    ("canteen", "The canteen provides healthy vegetarian and non-vegetarian meals."),
    ("library", "Digital library with 20,000+ books, e-journals, NPTEL access."),
    ("events", "Annual events include 'Lakshya', technical fests, cultural nights, and national hackathons."),
    ("timings", "College runs from 9:00 AM to 4:30 PM, Monday to Saturday.")
]

cursor.executemany("INSERT OR IGNORE INTO info (topic, value) VALUES (?, ?)", data)

conn.commit()
conn.close()
print("Updated HITAM database successfully.")
