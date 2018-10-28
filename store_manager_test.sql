PGDMP     9    !            	    v            store_manager_test !   10.5 (Ubuntu 10.5-0ubuntu0.18.04) !   10.5 (Ubuntu 10.5-0ubuntu0.18.04)      �           0    0    ENCODING    ENCODING        SET client_encoding = 'UTF8';
                       false            �           0    0 
   STDSTRINGS 
   STDSTRINGS     (   SET standard_conforming_strings = 'on';
                       false            �           0    0 
   SEARCHPATH 
   SEARCHPATH     8   SELECT pg_catalog.set_config('search_path', '', false);
                       false            �           1262    65557    store_manager_test    DATABASE     �   CREATE DATABASE store_manager_test WITH TEMPLATE = template0 ENCODING = 'UTF8' LC_COLLATE = 'en_US.UTF-8' LC_CTYPE = 'en_US.UTF-8';
 "   DROP DATABASE store_manager_test;
             postgres    false                        2615    2200    public    SCHEMA        CREATE SCHEMA public;
    DROP SCHEMA public;
             postgres    false            �           0    0    SCHEMA public    COMMENT     6   COMMENT ON SCHEMA public IS 'standard public schema';
                  postgres    false    3                        3079    13041    plpgsql 	   EXTENSION     ?   CREATE EXTENSION IF NOT EXISTS plpgsql WITH SCHEMA pg_catalog;
    DROP EXTENSION plpgsql;
                  false            �           0    0    EXTENSION plpgsql    COMMENT     @   COMMENT ON EXTENSION plpgsql IS 'PL/pgSQL procedural language';
                       false    1            �            1259    73940 
   categories    TABLE     �   CREATE TABLE public.categories (
    category_id integer NOT NULL,
    category_name character varying(56) NOT NULL,
    created_at timestamp with time zone DEFAULT now()
);
    DROP TABLE public.categories;
       public         postgres    false    3            �            1259    73938    categories_category_id_seq    SEQUENCE     �   CREATE SEQUENCE public.categories_category_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 1   DROP SEQUENCE public.categories_category_id_seq;
       public       postgres    false    3    199            �           0    0    categories_category_id_seq    SEQUENCE OWNED BY     Y   ALTER SEQUENCE public.categories_category_id_seq OWNED BY public.categories.category_id;
            public       postgres    false    198            �            1259    73929    products    TABLE     �   CREATE TABLE public.products (
    product_id integer NOT NULL,
    product_name character varying(38) NOT NULL,
    quantity integer NOT NULL,
    unit_cost integer NOT NULL,
    created_at timestamp without time zone DEFAULT now()
);
    DROP TABLE public.products;
       public         postgres    false    3            �            1259    73927    products_product_id_seq    SEQUENCE     �   CREATE SEQUENCE public.products_product_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 .   DROP SEQUENCE public.products_product_id_seq;
       public       postgres    false    197    3            �           0    0    products_product_id_seq    SEQUENCE OWNED BY     S   ALTER SEQUENCE public.products_product_id_seq OWNED BY public.products.product_id;
            public       postgres    false    196            �            1259    73951    users    TABLE     �   CREATE TABLE public.users (
    user_id integer NOT NULL,
    username character varying(35) NOT NULL,
    password character varying(240) NOT NULL,
    admin boolean DEFAULT false,
    registered_at timestamp without time zone DEFAULT now()
);
    DROP TABLE public.users;
       public         postgres    false    3            �            1259    73949    users_user_id_seq    SEQUENCE     �   CREATE SEQUENCE public.users_user_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 (   DROP SEQUENCE public.users_user_id_seq;
       public       postgres    false    201    3            �           0    0    users_user_id_seq    SEQUENCE OWNED BY     G   ALTER SEQUENCE public.users_user_id_seq OWNED BY public.users.user_id;
            public       postgres    false    200            �
           2604    73943    categories category_id    DEFAULT     �   ALTER TABLE ONLY public.categories ALTER COLUMN category_id SET DEFAULT nextval('public.categories_category_id_seq'::regclass);
 E   ALTER TABLE public.categories ALTER COLUMN category_id DROP DEFAULT;
       public       postgres    false    199    198    199            �
           2604    73932    products product_id    DEFAULT     z   ALTER TABLE ONLY public.products ALTER COLUMN product_id SET DEFAULT nextval('public.products_product_id_seq'::regclass);
 B   ALTER TABLE public.products ALTER COLUMN product_id DROP DEFAULT;
       public       postgres    false    197    196    197            �
           2604    73954    users user_id    DEFAULT     n   ALTER TABLE ONLY public.users ALTER COLUMN user_id SET DEFAULT nextval('public.users_user_id_seq'::regclass);
 <   ALTER TABLE public.users ALTER COLUMN user_id DROP DEFAULT;
       public       postgres    false    200    201    201            }          0    73940 
   categories 
   TABLE DATA               L   COPY public.categories (category_id, category_name, created_at) FROM stdin;
    public       postgres    false    199   /"       {          0    73929    products 
   TABLE DATA               ]   COPY public.products (product_id, product_name, quantity, unit_cost, created_at) FROM stdin;
    public       postgres    false    197   L"                 0    73951    users 
   TABLE DATA               R   COPY public.users (user_id, username, password, admin, registered_at) FROM stdin;
    public       postgres    false    201   i"       �           0    0    categories_category_id_seq    SEQUENCE SET     I   SELECT pg_catalog.setval('public.categories_category_id_seq', 1, false);
            public       postgres    false    198            �           0    0    products_product_id_seq    SEQUENCE SET     F   SELECT pg_catalog.setval('public.products_product_id_seq', 1, false);
            public       postgres    false    196            �           0    0    users_user_id_seq    SEQUENCE SET     ?   SELECT pg_catalog.setval('public.users_user_id_seq', 1, true);
            public       postgres    false    200            �
           2606    73948 '   categories categories_category_name_key 
   CONSTRAINT     k   ALTER TABLE ONLY public.categories
    ADD CONSTRAINT categories_category_name_key UNIQUE (category_name);
 Q   ALTER TABLE ONLY public.categories DROP CONSTRAINT categories_category_name_key;
       public         postgres    false    199            �
           2606    73946    categories categories_pkey 
   CONSTRAINT     a   ALTER TABLE ONLY public.categories
    ADD CONSTRAINT categories_pkey PRIMARY KEY (category_id);
 D   ALTER TABLE ONLY public.categories DROP CONSTRAINT categories_pkey;
       public         postgres    false    199            �
           2606    73935    products products_pkey 
   CONSTRAINT     \   ALTER TABLE ONLY public.products
    ADD CONSTRAINT products_pkey PRIMARY KEY (product_id);
 @   ALTER TABLE ONLY public.products DROP CONSTRAINT products_pkey;
       public         postgres    false    197            �
           2606    73937 "   products products_product_name_key 
   CONSTRAINT     e   ALTER TABLE ONLY public.products
    ADD CONSTRAINT products_product_name_key UNIQUE (product_name);
 L   ALTER TABLE ONLY public.products DROP CONSTRAINT products_product_name_key;
       public         postgres    false    197            �
           2606    73958    users users_pkey 
   CONSTRAINT     S   ALTER TABLE ONLY public.users
    ADD CONSTRAINT users_pkey PRIMARY KEY (user_id);
 :   ALTER TABLE ONLY public.users DROP CONSTRAINT users_pkey;
       public         postgres    false    201                        2606    73960    users users_username_key 
   CONSTRAINT     W   ALTER TABLE ONLY public.users
    ADD CONSTRAINT users_username_key UNIQUE (username);
 B   ALTER TABLE ONLY public.users DROP CONSTRAINT users_username_key;
       public         postgres    false    201            }      x������ � �      {      x������ � �         �   x��1�0 �9yC�V�c�nf6F�4qT	$�x=�����ϳ[��{}Ԇi�2�$��������J4��"���*��d.�Y�B<���I*Gŵ�Tb��z�%$�I(�9������$+     