CREATE SCHEMA clean_arch AUTHORIZATION swfjmtxl;

CREATE TABLE IF NOT EXISTS clean_arch.users (
    id BIGSERIAL NOT NULL,
    first_name VARCHAR(255) NOT NULL,
    last_name VARCHAR(255) NOT NULL,
    age BIGINT NOT NULL,
    primary key (id)
);