DROP TABLE IF EXISTS governor;
CREATE TABLE governor (
    Office text,
    State text,
    RaceYear smallint,
    Area text,
    AreaType text,
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
