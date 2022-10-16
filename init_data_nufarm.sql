CREATE TABLE nufarm (
    year NUMERIC PRIMARY KEY,
    sales bigint,
    eps numeric,
    cash_from_ops bigint,
    nopat bigint,
    debt bigint,
    equity bigint
);

INSERT INTO nufarm (year, sales, eps, cash_from_ops, nopat, debt, equity)
VALUES
    (2021, 3215651000, 15.2, 424191000, 65128000, 1041032000, 2121463000),
    (2020, 267320000, -24.5, -129989000, -92859000, 1030121000, 2030428000),
    (2019, 3757590000, 7.4, 98131000, 38310000, 1752816000, 2404944000),
    (2018, 3307847000, -8.5, -88169, -16007000, 1668413000, 1971624000),
    (2017, 3111115000, 38.7, 55443000, 115042000, 904054000, 1602923000),
    (2016, 2791217000, 6.1, 137375000, 27478000, 906878000, 1550228000);

/* Debt = "Loans and borrowings" in both current and non-current liabilities