-- VisuMRI v0 schema.
-- Table names were not specified in the request; these are defaults.
-- `references` is a reserved word in SQL, so the reference table is kb_references.
-- Run in the Supabase SQL editor, or via scripts/supabase_sync.py --schema.

create table if not exists datasets (
    id                  text primary key,
    anatomy             text[] not null default '{}',
    formats             text[] not null default '{}',
    source_url          text not null,
    sample_file_url     text,
    page_title          text,
    license_text        text,
    license_status      text not null default 'license to verify',
    size_text           text,
    acquisition_params  text,
    access              text check (access in ('open', 'gated', 'unknown')),
    analysis            jsonb not null default '{}'::jsonb,
    notes_path          text,
    updated_at          timestamptz not null default now()
);

create table if not exists kb_references (
    id                      text primary key,
    citation                text not null,
    doi                     text,
    url                     text,
    data_types              text[] not null default '{}',
    anatomy                 text[] not null default '{}',
    display_recommendation  text,
    verified                boolean not null default false,
    updated_at              timestamptz not null default now()
);

create table if not exists dataset_references (
    dataset_id    text not null references datasets(id) on delete cascade,
    reference_id  text not null references kb_references(id) on delete cascade,
    primary key (dataset_id, reference_id)
);
