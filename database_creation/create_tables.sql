-- drop table "User";
-- drop table Work_place;
-- drop table User_Work_place;
-- drop table Desk;
-- drop table User_Desk;
-- drop table "Group";
-- drop table Card;
-- drop table Label;
-- drop table Card_Label;
-- drop table File;
-- drop table Card_File;
-- drop table Action;

CREATE TABLE IF NOT EXISTS "User"
(
    user_id     SERIAL PRIMARY KEY,
    login       VARCHAR(60) NOT NULL,
    password    VARCHAR(60) NOT NULL,
    mail        VARCHAR(60) NOT NULL,
    personality VARCHAR(1023)
);

CREATE TABLE IF NOT EXISTS Work_place
(
    work_place_id SERIAL PRIMARY KEY,
    name          VARCHAR(60) NOT NULL,
    type          VARCHAR(60) NOT NULL,
    description   VARCHAR(255),
    admin_id      INTEGER NOT NULL,
    FOREIGN KEY (admin_id) REFERENCES "User" (user_id) ON DELETE CASCADE ON UPDATE CASCADE
);

CREATE TABLE IF NOT EXISTS User_Work_place
(
    user_id       INTEGER NOT NULL,
    work_place_id INTEGER NOT NULL,
    FOREIGN KEY (user_id)       REFERENCES "User" (user_id) ON DELETE CASCADE ON UPDATE CASCADE,
    FOREIGN KEY (work_place_id) REFERENCES Work_place (work_place_id) ON DELETE CASCADE ON UPDATE CASCADE
);

CREATE TABLE IF NOT EXISTS Desk
(
    desk_id       SERIAL PRIMARY KEY,
    name          VARCHAR(60) NOT NULL,
    access        VARCHAR(60) NOT NULL,
    background    VARCHAR(60),
    admin_id      INTEGER NOT NULL,
    work_place_id INTEGER NOT NULL,
    FOREIGN KEY (admin_id)      REFERENCES "User" (user_id) ON DELETE CASCADE ON UPDATE CASCADE,
    FOREIGN KEY (work_place_id) REFERENCES Work_place (work_place_id) ON DELETE CASCADE ON UPDATE CASCADE
);

CREATE TABLE IF NOT EXISTS User_Desk
(
    user_id INTEGER NOT NULL,
    desk_id INTEGER NOT NULL,
    FOREIGN KEY (user_id) REFERENCES "User" (user_id) ON DELETE CASCADE ON UPDATE CASCADE,
    FOREIGN KEY (desk_id) REFERENCES Desk (desk_id) ON DELETE CASCADE ON UPDATE CASCADE
);

CREATE TABLE IF NOT EXISTS "Group"
(
    group_id SERIAL PRIMARY KEY,
    name     VARCHAR(60) NOT NULL,
    desk_id  INTEGER NOT NULL,
    FOREIGN KEY (desk_id) REFERENCES Desk (desk_id) ON DELETE CASCADE ON UPDATE CASCADE
);

CREATE TABLE IF NOT EXISTS Card
(
    card_id      SERIAL PRIMARY KEY,
    name         VARCHAR(60) NOT NULL,
    description  VARCHAR(255),
    deadlines    TIMESTAMPTZ,
    progress_bar SMALLINT,
    group_id     INTEGER NOT NULL,
    FOREIGN KEY (group_id) REFERENCES "Group" (group_id) ON DELETE CASCADE ON UPDATE CASCADE
);

CREATE TABLE IF NOT EXISTS Label
(
    label_id SERIAL PRIMARY KEY,
    colour   VARCHAR(60) NOT NULL,
    text     VARCHAR(60),
    work_place_id  INTEGER NOT NULL,
    FOREIGN KEY (work_place_id) REFERENCES Work_place (work_place_id) ON DELETE CASCADE ON UPDATE CASCADE
);

CREATE TABLE IF NOT EXISTS Card_Label
(
    card_id  INTEGER NOT NULL,
    label_id INTEGER NOT NULL,
    FOREIGN KEY (card_id)  REFERENCES Card (card_id) ON DELETE CASCADE ON UPDATE CASCADE,
    FOREIGN KEY (label_id) REFERENCES Label (label_id) ON DELETE CASCADE ON UPDATE CASCADE
);

CREATE TABLE IF NOT EXISTS File
(
    file_id   SERIAL PRIMARY KEY,
    file_path VARCHAR(60) NOT NULL
);

CREATE TABLE IF NOT EXISTS Card_File
(
    card_id INTEGER NOT NULL,
    file_id INTEGER NOT NULL,
    FOREIGN KEY (card_id)  REFERENCES Card (card_id) ON DELETE CASCADE ON UPDATE CASCADE,
    FOREIGN KEY (file_id) REFERENCES File (file_id) ON DELETE CASCADE ON UPDATE CASCADE
);

CREATE TABLE IF NOT EXISTS Action
(
    action_id  SERIAL PRIMARY KEY,
    data       VARCHAR(1023),
    date       TIMESTAMPTZ NOT NULL,
    is_comment BOOLEAN NOT NULL,
    user_id    INTEGER NOT NULL,
    card_id    INTEGER NOT NULL,
    FOREIGN KEY (user_id) REFERENCES "User" (user_id) ON DELETE CASCADE ON UPDATE CASCADE,
    FOREIGN KEY (card_id) REFERENCES Card (card_id) ON DELETE CASCADE ON UPDATE CASCADE
);