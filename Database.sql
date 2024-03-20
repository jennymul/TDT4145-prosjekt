BEGIN TRANSACTION;

DROP TABLE IF EXISTS Ansatt;
CREATE TABLE Ansatt (
    AnsattID INT,
    Navn TEXT NOT NULL,
    AnsattStatus TEXT NOT NULL, 
    Epost TEXT NOT NULL,
    PRIMARY KEY (AnsattID)
);

DROP TABLE IF EXISTS Oppgave;
CREATE TABLE Oppgave (
    OppgaveID INT,
    Tittel TEXT NOT NULL,
    Beskrivelse TEXT NOT NULL,
    TeaterStykke INT NOT NULL,
    PRIMARY KEY (OppgaveID),
    FOREIGN KEY (TeaterStykke) REFERENCES TeaterStykke(TeaterStykkeID)
);

DROP TABLE IF EXISTS TildeltOppgave;
CREATE TABLE TildeltOppgave (
    Ansatt INT,
    Oppgave INT,
    PRIMARY KEY (Ansatt, Oppgave),
    FOREIGN KEY (Ansatt) REFERENCES Ansatt(AnsattID),
    FOREIGN KEY (Oppgave) REFERENCES Oppgave(OppgaveID)
);

DROP TABLE IF EXISTS TeaterStykke;
CREATE TABLE TeaterStykke (
    TeaterStykkeID INT,
    Tittel TEXT NOT NULL,
    Forfatter TEXT NOT NULL,
    Sal INT NOT NULL,
    PRIMARY KEY (TeaterStykkeID),
    FOREIGN KEY (Sal) REFERENCES TeaterSal(SalID)
);

DROP TABLE IF EXISTS Akt;
CREATE TABLE Akt (
    TeaterStykke INT,
    AktNummer INT,
    PRIMARY KEY (TeaterStykke, AktNummer),
    FOREIGN KEY (TeaterStykke) REFERENCES TeaterStykke(TeaterStykkeID)
);

DROP TABLE IF EXISTS Rolle;
CREATE TABLE Rolle (
    RolleID INT,
    Navn TEXT NOT NULL,
    PRIMARY KEY (RolleID)
);

DROP TABLE IF EXISTS RolleIAkt;
CREATE TABLE RolleIAkt (
    Rolle INT,
    Akt INT,
    TeaterStykke INT,
    PRIMARY KEY (Rolle, Akt, TeaterStykke),
    FOREIGN KEY (Rolle) REFERENCES Rolle(RolleID),
    FOREIGN KEY (Akt) REFERENCES Akt(AktNummer),
    FOREIGN KEY (TeaterStykke) REFERENCES TeaterStykke(TeaterStykkeID)
);

DROP TABLE IF EXISTS Skuespiller;
CREATE TABLE Skuespiller (
    SkuespillerID INT,
    Navn TEXT NOT NULL,
    PRIMARY KEY (SkuespillerID)
);

DROP TABLE IF EXISTS SpillesAv;
CREATE TABLE SpillesAv (
    Skuespiller INT,
    Rolle INT,
    PRIMARY KEY (Skuespiller, Rolle),
    FOREIGN KEY (Skuespiller) REFERENCES Skuespiller(SkuespillerID),
    FOREIGN KEY (Rolle) REFERENCES Rolle(RolleID)
);

DROP TABLE IF EXISTS TeaterSal;
CREATE TABLE TeaterSal (
    SalID INT,
    Navn TEXT NOT NULL,
    Maxplasser INT NOT NULL,
    PRIMARY KEY (SalID)
);

DROP TABLE IF EXISTS Plass;
CREATE TABLE Plass (
    StolNummer INT,
    RadNummer INT,
    Omraade TEXT,
    Sal INT,
    PRIMARY KEY (Sal, StolNummer, RadNummer, Omraade),
    FOREIGN KEY (Sal) REFERENCES TeaterSal(SalID)
);

DROP TABLE IF EXISTS Forestilling;
CREATE TABLE Forestilling (
    Dato DATE,
    Klokkeslett TIME,
    TeaterStykke INT,
    PRIMARY KEY (TeaterStykke, Dato, Klokkeslett),
    FOREIGN KEY (TeaterStykke) REFERENCES TeaterStykke(TeaterStykkeID)
);

DROP TABLE IF EXISTS PrisType;
CREATE TABLE PrisType(
    Type TEXT,
    Pris INT NOT NULL,
    TeaterStykke INT,
    PRIMARY KEY (Type, TeaterStykke),
    FOREIGN KEY (TeaterStykke) REFERENCES TeaterStykke(TeaterStykkeID)
);

DROP TABLE IF EXISTS Billett;
CREATE TABLE Billett (
    BillettID INT,
    Type TEXT NOT NULL,
    Stolnummer INT NOT NULL,
    RadNummer INT NOT NULL,
    Omraade TEXT NOT NULL,
    Dato DATE NOT NULL,
    Klokkeslett TIME NOT NULL,
    Sal INT NOT NULL,
    TeaterStykke INT NOT NULL,
    Kjop INT NOT NULL,
    PRIMARY KEY (BillettID)
    FOREIGN KEY (Stolnummer, RadNummer, Omraade) REFERENCES Plass(StolNummer, RadNummer, Omraade),
    FOREIGN KEY (Dato, Klokkeslett) REFERENCES Forestilling(Dato, Klokkeslett),
    FOREIGN KEY (Sal) REFERENCES TeaterSal(SalID),
    FOREIGN KEY (TeaterStykke) REFERENCES TeaterStykke(TeaterStykkeID),
    FOREIGN KEY (Type, TeaterStykke) REFERENCES PrisType(Type, TeaterStykke),
    FOREIGN KEY (Kjop) REFERENCES BillettKjop(KjopID)
);

DROP TABLE IF EXISTS BillettKjop;
CREATE TABLE BillettKjop (
    KjopID INT,
    TotalPris INT NOT NULL,
    Dato DATE NOT NULL,
    Klokkeslett TIME NOT NULL,
    Kunde INT NOT NULL,
    PRIMARY KEY (KjopID),
    FOREIGN KEY (Kunde) REFERENCES Kunde(KundeNr)
);

DROP TABLE IF EXISTS Kunde;
CREATE TABLE Kunde (
    KundeNr INT,
    Navn TEXT NOT NULL,
    Adresse TEXT NOT NULL,
    MobilNummer TEXT NOT NULL,
    PRIMARY KEY (KundeNr)
);

COMMIT;
