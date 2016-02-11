DROP TABLE IF EXISTS presidential,senate,house,governor;
CREATE TABLE presidential (
    Office text,
    State text,
    RaceYear smallint,
    Area text,
    AreaType text,
    TotalVotes int,
    RepVotes int,
    RepCandidate text,
    RepStatus text,
    DemVotes int,
    DemCandiate text,
    DemStatus text,
    ThirdParty text,
    ThirdVotes int,
    ThirdCandidate text,
    ThirdStatus text,
    OtherVotes int
);
