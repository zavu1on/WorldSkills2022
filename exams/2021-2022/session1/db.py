import mysql.connector as mysql

conn = mysql.connect(
    user='worldskills',
    password='worldskills',
    port=3306,
    host='127.0.0.1',
    database='worldskills',
    autocommit=True
)
cur = conn.cursor()

cur.execute("""
create table if not exists Client (
    Code varchar(6) primary key not null,
    LastName varchar(100) not null,
    FirstName varchar(50) not null,
    Patronymic varchar(50) not null,
    Gender char(1) not null,
    Phone varchar(20) not null,
    Email varchar(50) not null
);
""")
cur.execute("""
create table if not exists Country (
    Code varchar(3) primary key not null,
    Name varchar(100) not null,
    Flag binary
);
""")
cur.execute("""
create table if not exists Hotel (
    ID int primary key not null auto_increment,
    Name varchar(200) not null,
    CountryID varchar(6) not null unique,
    FOREIGN KEY (CountryID) REFERENCES Country(Code)
);
""")
cur.execute("""
create table if not exists HotelPhoto (
    ID int primary key not null auto_increment,
    Flag binary not null,
    PhotoPath varchar(200) not null,
    HotelID int not null,
    FOREIGN KEY (HotelID) REFERENCES Hotel(ID)
);
""")
cur.execute("""
create table if not exists Partner (
    ID int primary key not null auto_increment,
    Name varchar(200) not null
);
""")
cur.execute("""
create table if not exists Service (
    ID int primary key not null auto_increment,
    Name varchar(200) not null,
    PartnerID int not null,
    HotelID int not null,
    Price decimal(10.2) not null,
    FOREIGN KEY (PartnerID) REFERENCES Partner(ID),
    FOREIGN KEY (HotelID) REFERENCES Hotel(ID)
);
""")
cur.execute("""
create table if not exists ServiceByTour (
    ID int primary key not null auto_increment,
    ServiceID int not null,
    IsControl boolean,
    FOREIGN KEY (ServiceID) REFERENCES Service(ID)
);
""")
cur.execute("""
create table if not exists User (
    ID int primary key not null auto_increment,
    Number int not null,
    Password varchar(200) not null,
    Role varchar(200)
);
""")

cur.execute("SHOW TABLES;")
print(cur.fetchall())

conn.close()
