CREATE TABLE Users (
    ID int NOT NULL AUTO_INCREMENT,
    UserName varchar(32) NOT NULL,
    PasswordHash binary(32) NOT NULL,
    CONSTRAINT PK_Users PRIMARY KEY (ID),
    CONSTRAINT UC_Users UNIQUE (UserName)
);

-- Specialization of User
CREATE TABLE Groups (
    ID int NOT NULL,
    CONSTRAINT FK_UserGroup FOREIGN KEY (ID)
    REFERENCES Users(ID),
    CONSTRAINT PK_Groups PRIMARY KEY (ID)
);

CREATE TABLE Members (
    UserID int NOT NULL,
    GroupID int NOT NULL,
    CONSTRAINT FK_UserMember FOREIGN KEY (UserID)
    REFERENCES Users(ID),
    CONSTRAINT FK_GroupMember FOREIGN KEY (GroupID)
    REFERENCES Groups(ID),
    CONSTRAINT PK_Members PRIMARY KEY (UserID,GroupID)
);

CREATE TABLE Events (
    EventID int NOT NULL AUTO_INCREMENT,
    HostID int NOT NULL,
    EventName varchar(64) NOT NULL,
    CONSTRAINT FK_UserEvent FOREIGN KEY (HOSTID)
    REFERENCES Users(ID),
    CONSTRAINT PK_Events PRIMARY KEY (EventID)
);

CREATE TABLE Attendees (
    EventID int NOT NULL,
    AttendeeID int NOT NULL,
    CONSTRAINT FK_EventAttendee FOREIGN KEY (EventID)
    REFERENCES Events(ID),
    CONSTRAINT FK_UserAttendee FOREIGN KEY (AttendeeID)
    REFERENCES User(ID),
    CONSTRAINT PK_Attendees PRIMARY KEY (EventID,AttendeeID)
);