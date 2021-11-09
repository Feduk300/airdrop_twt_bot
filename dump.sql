-- we don't know how to generate root <with-no-name> (class Root) :(
create table users
(
	user_id bigint not null
		constraint users_pk
			primary key,
	balance numeric default 0,
	has_paid boolean default false,
	number varchar(150),
	full_name varchar(150),
	card integer
);

alter table users owner to postgres;

