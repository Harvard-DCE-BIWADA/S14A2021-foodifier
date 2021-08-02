--
-- PostgreSQL database dump
--

-- Dumped from database version 13.3
-- Dumped by pg_dump version 13.3

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
-- Name: foods; Type: TABLE; Schema: public; Owner: 37114702162
--

CREATE TABLE public.foods (
    fid integer NOT NULL,
    uid integer NOT NULL,
    foodname text NOT NULL,
    calorie integer NOT NULL
);


ALTER TABLE public.foods OWNER TO "37114702162";

--
-- Name: foods_fid_seq; Type: SEQUENCE; Schema: public; Owner: 37114702162
--

CREATE SEQUENCE public.foods_fid_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.foods_fid_seq OWNER TO "37114702162";

--
-- Name: foods_fid_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: 37114702162
--

ALTER SEQUENCE public.foods_fid_seq OWNED BY public.foods.fid;


--
-- Name: goals; Type: TABLE; Schema: public; Owner: 37114702162
--

CREATE TABLE public.goals (
    uid integer NOT NULL,
    weeklyg text NOT NULL,
    weekly text NOT NULL,
    dailyg text NOT NULL,
    daily text NOT NULL
);


ALTER TABLE public.goals OWNER TO "37114702162";

--
-- Name: goals_uid_seq; Type: SEQUENCE; Schema: public; Owner: 37114702162
--

CREATE SEQUENCE public.goals_uid_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.goals_uid_seq OWNER TO "37114702162";

--
-- Name: goals_uid_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: 37114702162
--

ALTER SEQUENCE public.goals_uid_seq OWNED BY public.goals.uid;


--
-- Name: userdashboard; Type: TABLE; Schema: public; Owner: 37114702162
--

CREATE TABLE public.userdashboard (
    uid integer NOT NULL,
    username text NOT NULL,
    weeklyg text NOT NULL,
    weekly text NOT NULL,
    dailyg text NOT NULL,
    daily text NOT NULL
);


ALTER TABLE public.userdashboard OWNER TO "37114702162";

--
-- Name: userdashboard_uid_seq; Type: SEQUENCE; Schema: public; Owner: 37114702162
--

CREATE SEQUENCE public.userdashboard_uid_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.userdashboard_uid_seq OWNER TO "37114702162";

--
-- Name: userdashboard_uid_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: 37114702162
--

ALTER SEQUENCE public.userdashboard_uid_seq OWNED BY public.userdashboard.uid;


--
-- Name: users; Type: TABLE; Schema: public; Owner: 37114702162
--

CREATE TABLE public.users (
    uid integer NOT NULL,
    username text NOT NULL,
    password text NOT NULL,
    weeklyg integer NOT NULL,
    weekly integer NOT NULL,
    dailyg integer NOT NULL,
    daily integer NOT NULL,
    firstlogin integer
);


ALTER TABLE public.users OWNER TO "37114702162";

--
-- Name: users_uid_seq; Type: SEQUENCE; Schema: public; Owner: 37114702162
--

CREATE SEQUENCE public.users_uid_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.users_uid_seq OWNER TO "37114702162";

--
-- Name: users_uid_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: 37114702162
--

ALTER SEQUENCE public.users_uid_seq OWNED BY public.users.uid;


--
-- Name: foods fid; Type: DEFAULT; Schema: public; Owner: 37114702162
--

ALTER TABLE ONLY public.foods ALTER COLUMN fid SET DEFAULT nextval('public.foods_fid_seq'::regclass);


--
-- Name: goals uid; Type: DEFAULT; Schema: public; Owner: 37114702162
--

ALTER TABLE ONLY public.goals ALTER COLUMN uid SET DEFAULT nextval('public.goals_uid_seq'::regclass);


--
-- Name: userdashboard uid; Type: DEFAULT; Schema: public; Owner: 37114702162
--

ALTER TABLE ONLY public.userdashboard ALTER COLUMN uid SET DEFAULT nextval('public.userdashboard_uid_seq'::regclass);


--
-- Name: users uid; Type: DEFAULT; Schema: public; Owner: 37114702162
--

ALTER TABLE ONLY public.users ALTER COLUMN uid SET DEFAULT nextval('public.users_uid_seq'::regclass);


--
-- Data for Name: foods; Type: TABLE DATA; Schema: public; Owner: 37114702162
--

COPY public.foods (fid, uid, foodname, calorie) FROM stdin;
1	1	sushi	21
2	1	frozen yogurt	61
\.


--
-- Data for Name: goals; Type: TABLE DATA; Schema: public; Owner: 37114702162
--

COPY public.goals (uid, weeklyg, weekly, dailyg, daily) FROM stdin;
2	10000	5000	2300	1300
\.


--
-- Data for Name: userdashboard; Type: TABLE DATA; Schema: public; Owner: 37114702162
--

COPY public.userdashboard (uid, username, weeklyg, weekly, dailyg, daily) FROM stdin;
2	3	10000	5000	2300	1300
\.


--
-- Data for Name: users; Type: TABLE DATA; Schema: public; Owner: 37114702162
--

COPY public.users (uid, username, password, weeklyg, weekly, dailyg, daily, firstlogin) FROM stdin;
2	TestUser	$5$rounds=535000$Sz2fZU.BoBiesbAu$rZmuvtSTj3IJpP1anIfXF5uFatPO4wW0KFWE2N9IUBB	0	0	1000	0	\N
3	Time	$5$rounds=535000$53fVbWVbzm9tcZ7H$sIo8vmoUqyqVaBCy5aqGSuUHSuxHBbhBWf4.ukG.du7	0	0	1000	0	7
1	Arda	$5$rounds=535000$Xdabu3A7rSOowBK0$.zQ8T.LHBSnPTYXRJGBZ9SXV9y/SHom5/BvK09RcXk7	0	61	1000	61	7
\.


--
-- Name: foods_fid_seq; Type: SEQUENCE SET; Schema: public; Owner: 37114702162
--

SELECT pg_catalog.setval('public.foods_fid_seq', 2, true);


--
-- Name: goals_uid_seq; Type: SEQUENCE SET; Schema: public; Owner: 37114702162
--

SELECT pg_catalog.setval('public.goals_uid_seq', 1, false);


--
-- Name: userdashboard_uid_seq; Type: SEQUENCE SET; Schema: public; Owner: 37114702162
--

SELECT pg_catalog.setval('public.userdashboard_uid_seq', 1, false);


--
-- Name: users_uid_seq; Type: SEQUENCE SET; Schema: public; Owner: 37114702162
--

SELECT pg_catalog.setval('public.users_uid_seq', 4, true);


--
-- Name: foods foods_pkey; Type: CONSTRAINT; Schema: public; Owner: 37114702162
--

ALTER TABLE ONLY public.foods
    ADD CONSTRAINT foods_pkey PRIMARY KEY (fid);


--
-- Name: goals goals_pkey; Type: CONSTRAINT; Schema: public; Owner: 37114702162
--

ALTER TABLE ONLY public.goals
    ADD CONSTRAINT goals_pkey PRIMARY KEY (uid);


--
-- Name: userdashboard userdashboard_pkey; Type: CONSTRAINT; Schema: public; Owner: 37114702162
--

ALTER TABLE ONLY public.userdashboard
    ADD CONSTRAINT userdashboard_pkey PRIMARY KEY (uid);


--
-- Name: users users_pkey; Type: CONSTRAINT; Schema: public; Owner: 37114702162
--

ALTER TABLE ONLY public.users
    ADD CONSTRAINT users_pkey PRIMARY KEY (uid);


--
-- Name: foods foods_uid_fkey; Type: FK CONSTRAINT; Schema: public; Owner: 37114702162
--

ALTER TABLE ONLY public.foods
    ADD CONSTRAINT foods_uid_fkey FOREIGN KEY (uid) REFERENCES public.users(uid);


--
-- PostgreSQL database dump complete
--

