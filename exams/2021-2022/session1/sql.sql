create table if not exists Client (
    Code varchar(6) primary key not null,
    LastName varchar(100) not null,
    FirstName varchar(50) not null,
    Patronymic varchar(50) not null,
    Gender char(1) not null,
    Phone varchar(20) not null,
    Email varchar(50) not null
);

create table if not exists Country (
    Code varchar(3) primary key not null,
    Name varchar(100) not null,
    Flag varbinary
);

create table if not exists Hotel (
    ID int primary key not null auto_increment,
    Name varchar(200) not null,
    CountryID varchar(6) not null,
    FOREIGN KEY (CountryID) REFERENCES Country(Code)
);

create table if not exists HotelPhoto (
    ID int primary key not null auto_increment,
    Flag binary not null,
    PhotoPath varchar(200) not null,
    HotelID int not null,
    FOREIGN KEY (HotelID) REFERENCES Hotel(ID)
);

create table if not exists Partner (
    ID int primary key not null auto_increment,
    Name varchar(200) not null
);

create table if not exists Service (
    ID int primary key not null auto_increment,
    Name varchar(200) not null,
    PartnerID int not null,
    HotelID int not null,
    Price decimal(10.2) not null,
    FOREIGN KEY (PartnerID) REFERENCES Partner(ID),
    FOREIGN KEY (HotelID) REFERENCES Hotel(ID)
);

create table if not exists ServiceByTour (
    ID int primary key not null auto_increment,
    ServiceID int not null,
    IsControl boolean,
    FOREIGN KEY (ServiceID) REFERENCES Service(ID)
);