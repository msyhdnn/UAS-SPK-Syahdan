--
-- PostgreSQL database dump
--

-- Dumped from database version 16.0
-- Dumped by pg_dump version 16.0

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- Name: bigbike; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.bigbike (
    "Nama" text,
    "Harga" bigint,
    cc real,
    "full_tank" real,
    "Daya_KW" real,
    "Torsi_Max" real
);


ALTER TABLE public.bigbike OWNER TO postgres;

--
-- Data for Name: bigbike; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.bigbike ("Nama", "Harga", cc, "full_tank", "Daya_KW", "Torsi_Max") FROM stdin;
Honda CB650R	291006000	648.72	15.4	66.5	60.7
Honda CBR1000RR-R	1076696000	999	16.1	160	112
CRF1100L AFRICA TWIN	620774000	820	24.8	73	103
Honda CB500X	204513000	471	17.7	37	44.6
XL750 Transalp	330500000	755	16.9	67.5	75
HONDA GOLD WING 1800	1052500000	1200	21	93	170
HONDA REBEL	201688000	471.03	18	33.5	43.6
Yamaha MT09	261500000	847	14	84.6	87.5
Yamaha V-Max	457000000	1.679	15	147.2	166.8
Yamaha T-Max DX	292600000	530	15	33.8	53
\.


--
-- PostgreSQL database dump complete
--

